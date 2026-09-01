from __future__ import annotations

import json
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOKING = "https://calendar.app.google/qwZB5sgoY74tPssA6"
FORM_ID = "b972ec68-3a3b-47f8-b97d-d07a1e077474"
PORTAL_ID = "49371050"
FORM_FALLBACK = "https://te6y2.share.hsforms.com/2uXLsaDo7R_i5fdB6Hgd0dA"


PAGES: dict[str, dict] = {}


PAGES.update({
    "tree-service-companies": {
        "industry": "tree-service",
        "title": "Tree Service Marketing & Lead Generation | REFRDAI",
        "meta": "Tree service marketing and lead generation for removal, storm cleanup, hazard evaluation, and other high-value tree projects in more towns.",
        "og_title": "Tree Service Marketing & Lead Generation",
        "og_desc": "Help property owners find your tree company for the work your crews and equipment are prepared to handle.",
        "page_name": "Tree service marketing and lead generation",
        "page_desc": "A REFRDAI offer for tree companies that want a customer-owned territory website focused on one high-value tree service.",
        "service_name": "REFRDAI territory website for tree service companies",
        "service_desc": "A $3,400 customer-owned territory website for one primary tree service within an agreed 30-mile radius.",
        "crumb": "Tree Service Companies",
        "eyebrow": "Tree service marketing and lead generation",
        "h1": "Be easier to find for tree work that fits your crews, equipment, and response capacity.",
        "hero": "A leaning tree near a roof, a planned removal beside a driveway, and storm debris across a property are not the same sales conversation. REFRDAI builds a separate website your company owns alongside its current site, focused on one tree service and the towns where you want better-fit requests.",
        "secondary_href": "#tree-call",
        "secondary": "See the Tree-Work Decision Path",
        "fine": "The website does not evaluate a tree remotely or guarantee calls, removals, storm demand, rankings, contracts, or revenue.",
        "panel_title": "A tree-work request starts with risk, access, and scope.",
        "panel_intro": "Useful pages help an owner explain what is happening before your company decides whether an inspection, estimate, or emergency response is appropriate.",
        "panel_steps": [
            ("01", "What changed?", "A visible defect, storm damage, construction conflict, dead tree, clearance problem, or planned landscape change."),
            ("02", "What could be affected?", "People, a home, vehicles, utilities, neighboring property, access routes, or other trees."),
            ("03", "What does the site allow?", "Crew access, equipment position, rigging space, slope, gates, overhead lines, debris handling, and stump expectations."),
        ],
        "offer": [
            ("One primary tree service", "Choose removal, storm cleanup, hazard evaluation, or another clearly defined service."),
            ("A realistic response territory", "Focus on towns your crews can serve safely and profitably."),
            ("A website your company owns", "The new territory website runs alongside your current site."),
        ],
        "sections": [
            '''<section id="tree-call"><div class="container"><div class="section-heading"><p class="kicker">Separate urgency from panic</p><h2>Help owners describe the situation without diagnosing the tree online.</h2><p>Some callers need prompt professional attention. Others are planning work weeks or months ahead. The page gives both a useful path while leaving the site-specific judgment to a qualified tree professional.</p></div><div class="decision-path"><article class="decision-step"><span class="step-number">Now</span><div><strong>Immediate danger or blocked access</strong><p>Tell owners how to reach the company and when to contact emergency services or the utility instead of approaching a hazardous area.</p></div></article><article class="decision-step"><span class="step-number">Soon</span><div><strong>New damage or a concerning change</strong><p>Invite photos and property details while making clear that an image cannot replace an on-site evaluation.</p></div></article><article class="decision-step"><span class="step-number">Plan</span><div><strong>Removal, clearance, or construction preparation</strong><p>Prepare the owner to discuss goals, access, neighboring property, debris, stump work, timing, and written scope.</p></div></article></div><p class="callout">Professional tree work depends on current practices, qualifications, and job-specific specifications. <a href="https://treecareindustryassociation.org/business-support/ansi-a300-standards/">Review the ANSI A300 tree-care standards overview</a>.</p></div></section>''',
            '''<section class="band"><div class="container two-col"><div><div class="section-heading"><p class="kicker">Better-fit requests</p><h2>Show the work you want before the phone rings.</h2><p>A tree company may prune, remove, cable, grind stumps, clear rights of way, or handle storm work. The first build should not pretend every company offers every service.</p></div><ul class="plain-list"><li>Name the primary service and whether estimates, inspections, or emergency routing are available.</li><li>Explain the property information that helps your team judge access and equipment needs.</li><li>State real insurance, credentials, licenses, and affiliations only when verified.</li><li>Clarify wood, brush, chip, log, and stump responsibilities before the estimate.</li><li>Give owners a direct path to call or request an estimate from your company.</li></ul></div><aside class="scope-box"><h3>Trust matters around expensive property</h3><p>The page should help an owner evaluate professionalism without using fear to force a call.</p><div class="scope-grid"><div class="scope-item"><b>Real crew</b><span>Use actual capabilities rather than generic claims.</span></div><div class="scope-item"><b>Clear scope</b><span>Separate removal, pruning, cleanup, and stump work.</span></div><div class="scope-item"><b>Safe language</b><span>Do not tell an owner to inspect a dangerous tree.</span></div><div class="scope-item"><b>Local fit</b><span>Cover towns inside the practical response area.</span></div></div></aside></div></section>''',
            '''<section><div class="container"><div class="section-heading"><p class="kicker">Town-by-town usefulness</p><h2>Build around the tree questions property owners actually ask.</h2><p>Every approved town receives one main service page and two original question pages. The questions can vary with storm exposure, lot patterns, utilities, access, local rules, and the tree service selected for the first build.</p></div><div class="cards"><article class="card"><span class="tag">Property</span><h3>Can the crew reach the work?</h3><p>Discuss gates, driveways, slopes, lawns, neighboring land, structures, and equipment position without quoting from a photo.</p></article><article class="card"><span class="tag">Scope</span><h3>What happens to the material?</h3><p>Explain the company’s normal options for wood, brush, chips, logs, stump grinding, and site cleanup.</p></article><article class="card"><span class="tag">Next step</span><h3>What should the owner prepare?</h3><p>Request the location, reason for concern, recent changes, access notes, photos when safe, and the owner’s preferred result.</p></article></div></div></section>''',
        ],
        "primary_scope": "One primary tree service",
        "review_h2": "Which towns do you want more removal, storm, or planned tree-work requests from?",
        "faqs": [
            ("Can the page promise emergency availability?", "Only when the company has verified that availability and defines how emergency requests are handled."),
            ("Will the website decide whether a tree is dangerous?", "No. It can help an owner describe the concern, but a qualified professional must evaluate the tree and site."),
            ("Can we focus on removals instead of routine pruning?", "Yes. The first build can focus on one primary tree service and clearly separate other work."),
            ("Can the site show our equipment and credentials?", "Yes, when the equipment, insurance, credentials, licenses, and affiliations are current and approved for public use."),
            ("Does this replace our current website?", "No. The customer-owned territory website runs alongside it."),
            ("Are tree-service leads guaranteed?", "No. REFRDAI does not guarantee indexing, rankings, inquiries, estimates, contracts, or revenue."),
            ("Who owns the completed website?", "Your company owns and keeps the website and domain. The optional annual plan is not required for ownership."),
        ],
    },
    "asphalt-paving-contractors": {
        "industry": "asphalt-paving",
        "title": "Asphalt Paving Marketing & Lead Generation | REFRDAI",
        "meta": "Asphalt paving marketing and lead generation for driveway, parking-lot, resurfacing, and other paving projects in more towns.",
        "og_title": "Asphalt Paving Marketing & Lead Generation",
        "og_desc": "Help property owners and managers find your paving company for projects that fit your crew and production schedule.",
        "page_name": "Asphalt paving contractor marketing and lead generation",
        "page_desc": "A REFRDAI offer for asphalt paving companies that want a customer-owned territory website focused on one paving service.",
        "service_name": "REFRDAI territory website for asphalt paving contractors",
        "service_desc": "A $3,400 customer-owned territory website for one primary asphalt paving service within an agreed 30-mile radius.",
        "crumb": "Asphalt Paving Contractors",
        "eyebrow": "Asphalt paving marketing and lead generation",
        "h1": "Get found for paving projects that match your crew, equipment, and minimum job size.",
        "hero": "A residential driveway, a retail parking lot, and an industrial access road create different estimating and scheduling demands. REFRDAI builds a separate website your company owns alongside its current site, focused on the paving work you want in the towns your operation can serve well.",
        "secondary_href": "#paving-fit",
        "secondary": "See the Paving-Project Path",
        "fine": "REFRDAI does not diagnose pavement from photos or guarantee bids, awarded projects, rankings, production volume, or revenue.",
        "panel_title": "A useful paving request starts below the surface.",
        "panel_intro": "Owners often ask for a price by square foot before the contractor has enough information about use, drainage, base condition, access, or phasing.",
        "panel_steps": [
            ("Use", "How will the surface be used?", "Passenger vehicles, trucks, deliveries, parking, private access, commercial traffic, or another defined use."),
            ("Site", "What is there now?", "Existing pavement, gravel, soil, drainage problems, soft areas, edge failure, utilities, structures, and traffic constraints."),
            ("Plan", "How must work be staged?", "Access, shutdown windows, tenant needs, striping, drainage, curing or reopening expectations, and other trades."),
        ],
        "offer": [
            ("One paving service", "Choose driveways, parking lots, resurfacing, or another primary project type."),
            ("A production-aware territory", "Cover towns that fit hauling, crew movement, plant access, and project economics."),
            ("An owned marketing asset", "The territory website belongs to your company."),
        ],
        "sections": [
            '''<section id="paving-fit"><div class="container two-col"><div><div class="section-heading"><p class="kicker">Qualify the surface</p><h2>Move the conversation beyond “How much per square foot?”</h2><p>Useful paving content helps an owner understand why area alone does not settle the scope. The page prepares the facts your estimator needs without turning a marketing page into a pavement design.</p></div><ul class="plain-list"><li>Approximate dimensions and intended traffic.</li><li>Existing surface and known base or drainage concerns.</li><li>Edges, slopes, structures, utilities, gates, and equipment access.</li><li>Removal, grading, drainage, paving, striping, and cleanup responsibilities.</li><li>Commercial phasing, business access, and reopening constraints.</li></ul><p class="callout">Asphalt work spans construction, maintenance, rehabilitation, and different pavement uses. <a href="https://www.asphaltpavement.org/">Explore National Asphalt Pavement Association resources</a>.</p></div><aside class="scope-box"><h3>Choose the lane you want to sell</h3><div class="scope-grid"><div class="scope-item"><b>New paving</b><span>Prepare a new drive, lot, or access surface.</span></div><div class="scope-item"><b>Replacement</b><span>Remove and rebuild when that is the actual scope.</span></div><div class="scope-item"><b>Resurfacing</b><span>Explain evaluation before an overlay is assumed.</span></div><div class="scope-item"><b>Commercial work</b><span>Address traffic, tenants, striping, and phasing.</span></div></div></aside></div></section>''',
            '''<section class="band"><div class="container"><div class="section-heading"><p class="kicker">The estimate path</p><h2>Help the right project reach the estimator with useful details.</h2></div><div class="decision-path"><article class="decision-step"><span class="step-number">01</span><div><strong>Identify the surface and use</strong><p>Is this a home driveway, private road, commercial lot, industrial yard, farm access, or another verified project type?</p></div></article><article class="decision-step"><span class="step-number">02</span><div><strong>Review current condition</strong><p>Cracking, settling, rutting, ponding, failed edges, vegetation, patching, and previous overlays may affect the site conversation.</p></div></article><article class="decision-step"><span class="step-number">03</span><div><strong>Plan access and staging</strong><p>Equipment movement, material delivery, business continuity, neighboring access, and weather-sensitive scheduling belong in the estimate process.</p></div></article><article class="decision-step"><span class="step-number">04</span><div><strong>Write the actual scope</strong><p>Make removal, base work, drainage, thickness, edges, striping, and exclusions clear only after the contractor evaluates the project.</p></div></article></div></div></section>''',
            '''<section><div class="container"><div class="section-heading"><p class="kicker">Local project pages</p><h2>Give every approved town a paving story that fits the market.</h2><p>A rural driveway page should not read like a shopping-center lot page. Town-specific questions can address traffic type, site access, local permitting, drainage responsibility, seasonal scheduling, commercial phasing, or the contractor’s chosen project minimum.</p></div><div class="cards"><article class="card"><span class="tag">Homeowners</span><h3>Driveway planning</h3><p>Explain measurements, access, existing material, drainage observations, edges, parking needs, and the estimate visit.</p></article><article class="card"><span class="tag">Property managers</span><h3>Parking-lot planning</h3><p>Address tenants, entrances, striping, accessible spaces, loading areas, work windows, and communication responsibilities.</p></article><article class="card"><span class="tag">Operators</span><h3>Private-road and work-yard planning</h3><p>Start with vehicle type, drainage, grades, traffic disruption, material movement, and long-term use.</p></article></div></div></section>''',
        ],
        "primary_scope": "One primary asphalt paving service",
        "review_h2": "Which towns do you want more driveway, lot, or resurfacing requests from?",
        "faqs": [
            ("Can the website quote a paving price per square foot?", "Only if the contractor supplies and approves a truthful range with its conditions. The website will not invent a price."),
            ("Can we focus only on commercial parking lots?", "Yes. The first build can focus on one primary paving service and buyer type."),
            ("Will the pages say an overlay is always possible?", "No. Existing condition, drainage, base, traffic, and other factors require contractor evaluation."),
            ("Can we publish our project minimum?", "Yes, when the company verifies and approves the minimum and any conditions."),
            ("Will this change our current website?", "No. The customer-owned territory website runs alongside it."),
            ("Are paving bids or projects guaranteed?", "No. REFRDAI does not guarantee indexing, rankings, inquiries, bids, contracts, or revenue."),
            ("Is the optional annual review required?", "No. It may renew territory protection and includes the applicable domain renewal for that term, but it is not required to own the site."),
        ],
    },
    "concrete-driveway-contractors": {
        "industry": "concrete-driveway-flatwork",
        "title": "Concrete Contractor Marketing & Lead Generation | REFRDAI",
        "meta": "Concrete contractor marketing and lead generation for driveways, patios, walkways, slabs, and other selected flatwork projects.",
        "og_title": "Concrete Contractor Marketing & Lead Generation",
        "og_desc": "Help property owners find your concrete company for the flatwork projects you most want to estimate.",
        "page_name": "Concrete contractor marketing and lead generation",
        "page_desc": "A REFRDAI offer for concrete companies that want a customer-owned territory website focused on one driveway or flatwork service.",
        "service_name": "REFRDAI territory website for concrete driveway contractors",
        "service_desc": "A $3,400 customer-owned territory website for one primary concrete flatwork service within an agreed 30-mile radius.",
        "crumb": "Concrete Driveway and Flatwork Contractors",
        "eyebrow": "Concrete contractor marketing and lead generation",
        "h1": "Be easier to find for concrete projects that fit your forms, finishers, and schedule.",
        "hero": "A replacement driveway, decorative patio, equipment pad, and commercial walkway require different preparation, forming, finishing, and coordination. REFRDAI builds a separate website your company owns alongside its current site, focused on one concrete service and the towns where you want more suitable estimate requests.",
        "secondary_href": "#concrete-scope",
        "secondary": "See the Concrete-Project Path",
        "fine": "The website does not design a slab or guarantee estimates, pours, project timing, rankings, contracts, or revenue.",
        "panel_title": "Good concrete inquiries include the use and the site.",
        "panel_intro": "Square footage matters, but so do the intended load, existing material, drainage, access, edges, finish, weather, and surrounding work.",
        "panel_steps": [
            ("01", "What is being built or replaced?", "A driveway, patio, walkway, pad, slab, curb, step, apron, or another selected flatwork project."),
            ("02", "What must happen before placement?", "Removal, excavation, subgrade review, base preparation, drainage planning, forms, reinforcement, and inspections as applicable."),
            ("03", "What finish and use are expected?", "Vehicle traffic, foot traffic, equipment, texture, color, joints, edges, adjacent surfaces, and reopening needs."),
        ],
        "offer": [
            ("One concrete service", "Choose driveways, patios, walkways, slabs, or another clear flatwork focus."),
            ("One workable radius", "Use towns that fit batching, delivery, crew, and scheduling realities."),
            ("Customer-owned website", "Keep the marketing asset alongside your current site."),
        ],
        "sections": [
            '''<section id="concrete-scope"><div class="container"><div class="section-heading"><p class="kicker">From idea to written scope</p><h2>Prepare the owner for the decisions that happen before the pour.</h2><p>Concrete buyers often begin with a photo and dimensions. Useful content shows why the contractor still needs to understand use, site condition, water movement, access, edges, and desired finish.</p></div><div class="cards"><article class="card"><span class="tag">Replacement</span><h3>What must come out?</h3><p>Existing concrete, asphalt, pavers, roots, structures, utilities, poor material, or an unknown base can change the site discussion.</p></article><article class="card"><span class="tag">New work</span><h3>What must the slab support?</h3><p>Passenger vehicles, heavier loads, foot traffic, outdoor living, equipment, drainage, and adjoining surfaces shape the conversation.</p></article><article class="card"><span class="tag">Finish</span><h3>What should the completed surface look and feel like?</h3><p>Broom finish, exposed aggregate, color, pattern, texture, joints, edges, and slip concerns should be discussed accurately.</p></article></div><p class="callout">Concrete quality depends on materials, site preparation, placement, finishing, curing, weather, and applicable project requirements. <a href="https://www.concrete.org/contractors.aspx">Explore American Concrete Institute contractor resources</a>.</p></div></section>''',
            '''<section class="band"><div class="container two-col"><div><div class="section-heading"><p class="kicker">Set expectations honestly</p><h2>Sell craftsmanship without promising crack-free concrete.</h2><p>Owners deserve a plain explanation of the contractor’s process, responsibilities, and warranty language. They do not need an absolute claim that no slab will ever crack, settle, discolor, or change.</p></div><ul class="plain-list"><li>Explain the estimate, measurements, site review, written scope, selections, scheduling, and payment process.</li><li>Describe demolition, haul-off, base, drainage, forming, reinforcement, placement, finishing, joints, curing, and cleanup only as provided.</li><li>Use real project photos and captions that identify the actual work.</li><li>Publish verified license, insurance, certification, warranty, and service-area information.</li><li>Separate structural engineering or code decisions from the contractor’s marketing claims.</li></ul></div><aside class="scope-box"><h3>The page should filter, not overpromise</h3><div class="scope-grid"><div class="scope-item"><b>Right project</b><span>Focus on the flatwork the crew wants.</span></div><div class="scope-item"><b>Right territory</b><span>Account for travel and concrete logistics.</span></div><div class="scope-item"><b>Right proof</b><span>Use verified work, finishes, and capabilities.</span></div><div class="scope-item"><b>Right next step</b><span>Invite an estimate, not an online design.</span></div></div></aside></div></section>''',
            '''<section><div class="container"><div class="section-heading"><p class="kicker">Three pages per town</p><h2>Answer different concrete questions in different communities.</h2><p>One town page presents the primary service. Two original question pages can address replacement planning, drainage, finish selection, access, cold- or hot-weather scheduling, property type, local requirements, or the estimate process when those topics are relevant and supportable.</p></div><div class="decision-path"><article class="decision-step"><span class="step-number">Measure</span><div><strong>Describe the area and intended use</strong><p>Give the estimator a starting point without treating an online measurement as final.</p></div></article><article class="decision-step"><span class="step-number">Review</span><div><strong>Inspect the site and surrounding conditions</strong><p>Look at access, removal, elevations, drainage, utilities, edges, and adjoining construction.</p></div></article><article class="decision-step"><span class="step-number">Specify</span><div><strong>Agree on the work in writing</strong><p>Define materials, preparation, finish, responsibilities, exclusions, schedule, and payment before production.</p></div></article></div></div></section>''',
        ],
        "primary_scope": "One primary concrete driveway or flatwork service",
        "review_h2": "Which towns do you want more driveway, patio, or flatwork estimates from?",
        "faqs": [
            ("Can the website promise that concrete will never crack?", "No. It can explain the company’s process and verified warranty, but it will not make an absolute crack-free promise."),
            ("Can we focus on decorative patios instead of driveways?", "Yes. The first build focuses on one agreed primary concrete service."),
            ("Will REFRDAI calculate slab thickness or reinforcement?", "No. Project requirements must come from the contractor, plans, applicable codes, specifications, or qualified design professionals."),
            ("Can we use our completed-project photos?", "Yes, when your company owns them or has permission and the captions describe the work accurately."),
            ("Does the territory site replace our current website?", "No. It runs alongside your current site."),
            ("Are concrete leads or awarded jobs guaranteed?", "No. REFRDAI does not guarantee indexing, rankings, estimate requests, contracts, or revenue."),
            ("Do we keep the website if we decline the optional annual plan?", "Yes. You keep the website and domain. Only territory protection expires if the optional review is not renewed."),
        ],
    },
    "fence-installation-contractors": {
        "industry": "fence-installation",
        "title": "Fence Contractor Marketing & Lead Generation | REFRDAI",
        "meta": "Fence contractor marketing and lead generation for residential, commercial, privacy, security, and other selected installation projects.",
        "og_title": "Fence Contractor Marketing & Lead Generation",
        "og_desc": "Help property owners find your fence company while they compare purpose, material, layout, gates, and installation fit.",
        "page_name": "Fence contractor marketing and lead generation",
        "page_desc": "A REFRDAI offer for fence companies that want a customer-owned territory website focused on one installation service.",
        "service_name": "REFRDAI territory website for fence installation contractors",
        "service_desc": "A $3,400 customer-owned territory website for one primary fence installation service within an agreed 30-mile radius.",
        "crumb": "Fence Installation Contractors",
        "eyebrow": "Fence contractor marketing and lead generation",
        "h1": "Get found for fence projects that match the customers, materials, and installations you want.",
        "hero": "A backyard privacy fence, pool enclosure, commercial perimeter, farm fence, and automated gate begin with different goals and requirements. REFRDAI builds a separate website your company owns alongside its current site, focused on one fence service and the towns where you want more suitable project inquiries.",
        "secondary_href": "#fence-purpose",
        "secondary": "See the Fence-Buyer Path",
        "fine": "The website does not establish a property line or guarantee permits, inquiries, installations, rankings, contracts, or revenue.",
        "panel_title": "The right fence begins with the reason for building it.",
        "panel_intro": "Purpose guides material, height, visibility, gates, hardware, layout, budget, maintenance, and the approvals that may be needed.",
        "panel_steps": [
            ("Goal", "What must the fence accomplish?", "Privacy, safety, pool protection, pets, livestock, appearance, access control, security, or boundary definition."),
            ("Place", "Where will it go?", "Property information, terrain, utilities, structures, trees, gates, driveways, neighbors, easements, and access."),
            ("Rules", "What must be verified?", "Survey needs, permits, zoning, pool rules, HOA requirements, utility marking, and product-specific standards."),
        ],
        "offer": [
            ("One fence market", "Choose residential privacy, commercial security, farm fencing, gates, or another primary service."),
            ("A practical install territory", "Focus on towns your crews, suppliers, and estimators can support."),
            ("A site your company keeps", "The new website and domain belong to the client."),
        ],
        "sections": [
            '''<section id="fence-purpose"><div class="container"><div class="section-heading"><p class="kicker">Begin with purpose</p><h2>Help buyers compare the fence they need, not every product in a catalog.</h2><p>A useful page narrows the decision without pretending one material or design fits every property. It explains what the contractor installs and what information belongs in the estimate conversation.</p></div><div class="cards"><article class="card"><span class="tag">Residential</span><h3>Privacy, pets, yards, and appearance</h3><p>Prepare the owner to discuss layout, height, gates, grade, neighboring conditions, material choices, maintenance, and household priorities.</p></article><article class="card"><span class="tag">Pool</span><h3>Enclosure and controlled access</h3><p>Make clear that applicable barrier, gate, latch, spacing, permit, and inspection requirements must be verified for the property.</p></article><article class="card"><span class="tag">Commercial</span><h3>Perimeter, traffic, and access control</h3><p>Start with site security, vehicle and pedestrian flow, gate cycles, hardware, operators, emergency access, and written specifications.</p></article></div><p class="callout">Fence contractors work across different project and product types, and credentials can help buyers evaluate professionalism. <a href="https://www.americanfenceassociation.com/page/find_a_contractor/">Review the American Fence Association contractor resource</a>.</p></div></section>''',
            '''<section class="band"><div class="container"><div class="section-heading"><p class="kicker">Prevent the wrong estimate</p><h2>Surface the property questions before material and price take over.</h2></div><div class="decision-path"><article class="decision-step"><span class="step-number">01</span><div><strong>Confirm the desired line and purpose</strong><p>The owner explains what should be enclosed, screened, protected, separated, or controlled.</p></div></article><article class="decision-step"><span class="step-number">02</span><div><strong>Identify responsibility for boundaries and approvals</strong><p>The page never presents a contractor’s visual assumption as a legal property line.</p></div></article><article class="decision-step"><span class="step-number">03</span><div><strong>Walk gates, grade, access, and obstructions</strong><p>Driveways, slopes, utilities, trees, walls, structures, drainage, and equipment access belong in the field conversation.</p></div></article><article class="decision-step"><span class="step-number">04</span><div><strong>Select system and write the scope</strong><p>Define material, posts, height, gates, hardware, removal, disposal, finish, warranty, and exclusions accurately.</p></div></article></div></div></section>''',
            '''<section><div class="container two-col"><div><div class="section-heading"><p class="kicker">Own the local explanation</p><h2>Use town pages to answer the fence questions that vary by place and property.</h2><p>Each approved town receives one main service page and two original question pages. Useful subjects may include survey preparation, pool-barrier planning, terrain, gate placement, material choices, commercial access, HOA coordination, or the estimate process.</p></div><ul class="plain-list"><li>State only the fence types, materials, gate systems, and markets the company actually serves.</li><li>Use current local information when discussing permits or zoning.</li><li>Do not copy one municipality’s rules onto every town page.</li><li>Show real installations with accurate project descriptions.</li><li>Give buyers a clear way to request an estimate from the fence company.</li></ul></div><aside class="scope-box"><h3>Make the site useful before the yard walk</h3><div class="scope-grid"><div class="scope-item"><b>Purpose</b><span>Why the customer needs a fence.</span></div><div class="scope-item"><b>Property</b><span>Where conditions affect the layout.</span></div><div class="scope-item"><b>Product</b><span>What the contractor actually installs.</span></div><div class="scope-item"><b>Process</b><span>How the estimate becomes a clear scope.</span></div></div></aside></div></section>''',
        ],
        "primary_scope": "One primary fence installation service",
        "review_h2": "Which towns do you want more fence-installation estimates from?",
        "faqs": [
            ("Will the website tell homeowners where their legal property line is?", "No. Boundary information must come from reliable property records, surveys, or other qualified sources."),
            ("Can the first build focus only on commercial fencing?", "Yes. Choose one primary fence market or installation service."),
            ("Can town pages discuss permits and pool-fence rules?", "Yes, only when the information is current, locally applicable, and supported by the responsible authority."),
            ("Can we show brands and gate systems?", "Yes, when your company actually provides them and the claims and permissions are verified."),
            ("Will the new site replace our existing website?", "No. It runs alongside the current site."),
            ("Are fence leads or installations guaranteed?", "No. REFRDAI does not guarantee indexing, rankings, inquiries, estimates, contracts, or revenue."),
            ("Is phone required to request the free review?", "No. Email and company website are required for the intake; phone is optional."),
        ],
    },
})


