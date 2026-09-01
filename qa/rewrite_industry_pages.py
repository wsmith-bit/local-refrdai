from __future__ import annotations

import json
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOKING = "https://calendar.app.google/qwZB5sgoY74tPssA6"
FORM_ID = "b972ec68-3a3b-47f8-b97d-d07a1e077474"
PORTAL_ID = "49371050"
FORM_FALLBACK = "https://te6y2.share.hsforms.com/2uXLsaDo7R_i5fdB6Hgd0dA"


PAGES = {
    "septic-installation-contractors": {
        "industry": "septic-installation",
        "title": "Septic Installation Contractor Territory Websites | REFRDAI",
        "meta": "A customer-owned territory website for septic contractors pursuing new-system installations, failed-system replacements, and drainfield projects.",
        "og_title": "Territory Websites for Septic Installation Contractors",
        "og_desc": "Help property owners find your septic company while they are planning an installation, replacement, or drainfield project.",
        "page_name": "Territory websites for septic installation contractors",
        "page_desc": "A REFRDAI offer for septic contractors that want a customer-owned territory website focused on one installation, replacement, or drainfield service.",
        "service_name": "REFRDAI territory website for septic installation contractors",
        "service_desc": "A $3,400 customer-owned territory website for one primary septic service within an agreed 30-mile radius.",
        "crumb": "Septic Installation Contractors",
        "eyebrow": "For septic installation and replacement contractors",
        "h1": "Be easier to find for septic installation and replacement projects in the towns you serve.",
        "hero": "Pumping calls are different from new-system installations and failed-system replacements. REFRDAI builds a separate website your company owns alongside its current site, focused on one septic service and the towns where you want more qualified project inquiries.",
        "secondary_href": "#septic-path",
        "secondary": "See the Septic Project Path",
        "fine": "The review is free and creates no purchase obligation. REFRDAI does not guarantee rankings, inquiries, installations, projects, or revenue.",
        "panel_title": "A septic project moves through several decisions.",
        "panel_intro": "Useful town pages help property owners understand what must be checked before they assume a system type, layout, price, or schedule.",
        "panel_steps": [
            ("01", "Why is the project starting?", "New construction, a failing system, a replacement field, an addition, a property transfer, or another verified need."),
            ("02", "What must be checked on the property?", "Records, soils, setbacks, lot limits, access, system condition, site evaluation, and the local approval process."),
            ("03", "What does the contractor handle?", "Evaluation, design coordination, permits, excavation, installation, inspection coordination, and closeout only as the company actually provides them."),
        ],
        "offer": [
            ("One primary septic service", "Choose new-system installation, failed-system replacement, drainfield work, or another clearly defined septic service."),
            ("One agreed 30-mile territory", "Every eligible community on the approved inventory is included, up to 100."),
            ("One website your company owns", "The new territory website runs alongside your current site."),
        ],
        "sections": [
            '''<section id="septic-path"><div class="container"><div class="section-heading"><p class="kicker">Keep the project clear</p><h2>Keep installation work separate from routine service.</h2><p>A homeowner replacing a failed system, a builder preparing a lot, and a buyer reviewing an existing system are not asking the same question. The first territory build makes one project path easy to understand.</p></div><div class="decision-path"><article class="decision-step"><span class="step-number">01</span><div><strong>Can the property support the planned work?</strong><p>Explain why site conditions and local requirements must be checked before a system type or layout is treated as settled.</p></div></article><article class="decision-step"><span class="step-number">02</span><div><strong>Is this repair, replacement, or new construction?</strong><p>Make the primary project clear so pumping, alarm, inspection, and routine-service searches do not define the page.</p></div></article><article class="decision-step"><span class="step-number">03</span><div><strong>Who is responsible for each step?</strong><p>The website explains which parts your company handles and clearly separates your role from the health department, designer, engineer, or permitting authority.</p></div></article></div><p class="callout">Septic rules and responsible authorities vary by state and locality. Local permit and approval information is included only when it is current and supported by the responsible authority. <a href="https://www.epa.gov/septic/frequent-questions-septic-systems">Review U.S. EPA septic guidance</a>.</p></div></section>''',
            '''<section class="band"><div class="container"><div class="section-heading"><p class="kicker">Choose the work</p><h2>Choose the septic work the first build should support.</h2></div><div class="cards"><article class="card"><span class="tag">New systems</span><h3>New septic-system installation</h3><p>Help property owners and builders prepare for records, site readiness, approval steps, access, schedule, and installation responsibility.</p></article><article class="card"><span class="tag">Replacement</span><h3>Failed-system replacement</h3><p>Help owners understand why evaluation comes before a confident scope when system condition, property limits, or failure symptoms affect the project.</p></article><article class="card"><span class="tag">Drainfield</span><h3>Drainfield replacement or repair</h3><p>Show property owners the drainfield work your company actually provides and the evaluation, design, and approval steps they may need to expect.</p></article></div></div></section>''',
            '''<section><div class="container two-col"><div><div class="section-heading"><p class="kicker">What REFRDAI builds</p><h2>Three original pages for every approved town.</h2><p>Every approved town receives pages focused on the agreed septic service.</p></div><ul class="plain-list"><li>One main town-and-service page that clearly explains the installation, replacement, or drainfield service.</li><li>One original question page about the first local decision, such as records, site evaluation, or permits.</li><li>One different question page about replacement planning, lot limits, access, or project sequence.</li><li>Every page gives property owners a clear way to call or request an estimate from your company.</li></ul></div><aside class="scope-box"><h3>Useful information without false certainty</h3><p>The site helps owners prepare for the next conversation without pretending every property has the same answer.</p><div class="scope-grid"><div class="scope-item"><b>Useful</b><span>Answers real customer questions in plain language.</span></div><div class="scope-item"><b>Accurate</b><span>Uses verified local rules, qualifications, and services.</span></div><div class="scope-item"><b>Focused</b><span>Keeps installation intent separate from pumping.</span></div><div class="scope-item"><b>Owned</b><span>Your company owns and keeps the website and domain.</span></div></div></aside></div></section>''',
        ],
        "primary_scope": "One primary septic service",
        "review_h2": "Which towns do you want more septic installation or replacement inquiries from?",
        "faqs": [
            ("Is this for septic pumping companies?", "A company may also pump or inspect, but the first build focuses on one primary installation, replacement, or drainfield service."),
            ("Will every town use the same permit information?", "No. Rules and responsible authorities vary. Local statements must use current, authoritative information for that location."),
            ("Will this replace my current website?", "No. The new customer-owned territory website runs alongside your current site."),
            ("Who owns the website and domain?", "You own and keep the completed website. REFRDAI pays for the domain’s first year and transfers it after launch and cleared final payment as soon as the registrar permits."),
            ("Are septic installation projects guaranteed?", "No. REFRDAI does not guarantee indexing, rankings, inquiries, installations, projects, or revenue."),
            ("Is hosting included?", "Managed hosting under normal usage is included. Unlimited hosting is not promised."),
            ("Does the first build cover every septic service?", "No. It focuses on one agreed primary septic service. Additional services require separate scope and pricing."),
        ],
    },
    "water-well-drilling-contractors": {
        "industry": "water-well-drilling",
        "title": "Water-Well Drilling Contractor Territory Websites | REFRDAI",
        "meta": "A customer-owned territory website for water-well contractors pursuing new-well, replacement-well, or pump-system projects in more towns.",
        "og_title": "Territory Websites for Water-Well Contractors",
        "og_desc": "Help property owners move from a water need to the right drilling or pump-system conversation.",
        "page_name": "Territory websites for water-well drilling contractors",
        "page_desc": "A REFRDAI offer for water-well contractors that want a customer-owned territory website focused on one drilling or pump-system service.",
        "service_name": "REFRDAI territory website for water-well contractors",
        "service_desc": "A $3,400 customer-owned territory website for one primary water-well or pump-system service within an agreed 30-mile radius.",
        "crumb": "Water-Well Drilling Contractors",
        "eyebrow": "For water-well drilling and pump-system companies",
        "h1": "Get found for more of the well-drilling or pump-system projects you want to quote.",
        "hero": "Your equipment and local ground knowledge matter only after the right property owner finds and contacts your company. REFRDAI builds a separate website your company owns alongside its current site, focused on one water-well or pump-system service.",
        "secondary_href": "#water-path",
        "secondary": "See the Water-Project Path",
        "fine": "The site supports discovery and better project conversations. It does not predict well depth, yield, water quality, project cost, inquiries, contracts, or revenue.",
        "panel_title": "A useful well inquiry starts with the property.",
        "panel_intro": "The page prepares an owner to discuss the property and water need instead of expecting a fixed answer before records and site conditions are reviewed.",
        "panel_steps": [
            ("01", "What property needs water?", "A new home, existing home, farm, business, replacement need, or undeveloped parcel."),
            ("02", "What service is being considered?", "A new well, replacement well, pump installation, pump replacement, storage, pressure system, or another agreed primary service."),
            ("03", "What must be checked locally?", "Access, records, permits, setbacks, geology, utilities, equipment position, and the contractor’s actual service range."),
        ],
        "offer": [
            ("One primary water-system service", "Keep the first build focused instead of mixing every drilling and pump need."),
            ("One agreed 30-mile territory", "Approve the center and eligible communities before production begins."),
            ("One website your company owns", "The new territory website runs alongside your current site."),
        ],
        "sections": [
            '''<section id="water-path"><div class="container"><div class="section-heading"><p class="kicker">Match the water need</p><h2>Different water needs require different conversations.</h2><p>Someone building on raw land does not make the same decision as an owner with an aging well or failed pump. The first territory build should make one path unmistakable.</p></div><div class="cards"><article class="card"><span class="tag">New well</span><h3>Start with the property and intended use</h3><p>Help the owner gather the address, intended use, available records, construction timing, and access information before requesting a drilling consultation.</p></article><article class="card"><span class="tag">Replacement</span><h3>Start with the existing system history</h3><p>Prompt for known records, system age, symptoms, recent changes, and prior inspection without diagnosing the cause online.</p></article><article class="card"><span class="tag">Pump systems</span><h3>Separate drilling from equipment service</h3><p>State clearly whether the company installs or replaces pumps, pressure tanks, controls, storage, or related equipment.</p></article></div><p class="callout">Your website can show current, verified qualifications, equipment, insurance, contract practices, well-log procedures, and local-code knowledge that help an owner evaluate your company. <a href="https://wellowner.org/resources/working-with-contractors/how-to-hire-a-water-well-contractor/">Review the WellOwner.org contractor checklist</a>.</p></div></section>''',
            '''<section class="band"><div class="container two-col"><div><div class="section-heading"><p class="kicker">Customer language</p><h2>Start with the way property owners describe the water problem.</h2><p>Each town page connects the owner’s water need with the contractor’s accurate service language.</p></div><ul class="plain-list"><li>Water-well drilling for a new home, farm, business, or undeveloped property.</li><li>Replacement-well planning when an existing source is no longer dependable.</li><li>Well-pump installation or replacement when that is the agreed primary service.</li><li>Records, access, permits, written scope, testing responsibilities, and project closeout.</li></ul></div><aside class="scope-box"><h3>Explain the process without promising what is underground</h3><div class="scope-grid"><div class="scope-item"><b>No depth prediction</b><span>Local history may inform a conversation but cannot guarantee a result.</span></div><div class="scope-item"><b>No yield promise</b><span>Actual water availability is specific to the property.</span></div><div class="scope-item"><b>Supported local information</b><span>Any statement about local ground conditions is tied to reliable evidence.</span></div><div class="scope-item"><b>One clear service</b><span>The first build does not bundle every water-system need.</span></div></div></aside></div></section>''',
            '''<section><div class="container"><div class="section-heading"><p class="kicker">What REFRDAI builds</p><h2>Build each town around a decision the owner can make.</h2></div><div class="decision-path"><article class="decision-step"><span class="step-number">01</span><div><strong>Need</strong><p>Explain why a new or replacement water source is being considered.</p></div></article><article class="decision-step"><span class="step-number">02</span><div><strong>Records</strong><p>Show how prior well records, surveys, plans, and local requirements can shape the next step.</p></div></article><article class="decision-step"><span class="step-number">03</span><div><strong>Property review</strong><p>Prepare the owner to discuss access, equipment space, utilities, setbacks, and site conditions.</p></div></article><article class="decision-step"><span class="step-number">04</span><div><strong>Written scope</strong><p>Encourage clear responsibilities without presenting the drilling result as fixed.</p></div></article></div><p class="callout">Each approved town receives one main town-and-primary-service page and two original question pages about the property, records, access, scope, pumps, or contractor selection.</p></div></section>''',
        ],
        "primary_scope": "One primary water-well or pump-system service",
        "review_h2": "Where do you want more well-drilling or pump-system projects?",
        "faqs": [
            ("Can the first build cover drilling and every pump service?", "No. Choose one primary service. Additional services require separate scope and pricing."),
            ("Will REFRDAI estimate well depth or yield?", "No. The website will not predict site-specific underground conditions or drilling results."),
            ("Can the website use my real qualifications?", "Yes, when they are current, verified, and approved for public use."),
            ("What happens to my existing website?", "Nothing. The new customer-owned territory website runs alongside it."),
            ("Are drilling projects guaranteed?", "No. REFRDAI does not guarantee indexing, rankings, inquiries, signed work, or revenue."),
            ("How many pages are built for each approved town?", "One main town-and-service page plus two original town-specific customer-question pages."),
            ("Who owns the domain?", "REFRDAI pays for the first year and transfers the domain after launch and cleared final payment as soon as the registrar permits."),
        ],
    },
    "land-clearing-site-preparation-contractors": {
        "industry": "land-clearing-site-preparation",
        "title": "Land-Clearing Contractor Territory Websites | REFRDAI",
        "meta": "A customer-owned territory website for land-clearing and site-preparation companies pursuing better-fit acreage, lot, mulching, and site-work projects.",
        "og_title": "Territory Websites for Land-Clearing Contractors",
        "og_desc": "Help property owners describe acreage, access, material, and intended use before they request an estimate.",
        "page_name": "Territory websites for land-clearing and site-preparation contractors",
        "page_desc": "A REFRDAI offer for land contractors that want a customer-owned territory website focused on one clearing or site-preparation service.",
        "service_name": "REFRDAI territory website for land-clearing contractors",
        "service_desc": "A $3,400 customer-owned territory website for one primary land-clearing or site-preparation service within an agreed 30-mile radius.",
        "crumb": "Land Clearing and Site Preparation",
        "eyebrow": "For land-clearing and site-preparation contractors",
        "h1": "Be easier to find for land-clearing projects that fit your equipment and crew.",
        "hero": "“Clear my land” may mean a backyard brush job, a multi-acre home site, a commercial pad, or ground that is not ready for your machines. REFRDAI builds a separate website your company owns alongside its current site, helping prospects describe acreage, access, material, and intended use before they call.",
        "secondary_href": "#project-fit",
        "secondary": "See How the Site Helps Clarify Work",
        "fine": "REFRDAI does not guarantee inquiries, machine hours, awarded projects, rankings, or revenue.",
        "panel_title": "A useful clearing inquiry starts before price.",
        "panel_intro": "The page helps property owners share the project details you need before deciding whether a site visit is the right next step.",
        "panel_steps": [
            ("01", "Acreage and boundaries", "How much land is involved, what must remain, and whether surveys, plans, or marked boundaries exist."),
            ("02", "Intended next use", "A home site, driveway, pasture, view, building pad, development, storm cleanup, or maintenance project."),
            ("03", "Access and material", "Machine access, slope, utilities, timber, brush, stumps, debris, rock, wet ground, and disposal expectations."),
        ],
        "offer": [
            ("One project type you want more of", "Choose clearing, forestry mulching, grubbing, pad preparation, or another agreed primary service."),
            ("One practical 30-mile territory", "Approve the center and eligible communities before production."),
            ("One website your company owns", "The new territory website runs alongside your current site."),
        ],
        "sections": [
            '''<section id="project-fit"><div class="container"><div class="section-heading"><p class="kicker">Project fit</p><h2>The estimate begins with project fit.</h2><p>A small brush job and a complete site package should not be described as interchangeable. The first build names the work you want and explains what changes the scope.</p></div><div class="decision-path"><article class="decision-step"><span class="step-number">01</span><div><strong>What needs to be removed?</strong><p>Brush, standing timber, stumps, roots, structures, debris, unsuitable soil, or a mix of material.</p></div></article><article class="decision-step"><span class="step-number">02</span><div><strong>What must the finished ground support?</strong><p>Construction, access, drainage, pasture, landscaping, visibility, or another defined next use.</p></div></article><article class="decision-step"><span class="step-number">03</span><div><strong>Can the crew and equipment work safely?</strong><p>Access, utilities, slope, wet ground, traffic, neighbors, disposal, and limits of disturbance can change the project.</p></div></article></div></div></section>''',
            '''<section class="band"><div class="container"><div class="section-heading"><p class="kicker">Respect the property</p><h2>Give property owners a clearer picture of the work before they request an estimate.</h2><p>Useful town pages explain why property details matter before an estimate. They do not invent a per-acre price or suggest that photos always replace a site visit.</p></div><div class="cards"><article class="card"><span class="tag">Equipment fit</span><h3>Match the job to real capability</h3><p>Describe the machines, access, material, and project size the company can actually handle.</p></article><article class="card"><span class="tag">Scope clarity</span><h3>Separate the services</h3><p>Keep clearing, mulching, grubbing, excavation, and full site preparation distinct.</p></article><article class="card"><span class="tag">Finish requirements</span><h3>Define what happens next</h3><p>Explain the condition the owner needs when the crew leaves and who performs the next phase.</p></article></div><p class="callout">Your website presents only the equipment, services, safety controls, and site-preparation work your company actually provides. <a href="https://www.osha.gov/etools/oil-and-gas/site-preparation/">Review OSHA site-preparation information</a>.</p></div></section>''',
            '''<section><div class="container two-col"><div><div class="section-heading"><p class="kicker">What owners need to share</p><h2>Answer the first questions before the owner calls.</h2></div><ul class="plain-list"><li><strong>Property:</strong> Town, acreage, boundaries, access point, current condition, and available plans.</li><li><strong>Material:</strong> Brush, timber, stumps, debris, structures, rock, soil, or wet areas.</li><li><strong>Finish:</strong> Mulched, cleared, grubbed, rough graded, pad-ready, hauled, burned, or left on site where lawful.</li><li><strong>Timing:</strong> Project deadline, following contractor, weather constraints, approvals, and site-visit availability.</li></ul></div><aside class="scope-box"><h3>Three original pages per approved town</h3><p>One main page explains the agreed service. Two different town-specific question pages address project conditions and local requirements that matter there.</p><div class="scope-grid"><div class="scope-item"><b>Lot clearing</b><span>Boundaries, access, trees to retain, stumps, debris, and rough grade.</span></div><div class="scope-item"><b>Forestry mulching</b><span>Trails, fence lines, pasture recovery, vegetation, and maintenance.</span></div><div class="scope-item"><b>Site preparation</b><span>Excavation, pad work, access, drainage, compaction, and plans.</span></div><div class="scope-item"><b>No invented quote</b><span>Real site conditions still shape the estimate.</span></div></div></aside></div></section>''',
        ],
        "primary_scope": "One primary land-clearing or site-preparation service",
        "review_h2": "Which towns do you want more clearing or site-preparation inquiries from?",
        "faqs": [
            ("Can the first build target every type of dirt work?", "No. It focuses on one primary service even when the company offers several."),
            ("Will the pages quote projects by the acre?", "Only if the contractor has verified, approved pricing suitable for publication. Material, access, disposal, equipment, finish, and site conditions often change the scope."),
            ("Can the website focus on larger projects?", "Yes. It can state the desired project type and honest minimum-fit factors without promising that every inquiry will qualify."),
            ("Will it replace my current website?", "No. The customer-owned territory website runs alongside your current site."),
            ("Are land-clearing projects guaranteed?", "No. REFRDAI does not guarantee indexing, rankings, inquiries, awarded projects, or revenue."),
            ("Who owns the domain?", "REFRDAI pays for the first year and transfers the domain after launch and cleared final payment as soon as the registrar permits."),
            ("Is managed hosting included?", "Yes, under normal usage. Unlimited hosting is not promised."),
        ],
    },
    "standby-generator-installers": {
        "industry": "standby-generator-installation",
        "title": "Standby-Generator Installer Territory Websites | REFRDAI",
        "meta": "A customer-owned territory website for generator dealers and electrical contractors pursuing complete permanent standby-installation projects.",
        "og_title": "Territory Websites for Standby-Generator Installers",
        "og_desc": "Help homeowners understand the complete installed system and request a property consultation while planning backup power.",
        "page_name": "Territory websites for standby-generator installers",
        "page_desc": "A REFRDAI offer for generator dealers and electrical contractors that want a customer-owned territory website focused on complete standby installation.",
        "service_name": "REFRDAI territory website for standby-generator installers",
        "service_desc": "A $3,400 customer-owned territory website for one primary standby-generator service within an agreed 30-mile radius.",
        "crumb": "Standby-Generator Installers",
        "eyebrow": "For standby-generator dealers and installers",
        "h1": "Be easier to find while homeowners are planning a complete standby-generator installation.",
        "hero": "A complete installation is more than the generator. REFRDAI builds a separate website your company owns alongside its current site, helping homeowners understand the installed system and request a property consultation before they focus only on equipment price.",
        "secondary_href": "#installation-path",
        "secondary": "See the Installation-Decision Path",
        "fine": "REFRDAI does not guarantee storm demand, rankings, consultations, installations, sales, or revenue.",
        "panel_title": "Help homeowners prepare for a useful installation consultation.",
        "panel_intro": "The page helps a homeowner organize the property information a qualified installer needs for a useful consultation.",
        "panel_steps": [
            ("01", "Backup-power goal", "Essential circuits, selected loads, broader whole-home coverage, or another clearly defined priority."),
            ("02", "Property readiness", "Electrical service, fuel source, possible placement, access, clearances, utilities, and local approval."),
            ("03", "Complete installed scope", "Equipment, transfer equipment, qualified electrical and fuel work, startup, homeowner handoff, and future service as actually provided."),
        ],
        "offer": [
            ("One primary installation service", "Focus on complete permanent standby installation instead of a catch-all electrical page."),
            ("Useful pages before the installation consultation", "Give homeowners clear information about the property and installation questions to discuss with your company."),
            ("One website your company owns", "The new territory website runs alongside your current site."),
        ],
        "sections": [
            '''<section id="installation-path"><div class="container"><div class="section-heading"><p class="kicker">The complete installation</p><h2>Explain the installed system, not just the box.</h2><p>Useful pages answer the questions that lead to a property review without selecting equipment or giving electrical, fuel, placement, or code advice online.</p></div><div class="cards"><article class="card"><span class="tag">Loads</span><h3>What needs backup power?</h3><p>Prepare for a professional conversation about essential circuits, selected loads, and broader coverage.</p></article><article class="card"><span class="tag">Fuel</span><h3>What fuel is available?</h3><p>Explain why fuel planning and qualified providers may be part of the installed scope.</p></article><article class="card"><span class="tag">Placement</span><h3>What must the property support?</h3><p>Access, utilities, noise, exhaust, clearances, equipment location, and local rules can affect the project.</p></article></div><p class="callout">The final system must be based on the actual property and qualified local work. A generic house-size chart is not a substitute for load evaluation or site assessment.</p></div></section>''',
            '''<section class="band"><div class="container"><div class="section-heading"><p class="kicker">Different starting points</p><h2>Homeowners reach the decision for different reasons.</h2></div><div class="cards"><article class="card"><span class="tag">Advance planner</span><h3>Planning before backup power is urgent</h3><p>Wants a system in place before work, travel, medical, weather, or household needs make an outage harder to manage.</p></article><article class="card"><span class="tag">Recent outage</span><h3>Ready to understand the complete project</h3><p>Has a clear reason to act but still needs a property consultation rather than a rushed equipment recommendation.</p></article><article class="card"><span class="tag">Replacement</span><h3>Existing equipment changes the scope</h3><p>Transfer hardware, fuel, monitoring, equipment age, and service history may all matter.</p></article></div></div></section>''',
            '''<section><div class="container two-col"><div><div class="section-heading"><p class="kicker">What REFRDAI builds</p><h2>Give every approved town a useful installation path.</h2><p>Each town receives one main page explaining the complete installation plus two original pages answering different buyer questions.</p></div><ul class="plain-list"><li>How the property consultation begins and what the installer needs.</li><li>Loads, fuel, placement, access, permits, and coordination.</li><li>Transfer equipment, qualified trades, startup, testing, handoff, and future service.</li><li>Current local details only when they are verified and supported.</li></ul></div><aside class="scope-box"><h3>Build trust with verified details</h3><div class="scope-grid"><div class="scope-item"><b>Verified</b><span>No invented dealer badges, licenses, or brand relationships.</span></div><div class="scope-item"><b>Local</b><span>Real permit, fuel, inspection, and utility context only.</span></div><div class="scope-item"><b>Complete</b><span>Explain the installed system, not just equipment.</span></div><div class="scope-item"><b>Measured</b><span>Review search visibility and engagement by town after launch.</span></div></div></aside></div></section>''',
        ],
        "primary_scope": "One primary standby-generator service",
        "review_h2": "Which towns do you want more complete standby-installation consultations from?",
        "faqs": [
            ("Is this for portable-generator sales?", "No. This page is for complete permanently installed standby systems unless a different primary service is separately approved."),
            ("Will the website recommend generator size?", "No. Qualified professionals must evaluate the actual property, loads, fuel, equipment, and local requirements."),
            ("Can the website feature brands and dealer status?", "Yes, only when the information is current, verified, and approved for public use."),
            ("Does my company own the website?", "Yes. You own and keep the completed site even if you decline optional annual territory protection."),
            ("Are standby installations guaranteed?", "No. REFRDAI does not guarantee indexing, rankings, consultations, installations, sales, or revenue."),
            ("Is managed hosting included?", "Yes, under normal usage. Unlimited hosting is not promised."),
            ("Does submitting the form enroll me in anything?", "No. It requests a free review only. It does not authorize a purchase, automatic outreach, or enrollment."),
        ],
    },
    "drainage-grading-erosion-control-contractors": {
        "industry": "drainage-grading-erosion-control",
        "title": "Drainage and Grading Contractor Territory Websites | REFRDAI",
        "meta": "A customer-owned territory website for drainage, grading, and erosion-control contractors pursuing site-evaluation and correction projects.",
        "og_title": "Territory Websites for Drainage and Grading Contractors",
        "og_desc": "Help property owners explain where water starts, where it moves, and what it affects before a correction is recommended.",
        "page_name": "Territory websites for drainage, grading, and erosion-control contractors",
        "page_desc": "A REFRDAI offer for contractors that want a customer-owned territory website focused on one drainage, grading, or erosion-control service.",
        "service_name": "REFRDAI territory website for drainage and grading contractors",
        "service_desc": "A $3,400 customer-owned territory website for one primary drainage, grading, or erosion-control service within an agreed 30-mile radius.",
        "crumb": "Drainage, Grading, and Erosion Control",
        "eyebrow": "For drainage, grading, and erosion-control contractors",
        "h1": "Be easier to find for water and grading projects in the towns you serve.",
        "hero": "A wet yard, washed slope, flooded drive, and foundation-side drainage complaint may look similar online but require different investigation. REFRDAI builds a separate website your company owns alongside its current site, focused on the water or grading problem your company is equipped to correct.",
        "secondary_href": "#water-path",
        "secondary": "Follow the Water-Decision Path",
        "fine": "The website will not diagnose a property, claim engineered design, promise permits, or guarantee rankings, inquiries, projects, or revenue.",
        "panel_title": "Start with how water moves across the property.",
        "panel_intro": "Useful pages help an owner describe the source, path, symptom, and possible outlet before asking which correction may fit.",
        "panel_steps": [
            ("S", "Source", "Roof runoff, uphill land, streets, hard surfaces, groundwater, disturbed soil, or an unknown source."),
            ("P", "Path", "Across the yard, toward a structure, down a slope, through a drive, or into a low area."),
            ("O", "Outlet", "Where collected water may be able to go legally and safely after professional evaluation."),
        ],
        "offer": [
            ("One primary water or grading service", "Focus the first build instead of presenting a generic excavation catalog."),
            ("One agreed 30-mile territory", "The website includes terrain, rainfall, soil, and local-rule information only when it is supported by reliable sources."),
            ("One website your company owns", "The new territory website runs alongside your current site."),
        ],
        "sections": [
            '''<section id="water-path"><div class="container"><div class="section-heading"><p class="kicker">Read the whole property</p><h2>Help owners understand why the visible symptom may not reveal the full scope.</h2><p>A useful drainage page does not jump from “standing water” to one standard product. It explains why elevations, soil, runoff, structures, and discharge conditions matter.</p></div><div class="decision-path"><article class="decision-step"><span class="step-number">01</span><div><strong>Document what happens during and after rain</strong><p>Where water appears, how long it remains, which direction it moves, and what property or access it affects.</p></div></article><article class="decision-step"><span class="step-number">02</span><div><strong>Read the site, not only the wet spot</strong><p>Slopes, low points, roof discharge, neighboring grade, driveways, retaining features, compacted soil, and disturbed areas may change the correction.</p></div></article><article class="decision-step"><span class="step-number">03</span><div><strong>Define the intended result</strong><p>Protect a structure, restore usable yard, stabilize soil, keep a drive passable, prepare construction, or manage runoff without shifting harm elsewhere.</p></div></article></div><p class="callout">Grading work should account for slopes, drainage patterns, land use, soil, and stormwater controls. <a href="https://www.epa.gov/system/files/documents/2021-11/bmp-land-grading.pdf">Review U.S. EPA land-grading guidance</a>.</p></div></section>''',
            '''<section class="band"><div class="container"><div class="section-heading"><p class="kicker">Choose the correction</p><h2>Choose the drainage, grading, or erosion-control service you want the first build to make clear.</h2></div><div class="cards"><article class="card"><span class="tag">Drainage correction</span><h3>Manage water responsibly</h3><p>Explain collection, conveyance, infiltration, discharge, roof water, surface flow, and the conditions that shape the next decision.</p></article><article class="card"><span class="tag">Grading</span><h3>Reshape the site for a defined result</h3><p>Explain rough or finish grading, elevation relationships, access, soil, stabilization, drainage patterns, and plan coordination.</p></article><article class="card"><span class="tag">Erosion control</span><h3>Keep disturbed soil from continuing to move</h3><p>Address bare slopes, washouts, concentrated runoff, sediment movement, stabilization, and maintenance without claiming engineering authority.</p></article></div></div></section>''',
            '''<section><div class="container two-col"><div><div class="section-heading"><p class="kicker">Prepare for evaluation</p><h2>Answer the questions that prepare an owner for evaluation.</h2></div><ul class="plain-list"><li>Why does water collect in this part of the property?</li><li>When might grading be part of a drainage correction?</li><li>What should the owner document before a site visit?</li><li>Where may collected water discharge?</li><li>How can disturbed soil and slope conditions affect the project sequence?</li></ul></div><aside class="scope-box"><h3>Every approved town gets three useful pages</h3><p>One main town-and-service page plus two original town-specific question pages.</p><div class="scope-grid"><div class="scope-item"><b>Supported local information</b><span>Rainfall, soil, permit, and drainage-rule statements are tied to reliable local sources.</span></div><div class="scope-item"><b>No instant diagnosis</b><span>Photos do not replace site evaluation.</span></div><div class="scope-item"><b>No shifted harm</b><span>Content will not advise moving water onto another property.</span></div><div class="scope-item"><b>No false authority</b><span>Engineering, utility, and permit roles stay accurate.</span></div></div></aside></div></section>''',
        ],
        "primary_scope": "One primary drainage, grading, or erosion-control service",
        "review_h2": "Where do you want more drainage, grading, or erosion-control projects worth evaluating?",
        "faqs": [
            ("Can the website diagnose a drainage problem from a photo?", "No. Photos can show symptoms, but the correction depends on the whole property and professional evaluation."),
            ("Can one build target every excavation service?", "No. The first build focuses on one primary drainage, grading, or erosion-control service."),
            ("Can local permit information be included?", "Yes, only when it is current, authoritative, relevant, and clearly attributed."),
            ("Who owns the new website?", "You own and keep it. The territory website runs alongside your current site."),
            ("Are drainage or grading projects guaranteed?", "No. REFRDAI does not guarantee indexing, rankings, inquiries, projects, or revenue."),
            ("Is annual renewal mandatory?", "No. The $495 review is optional. Declining it ends territory protection, not ownership of the website or domain."),
            ("Is managed hosting included?", "Yes, under normal usage. Unlimited hosting is not promised."),
        ],
    },
    "inground-pool-builders": {
        "industry": "inground-pool-construction",
        "title": "Inground-Pool Builder Territory Websites | REFRDAI",
        "meta": "A customer-owned territory website for inground-pool builders pursuing complete design-build consultations in more towns they serve.",
        "og_title": "Territory Websites for Inground-Pool Builders",
        "og_desc": "Help homeowners move from pool inspiration to a useful design, property, budget, and construction conversation.",
        "page_name": "Territory websites for inground-pool builders",
        "page_desc": "A REFRDAI offer for inground-pool builders that want a customer-owned territory website focused on one new-pool construction service.",
        "service_name": "REFRDAI territory website for inground-pool builders",
        "service_desc": "A $3,400 customer-owned territory website for one primary inground-pool construction service within an agreed 30-mile radius.",
        "crumb": "Inground-Pool Builders",
        "eyebrow": "For inground-pool design-build companies",
        "h1": "Be easier to find for complete inground-pool projects, not routine pool service.",
        "hero": "Cleaning, equipment, liner repair, retail, and new construction can appear in the same search results while leading to very different calls. REFRDAI builds a separate website your company owns alongside its current site, making your inground-pool design-build service clear before the consultation.",
        "secondary_href": "#pool-path",
        "secondary": "See the Pool-Buyer Path",
        "fine": "REFRDAI does not invent project prices or build times and does not guarantee permits, rankings, consultations, contracts, or revenue.",
        "panel_title": "A qualified pool inquiry includes more than shape and price.",
        "panel_intro": "Useful pages help a homeowner think through the desired experience, the property, and the construction process without burying the buyer in trade jargon.",
        "panel_steps": [
            ("01", "Desired experience", "Family use, entertaining, exercise, a landscape centerpiece, a compact yard, or a larger outdoor-living plan."),
            ("02", "Property conditions", "Access, slope, utilities, setbacks, drainage, soil, existing structures, and neighborhood requirements."),
            ("03", "Build fit", "Pool type, design process, budget readiness, schedule, selections, approvals, and the builder’s real capacity."),
        ],
        "offer": [
            ("New-construction focus", "Keep the first build focused on new inground construction rather than repair, cleaning, retail, or above-ground service."),
            ("A practical build territory", "Focus the territory on towns where your company accepts complete inground-pool projects."),
            ("One website your company owns", "The new territory website runs alongside your current site."),
        ],
        "sections": [
            '''<section id="pool-path"><div class="container"><div class="section-heading"><p class="kicker">The buyer’s decision</p><h2>A long project decision deserves useful answers.</h2><p>The territory website does more than display a gallery. It answers the questions that determine whether a design consultation fits the homeowner and the builder.</p></div><div class="decision-path"><article class="decision-step"><span class="step-number">01</span><div><strong>Vision</strong><p>How does the household want to use the pool and surrounding space?</p></div></article><article class="decision-step"><span class="step-number">02</span><div><strong>Property</strong><p>What access, grade, utilities, drainage, setbacks, existing features, and plans may affect the project?</p></div></article><article class="decision-step"><span class="step-number">03</span><div><strong>Choices and readiness</strong><p>Which build type, features, finishes, timing, decision makers, and budget conversation belong in the consultation?</p></div></article></div><p class="callout">Your website explains your real design and construction process without giving homeowners unsafe technical instructions. <a href="https://www.phta.org/education-and-events/education/construction-courses/">Review Pool &amp; Hot Tub Alliance construction topics</a>.</p></div></section>''',
            '''<section class="band"><div class="container"><div class="section-heading"><p class="kicker">Clarify project fit</p><h2>Clarify project fit without talking down to the homeowner.</h2></div><div class="cards"><article class="card"><span class="tag">New construction</span><h3>Is this a new inground build?</h3><p>Homeowners can quickly see whether you build fiberglass, vinyl-liner, concrete, gunite, custom, or another verified pool type.</p></article><article class="card"><span class="tag">Service area</span><h3>Is the property inside the real territory?</h3><p>The website covers towns inside your practical construction service area.</p></article><article class="card"><span class="tag">Consultation</span><h3>Is the household ready for design and site review?</h3><p>Invite a practical conversation about goals, property, choices, timing, decision makers, and budget without inventing minimums.</p></article></div></div></section>''',
            '''<section><div class="container two-col"><div><div class="section-heading"><p class="kicker">What REFRDAI builds</p><h2>Give each approved town a useful pool-construction path.</h2><p>One main town-and-service page explains the builder, build types, property fit, and consultation. Two original question pages address different decisions.</p></div><ul class="plain-list"><li>Is the property ready for pool design?</li><li>What should the buyer decide before consulting?</li><li>How do access, grade, utilities, setbacks, drainage, and approvals affect planning?</li><li>How should desired use, options, timing, decision makers, and budget be organized?</li></ul></div><aside class="scope-box"><h3>Use real project proof</h3><p>Photos, designs, testimonials, awards, brands, financing, warranties, and price ranges appear only when verified and approved.</p><div class="scope-grid"><div class="scope-item"><b>Real portfolio</b><span>Never present stock imagery as completed client work.</span></div><div class="scope-item"><b>Clear build types</b><span>Claim only construction methods the builder provides.</span></div><div class="scope-item"><b>Accurate territory</b><span>Use towns inside the practical service area.</span></div><div class="scope-item"><b>Honest timing</b><span>Do not promise a generic completion date.</span></div></div></aside></div></section>''',
        ],
        "primary_scope": "One primary inground-pool construction service",
        "review_h2": "Which towns do you want more inground-pool design consultations from?",
        "faqs": [
            ("Can the first build focus only on new inground-pool construction?", "Yes. It can clearly exclude cleaning, repair, retail, and above-ground inquiries."),
            ("Will REFRDAI publish pool prices?", "Only verified, builder-approved pricing or qualification ranges. REFRDAI will not invent a project price."),
            ("Can the website use completed-project photos?", "Yes, when the builder owns the images or has permission to use them and the captions are accurate."),
            ("Will this replace the builder’s current website?", "No. The customer-owned territory website runs alongside it."),
            ("Are pool consultations or contracts guaranteed?", "No. REFRDAI does not guarantee indexing, rankings, consultations, contracts, or revenue."),
            ("Is the annual plan required?", "No. The $495 review is optional. It may renew territory protection and includes the applicable domain renewal for that term. It does not determine ownership of the site or domain."),
            ("How many pages are built for each approved town?", "One main town-and-service page plus two original town-specific customer-question pages."),
        ],
    },
}


