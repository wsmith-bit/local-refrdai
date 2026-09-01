from __future__ import annotations

import json
import re
from html import unescape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", "", value))).strip()


for path in sorted((ROOT / "industries").glob("*/index.html")):
    source = path.read_text(encoding="utf-8")
    pairs = re.findall(r'<article\s+class="faq"[^>]*>\s*<h3>(.*?)</h3>\s*<p>(.*?)</p>\s*</article>', source, re.I | re.S)
    if not pairs:
        raise RuntimeError(f"No visible FAQs found in {path}")
    match = re.search(r'(<script\s+type="application/ld\+json"[^>]*>)(.*?)(</script>)', source, re.I | re.S)
    if not match:
        raise RuntimeError(f"No JSON-LD found in {path}")
    data = json.loads(match.group(2))
    faq = next((item for item in data.get("@graph", []) if item.get("@type") == "FAQPage"), None)
    if faq is None:
        raise RuntimeError(f"No FAQPage object found in {path}")
    faq["mainEntity"] = [
        {
            "@type": "Question",
            "name": clean(question),
            "acceptedAnswer": {"@type": "Answer", "text": clean(answer)},
        }
        for question, answer in pairs
    ]
    replacement = match.group(1) + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + match.group(3)
    updated = source[:match.start()] + replacement + source[match.end():]
    path.write_text(updated, encoding="utf-8", newline="")
    print(f"Synced {len(pairs)} visible FAQs: {path.parent.name}")