PAGES.update({
    "aging-in-place-remodelers": {
        "industry": "aging-in-place-remodeling",
        "title": "Aging-in-Place Remodeler Marketing | REFRDAI",
        "meta": "Marketing for aging-in-place and home-accessibility remodelers pursuing bathrooms, entries, circulation, and whole-home modification projects.",
        "og_title": "Aging-in-Place Remodeler Marketing",
        "og_desc": "Help families find your company while they plan respectful, practical home modifications for safer and more comfortable living.",
        "page_name": "Aging-in-place remodeler marketing",
        "page_desc": "A REFRDAI offer for accessibility remodelers that want a customer-owned territory website focused on one home-modification service.",
        "service_name": "REFRDAI territory website for aging-in-place remodelers",
        "service_desc": "A $3,400 customer-owned territory website for one primary aging-in-place remodeling service within an agreed 30-mile radius.",
        "crumb": "Aging-in-Place and Home-Accessibility Remodelers",
        "eyebrow": "Aging-in-place and home-accessibility remodeler marketing",
        "h1": "Help families find your company when the home needs to work better for the person living there.",
        "hero": "A rushed bathroom change after a fall, a planned first-floor living project, and a long-term accessibility remodel are different decisions. REFRDAI builds a separate website your company owns alongside its current site, focused on one modification service and the communities where your team can provide thoughtful project support.",
        "secondary_href": "#living-goals",
        "secondary": "See the Home-Modification Path",
        "fine": "The website does not give medical advice or guarantee project fit, inquiries, rankings, contracts, safety outcomes, or revenue.",
        "panel_title": "Start with the person, the activity, and the home.",
        "panel_intro": "Useful content respects the resident’s choices and helps the household explain what is difficult before jumping to a product or generic checklist.",
        "panel_steps": [
            ("Person", "Who uses the space?", "The resident, partner, family, caregivers, visitors, and any occupational or physical professionals involved."),
            ("Activity", "What needs to become easier?", "Entering, bathing, toileting, cooking, reaching, moving between rooms, using stairs, or managing daily routines."),
            ("Home", "What can the property support?", "Layout, structure, clearances, plumbing, electrical work, thresholds, stairs, budget, timing, and possible phases."),
        ],
        "offer": [
            ("One modification focus", "Choose accessible bathrooms, entries, first-floor living, or another primary service."),
            ("A relationship-based territory", "Use communities where your team and professional partners can serve clients well."),
            ("An owned educational website", "Build trust alongside the company’s existing site."),
        ],
        "sections": [
            '''<section id="living-goals"><div class="container two-col"><div><div class="section-heading"><p class="kicker">Respect before recommendations</p><h2>Write for adults making decisions about their own homes.</h2><p>The strongest accessibility content does not frighten, stereotype, or talk past the resident. It explains choices in plain language and makes room for family, caregiver, designer, contractor, and clinical input when each is appropriate.</p></div><ul class="plain-list"><li>Describe the activity or barrier the household wants to address.</li><li>Ask what works today and what may change in the near future.</li><li>Separate a quick modification from a larger remodeling project.</li><li>Explain when an occupational therapist, designer, engineer, or other specialist may join the team.</li><li>Let the resident’s priorities guide appearance, privacy, comfort, independence, and budget.</li></ul><p class="callout">Aging-in-place projects can range from lighting and entries to bathrooms and first-floor living. <a href="https://www.nahb.org/education-and-events/credentials/certified-aging-in-place-specialist-caps/additional-caps-resources/aging-in-place-remodeling-checklist">Review the NAHB aging-in-place remodeling checklist</a>.</p></div><aside class="scope-box"><h3>Sell a thoughtful process</h3><div class="scope-grid"><div class="scope-item"><b>Listen</b><span>Understand the resident’s goals and routines.</span></div><div class="scope-item"><b>Assess</b><span>Review the home and project constraints.</span></div><div class="scope-item"><b>Prioritize</b><span>Separate urgent needs from later phases.</span></div><div class="scope-item"><b>Build</b><span>Deliver only the agreed remodeling scope.</span></div></div></aside></div></section>''',
            '''<section class="band"><div class="container"><div class="section-heading"><p class="kicker">Different starting points</p><h2>Help each household find the right first conversation.</h2></div><div class="cards"><article class="card"><span class="tag">Immediate need</span><h3>A recent change exposed a barrier</h3><p>The family may need a prompt, focused discussion about bathing, entry, stairs, circulation, or another daily activity while avoiding a rushed one-size-fits-all solution.</p></article><article class="card"><span class="tag">Planned remodel</span><h3>The homeowner wants to prepare before a crisis</h3><p>The project can consider appearance, long-term use, resale, visitors, future support, budget, and construction sequencing.</p></article><article class="card"><span class="tag">Whole-home view</span><h3>Several spaces affect independence</h3><p>Entry, bedroom, bath, kitchen, laundry, lighting, flooring, doors, stairs, and exterior access may need priorities and phases.</p></article></div></div></section>''',
            '''<section><div class="container"><div class="section-heading"><p class="kicker">Community-specific guidance</p><h2>Answer the local questions without giving medical or design instructions online.</h2><p>Every approved community receives one main service page and two original question pages. Subjects can reflect housing stock, common entries, bathroom layouts, multigenerational living, local permit responsibilities, professional partnerships, or the company’s project process.</p></div><div class="decision-path"><article class="decision-step"><span class="step-number">1</span><div><strong>Describe the daily goal</strong><p>Focus on the activity the resident wants to perform more comfortably or independently.</p></div></article><article class="decision-step"><span class="step-number">2</span><div><strong>Review the home and team</strong><p>Identify who should participate and what property conditions may affect the work.</p></div></article><article class="decision-step"><span class="step-number">3</span><div><strong>Set priorities and budget</strong><p>Separate the first useful project from future possibilities.</p></div></article><article class="decision-step"><span class="step-number">4</span><div><strong>Confirm design and scope</strong><p>Move from general ideas to a project-specific plan created by the appropriate professionals.</p></div></article></div></div></section>''',
        ],
        "primary_scope": "One primary aging-in-place or accessibility remodeling service",
        "review_h2": "Which communities do you want more home-accessibility remodeling conversations from?",
        "faqs": [
            ("Will the website recommend medical equipment or clinical treatment?", "No. It explains the contractor’s remodeling process and may encourage appropriate professional collaboration without giving medical advice."),
            ("Can we focus on accessible bathroom remodeling?", "Yes. The first build can focus on one primary modification service."),
            ("Can the pages mention CAPS credentials?", "Yes, when the credential is current, belongs to the named professional, and is approved for public use."),
            ("How should the copy talk about older adults?", "With respect, direct language, and attention to the resident’s goals. It should not stereotype or use fear as a sales device."),
            ("Does the new site replace our remodeling website?", "No. It runs alongside your current site."),
            ("Are accessibility remodeling projects guaranteed?", "No. REFRDAI does not guarantee indexing, rankings, inquiries, projects, contracts, or revenue."),
            ("Who controls the completed website?", "Your company owns and keeps the website and domain after the agreed transfer process."),
        ],
    },
    "insulation-contractors": {
        "industry": "insulation-air-sealing",
        "title": "Insulation Contractor Marketing & Leads | REFRDAI",
        "meta": "Insulation contractor marketing and lead generation for attic, wall, crawl-space, spray-foam, air-sealing, and other selected projects.",
        "og_title": "Insulation Contractor Marketing & Leads",
        "og_desc": "Help homeowners find your insulation company while they investigate comfort, air leakage, energy use, and building-envelope improvements.",
        "page_name": "Insulation contractor marketing and lead generation",
        "page_desc": "A REFRDAI offer for insulation companies that want a customer-owned territory website focused on one insulation or air-sealing service.",
        "service_name": "REFRDAI territory website for insulation contractors",
        "service_desc": "A $3,400 customer-owned territory website for one primary insulation or air-sealing service within an agreed 30-mile radius.",
        "crumb": "Insulation and Air-Sealing Contractors",
        "eyebrow": "Insulation contractor marketing and lead generation",
        "h1": "Be easier to find when homeowners are ready to solve a comfort or insulation problem properly.",
        "hero": "A hot upstairs, cold floor, drafty addition, damp attic, and high energy bill can point owners toward insulation without identifying the actual cause. REFRDAI builds a separate website your company owns alongside its current site, focused on one insulation or air-sealing service and a clear evaluation-first conversation.",
        "secondary_href": "#envelope-path",
        "secondary": "See the Building-Envelope Path",
        "fine": "The website does not diagnose a building, promise energy savings, or guarantee inquiries, rankings, projects, rebates, or revenue.",
        "panel_title": "Comfort complaints need a building-specific review.",
        "panel_intro": "Useful pages help homeowners organize symptoms, building history, previous work, moisture concerns, mechanical systems, and accessible areas before a contractor recommends material or scope.",
        "panel_steps": [
            ("Symptom", "What does the owner notice?", "Drafts, uneven rooms, hot or cold surfaces, noise, dust, moisture, ice, equipment runtime, or a planned renovation."),
            ("Envelope", "Where may air and heat move?", "Attic, roofline, walls, rim joists, floors, crawl spaces, penetrations, ducts, additions, and transitions."),
            ("Safety", "What else must be considered?", "Moisture, ventilation, combustion appliances, wiring, recessed fixtures, pests, roof leaks, and applicable codes."),
        ],
        "offer": [
            ("One insulation service", "Choose attic insulation, spray foam, air sealing, crawl-space work, or another primary focus."),
            ("Climate-aware local pages", "Use supported local context without making a universal savings claim."),
            ("A website your company owns", "Build a long-term customer education asset."),
        ],
        "sections": [
            '''<section id="envelope-path"><div class="container"><div class="section-heading"><p class="kicker">Evaluate before material</p><h2>Do not let “spray foam versus fiberglass” become the entire sales conversation.</h2><p>The useful first question is what the building needs. Material selection follows the assembly, location, moisture, air barrier, thermal boundary, ventilation, safety, budget, and project goals.</p></div><div class="decision-path"><article class="decision-step"><span class="step-number">Observe</span><div><strong>Gather symptoms and history</strong><p>Ask when the issue occurs, what rooms are affected, what work has been done, and whether leaks, odors, moisture, pests, or equipment changes are involved.</p></div></article><article class="decision-step"><span class="step-number">Inspect</span><div><strong>Review accessible building conditions</strong><p>The qualified contractor determines what can be evaluated and whether another trade or test is needed.</p></div></article><article class="decision-step"><span class="step-number">Plan</span><div><strong>Align air, thermal, and moisture strategies</strong><p>The scope should fit the assembly and not create unsupported claims about savings, comfort, or indoor air quality.</p></div></article></div><p class="callout">Insulation and air sealing work together as part of the building enclosure, and spray foam can serve different functions in different assemblies. <a href="https://bsesc.energy.gov/energy-basics/tight-air-sealed-homes">Review U.S. Department of Energy building-science guidance</a>.</p></div></section>''',
            '''<section class="band"><div class="container two-col"><div><div class="section-heading"><p class="kicker">Choose the right project lane</p><h2>Separate upgrade work from every comfort complaint.</h2><p>The first territory build should reflect the work the contractor is equipped, trained, insured, and willing to perform.</p></div><ul class="plain-list"><li>Attic insulation removal, replacement, or added coverage.</li><li>Targeted air sealing before or alongside insulation.</li><li>Spray-foam work in defined assemblies and locations.</li><li>Rim-joist, floor, wall, roofline, or crawl-space projects.</li><li>New-construction or renovation insulation coordination.</li></ul></div><aside class="scope-box"><h3>Never skip the cautions</h3><div class="scope-grid"><div class="scope-item"><b>Moisture</b><span>Investigate leaks and wet materials before covering them.</span></div><div class="scope-item"><b>Ventilation</b><span>Do not assume tighter is automatically complete.</span></div><div class="scope-item"><b>Combustion</b><span>Account for fuel-burning equipment and venting.</span></div><div class="scope-item"><b>Electrical</b><span>Respect fixtures, wiring, clearances, and local requirements.</span></div></div></aside></div></section>''',
            '''<section><div class="container"><div class="section-heading"><p class="kicker">Original pages by town</p><h2>Connect local homes with the contractor’s real evaluation process.</h2><p>Town pages can address the selected service, prevalent housing eras, common assemblies, seasonal comfort questions, local program information, and permit or code context only when reliable sources support the statements.</p></div><div class="cards"><article class="card"><span class="tag">Existing homes</span><h3>What is already in the assembly?</h3><p>Prepare owners to discuss prior insulation, renovations, additions, access, moisture events, equipment, and known problem areas.</p></article><article class="card"><span class="tag">Project planning</span><h3>What should happen first?</h3><p>Explain evaluation, testing when offered, related repairs, written scope, preparation, installation, cleanup, and follow-up.</p></article><article class="card"><span class="tag">Proof</span><h3>What can the contractor verify?</h3><p>Show real training, certifications, products, warranties, diagnostic services, project photos, and rebate participation only when current.</p></article></div></div></section>''',
        ],
        "primary_scope": "One primary insulation or air-sealing service",
        "review_h2": "Which towns do you want more insulation or air-sealing project inquiries from?",
        "faqs": [
            ("Will the website promise a specific energy-bill reduction?", "No. Energy use depends on the building, occupants, systems, weather, rates, and completed scope."),
            ("Can the first build focus only on spray-foam projects?", "Yes, when the company’s actual service, training, safety practices, and project types are clearly defined."),
            ("Can pages mention tax credits or rebates?", "Only when the program information is current, applicable, and linked to an authoritative source. Eligibility is not guaranteed."),
            ("Will the site diagnose moisture or indoor-air problems?", "No. It can encourage evaluation and explain the contractor’s process without diagnosing the building online."),
            ("Does the territory website replace our current site?", "No. It runs alongside your current website."),
            ("Are insulation leads or projects guaranteed?", "No. REFRDAI does not guarantee indexing, rankings, inquiries, projects, savings, or revenue."),
            ("Is the $500 monthly expansion automatic?", "No. It is optional, separate, and may be offered only when enough usable performance data exists."),
        ],
    },
    "epoxy-floor-concrete-coating-contractors": {
        "industry": "concrete-coatings",
        "title": "Concrete Coating Marketing & Leads | REFRDAI",
        "meta": "Concrete coating and epoxy-floor contractor marketing for garage, commercial, industrial, and other selected floor projects.",
        "og_title": "Concrete Coating Contractor Marketing & Leads",
        "og_desc": "Help property owners find your coating company while they compare substrate condition, use, finish, and downtime.",
        "page_name": "Concrete coating contractor marketing and lead generation",
        "page_desc": "A REFRDAI offer for concrete coating companies that want a customer-owned territory website focused on one floor or surface market.",
        "service_name": "REFRDAI territory website for concrete coating contractors",
        "service_desc": "A $3,400 customer-owned territory website for one primary concrete coating service within an agreed 30-mile radius.",
        "crumb": "Epoxy-Floor and Concrete-Coating Contractors",
        "eyebrow": "Concrete coating contractor marketing and lead generation",
        "h1": "Get found for coating projects that fit your preparation process, system, and crew.",
        "hero": "A residential garage, restaurant back room, warehouse aisle, and manufacturing floor expose coatings to different traffic, chemicals, moisture, cleaning, appearance, and shutdown constraints. REFRDAI builds a separate website your company owns alongside its current site, focused on the coating market you want to serve.",
        "secondary_href": "#surface-first",
        "secondary": "See the Coating-Project Path",
        "fine": "The website does not select a coating system remotely or guarantee adhesion, timing, inquiries, rankings, contracts, or revenue.",
        "panel_title": "The surface decides whether the sales promise is believable.",
        "panel_intro": "Color and flakes attract attention. Condition assessment, moisture, contamination, repairs, preparation, system choice, use, and downtime determine whether the project conversation is complete.",
        "panel_steps": [
            ("Surface", "What condition is the concrete in?", "Age, previous coatings, curing products, sealers, contamination, cracks, spalls, moisture, repairs, and unknown history."),
            ("Use", "What will the floor face?", "Vehicles, foot traffic, impact, chemicals, hot tires, food service, cleaning, sunlight, slip concerns, or decorative use."),
            ("Window", "How can the area be taken out of service?", "Contents, equipment, business hours, preparation dust, installation stages, ventilation, cure, and return-to-use needs."),
        ],
        "offer": [
            ("One coating market", "Choose residential garages, commercial floors, industrial surfaces, or another primary focus."),
            ("A serviceable territory", "Account for crew travel, equipment, site visits, and project size."),
            ("An owned sales asset", "Show the company’s real process and work."),
        ],
        "sections": [
            '''<section id="surface-first"><div class="container two-col"><div><div class="section-heading"><p class="kicker">Assessment before color</p><h2>Lead with what makes a coating project succeed or fail.</h2><p>Owners often shop by color, shine, warranty, and installation time. The page should make preparation and system fit just as visible, without turning general content into a site-specific specification.</p></div><ul class="plain-list"><li>Identify the concrete, current finish, prior coating, contamination, repairs, and known moisture history.</li><li>Explain the contractor’s evaluation and surface-preparation process in accurate terms.</li><li>Match the system discussion to traffic, exposure, cleaning, appearance, slip concerns, and maintenance.</li><li>Define contents, access, ventilation, dust control, work hours, cure, and return-to-service expectations.</li><li>Present warranty language only as written and approved by the company.</li></ul><p class="callout">Concrete assessment, moisture, contamination, defects, and surface preparation affect protection-system installation. <a href="https://www.concrete.org/Portals/0/Files/PDF/Previews/515.3R-20_preview.pdf">Review the ACI surface-preparation guide preview</a>.</p></div><aside class="scope-box"><h3>Different floors need different stories</h3><div class="scope-grid"><div class="scope-item"><b>Garage</b><span>Vehicles, hot tires, storage, appearance, and return to use.</span></div><div class="scope-item"><b>Commercial</b><span>Customers, employees, cleaning, traffic, and business hours.</span></div><div class="scope-item"><b>Industrial</b><span>Equipment, impact, chemicals, safety, and production windows.</span></div><div class="scope-item"><b>Outdoor</b><span>Weather, sunlight, drainage, texture, and exposure.</span></div></div></aside></div></section>''',
            '''<section class="band"><div class="container"><div class="section-heading"><p class="kicker">The buyer’s real sequence</p><h2>Turn a finish request into a qualified site conversation.</h2></div><div class="decision-path"><article class="decision-step"><span class="step-number">Inspect</span><div><strong>Understand the existing surface</strong><p>Photos can start a conversation, but the contractor still needs to evaluate the actual slab and site.</p></div></article><article class="decision-step"><span class="step-number">Prepare</span><div><strong>Define cleaning, repair, and profiling</strong><p>The page explains why preparation is part of the installed system rather than an invisible extra.</p></div></article><article class="decision-step"><span class="step-number">Select</span><div><strong>Match system and finish to use</strong><p>Color and appearance belong alongside exposure, traffic, maintenance, safety, and performance expectations.</p></div></article><article class="decision-step"><span class="step-number">Schedule</span><div><strong>Plan access and downtime</strong><p>Customers need an honest sequence for emptying the area, installation, cure, inspection, and return to use.</p></div></article></div></div></section>''',
            '''<section><div class="container"><div class="section-heading"><p class="kicker">Local pages with proof</p><h2>Let each town page show the coating work your company is built to perform.</h2><p>One page explains the primary market. Two original question pages can address surface preparation, garage planning, commercial downtime, industrial exposure, maintenance, finish options, or choosing a contractor. Real projects and verified process details matter more than generic product claims.</p></div><div class="cards"><article class="card"><span class="tag">Proof</span><h3>Show the actual substrate and finished result</h3><p>Use real before-and-after images with accurate captions, not stock photos presented as company work.</p></article><article class="card"><span class="tag">Process</span><h3>Explain the steps the crew really performs</h3><p>Assessment, repairs, preparation, installation, broadcast, topcoat, cure, and handoff appear only as applicable.</p></article><article class="card"><span class="tag">Fit</span><h3>Invite projects that match the company</h3><p>State the service area, market, typical size, site conditions, and scheduling requirements without inventing minimums.</p></article></div></div></section>''',
        ],
        "primary_scope": "One primary concrete coating or epoxy-floor service",
        "review_h2": "Which towns do you want more garage, commercial, or industrial coating projects from?",
        "faqs": [
            ("Will the website call every floor an epoxy floor?", "No. It will use the company’s accurate system and service language rather than treating every coating as the same product."),
            ("Can we focus only on residential garage floors?", "Yes. The first build can focus on one primary coating market."),
            ("Can the page promise one-day installation?", "Only if the company verifies the exact offer and conditions. The website will not turn a conditional schedule into a universal promise."),
            ("Will REFRDAI specify surface preparation?", "No. The contractor must evaluate the slab and define the appropriate project-specific preparation and coating system."),
            ("Can we show real before-and-after photos?", "Yes, with ownership or permission and accurate project captions."),
            ("Are coating leads or contracts guaranteed?", "No. REFRDAI does not guarantee indexing, rankings, inquiries, projects, adhesion, or revenue."),
            ("Do we own the new website?", "Yes. Your company owns and keeps the website and domain under the stated transfer terms."),
        ],
    },
    "deck-outdoor-living-contractors": {
        "industry": "deck-outdoor-living",
        "title": "Deck Builder Marketing & Lead Generation | REFRDAI",
        "meta": "Deck builder marketing and lead generation for new decks, replacements, porches, railings, and other selected outdoor-living projects.",
        "og_title": "Deck Builder Marketing & Lead Generation",
        "og_desc": "Help homeowners find your deck company while they plan use, structure, materials, railings, stairs, and outdoor-living features.",
        "page_name": "Deck builder marketing and lead generation",
        "page_desc": "A REFRDAI offer for deck builders that want a customer-owned territory website focused on one outdoor-living construction service.",
        "service_name": "REFRDAI territory website for deck and outdoor-living contractors",
        "service_desc": "A $3,400 customer-owned territory website for one primary deck or outdoor-living service within an agreed 30-mile radius.",
        "crumb": "Deck and Outdoor-Living Contractors",
        "eyebrow": "Deck builder marketing and lead generation",
        "h1": "Be easier to find for complete deck projects that fit your design and construction process.",
        "hero": "A small replacement platform, second-story deck, screened porch, composite outdoor room, and repair request require different design, structural, permit, and budget conversations. REFRDAI builds a separate website your company owns alongside its current site, focused on one outdoor-living service and the towns where you want better project inquiries.",
        "secondary_href": "#deck-vision",
        "secondary": "See the Deck-Buyer Path",
        "fine": "The website does not inspect or design a deck remotely and does not guarantee permits, inquiries, rankings, projects, contracts, or revenue.",
        "panel_title": "The deck decision starts with use and structure.",
        "panel_intro": "A homeowner’s inspiration photo matters, but so do the house connection, site, height, footings, stairs, rails, loads, drainage, utilities, setbacks, and approval process.",
        "panel_steps": [
            ("Use", "How should the space work?", "Dining, gathering, grilling, pool access, quiet seating, shade, screening, multiple levels, or another outdoor-living goal."),
            ("Structure", "What must be evaluated?", "Existing deck, ledger, house wall, grade, footings, posts, beams, joists, stairs, rails, utilities, and site drainage."),
            ("Finish", "What choices shape the project?", "Wood or composite products, color, railing, lighting, privacy, stairs, skirting, features, maintenance, and budget."),
        ],
        "offer": [
            ("One outdoor-living service", "Choose new decks, replacements, porches, railings, or another primary focus."),
            ("A realistic build territory", "Use towns that fit design, permit, crew, and project economics."),
            ("An owned portfolio path", "Connect local buyers with the builder’s real work."),
        ],
        "sections": [
            '''<section id="deck-vision"><div class="container"><div class="section-heading"><p class="kicker">From inspiration to buildable scope</p><h2>Help the homeowner organize the project before choosing boards and colors.</h2><p>Good deck marketing makes design feel approachable while respecting the structural and approval work that comes before construction.</p></div><div class="cards"><article class="card"><span class="tag">New deck</span><h3>Start with the home, yard, and intended use</h3><p>Discuss door location, height, grade, setbacks, utilities, drainage, circulation, furniture, grilling, views, shade, privacy, and future plans.</p></article><article class="card"><span class="tag">Replacement</span><h3>Do not assume the old structure can remain</h3><p>Explain why the contractor must evaluate the existing deck, connections, supports, footings, stairs, rails, deterioration, and current requirements.</p></article><article class="card"><span class="tag">Outdoor room</span><h3>Coordinate the features around the structure</h3><p>Porches, roofs, screens, lighting, kitchens, fireplaces, spas, and drainage may involve added design, trades, approvals, and budget.</p></article></div><p class="callout">Deck codes, licensing, and safety considerations remain important parts of professional construction. <a href="https://www.nadra.org/code">Review North American Deck and Railing Association code resources</a>.</p></div></section>''',
            '''<section class="band"><div class="container two-col"><div><div class="section-heading"><p class="kicker">Qualify the project</p><h2>Make the first conversation useful for both the builder and homeowner.</h2><p>The town page should attract people who want the kind of project the company is set up to design and build.</p></div><ul class="plain-list"><li>New construction, replacement, resurfacing, repair, porch, railing, stair, or another clearly defined service.</li><li>Property address, photos, approximate dimensions, height, access, existing conditions, and desired use.</li><li>Decision makers, budget conversation, material preferences, features, timing, and permit expectations.</li><li>Designer, engineer, electrician, plumber, roofer, landscaper, or other trade coordination when needed.</li><li>Real portfolio examples with accurate scope and material descriptions.</li></ul></div><aside class="scope-box"><h3>Keep safety out of the sales shortcut</h3><div class="scope-grid"><div class="scope-item"><b>No remote approval</b><span>Photos cannot confirm structural safety.</span></div><div class="scope-item"><b>No copied code</b><span>Use current locally applicable requirements.</span></div><div class="scope-item"><b>No fake portfolio</b><span>Stock imagery is never labeled as completed work.</span></div><div class="scope-item"><b>No fixed schedule</b><span>Timing follows the real scope and approvals.</span></div></div></aside></div></section>''',
            '''<section><div class="container"><div class="section-heading"><p class="kicker">The decision sequence</p><h2>Give each approved town a clear path from idea to consultation.</h2></div><div class="decision-path"><article class="decision-step"><span class="step-number">Imagine</span><div><strong>Define the outdoor experience</strong><p>How the household wants to live outside guides size, circulation, features, and priorities.</p></div></article><article class="decision-step"><span class="step-number">Review</span><div><strong>Understand the house and site</strong><p>The builder evaluates property conditions, existing structure, access, rules, and design needs.</p></div></article><article class="decision-step"><span class="step-number">Choose</span><div><strong>Compare materials and features</strong><p>Appearance, maintenance, heat, texture, railing, lighting, privacy, and budget become an organized conversation.</p></div></article><article class="decision-step"><span class="step-number">Scope</span><div><strong>Confirm plans, approvals, and responsibilities</strong><p>The contract should state design, permits, construction, trade coordination, selections, schedule, and exclusions.</p></div></article></div></div></section>''',
        ],
        "primary_scope": "One primary deck or outdoor-living construction service",
        "review_h2": "Which towns do you want more new-deck or outdoor-living consultations from?",
        "faqs": [
            ("Can the website say an existing deck is safe?", "No. A qualified professional must inspect and evaluate the actual structure and site."),
            ("Can we focus only on complete new decks?", "Yes. The first build can exclude repair-only or resurfacing inquiries when that is the company’s chosen focus."),
            ("Can the pages discuss local deck permits?", "Yes, only with current information from the responsible local authority and without treating general guidance as project approval."),
            ("Can we use manufacturer photos?", "Only with permission and clear labeling. They must not be presented as the builder’s completed projects."),
            ("Will the territory site replace our current portfolio site?", "No. It runs alongside the current site and can direct suitable local buyers to the company."),
            ("Are deck projects or contracts guaranteed?", "No. REFRDAI does not guarantee indexing, rankings, inquiries, consultations, contracts, or revenue."),
            ("Is phone required for the free review?", "No. Phone is optional. Company website and email are required for the intake."),
        ],
    },
})