def faq_schema(faqs):
    return [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
        for q, a in faqs
    ]


def head(slug: str, page: dict) -> str:
    url = f"https://local.refrdai.com/industries/{slug}/"
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebPage", "@id": url + "#page", "url": url, "name": page["page_name"], "description": page["page_desc"], "inLanguage": "en-US", "isPartOf": {"@id": "https://local.refrdai.com/#website"}, "about": {"@id": url + "#service"}},
            {"@type": "Service", "@id": url + "#service", "name": page["service_name"], "description": page["service_desc"], "serviceType": "Customer-owned territory website build", "provider": {"@id": "https://refrdai.com/#organization"}, "areaServed": {"@type": "Country", "name": "United States"}, "offers": {"@type": "Offer", "price": "3400", "priceCurrency": "USD", "description": "One-time initial build. $1,700 to begin and $1,700 after staging approval, before launch."}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "REFRDAI Local", "item": "https://local.refrdai.com/"},
                {"@type": "ListItem", "position": 2, "name": "Industries", "item": "https://local.refrdai.com/industries/"},
                {"@type": "ListItem", "position": 3, "name": page["crumb"], "item": url},
            ]},
            {"@type": "FAQPage", "mainEntity": faq_schema(page["faqs"])},
        ],
    }
    return f'''<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(page["title"])}</title><meta name="description" content="{escape(page["meta"], quote=True)}"><meta name="author" content="William Smith, Founder of REFRDAI"><meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large"><meta name="theme-color" content="#21ddb4"><link rel="canonical" href="{url}"><link rel="manifest" href="/manifest.json"><link rel="stylesheet" href="/assets/industry-pages.css"><meta property="og:type" content="website"><meta property="og:site_name" content="REFRDAI Local"><meta property="og:locale" content="en_US"><meta property="og:url" content="{url}"><meta property="og:title" content="{escape(page["og_title"], quote=True)}"><meta property="og:description" content="{escape(page["og_desc"], quote=True)}"><meta property="og:image" content="https://local.refrdai.com/assets/local-refrdai-social-preview.png"><meta property="og:image:alt" content="REFRDAI Territory Expansion map"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{escape(page["og_title"], quote=True)}"><meta name="twitter:description" content="{escape(page["og_desc"], quote=True)}"><script type="application/ld+json">{json.dumps(data, ensure_ascii=False, separators=(",", ":"))}</script></head>'''


