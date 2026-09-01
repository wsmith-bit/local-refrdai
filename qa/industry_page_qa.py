from __future__ import annotations

import json
import re
import sys
from html import unescape
from html.parser import HTMLParser
from itertools import combinations
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
PAGES = sorted((ROOT / "industries").glob("*/index.html"))
FULL_SET = [ROOT / "industries" / "index.html", *PAGES, ROOT / "foundation-crawlspace-waterproofing-contractors" / "index.html"]
BOOKING = "https://calendar.app.google/qwZB5sgoY74tPssA6"
HUBSPOT_FORM = "b972ec68-3a3b-47f8-b97d-d07a1e077474"
ROUTE_ALIASES = {
    "/entity-source-of-truth/": ROOT / "entity-source-of-truth.html",
    "/why-refrdai-exists/": ROOT / "why_refrdai_exists.html",
}
BANNED_VISIBLE_PHRASES = (
    "a page fails",
    "required website",
    "required email",
    "digital scout",
    "available intelligence",
    "meaningful territory presence",
    "copy brief",
    "content model",
    "niche-name",
    "normalized visible",
    "approved inventory",
    "schema markup",
    "search engine optimization",
    "generative engine optimization",
)


class VisibleTextParser(HTMLParser):
    def __init__(self, inside_main_only: bool = True) -> None:
        super().__init__(convert_charrefs=True)
        self.inside_main_only = inside_main_only
        self.skip_depth = 0
        self.main_depth = 0
        self.text: list[str] = []
        self.headings: list[str] = []
        self.current_heading: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if self.skip_depth:
            self.skip_depth += 1
            return
        if tag in {"script", "style", "nav", "footer"} or attributes.get("data-qa-shared") == "true":
            self.skip_depth = 1
            return
        if tag == "main":
            self.main_depth += 1
        if self.main_depth and tag in {"h1", "h2", "h3"}:
            self.current_heading = []

    def handle_endtag(self, tag: str) -> None:
        if self.skip_depth:
            self.skip_depth -= 1
            return
        if tag == "main" and self.main_depth:
            self.main_depth -= 1
        if tag in {"h1", "h2", "h3"} and self.current_heading is not None:
            heading = " ".join(self.current_heading).strip()
            if heading:
                self.headings.append(heading)
            self.current_heading = None

    def handle_data(self, data: str) -> None:
        if self.skip_depth or (self.inside_main_only and not self.main_depth):
            return
        clean = re.sub(r"\s+", " ", data).strip()
        if clean:
            self.text.append(clean)
            if self.current_heading is not None:
                self.current_heading.append(clean)


def shingles(text: str, size: int = 5) -> set[tuple[str, ...]]:
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {tuple(words[i:i + size]) for i in range(max(0, len(words) - size + 1))}


def uniqueness(a: set[tuple[str, ...]], b: set[tuple[str, ...]]) -> float:
    union = a | b
    return 1.0 if not union else 1.0 - (len(a & b) / len(union))


def clean_fragment(value: str) -> str:
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", "", value))).strip()


def visible_faqs(source: str) -> set[tuple[str, str]]:
    pairs = re.findall(r'<article\s+class="faq"[^>]*>\s*<h3>(.*?)</h3>\s*<p>(.*?)</p>\s*</article>', source, re.I | re.S)
    return {(clean_fragment(question), clean_fragment(answer)) for question, answer in pairs}


def json_ld_errors(path: Path, source: str) -> list[str]:
    errors: list[str] = []
    blocks = re.findall(r'<script\s+type="application/ld\+json"[^>]*>(.*?)</script>', source, re.I | re.S)
    if not blocks:
        return ["missing JSON-LD"]
    for index, block in enumerate(blocks, 1):
        try:
            data = json.loads(block)
            graph = data.get("@graph", []) if isinstance(data, dict) else []
            page_faqs = visible_faqs(source)
            for item in graph:
                if item.get("@type") != "FAQPage":
                    continue
                for entity in item.get("mainEntity", []):
                    question = entity.get("name", "")
                    answer = entity.get("acceptedAnswer", {}).get("text", "")
                    if (question, answer) not in page_faqs:
                        errors.append(f"FAQ schema differs from visible answer: {question}")
        except json.JSONDecodeError as exc:
            errors.append(f"JSON-LD block {index}: {exc}")
    return errors