PAGES.update({
    "garage-door-installation-companies": {
        "industry": "garage-door-installation",
        "title": "Garage Door Company Marketing & Leads | REFRDAI",
        "meta": "Garage door company marketing and lead generation for replacement doors, new installations, openers, and other selected projects.",
        "og_title": "Garage Door Company Marketing & Leads",
        "og_desc": "Help homeowners find your company while they compare complete garage-door replacement and installation options.",
        "page_name": "Garage door company marketing and lead generation",
        "page_desc": "A REFRDAI offer for garage door companies that want a customer-owned territory website focused on one installation or replacement service.",
        "service_name": "REFRDAI territory website for garage door installation companies",
        "service_desc": "A $3,400 customer-owned territory website for one primary garage door service within an agreed 30-mile radius.",
        "crumb": "Garage Door Installation Companies",
        "eyebrow": "Garage door company marketing and lead generation",
        "h1": "Be easier to find for complete garage-door projects, not only emergency repair calls.",
        "hero": "A broken spring, noisy opener, damaged panel, outdated door, and full replacement can all begin with the same search. REFRDAI builds a separate website your company owns alongside its current site, focused on the installation or replacement work you want in the towns your team serves.",
        "secondary_href": "#door-decision",
        "secondary": "See the Garage-Door Buyer Path",
        "fine": "The website does not give do-it-yourself spring or cable instructions and does not guarantee calls, installations, rankings, contracts, or revenue.",
        "panel_title": "A complete door project is a system decision.",
        "panel_intro": "Door sections, track, springs, hardware, operator, controls, safety devices, opening, headroom, use, wind requirements, appearance, and insulation all belong in the conversation.",
        "panel_steps": [
            ("Need", "Repair or replacement?", "Operational failure, collision damage, deterioration, appearance, energy concerns, renovation, new construction, or a change in use."),
            ("Opening", "What must fit?", "Width, height, headroom, side room, back room, framing, floor, track, operator position, utilities, and obstructions."),
            ("System", "What should be selected together?", "Door construction, hardware, springs, track, operator, controls, safety features, glazing, finish, and verified wind requirements."),
        ],
        "offer": [
            ("One garage-door service", "Choose full replacement, new installation, openers, or another primary project type."),
            ("A response-ready territory", "Use towns that fit the company’s sales, installation, and service coverage."),
            ("A website the dealer owns", "Support long-term visibility alongside the current site."),
        ],
        "sections": [
            '''<section id="door-decision"><div class="container"><div class="section-heading"><p class="kicker">Separate the service paths</p><h2>Help homeowners know when they are shopping for a complete door system.</h2><p>Repair leads can fill a schedule, but replacement buyers need a different conversation about the opening, home, use, door, operator, appearance, safety, and installation process.</p></div><div class="cards"><article class="card"><span class="tag">Replacement</span><h3>The existing door no longer fits the need</h3><p>Damage, age, repeated failures, appearance, insulation, renovation, or a new vehicle may start the comparison.</p></article><article class="card"><span class="tag">New construction</span><h3>The opening and system must be coordinated</h3><p>Plans, framing, headroom, track, operator, power, finish, windows, use, and verified local requirements belong in the selection process.</p></article><article class="card"><span class="tag">Operator</span><h3>The door and opener must work together</h3><p>Controls, lighting, battery backup, connected features, safety devices, door balance, and manufacturer compatibility require accurate product-specific guidance.</p></article></div><p class="callout">Garage doors contain components under high tension, and professional installation and service matter. <a href="https://www.dasma.com/safety-tips/garage-door-systems/">Review DASMA garage-door safety guidance</a>.</p></div></section>''',
            '''<section class="band"><div class="container two-col"><div><div class="section-heading"><p class="kicker">Sell the project, not the coupon</p><h2>Make room for appearance, performance, and safe installation.</h2><p>A replacement page can help the household compare options without reducing every choice to a discounted service call.</p></div><ul class="plain-list"><li>Show the door styles, construction types, finishes, windows, insulation options, and brands actually offered.</li><li>Explain the in-home or on-site measuring and selection process.</li><li>Address removal, disposal, framing repairs, electrical responsibility, trim, finish, permits, and inspection only as applicable.</li><li>Use verified warranty and manufacturer information with the correct conditions.</li><li>Give homeowners a clear path to request a replacement or installation consultation.</li></ul></div><aside class="scope-box"><h3>Use trustworthy proof</h3><div class="scope-grid"><div class="scope-item"><b>Real products</b><span>Show brands and models the company can supply.</span></div><div class="scope-item"><b>Real technicians</b><span>Use current credentials and service capabilities.</span></div><div class="scope-item"><b>Real installations</b><span>Caption completed projects accurately.</span></div><div class="scope-item"><b>Real coverage</b><span>List towns inside the practical territory.</span></div></div></aside></div></section>''',
            '''<section><div class="container"><div class="section-heading"><p class="kicker">Town-specific buying help</p><h2>Answer the questions that move a homeowner toward a useful door consultation.</h2></div><div class="decision-path"><article class="decision-step"><span class="step-number">Photo</span><div><strong>Show the existing door and opening</strong><p>Photos can help route the conversation but do not replace field measurement or safety evaluation.</p></div></article><article class="decision-step"><span class="step-number">Use</span><div><strong>Explain how the garage serves the household</strong><p>Parking, storage, workshop use, living space above, frequency, security, and appearance shape priorities.</p></div></article><article class="decision-step"><span class="step-number">Choose</span><div><strong>Compare the complete system</strong><p>Door, track, hardware, spring system, operator, controls, safety features, and options should be considered together.</p></div></article><article class="decision-step"><span class="step-number">Install</span><div><strong>Confirm preparation and handoff</strong><p>Define access, contents, removal, installation, testing, cleanup, operation, maintenance, and warranty information.</p></div></article></div></div></section>''',
        ],
        "primary_scope": "One primary garage door installation or replacement service",
        "review_h2": "Which towns do you want more garage-door replacement or installation inquiries from?",
        "faqs": [
            ("Will the website provide spring or cable repair instructions?", "No. High-tension door components can be dangerous and should be handled by trained professionals."),
            ("Can the first build focus on complete replacements?", "Yes. The page can clearly separate replacement and new-installation projects from routine repair calls."),
            ("Can we list the door brands we sell?", "Yes, when the dealer relationship, product availability, trademarks, and claims are current and approved."),
            ("Will REFRDAI determine wind-load requirements?", "No. Applicable requirements and final product selection must be verified for the actual project by qualified parties."),
            ("Does the territory site replace our current service website?", "No. It runs alongside it."),
            ("Are garage-door leads or installations guaranteed?", "No. REFRDAI does not guarantee indexing, rankings, inquiries, projects, contracts, or revenue."),
            ("Do we keep the domain after the first year?", "Yes. The client owns the domain after transfer and pays future renewal directly unless choosing the optional annual plan."),
        ],
    },
    "chimney-masonry-repair-contractors": {
        "industry": "chimney-masonry-repair",
        "title": "Chimney Contractor Marketing & Leads | REFRDAI",
        "meta": "Chimney contractor marketing and lead generation for inspections, masonry repair, relining, caps, water problems, and other selected projects.",
        "og_title": "Chimney Contractor Marketing & Leads",
        "og_desc": "Help homeowners find your chimney company while they move from a symptom or inspection need to the right professional service.",
        "page_name": "Chimney contractor marketing and lead generation",
        "page_desc": "A REFRDAI offer for chimney companies that want a customer-owned territory website focused on one inspection or repair service.",
        "service_name": "REFRDAI territory website for chimney and masonry repair contractors",
        "service_desc": "A $3,400 customer-owned territory website for one primary chimney service within an agreed 30-mile radius.",
        "crumb": "Chimney and Masonry Repair Contractors",
        "eyebrow": "Chimney contractor marketing and lead generation",
        "h1": "Be easier to find when homeowners need the right chimney inspection or repair conversation.",
        "hero": "A routine sweep, water stain, damaged crown, loose brick, odor, draft complaint, appliance change, and post-fire concern do not begin with the same scope. REFRDAI builds a separate website your company owns alongside its current site, focused on one chimney service and the communities where you want more qualified requests.",
        "secondary_href": "#chimney-path",
        "secondary": "See the Chimney-Service Path",
        "fine": "The website does not declare a chimney safe, diagnose a venting system, or guarantee inspections, repairs, rankings, contracts, or revenue.",
        "panel_title": "Inspection, cleaning, and repair are related but different.",
        "panel_intro": "Useful pages help the homeowner explain the appliance, fuel, use, symptoms, recent events, visible concerns, access, and reason for service before a professional evaluates the system.",
        "panel_steps": [
            ("History", "What system is involved?", "Fireplace, stove, furnace, boiler, insert, fuel type, chimney construction, liners, prior work, and known records."),
            ("Reason", "Why is service being requested?", "Routine inspection, purchase or sale, appliance change, water entry, odor, debris, performance concern, visible damage, or a chimney-fire event."),
            ("Scope", "What follows the inspection?", "Cleaning, documentation, repair recommendations, masonry work, cap or crown work, relining, waterproofing, or referral only when supported."),
        ],
        "offer": [
            ("One chimney service", "Choose masonry repair, inspection, relining, water problems, or another primary focus."),
            ("A seasonal service territory", "Use towns that fit routing, roof access, crew, and weather realities."),
            ("An owned trust asset", "Explain the company’s process without fear-based claims."),
        ],
        "sections": [
            '''<section id="chimney-path"><div class="container"><div class="section-heading"><p class="kicker">Start with the reason for service</p><h2>Keep a routine visit separate from a repair decision.</h2><p>A homeowner may only know that something looks, smells, sounds, or performs differently. The page should route that concern to professional evaluation without announcing a cause or repair before the system is inspected.</p></div><div class="decision-path"><article class="decision-step"><span class="step-number">Routine</span><div><strong>Inspection and cleaning conversation</strong><p>Collect appliance, fuel, usage, last service, access, and known history so the company can explain its appointment process.</p></div></article><article class="decision-step"><span class="step-number">Change</span><div><strong>New appliance, property transfer, or altered use</strong><p>Make clear that compatibility, condition, clearances, venting, documentation, and local requirements need project-specific review.</p></div></article><article class="decision-step"><span class="step-number">Concern</span><div><strong>Water, masonry, odor, debris, performance, or damage</strong><p>Invite a professional assessment without promising that one visible symptom has one cause.</p></div></article></div><p class="callout">Chimney systems should be inspected and serviced as needed by qualified professionals. <a href="https://www.csia.org/homeowner-resources">Review Chimney Safety Institute of America homeowner resources</a>.</p></div></section>''',
            '''<section class="band"><div class="container two-col"><div><div class="section-heading"><p class="kicker">Build trust without alarm</p><h2>Explain what the company evaluates and what the customer receives.</h2><p>Chimney work touches fire, combustion products, roofs, masonry, and weather. The sales page should be calm, specific, and honest about the limits of remote information.</p></div><ul class="plain-list"><li>State the inspection, sweeping, repair, relining, cap, crown, masonry, or water-management services actually offered.</li><li>Explain appointment preparation, roof or interior access, photos, reports, estimates, and follow-up as the company provides them.</li><li>Use current certifications, memberships, licenses, insurance, and manufacturer relationships only when verified.</li><li>Do not label a stain, crack, odor, or draft as proof of a specific defect.</li><li>Do not use a generic “unsafe chimney” claim to force an appointment.</li></ul></div><aside class="scope-box"><h3>Let the inspection support the scope</h3><div class="scope-grid"><div class="scope-item"><b>Observe</b><span>Record the owner’s reason and system history.</span></div><div class="scope-item"><b>Inspect</b><span>Use the appropriate professional process.</span></div><div class="scope-item"><b>Explain</b><span>Document findings and limitations clearly.</span></div><div class="scope-item"><b>Propose</b><span>Recommend only supported cleaning or repair work.</span></div></div></aside></div></section>''',
            '''<section><div class="container"><div class="section-heading"><p class="kicker">Local service questions</p><h2>Build town pages around homes, systems, and service needs that can be supported.</h2><p>One main town page presents the selected chimney service. Two original question pages can address preparing for an inspection, chimney water entry, masonry deterioration, appliance changes, post-fire steps, caps and crowns, relining conversations, or choosing a qualified company.</p></div><div class="cards"><article class="card"><span class="tag">Before the visit</span><h3>What should the homeowner know?</h3><p>Appliance type, fuel, use, service history, visible changes, property access, roof height, pets, and recent events can prepare the appointment.</p></article><article class="card"><span class="tag">After inspection</span><h3>How are findings explained?</h3><p>The company can describe reports, images, priorities, repair options, limitations, referrals, and written estimates as actually provided.</p></article><article class="card"><span class="tag">Local fit</span><h3>Which systems and properties are served?</h3><p>State the real service area, chimney and appliance types, roof-access limits, seasonal schedule, and project minimums only when verified.</p></article></div></div></section>''',
        ],
        "primary_scope": "One primary chimney inspection or repair service",
        "review_h2": "Which towns do you want more chimney inspection or masonry-repair requests from?",
        "faqs": [
            ("Will the website say a chimney is safe after viewing a photo?", "No. Safety and condition require the appropriate professional inspection of the actual system."),
            ("Can the first build focus on chimney masonry repair?", "Yes. Choose one primary chimney service for the first build."),
            ("Can pages mention annual inspection guidance?", "Yes, when accurately attributed to an authoritative source and not presented as a substitute for professional judgment."),
            ("Can we publish CSIA certification?", "Yes, when the named professional’s certification is current and approved for public use."),
            ("Will the territory site replace our current site?", "No. It runs alongside the current website."),
            ("Are chimney leads or repair projects guaranteed?", "No. REFRDAI does not guarantee indexing, rankings, inquiries, inspections, contracts, or revenue."),
            ("Is the annual Territory Continuity Review required?", "No. It is optional and does not determine ownership of the completed website or domain."),
        ],
    },
    "water-fire-mold-restoration-companies": {
        "industry": "property-restoration",
        "title": "Restoration Company Marketing & Leads | REFRDAI",
        "meta": "Marketing and lead generation for water, fire, smoke, and mold-restoration companies pursuing the property-loss work they are equipped to handle.",
        "og_title": "Restoration Company Marketing & Leads",
        "og_desc": "Help property owners and managers find your restoration company during urgent and planned recovery decisions.",
        "page_name": "Property restoration company marketing and lead generation",
        "page_desc": "A REFRDAI offer for restoration companies that want a customer-owned territory website focused on one water, fire, smoke, or mold service.",
        "service_name": "REFRDAI territory website for property restoration companies",
        "service_desc": "A $3,400 customer-owned territory website for one primary restoration service within an agreed 30-mile radius.",
        "crumb": "Water, Fire, and Mold-Restoration Companies",
        "eyebrow": "Restoration company marketing and lead generation",
        "h1": "Help property owners find your company when the next recovery decision cannot wait.",
        "hero": "A burst pipe at midnight, slow leak discovered after weeks, fire-damaged room, smoke-affected building, and suspected mold condition require different safety, documentation, containment, drying, cleaning, and repair conversations. REFRDAI builds a separate website your company owns alongside its current site, focused on one restoration service and your real response territory.",
        "secondary_href": "#first-response",
        "secondary": "See the Restoration-Decision Path",
        "fine": "The website does not declare a building safe, replace emergency services, or guarantee calls, insurance payment, rankings, projects, or revenue.",
        "panel_title": "Urgent marketing must be useful before it is persuasive.",
        "panel_intro": "The page should help a caller protect people, stop only what can be stopped safely, contact the proper emergency or utility service, and reach the restoration company without making unsupported coverage or outcome promises.",
        "panel_steps": [
            ("Safety", "Is anyone in immediate danger?", "Fire, electrical, structural, contaminated-water, air-quality, gas, utility, and access concerns belong ahead of a sales pitch."),
            ("Source", "What happened and is it controlled?", "Known or unknown water source, extinguished fire, smoke spread, visible growth, storm opening, or another documented event."),
            ("Response", "What can the company actually provide?", "Emergency response, inspection, extraction, drying, cleaning, containment, contents, documentation, rebuild, or referral as verified."),
        ],
        "offer": [
            ("One restoration service", "Choose water damage, fire and smoke, mold remediation, or another primary focus."),
            ("A truthful response territory", "List only areas and hours the company can actually support."),
            ("A company-owned channel", "Reduce dependence on shared-lead marketplaces over time."),
        ],
        "sections": [
            '''<section id="first-response"><div class="container"><div class="section-heading"><p class="kicker">Safety and contact first</p><h2>Give a distressed property owner a calm, usable next step.</h2><p>Urgency can improve response, but fear-based copy can also mislead people. The page should separate emergency conditions, safe immediate actions, company contact, documentation, and the later scope discussion.</p></div><div class="decision-path"><article class="decision-step"><span class="step-number">1</span><div><strong>Protect people and follow emergency direction</strong><p>Tell visitors to contact emergency services, utilities, property management, or other appropriate authorities when the situation requires them.</p></div></article><article class="decision-step"><span class="step-number">2</span><div><strong>Share the event and current conditions</strong><p>Location, time discovered, suspected source, affected areas, visible conditions, utilities, occupancy, and safe access can help route the call.</p></div></article><article class="decision-step"><span class="step-number">3</span><div><strong>Explain the company’s real first response</strong><p>State response hours, service area, arrival process, inspection, documentation, emergency work authorization, and exclusions accurately.</p></div></article><article class="decision-step"><span class="step-number">4</span><div><strong>Move from stabilization to supported scope</strong><p>Drying, cleaning, remediation, contents, demolition, repair, and reconstruction follow the actual assessment and agreement.</p></div></article></div></div></section>''',
            '''<section class="band"><div class="container two-col"><div><div class="section-heading"><p class="kicker">Different loss, different story</p><h2>Do not combine water, fire, smoke, and mold into one interchangeable page.</h2><p>The first build should focus on the service the company most wants and is qualified to deliver.</p></div><ul class="plain-list"><li>Water pages can explain source categories, affected materials, extraction, drying, monitoring, documentation, and repair boundaries in careful terms.</li><li>Fire and smoke pages can discuss emergency handoff, soot and odor assessment, contents, cleaning, demolition, and reconstruction without declaring materials restorable online.</li><li>Mold pages can explain evaluation, moisture-source responsibility, containment, remediation process, documentation, and post-work steps without testing or diagnosing through a webpage.</li><li>Commercial pages can address occupancy, business continuity, stakeholders, access, safety, documentation, and phased work.</li></ul><p class="callout">Professional restoration work uses service-specific standards and documented processes. <a href="https://iicrc.org/iicrcstandardsfaqs/">Review IICRC standards information</a>.</p></div><aside class="scope-box"><h3>Claims that stay out</h3><div class="scope-grid"><div class="scope-item"><b>No coverage promise</b><span>The insurer decides policy coverage.</span></div><div class="scope-item"><b>No safety declaration</b><span>The actual site requires evaluation.</span></div><div class="scope-item"><b>No universal response time</b><span>State only verified availability.</span></div><div class="scope-item"><b>No guaranteed recovery</b><span>Conditions and scope vary by loss.</span></div></div></aside></div></section>''',
            '''<section><div class="container"><div class="section-heading"><p class="kicker">Local response pages</p><h2>Build each community page around a real recovery decision.</h2><p>One main town page presents the selected restoration service. Two original question pages can address what to do before the crew arrives, what the first visit includes, drying or cleaning documentation, commercial response planning, contents, rebuild coordination, or selecting a qualified firm.</p></div><div class="cards"><article class="card"><span class="tag">Before arrival</span><h3>What information helps route the response?</h3><p>Address, occupancy, event type, affected rooms, source status, utilities, access, hazards, responsible contacts, and safe photos when available.</p></article><article class="card"><span class="tag">First visit</span><h3>What will the company evaluate?</h3><p>Describe the actual inspection, moisture mapping, documentation, work authorization, stabilization, equipment, or referral process without guaranteeing scope.</p></article><article class="card"><span class="tag">Next phase</span><h3>Who handles cleaning, contents, and repairs?</h3><p>Clarify company capabilities, outside specialists, owner decisions, insurer communication boundaries, schedules, and separate agreements.</p></article></div></div></section>''',
        ],
        "primary_scope": "One primary water, fire, smoke, or mold-restoration service",
        "review_h2": "Which towns do you want more qualified restoration calls or project requests from?",
        "faqs": [
            ("Can the website promise a specific emergency arrival time?", "Only if the company verifies that service level and the exact conditions. Otherwise the page uses truthful availability language."),
            ("Will the page say insurance will pay?", "No. Coverage, deductibles, limits, and claim decisions belong to the policy and insurer."),
            ("Can the first build focus only on water damage?", "Yes. One clearly defined restoration service is preferred for the first build."),
            ("Will the site diagnose mold from a photo?", "No. It can explain the company’s evaluation and remediation process without identifying a condition remotely."),
            ("Can we publish IICRC credentials?", "Yes, when each credential and certified-firm status is current, verified, and approved for public use."),
            ("Are restoration calls or projects guaranteed?", "No. REFRDAI does not guarantee indexing, rankings, inquiries, projects, insurance outcomes, or revenue."),
            ("Will the new website replace our emergency-response site?", "No. It runs alongside the current site and focuses on the agreed service and territory."),
        ],
    },
    "commercial-cleaning-janitorial-companies": {
        "industry": "commercial-cleaning",
        "title": "Commercial Cleaning Marketing & Lead Generation | REFRDAI",
        "meta": "Commercial cleaning and janitorial marketing for companies pursuing recurring office, facility, medical, education, industrial, and other selected contracts.",
        "og_title": "Commercial Cleaning Marketing & Lead Generation",
        "og_desc": "Help facility decision makers find your cleaning company while they define scope, schedule, quality, staffing, and accountability.",
        "page_name": "Commercial cleaning company marketing and lead generation",
        "page_desc": "A REFRDAI offer for commercial cleaning companies that want a customer-owned territory website focused on one facility market or contract type.",
        "service_name": "REFRDAI territory website for commercial cleaning companies",
        "service_desc": "A $3,400 customer-owned territory website for one primary commercial cleaning service within an agreed 30-mile radius.",
        "crumb": "Commercial Cleaning and Janitorial Companies",
        "eyebrow": "Commercial cleaning marketing and lead generation",
        "h1": "Be easier to find for recurring cleaning contracts that fit your staffing and operating model.",
        "hero": "A small professional office, medical practice, school, warehouse, dealership, and multi-site property require different staffing, security, schedules, tasks, supplies, documentation, and quality controls. REFRDAI builds a separate website your company owns alongside its current site, focused on one facility market and the communities where you want stronger contract opportunities.",
        "secondary_href": "#facility-fit",
        "secondary": "See the Facility-Buyer Path",
        "fine": "The website does not guarantee bid invitations, contracts, staffing capacity, rankings, retention, or revenue.",
        "panel_title": "A cleaning contract begins with the facility and required standard.",
        "panel_intro": "Square footage alone cannot define labor, frequency, tools, supervision, risk, quality, or price. Useful pages prepare the buyer to discuss the actual building and service expectations.",
        "panel_steps": [
            ("Facility", "What kind of space is being maintained?", "Office, clinic, school, warehouse, retail, common area, industrial site, dealership, religious facility, or another market."),
            ("Program", "What standard and frequency are expected?", "Daily or periodic tasks, occupancy, hours, high-touch areas, restrooms, floors, waste, consumables, events, and special services."),
            ("Control", "How will performance be managed?", "Staffing, training, supervision, inspections, communication, issue response, security, safety, documentation, and measurable expectations."),
        ],
        "offer": [
            ("One facility market", "Choose offices, medical, education, industrial, multi-tenant, or another primary segment."),
            ("A route-aware territory", "Focus on communities that fit staffing, supervision, travel, and contract economics."),
            ("A company-owned bid channel", "Explain the operating system before the walkthrough."),
        ],
        "sections": [
            '''<section id="facility-fit"><div class="container two-col"><div><div class="section-heading"><p class="kicker">Qualify the contract</p><h2>Move the buyer beyond a square-foot price request.</h2><p>Commercial cleaning is a recurring operating commitment. The website should help a facility manager describe the building, desired condition, schedule, current problems, stakeholders, and accountability before expecting a responsible proposal.</p></div><ul class="plain-list"><li>Facility type, occupied areas, approximate size, hours, access, security, and parking.</li><li>Service frequency, task expectations, floor types, restrooms, kitchens, waste, consumables, and periodic work.</li><li>Current-provider transition, staffing restrictions, background requirements, keys, alarms, badges, and confidentiality.</li><li>Safety, training, chemical, equipment, infection-prevention, environmental, or industry-specific requirements as applicable.</li><li>Walkthrough, scope confirmation, proposal, startup, inspection, communication, and issue-resolution process.</li></ul><p class="callout">Commercial cleaning quality depends on the standard, scope, workloading, resources, and management system rather than one measurement alone. <a href="https://cims.issa.com/cims-standard-download/">Review the ISSA Cleaning Industry Management Standard overview</a>.</p></div><aside class="scope-box"><h3>Choose a market the company can serve deeply</h3><div class="scope-grid"><div class="scope-item"><b>Professional offices</b><span>Discretion, consistency, presentation, and after-hours access.</span></div><div class="scope-item"><b>Medical facilities</b><span>Defined procedures, training, documentation, and facility requirements.</span></div><div class="scope-item"><b>Education</b><span>Schedules, occupancy, events, breaks, safety, and large shared areas.</span></div><div class="scope-item"><b>Industrial and warehouse</b><span>Equipment, production, dust, floors, traffic, and site safety.</span></div></div></aside></div></section>''',
            '''<section class="band"><div class="container"><div class="section-heading"><p class="kicker">The buying committee</p><h2>Write for the people who approve, manage, and live with the contract.</h2><p>The owner, facility manager, office administrator, property manager, procurement team, occupants, and cleaning supervisor may judge different parts of the same program.</p></div><div class="cards"><article class="card"><span class="tag">Decision maker</span><h3>Can the company meet the contract requirements?</h3><p>Insurance, staffing, training, references, coverage, pricing structure, documentation, and agreement terms support the selection.</p></article><article class="card"><span class="tag">Facility contact</span><h3>How will daily service be managed?</h3><p>Schedules, access, tasks, supplies, inspections, communication, changes, complaints, and emergencies need clear ownership.</p></article><article class="card"><span class="tag">Occupants</span><h3>Will the space be ready for use?</h3><p>The program must match the agreed standard while respecting safety, privacy, operations, and the people using the facility.</p></article></div></div></section>''',
            '''<section><div class="container"><div class="section-heading"><p class="kicker">From discovery to startup</p><h2>Give every approved community a clearer contract path.</h2></div><div class="decision-path"><article class="decision-step"><span class="step-number">Fit</span><div><strong>Confirm facility type, location, and service needs</strong><p>The page attracts the buildings and recurring programs the company is equipped to manage.</p></div></article><article class="decision-step"><span class="step-number">Walk</span><div><strong>Review the actual space and expectations</strong><p>Rooms, surfaces, traffic, schedules, security, current issues, special requirements, and stakeholder priorities shape the scope.</p></div></article><article class="decision-step"><span class="step-number">Propose</span><div><strong>Define tasks, frequencies, exclusions, staffing, supplies, and price</strong><p>The proposal should state how performance will be measured and how changes will be handled.</p></div></article><article class="decision-step"><span class="step-number">Start</span><div><strong>Plan transition, access, communication, and quality control</strong><p>A strong startup establishes contacts, schedules, site rules, inspections, reporting, and issue response.</p></div></article></div><p class="callout">One town-and-service page plus two original question pages can address facility walkthroughs, contract scope, quality control, transition planning, staffing, security, specialty work, or selecting a building service contractor.</p></div></section>''',
        ],
        "primary_scope": "One primary commercial cleaning facility market or contract type",
        "review_h2": "Which communities do you want more recurring commercial cleaning opportunities from?",
        "faqs": [
            ("Can the website quote janitorial service from square footage alone?", "No. Facility type, scope, frequency, workloading, access, risk, supplies, supervision, and quality expectations also matter."),
            ("Can the first build focus only on medical offices?", "Yes. One facility market or recurring contract type can be the primary focus."),
            ("Can we publish CIMS certification?", "Yes, when the company’s certification is current, verified, and approved for public use."),
            ("Will the pages promise infection prevention or regulatory compliance?", "No. They can accurately describe verified procedures, training, certifications, and facility-specific requirements without guaranteeing an outcome."),
            ("Does the territory site replace our current company site?", "No. It runs alongside the current site."),
            ("Are commercial cleaning contracts guaranteed?", "No. REFRDAI does not guarantee indexing, rankings, inquiries, walkthroughs, bids, contracts, retention, or revenue."),
            ("Why can recurring cleaning fit the initial offer?", "A recurring contract can have meaningful lifetime value, but fit depends on the company’s market, staffing, margins, territory, and sales process."),
        ],
    },
})