def nav_and_hero(page: dict) -> str:
    steps = "".join(f'<div class="flow-item"><span class="flow-num">{escape(n)}</span><div><b>{escape(h)}</b><span>{escape(p)}</span></div></div>' for n, h, p in page["panel_steps"])
    facts = "".join(f'<div class="offer-fact"><b>{escape(h)}</b><span>{escape(p)}</span></div>' for h, p in page["offer"])
    return f'''<a class="skip" href="#main">Skip to main content</a><nav class="site-nav" aria-label="Primary navigation"><div class="container nav-inner"><a class="brand" href="/"><span class="brand-mark" aria-hidden="true">RD</span><span class="brand-name"><em>REFR</em>DAI · Local</span></a><div class="nav-links"><a href="/industries/">Industries</a><a href="#investment">Investment</a><a class="button button-primary" data-track="primary-cta" href="#territory-review">Request My Free 15-Minute Territory Review</a></div></div></nav><div class="container breadcrumb"><a href="/">Home</a> / <a href="/industries/">Industries</a> / {escape(page["crumb"])}</div><header class="hero"><div class="container hero-grid"><div><p class="eyebrow">{escape(page["eyebrow"])}</p><h1>{escape(page["h1"])}</h1><p class="hero-copy">{escape(page["hero"])}</p><div class="hero-actions"><a class="button button-primary" data-track="primary-cta" href="#territory-review">Request My Free 15-Minute Territory Review</a><a class="button button-secondary" href="{page["secondary_href"]}">{escape(page["secondary"])}</a></div><p class="fine-print">{escape(page["fine"])}</p></div><aside class="trade-panel"><h2>{escape(page["panel_title"])}</h2><p>{escape(page["panel_intro"])}</p><div class="trade-flow">{steps}</div></aside></div></header><div class="offer-strip" data-qa-shared="true"><div class="container offer-facts">{facts}</div></div>'''


