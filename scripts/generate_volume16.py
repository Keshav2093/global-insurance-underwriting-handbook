"""Generate Volume 16 - Specialty Insurance chapters using the repository chapter template."""

from pathlib import Path

BASE = Path("docs/volume-16-specialty-insurance")
BASE.mkdir(exist_ok=True)

INDEX = """# Volume 16 — Specialty Insurance

Volume 16 covers specialty and non-standard insurance lines: aviation, marine, energy, mining, political risk, trade credit, entertainment, jewellers block, fine art, space, kidnap & ransom, and other specialist covers. Specialty lines require deep technical knowledge, tailored wordings, and careful risk selection.

## Chapters

| Chapter | Title | Contents |
|---------|-------|----------|
| [16.1](01-aviation.md) | Aviation Insurance | Hull, liability, airport, products |
| [16.2](02-marine-hull.md) | Marine Hull | Hull & machinery, war risk |
| [16.3](03-cargo.md) | Marine Cargo | Goods in transit, multimodal |
| [16.4](04-energy.md) | Energy Insurance | Upstream, downstream, power |
| [16.5](05-mining.md) | Mining Insurance | Underground, open-pit, equipment |
| [16.6](06-political-risk.md) | Political Risk | Confiscation, expropriation, currency |
| [16.7](07-trade-credit.md) | Trade Credit | Buyer default, political cover |
| [16.8](08-entertainment.md) | Entertainment | Film, events, casts, cancellation |
| [16.9](09-jewellers-block.md) | Jewellers Block | Jewellers stock & property |
| [16.10](10-fine-art.md) | Fine Art | Collections, exhibitions, transit |
| [16.11](11-space.md) | Space Insurance | Launch, in-orbit, liability |
| [16.12](12-kidnap-ransom.md) | Kidnap & Ransom | Extortion, response, crisis |

## Learning Objectives

After completing this volume you should be able to:

1. Explain the structure of each specialty line.
2. Describe the coverages, limits, and exclusions.
3. Identify underwriting information and rating factors.
4. Explain claims and risk engineering considerations.

## Suggested Reading

- Start with [16.1 Aviation Insurance](01-aviation.md).
- Cross-reference Volume 2 (Personal), Volume 3 (Commercial), Volume 15 (Reinsurance).

---

*Part of the Global Insurance Underwriting Handbook — Volume 16*
"""


def chapter(num, title, subtitle, summary, coverages, risks, underwriting, rating, exclusions,
            keywords, related, prev, next, prev_title, next_title, review_qs, glossary, takeaways):
    cov_rows = "\n".join(f"| {c[0]} | {c[1]} | {c[2]} |" for c in coverages)
    risk_rows = "\n".join(f"| {r[0]} | {r[1]} | {r[2]} |" for r in risks)
    uw_rows = "\n".join(f"| {u[0]} | {u[1]} |" for u in underwriting)
    rate_rows = "\n".join(f"| {r[0]} | {r[1]} | {r[2]} |" for r in rating)
    excl_rows = "\n".join(f"| {e[0]} | {e[1]} |" for e in exclusions)
    nxt = f"[{next_title}]({next})" if next else "— (end of volume)"
    prv = f"[{prev_title}]({prev})" if prev else "Volume 16 Home"
    body = f"""# 16.{num} — {title}

> **Learning Objectives**
>
> After completing this chapter you should be able to:
>
> 1. Define {title.lower()} and describe the coverages provided.
> 2. Identify the principal risks, rating factors, and underwriting information.
> 3. Explain the key exclusions and claims considerations.
> 4. Describe reinsurance and capacity requirements.

<!-- Metadata (for RAG / AI knowledge base)
keywords: {keywords}
tags: specialty, {subtitle.lower().replace(' ', '-')}
categories: volume-16
related: {related}
-->

## Executive Summary

{summary}

---

## 16.{num}.1 {subtitle} — Overview

{title} is a specialised class of insurance requiring technical underwriting knowledge and tailored policy wordings.

| Feature | Description |
|---------|-------------|
| Market | Specialist insurers, Lloyd's, brokers |
| Underwriting | Technical, case-by-case |
| Coverage | {subtitle} risk-specific wordings |
| Rating | Exposure and experience-based |

---

## 16.{num}.2 Coverages

| Coverage | Description | Typical Limit |
|----------|-------------|---------------|
{cov_rows}

---

## 16.{num}.3 Key Risks

| Risk | Description | Mitigation |
|------|-------------|------------|
{risk_rows}

---

## 16.{num}.4 Underwriting Information

| Information | Purpose |
|-------------|---------|
{uw_rows}

---

## 16.{num}.5 Rating Factors

| Factor | Impact | Description |
|--------|--------|-------------|
{rate_rows}

---

## 16.{num}.6 Exclusions & Conditions

| Exclusion / Condition | Reason |
|-----------------------|--------|
{excl_rows}

---

## 16.{num}.7 Claims & Risk Engineering

| Stage | Action |
|-------|--------|
| Notification | Prompt notice, specialist adjusters |
| Investigation | Technical experts, causation analysis |
| Settlement | Within limits, subrogation reviewed |

---

## 16.{num}.8 Reinsurance & Capacity

| Requirement | Detail |
|-------------|--------|
| Capacity | Large limits via facultative/treaty |
| Accumulation | Geographic and modal exposures |
| Security | Reinsurer ratings and collateral |

---

## Review Questions

{review_qs}

---

## Glossary

| Term | Definition |
|------|------------|
{glossary}

---

## Key Takeaways

{takeaways}

---

## References & Further Reading

- Lloyd's Market Association — specialty wordings
- IUMI (International Union of Marine Insurance) publications
- Airports Council International — aviation guidance

---

**Previous:** {prv} | **Next:** {nxt}

---

*Part of the Global Insurance Underwriting Handbook — Volume 16*
"""
    return body