def faq_schema(faqs):
    return [
        {"@type": "Question", "name": question, "acceptedAnswer": {"@type": "Answer", "text": answer}}
        for question, answer in faqs
    ]


def head(slug: str, page: dict) -> str:
    url = f"https://local.refrdai.com/industries/{slug}/"
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": url + "#page",
                "url": url,
                "name": page["page_name"],
                "description": page["page_desc"],
                "inLanguage": "en-US",
                "isPartOf": {"@id": "https://local.refrdai.com/#website"},
                "about": {"@id": url + "#service"},
            },
            {
                "@type": "Service",
                "@id": url + "#service",
                "name": page["service_name"],
                "description": page["service_desc"],
                "serviceType": "Customer-owned territory website build",
                "provider": {"@id": "https://refrdai.com/#organization"},
                "areaServed": {"@type": "Country", "name": "United States"},
                "offers": {
                    "@type": "Offer",
                    "price": "3400",
                    "priceCurrency": "USD",
                    "description": "One-time initial build. $1,700 to begin and $1,700 after staging approval, before launch.",
                },
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "REFRDAI Local", "item": "https://local.refrdai.com/"},
                    {"@type": "ListItem", "position": 2, "name": "Industries", "item": "https://local.refrdai.com/industries/"},
                    {"@type": "ListItem", "position": 3, "name": page["crumb"], "item": url},
                ],
            },
            {"@type": "FAQPage", "mainEntity": faq_schema(page["faqs"])},
        ],
    }
    return f'''<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(page["title"])}</title><meta name="description" content="{escape(page["meta"], quote=True)}"><meta name="author" content="William Smith, Founder of REFRDAI"><meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large"><meta name="theme-color" content="#21ddb4"><link rel="canonical" href="{url}"><link rel="manifest" href="/manifest.json"><link rel="stylesheet" href="/assets/industry-pages.css"><meta property="og:type" content="website"><meta property="og:site_name" content="REFRDAI Local"><meta property="og:locale" content="en_US"><meta property="og:url" content="{url}"><meta property="og:title" content="{escape(page["og_title"], quote=True)}"><meta property="og:description" content="{escape(page["og_desc"], quote=True)}"><meta property="og:image" content="https://local.refrdai.com/assets/local-refrdai-social-preview.png"><meta property="og:image:alt" content="REFRDAI Territory Expansion map"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{escape(page["og_title"], quote=True)}"><meta name="twitter:description" content="{escape(page["og_desc"], quote=True)}"><script type="application/ld+json">{json.dumps(data, ensure_ascii=False, separators=(",", ":"))}</script></head>'''