def investment(page: dict) -> str:
    return f'''<section class="band" id="investment" data-qa-shared="true"><div class="container"><div class="section-heading"><p class="kicker">Clear investment</p><h2>Know the full initial price before you book.</h2><p>The customer-owned territory website costs $3,400.</p></div><div class="pricing"><article class="price-card"><span class="price-label">One-time initial build</span><div class="price">$3,400 <small>total</small></div><p>{escape(page["primary_scope"])}, one agreed 30-mile radius, and every eligible approved community, up to 100.</p><div class="payment-split"><div><b>$1,700</b><span>To begin production</span></div><div><b>$1,700</b><span>After staging approval, before launch</span></div></div><p>REFRDAI pays for the domain’s first year and transfers it after launch and cleared final payment as soon as the registrar permits. Managed hosting under normal usage is included.</p></article><div class="options"><article class="option-card"><span class="optional-label">Optional after the first year</span><h3>$495 Territory Continuity Review</h3><p>Includes the applicable domain renewal for that term and may renew territory protection after a scope and conflict review plus written renewal. If declined, you keep the site and domain, protection expires, and you pay the registrar directly for future renewal.</p></article><article class="option-card"><span class="optional-label">Separate and never automatic</span><h3>Possible $500 monthly expansion</h3><p>May be offered around month three only when enough usable search-performance data exists. It is optional and never starts automatically.</p></article></div></div></div></section>'''