C = [
    dict(num="1", title="Aviation Insurance", subtitle="Aviation", file="01-aviation.md",
         summary="Aviation insurance covers aircraft hulls, passengers, third parties, airports, and aviation products. Underwriting demands technical understanding of aircraft types, operators, maintenance, and usage.",
         coverages=[("Aircraft hull", "Physical damage to own aircraft", "Per hull"), ("Aviation liability", "Passenger and third-party liability", "Varies by fleet"), ("Airport liability", "Airport operations liability", "Varies")],
         risks=[("Aircraft type & age", "Hull and loss profile", "Age limits and hull schedules"), ("Operator experience", "Safety culture", "Review safety records"), ("Usage profile", "Passenger vs cargo, regions", "Geographic underwriting")],
         underwriting=[("Operator", "Experience and safety", "Pilot records"), ("Fleet", "Composition and values", "Hull schedule"), ("Usage", "Routes, sectors", "Utilisation report")],
         rating=[("Hull value", "High", "Premiums on declared values"), ("Operator quality", "High", "Experience and safety credits"), ("Usage", "Medium", "Risk profile by route/load")],
         exclusions=[("War & terrorism", "Separate cover"), ("Unapproved use", "Outside terms")],
         keywords="aviation, hull, liability, airport", related="volume-16-02, volume-16-04",
         prev=None, next="02-marine-hull.md", prev_title="Volume 16 Home", next_title="Marine Hull",
         review_qs="1. What are the main aviation coverages?\\n2. Why does operator quality matter to underwriters?",
         glossary="| Hull | Physical aircraft damage coverage |\\n| Fleet | All aircraft of an operator |",
         takeaways="1. **Aviation is a technical class** requiring specialist underwriting.\\n2. **Operator quality and maintenance records are critical.**"),
    dict(num="2", title="Marine Hull", subtitle="Marine Hull", file="02-marine-hull.md",
         summary="Marine hull insurance covers ships, machinery, and related liabilities. Underwriters assess vessel value, age, class, trade routes, and flag.",
         coverages=[("Hull & machinery", "Vessel physical damage", "Vessel value"), ("War risk", "War and strikes cover", "Additional"), ("Loss of hire", "Income protection", "Per day")],
         risks=[("Vessel class", "Classification society", "Require class maintained"), ("Age & condition", "Hull integrity", "Age limits, surveys"), ("Trading area", "Route risk profile", "Restrict trading areas")],
         underwriting=[("Vessel details", "Age, flag, tonnage", "Register details"), ("Classification", "Class society status", "Class certificate"), ("Trading area", "Geographic risk", "Trade warranty")],
         rating=[("Vessel value", "High", "Premium on hull value"), ("Age", "Medium", "Age-adjusted rates"), ("Trading area", "High", "Geographic rating")],
         exclusions=[("War & strikes", "Separate or additional cover"), ("Delay", "Not covered unless added")],
         keywords="marine, hull, machinery, vessel", related="volume-16-01, volume-16-03",
         prev="01-aviation.md", next="03-cargo.md", prev_title="Aviation Insurance", next_title="Marine Cargo",
         review_qs="1. What is a classification society?\\n2. What does hull & machinery cover?",
         glossary="| H&M | Hull & machinery |\\n| P&I | Protection & indemnity |",
         takeaways="1. **Hull value and condition drive pricing.**\\n2. **Trading area affects war and perils risk.**"),
    dict(num="3", title="Marine Cargo", subtitle="Cargo", file="03-cargo.md",
         summary="Cargo insurance protects goods in transit by sea, air, road, and rail. Cover may be on open cover or voyage basis with institute cargo clauses.",
         coverages=[("All risks", "Broad transit cover", "Consignment value"), ("Named perils", "Specific risks", "Consignment value"), ("War & strikes", "Political perils", "Additional")],
         risks=[("Commodity", "Hazard and packing", "Condition surveys"), ("Transit route", "Exposure to theft, damage", "Routing controls"), ("Carrier", "Reliability and security", "Approved carriers")],
         underwriting=[("Commodity", "Nature and packing", "Packing declarations"), ("Transit", "Route and modes", "Open cover details"), ("Values", "Consignment values", "Invoice values")],
         rating=[("Commodity", "High", "Per commodity rates"), ("Transit", "Medium", "Routing factors"), ("Value", "Medium", "Per consignment basis")],
         exclusions=[("Inherent vice", "Excluded under all risks"), ("Delay", "Not covered")],
         keywords="cargo, transit, marine, open cover", related="volume-16-02, volume-16-07",
         prev="02-marine-hull.md", next="04-energy.md", prev_title="Marine Hull", next_title="Energy Insurance",
         review_qs="1. What is an open cover?\\n2. What is the difference between all risks and named perils?",
         glossary="| Open cover | Automatic cargo cover |\\n| Institute clauses | Standard cargo wordings |",
         takeaways="1. **Commodity and route determine risk.**\\n2. **Open cover is common for regular shippers.**"),
    dict(num="4", title="Energy Insurance", subtitle="Energy", file="04-energy.md",
         summary="Energy insurance covers upstream oil and gas, downstream refining, power generation, construction, and operational risks. Losses can be catastrophic.",
         coverages=[("Upstream", "Exploration & production", "Varies"), ("Downstream", "Refineries, petrochemicals", "Varies"), ("Power", "Generation & distribution", "Varies")],
         risks=[("Facility type", "Process hazard", "Process safety reviews"), ("Location", "Political and natural perils", "Geographic analysis"), ("Safety systems", "Loss prevention", "Audits and surveys")],
         underwriting=[("Facility", "Operations and processes", "Engineering reports"), ("Location", "Country and site", "Political risk review"), ("Protection", "Fire and safety", "Survey reports")],
         rating=[("Process hazard", "High", "Hazard-rated premiums"), ("Location", "Medium", "Regional factors"), ("Protection", "Medium", "Loss prevention credits")],
         exclusions=[("Pollution", "Limited or separate", ""), ("War & terrorism", "Separate cover", "")],
         keywords="energy, upstream, downstream, power", related="volume-16-01, volume-16-05",
         prev="03-cargo.md", next="05-mining.md", prev_title="Marine Cargo", next_title="Mining Insurance",
         review_qs="1. What is upstream energy insurance?\\n2. Why is energy a high-severity class?",
         glossary="| Upstream | Exploration & production |\\n| Downstream | Refining & marketing |",
         takeaways="1. **Energy risks are high severity and low frequency.**\\n2. **Process safety is core to underwriting.**"),
    dict(num="5", title="Mining Insurance", subtitle="Mining", file="05-mining.md",
         summary="Mining insurance covers underground and open-pit operations, plant and equipment, business interruption, and liability. Specialist engineering input is essential.",
         coverages=[("Property & equipment", "Mining assets", "Varies"), ("Business interruption", "Loss of production", "Per policy"), ("Liability", "Operations and third parties", "Varies")],
         risks=[("Mining method", "Underground vs open-pit", "Engineering assessment"), ("Geological risk", "Ground, water, gas", "Geotechnical studies"), ("Equipment", "Age and maintenance", "Maintenance audits")],
         underwriting=[("Operations", "Method and scale", "Mine plan"), ("Geology", "Hazard conditions", "Geotechnical report"), ("Equipment", "Fleet values", "Asset schedule")],
         rating=[("Method", "High", "Underground vs open-pit"), ("Geology", "High", "Hazard-based factors"), ("Equipment", "Medium", "Fleet values")],
         exclusions=[("Ground movement", "Subsidence limits", ""), ("Pollution", "Separate cover", "")],
         keywords="mining, underground, open-pit, equipment", related="volume-16-04, volume-03",
         prev="04-energy.md", next="06-political-risk.md", prev_title="Energy Insurance", next_title="Political Risk",
         review_qs="1. How does mining method affect risk?\\n2. What is business interruption in mining?",
         glossary="| Open-pit | Surface mining method |\\n| BI | Business interruption |",
         takeaways="1. **Mining risk varies with method and geology.**\\n2. **Maintenance and safety culture matter.**"),
    dict(num="6", title="Political Risk", subtitle="Political Risk", file="06-political-risk.md",
         summary="Political risk insurance covers confiscation, expropriation, political violence, currency inconvertibility, and contract frustration. It protects cross-border investors.",
         coverages=[("Expropriation", "Government seizure", "Per project"), ("Political violence", "War, civil unrest", "Per project"), ("Currency", "Inconvertibility, transfer", "Per project")],
         risks=[("Country risk", "Political stability", "Country limits and review"), ("Investment structure", "Legal protections", "Treaty analysis"), ("Sector", "Sensitive industries", "Sector policies")],
         underwriting=[("Country", "Risk rating", "Country reports"), ("Investment", "Structure and protections", "Legal opinion"), ("Term", "Duration of exposure", "Project timeline")],
         rating=[("Country rating", "High", "Country-specific rates"), ("Sector", "Medium", "Sector risk factors"), ("Term", "Medium", "Term-based rates")],
         exclusions=[("War & terrorism", "Managed within violence cover"), ("Commercial risk", "Excluded")],
         keywords="political risk, expropriation, confiscation, currency", related="volume-16-07, volume-08",
         prev="05-mining.md", next="07-trade-credit.md", prev_title="Mining Insurance", next_title="Trade Credit",
         review_qs="1. What is expropriation cover?\\n2. Why is country risk central to political risk underwriting?",
         glossary="| Expropriation | Government seizure |\\n| PR | Political risk |",
         takeaways="1. **Country and sector analysis drive decisions.**\\n2. **Cover is project-specific and often short-term.**"),
    dict(num="7", title="Trade Credit", subtitle="Trade Credit", file="07-trade-credit.md",
         summary="Trade credit insurance protects suppliers against buyer default and political events, enabling trade on open account terms.",
         coverages=[("Whole turnover", "Portfolio buyer cover", "Credit limit"), ("Specific buyer", "Single debtor cover", "Credit limit"), ("Political cover", "Sovereign risk", "Per policy")],
         risks=[("Buyer creditworthiness", "Default risk", "Credit assessment"), ("Concentration", "Largest debtors", "Limit management"), ("Sector & country", "Economic risk", "Sector review")],
         underwriting=[("Turnover", "Insured sales", "Sales ledger"), ("Buyers", "Debtor credit profile", "Credit reports"), ("Terms", "Payment terms", "Contract terms")],
         rating=[("Buyer quality", "High", "Credit-rated premiums"), ("Concentration", "Medium", "Limits per buyer"), ("Sector", "Medium", "Sector factors")],
         exclusions=[("Disputed debts", "Excluded until resolved"), ("Pre-existing default", "Excluded")],
         keywords="trade credit, buyer default, open account, credit limit", related="volume-16-06, volume-03",
         prev="06-political-risk.md", next="08-entertainment.md", prev_title="Political Risk", next_title="Entertainment",
         review_qs="1. What does trade credit insurance protect?\\n2. What is a credit limit?",
         glossary="| Buyer default | Buyer insolvency/non-payment |\\n| Turnover | Annual sales |",
         takeaways="1. **Credit analysis of buyers is essential.**\\n2. **Cover enables open-account trade.**"),
    dict(num="8", title="Entertainment Insurance", subtitle="Entertainment", file="08-entertainment.md",
         summary="Entertainment insurance covers film, television, events, performances, casts, and equipment. Production and cancellation risks are central.",
         coverages=[("Production", "Cast, props, negatives", "Budget-based"), ("Cancellation", "Event cancellation", "Event budget"), ("Equipment", "Cameras, sound, gear", "Schedule")],
         risks=[("Production type", "Film, TV, live event", "Schedule control"), ("Cast risk", "Key personnel", "Key person protection"), ("Location", "Schedule and geography", "Location plans")],
         underwriting=[("Budget", "Scale of production", "Production budget"), ("Cast", "Key personnel", "Health and contracts"), ("Schedule", "Timeline", "Production schedule")],
         rating=[("Budget", "High", "Premium on budget"), ("Cast", "Medium", "Key person risk"), ("Schedule", "Medium", "Exposure duration")],
         exclusions=[("Nuclear", "Standing exclusion"), ("War & terrorism", "Separate cover")],
         keywords="entertainment, film, cast, cancellation, event", related="volume-16-10, volume-03",
         prev="07-trade-credit.md", next="09-jewellers-block.md", prev_title="Trade Credit", next_title="Jewellers Block",
         review_qs="1. What is cast insurance?\\n2. Why is cancellation cover important?",
         glossary="| Cast cover | Key person protection |\\n| Completion | Budget protection |",
         takeaways="1. **Production budgets drive limits.**\\n2. **Scheduling and key-person risk dominate.**"),
    dict(num="9", title="Jewellers Block", subtitle="Jewellers Block", file="09-jewellers-block.md",
         summary="Jewellers block covers jewellers' stock, property, and money on premises, in transit, and in the custody of customers.",
         coverages=[("Stock on premises", "Jewellery stock", "Per location"), ("Stock in transit", "Goods in transit", "Per policy"), ("Money cover", "Cash and valuables", "Per policy")],
         risks=[("Stock value", "Peak values", "Valuation schedules"), ("Security", "Alarms, safes", "Security audits"), ("Transit", "Couriers, vehicles", "Approved couriers")],
         underwriting=[("Stock", "Values and location", "Stock valuations"), ("Security", "Systems in place", "Security survey"), ("Transit", "Movement methods", "Courier procedures")],
         rating=[("Stock value", "High", "Value-based premium"), ("Security", "High", "Security credits/loadings"), ("Transit", "Medium", "Movement factors")],
         exclusions=[("Mysterious disappearance", "Limited or excluded", ""), ("Dishonesty", "Separate fidelity cover", "")],
         keywords="jewellers block, stock, transit, security", related="volume-16-10, volume-02",
         prev="08-entertainment.md", next="10-fine-art.md", prev_title="Entertainment", next_title="Fine Art",
         review_qs="1. What is jewellers block?\\n2. Why is security central?",
         glossary="| Stock in transit | Goods during movement |\\n| Jewellers block | Jewellers package |",
         takeaways="1. **Security systems reduce theft risk.**\\n2. **Stock values require current valuations.**"),
    dict(num="10", title="Fine Art", subtitle="Fine Art", file="10-fine-art.md",
         summary="Fine art insurance covers collections, individual works, exhibitions, and transit. Valuation, handling, and security are key.",
         coverages=[("Collections", "Private/corporate art", "Agreed value"), ("Exhibitions", "Loans and exhibits", "Per exhibition"), ("Transit", "Art in transit", "Per consignment")],
         risks=[("Valuation", "Current market value", "Appraisals"), ("Handling", "Expert installers", "Approved handlers"), ("Security", "Climate, theft controls", "Security plans")],
         underwriting=[("Valuation", "Declared value", "Appraisal reports"), ("Handling", "Installers and couriers", "Approved list"), ("Security", "Facility controls", "Risk survey")],
         rating=[("Valuation", "High", "Value-based premium"), ("Handling", "Medium", "Approved vs general"), ("Security", "Medium", "Control credits")],
         exclusions=[("Inherent vice", "Fragility and deterioration", ""), ("Wear & tear", "Excluded", "")],
         keywords="fine art, collection, exhibition, transit", related="volume-16-09, volume-02",
         prev="09-jewellers-block.md", next="11-space.md", prev_title="Jewellers Block", next_title="Space Insurance",
         review_qs="1. What is agreed value basis?\\n2. Why does handling matter?",
         glossary="| Agreed value | Pre-agreed insured amount |\\n| Fine art | High-value art work |",
         takeaways="1. **Valuation must be current.**\\n2. **Transit and handling risks are high.**"),
    dict(num="11", title="Space Insurance", subtitle="Space", file="11-space.md",
         summary="Space insurance covers launch failure, in-orbit operations, and third-party liability. It is high-severity, low-frequency, and heavily reinsured.",
         coverages=[("Launch", "Pre-launch to orbit", "Mission value"), ("In-orbit", "Satellite operations", "Per satellite"), ("Liability", "Third-party space liability", "Per policy")],
         risks=[("Mission profile", "Launch vehicle, orbit", "Technical review"), ("Satellite", "Technology maturity", "Maturity assessment"), ("Track record", "Vehicle reliability", "Experience records")],
         underwriting=[("Mission", "Launch and orbit", "Mission plan"), ("Satellite", "Design and build", "Technical dossier"), ("Track record", "Historical reliability", "Experience tables")],
         rating=[("Mission", "High", "Mission risk profile"), ("Satellite", "High", "Technology factor"), ("Track record", "Medium", "Experience credits")],
         exclusions=[("Design defects", "Excluded or limited", ""), ("Gradual degradation", "Excluded", "")],
         keywords="space, launch, satellite, in-orbit", related="volume-15, volume-16-01",
         prev="10-fine-art.md", next="12-kidnap-ransom.md", prev_title="Fine Art", next_title="Kidnap & Ransom",
         review_qs="1. What does launch cover protect?\\n2. Why is space heavily reinsured?",
         glossary="| Satellite | Spacecraft |\\n| Launch | Mission placement |",
         takeaways="1. **Space is high-severity and technical.**\\n2. **Reliability records guide underwriting.**"),
    dict(num="12", title="Kidnap & Ransom", subtitle="Kidnap & Ransom", file="12-kidnap-ransom.md",
         summary="Kidnap and ransom insurance covers ransom payments, crisis response, and extortion. It provides response consultants and expense cover.",
         coverages=[("Ransom", "Ransom payment cover", "Per policy"), ("Crisis response", "Consultants, negotiation", "Per policy"), ("Extortion", "Threats and extortion", "Per policy")],
         risks=[("Exposure", "Travel, regional risk", "Travel guidance"), ("Security", "Protective measures", "Security review"), ("Response", "Crisis consultants", "Response plan")],
         underwriting=[("Exposure", "Geographic activity", "Travel schedules"), ("Security", "Protection measures", "Security audit"), ("Response", "Crisis readiness", "Response plan")],
         rating=[("Exposure", "High", "Geographic rates"), ("Security", "Medium", "Protection credits"), ("Response", "Medium", "Readiness factor")],
         exclusions=[("Excluded jurisdictions", "Wording-specific", ""), ("Punitive damages", "Excluded", "")],
         keywords="kidnap, ransom, extortion, crisis", related="volume-16-06, volume-17",
         prev="11-space.md", next=None, prev_title="Space Insurance", next_title=None,
         review_qs="1. What does K&R cover?\\n2. Why are crisis response services part of cover?",
         glossary="| K&R | Kidnap & ransom |\\n| Extortion | Threats for payment |",
         takeaways="1. **Cover includes response services, not just ransom.**\\n2. **Security measures reduce exposure.**"),
]

(BASE / "index.md").write_text(INDEX, encoding="utf-8")

for s in C:
    rendered = chapter(
        s["num"], s["title"], s["subtitle"], s["summary"], s["coverages"], s["risks"],
        s["underwriting"], s["rating"], s["exclusions"], s["keywords"], s["related"],
        s["prev"], s["next"], s["prev_title"], s["next_title"], s["review_qs"],
        s["glossary"], s["takeaways"],
    )
    (BASE / s["file"]).write_text(rendered, encoding="utf-8")
    print(f"Created {s['file']}")

print("Volume 16 generation complete.")