def nav_and_hero(page: dict) -> str:
    steps = "".join(
        f'<div class="flow-item"><span class="flow-num">{escape(number)}</span><div><b>{escape(heading)}</b><span>{escape(copy)}</span></div></div>'
        for number, heading, copy in page["panel_steps"]
    )
    facts = "".join(
        f'<div class="offer-fact"><b>{escape(heading)}</b><span>{escape(copy)}</span></div>'
        for heading, copy in page["offer"]
    )
    return f'''<a class="skip" href="#main">Skip to main content</a><nav class="site-nav" aria-label="Primary navigation"><div class="container nav-inner"><a class="brand" href="/"><span class="brand-mark" aria-hidden="true">RD</span><span class="brand-name"><em>REFR</em>DAI · Local</span></a><div class="nav-links"><a href="/industries/">Industries</a><a href="#investment">Investment</a><a class="button button-primary" data-track="primary-cta" href="#territory-review">Request My Free 15-Minute Territory Review</a></div></div></nav><div class="container breadcrumb"><a href="/">Home</a> / <a href="/industries/">Industries</a> / {escape(page["crumb"])}</div><header class="hero"><div class="container hero-grid"><div><p class="eyebrow">{escape(page["eyebrow"])}</p><h1>{escape(page["h1"])}</h1><p class="hero-copy">{escape(page["hero"])}</p><div class="hero-actions"><a class="button button-primary" data-track="primary-cta" href="#territory-review">Request My Free 15-Minute Territory Review</a><a class="button button-secondary" href="{page["secondary_href"]}">{escape(page["secondary"])}</a></div><p class="fine-print">{escape(page["fine"])}</p></div><aside class="trade-panel"><h2>{escape(page["panel_title"])}</h2><p>{escape(page["panel_intro"])}</p><div class="trade-flow">{steps}</div></aside></div></header><div class="offer-strip" data-qa-shared="true"><div class="container offer-facts">{facts}</div></div>'''