def faq_section(page: dict) -> str:
    cards = "".join(f'<article class="faq"><h3>{escape(q)}</h3><p>{escape(a)}</p></article>' for q, a in page["faqs"])
    return f'''<section><div class="container"><div class="section-heading"><p class="kicker">Questions before the review</p><h2>{escape(page["crumb"])} questions</h2><p>Clear answers before you decide whether the first build fits.</p></div><div class="faq-grid">{cards}</div></div></section>'''


def review(page: dict) -> str:
    return f'''<section class="review-section band" id="territory-review" data-qa-shared="true"><div class="container review-grid"><div class="review-copy"><p class="kicker">Free 15-minute review</p><h2>{escape(page["review_h2"])}</h2><p>Share your company name, company website, email, and the towns or counties you want to review. Phone is optional.</p><div class="review-facts"><div class="review-fact"><b>Meeting</b><span>15-minute Google Meet</span></div><div class="review-fact"><b>Hours</b><span>Monday through Friday, 10:00 AM to 5:00 PM Eastern</span></div><div class="review-fact"><b>Booking</b><span>At least 24 hours ahead and up to 30 days out</span></div><div class="review-fact"><b>Cost</b><span>Free, with no purchase obligation</span></div></div><p class="privacy">Submitting the form does not authorize automatic outreach, enrollment, or a purchase.</p></div><div class="form-card"><h2>Request My Free 15-Minute Territory Review</h2><p>Complete the short intake, then choose an available Google Meet time.</p><script src="https://js.hsforms.net/forms/embed/{PORTAL_ID}.js" defer></script><div class="hs-form-frame" data-region="na1" data-form-id="{FORM_ID}" data-portal-id="{PORTAL_ID}"></div><noscript><p>JavaScript is required to load the intake form.</p></noscript><a class="form-fallback" href="{FORM_FALLBACK}" rel="nofollow">Open the Secure Intake Form</a><div class="booking-panel" data-booking-panel aria-hidden="true"><h3>Choose Your 15-Minute Review Time</h3><p>The appointment calendar appears after a successful form submission.</p><iframe title="Book a Territory Opportunity Review with William Smith" src="{BOOKING}" loading="lazy"></iframe><a class="booking-fallback" data-booking-link href="{BOOKING}">Open Google Calendar in a New Page</a></div></div></div></section>'''


def render(slug: str, page: dict) -> str:
    sections = "".join(page["sections"])
    return f'''<!doctype html><html lang="en-US">{head(slug, page)}<body data-industry="{page["industry"]}">{nav_and_hero(page)}<main id="main">{sections}{investment(page)}{faq_section(page)}{review(page)}</main><footer><div class="container footer-inner"><span>© 2026 REFRDAI Local. Customer-owned territory websites for local service businesses.</span><div class="footer-links"><a href="/">Home</a><a href="/industries/">Industries</a><a href="/entity-source-of-truth/">Definitions</a><a href="/insights/">Insights</a></div></div></footer><script src="/assets/industry-pages.js" defer></script></body></html>\n'''


for slug, page in PAGES.items():
    path = ROOT / "industries" / slug / "index.html"
    path.write_text(render(slug, page), encoding="utf-8", newline="\n")
    print(f"Rewrote copy: {path}")