def main() -> int:
    failures: list[str] = []
    parsed: dict[str, tuple[set[tuple[str, ...]], list[str]]] = {}
    titles: dict[str, str] = {}
    print(f"Checking {len(PAGES)} industry pages")
    if len(PAGES) != 6:
        failures.append(f"expected 6 pages, found {len(PAGES)}")

    for path in PAGES:
        source = path.read_text(encoding="utf-8")
        label = path.parent.name
        parser = VisibleTextParser(inside_main_only=False)
        parser.feed(source)
        parsed[label] = (shingles(" ".join(parser.text)), parser.headings)

        requirements = {
            "canonical": f'https://local.refrdai.com/industries/{label}/',
            "HubSpot form": HUBSPOT_FORM,
            "Google booking": BOOKING,
            "primary CTA": "Request My Free 15-Minute Territory Review",
            "business price": "$3,400",
            "optional annual plan": "$495",
            "optional monthly plan": "$500",
            "analytics script": "/assets/industry-pages.js",
            "industry attribution": "data-industry=",
        }
        missing = [name for name, needle in requirements.items() if needle not in source]
        missing.extend(json_ld_errors(path, source))
        if source.lower().count("<h1") != 1:
            missing.append("exactly one H1")
        if "<title>" not in source or 'name="description"' not in source:
            missing.append("title or meta description")
        title_match = re.search(r"<title>(.*?)</title>", source, re.I | re.S)
        if title_match:
            title = re.sub(r"\s+", " ", title_match.group(1)).strip()
            if title in titles:
                missing.append(f"duplicate title with {titles[title]}")
            titles[title] = label
        for href in re.findall(r'href="(/[^"]*)"', source, re.I):
            target = urlparse(href).path
            local = ROUTE_ALIASES.get(target, ROOT / target.lstrip("/"))
            if target.endswith("/") and target not in ROUTE_ALIASES:
                local /= "index.html"
            if target and not local.exists():
                missing.append(f"broken local link {target}")
        if missing:
            failures.append(f"{label}: {', '.join(missing)}")
        print(f"- {label}: {len(parser.text)} text segments, {len(parser.headings)} headings")

    print("\nFull-set copy and structured-data audit:")
    for path in FULL_SET:
        source = path.read_text(encoding="utf-8")
        parser = VisibleTextParser(inside_main_only=False)
        parser.feed(source)
        visible = " ".join(parser.text).lower()
        label = str(path.relative_to(ROOT))
        banned = [phrase for phrase in BANNED_VISIBLE_PHRASES if phrase in visible]
        errors = json_ld_errors(path, source)
        if source.lower().count("<h1") != 1:
            errors.append("expected exactly one H1")
        if path != ROOT / "industries" / "index.html":
            if "Phone is optional" not in source:
                errors.append("phone optional statement missing")
            if "Request My Free 15-Minute Territory Review" not in source:
                errors.append("primary CTA missing")
        if banned:
            errors.append("visible internal language: " + ", ".join(banned))
        if errors:
            failures.append(f"{label}: {', '.join(errors)}")
        print(f"- {label}: {'PASS' if not errors else 'FAIL'}")

    print("\nPairwise visible-main-content uniqueness (shared commercial/form blocks excluded):")
    lowest = 1.0
    for left, right in combinations(parsed, 2):
        score = uniqueness(parsed[left][0], parsed[right][0])
        lowest = min(lowest, score)
        print(f"- {left} vs {right}: {score:.1%}")
        if score < 0.55:
            failures.append(f"uniqueness below 55%: {left} vs {right} = {score:.1%}")

    print(f"\nLowest uniqueness: {lowest:.1%}")
    if failures:
        print("\nFAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("\nPASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