def investment(page: dict) -> str:
    return f'''<section class="band" id="investment" data-qa-shared="true"><div class="container"><div class="section-heading"><p class="kicker">Clear investment</p><h2>Know the full initial price before you book.</h2><p>The customer-owned territory website costs $3,400.</p></div><div class="pricing"><article class="price-card"><span class="price-label">One-time initial build</span><div class="price">$3,400 <small>total</small></div><p>{escape(page["primary_scope"])}, one agreed 30-mile radius, and every eligible approved community, up to 100.</p><div class="payment-split"><div><b>$1,700</b><span>To begin production</span></div><div><b>$1,700</b><span>After staging approval, before launch</span></div></div><p>REFRDAI pays for the domain’s first year and transfers it after launch and cleared final payment as soon as the registrar permits. Managed hosting under normal usage is included.</p></article><div class="options"><article class="option-card"><span class="optional-label">Optional after the first year</span><h3>$495 Territory Continuity Review</h3><p>Includes the applicable domain renewal for that term and may renew territory protection after a scope and conflict review plus written renewal. If declined, you keep the site and domain, protection expires, and you pay the registrar directly for future renewal.</p></article><article class="option-card"><span class="optional-label">Separate and never automatic</span><h3>Possible $500 monthly expansion</h3><p>May be offered around month three only when enough usable search-performance data exists. It is optional and never starts automatically.</p></article></div></div></div></section>'''


def faq_section(page: dict) -> str:
    cards = "".join(
        f'<article class="faq"><h3>{escape(question)}</h3><p>{escape(answer)}</p></article>'
        for question, answer in page["faqs"]
    )
    return f'''<section><div class="container"><div class="section-heading"><p class="kicker">Questions before the review</p><h2>{escape(page["crumb"])} questions</h2><p>Clear answers before you decide whether the first build fits.</p></div><div class="faq-grid">{cards}</div></div></section>'''


def review(page: dict) -> str:
    return f'''<section class="review-section band" id="territory-review" data-qa-shared="true"><div class="container review-grid"><div class="review-copy"><p class="kicker">Free 15-minute review</p><h2>{escape(page["review_h2"])}</h2><p>Share your company name, company website, email, and the towns or counties you want to review. Phone is optional.</p><div class="review-facts"><div class="review-fact"><b>Meeting</b><span>15-minute Google Meet</span></div><div class="review-fact"><b>Hours</b><span>Monday through Friday, 10:00 AM to 5:00 PM Eastern</span></div><div class="review-fact"><b>Booking</b><span>At least 24 hours ahead and up to 30 days out</span></div><div class="review-fact"><b>Cost</b><span>Free, with no purchase obligation</span></div></div><p class="privacy">Submitting the form does not authorize automatic outreach, enrollment, or a purchase.</p></div><div class="form-card"><h2>Request My Free 15-Minute Territory Review</h2><p>Complete the short intake, then choose an available Google Meet time.</p><script src="https://js.hsforms.net/forms/embed/{PORTAL_ID}.js" defer></script><div class="hs-form-frame" data-region="na1" data-form-id="{FORM_ID}" data-portal-id="{PORTAL_ID}"></div><noscript><p>JavaScript is required to load the intake form.</p></noscript><a class="form-fallback" href="{FORM_FALLBACK}" rel="nofollow">Open the Secure Intake Form</a><div class="booking-panel" data-booking-panel aria-hidden="true"><h3>Choose Your 15-Minute Review Time</h3><p>The appointment calendar appears after a successful form submission.</p><iframe title="Book a Territory Opportunity Review with William Smith" src="{BOOKING}" loading="lazy"></iframe><a class="booking-fallback" data-booking-link href="{BOOKING}">Open Google Calendar in a New Page</a></div></div></div></section>'''


def render(slug: str, page: dict) -> str:
    sections = "".join(page["sections"])
    return f'''<!doctype html><html lang="en-US">{head(slug, page)}<body data-industry="{page["industry"]}">{nav_and_hero(page)}<main id="main">{sections}{investment(page)}{faq_section(page)}{review(page)}</main><footer><div class="container footer-inner"><span>© 2026 REFRDAI Local. Customer-owned territory websites for local service businesses.</span><div class="footer-links"><a href="/">Home</a><a href="/industries/">Industries</a><a href="/entity-source-of-truth/">Definitions</a><a href="/insights/">Insights</a></div></div></footer><script src="/assets/industry-pages.js" defer></script></body></html>\n'''


for slug, page in PAGES.items():
    path = ROOT / "industries" / slug / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render(slug, page), encoding="utf-8", newline="\n")
    print(f"Built {path.relative_to(ROOT)}")
