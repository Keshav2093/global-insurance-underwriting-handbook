"""Generate Volume 17 - Insurance Fraud handbook chapters."""

from pathlib import Path

BASE = Path("docs/volume-17-fraud")
BASE.mkdir(exist_ok=True)

INDEX = """# Volume 17 — Insurance Fraud

Volume 17 covers insurance fraud detection, prevention, and investigation: the types of fraud across personal and commercial lines, red flags, special investigation units (SIU), analytics, and emerging fraud schemes.

## Chapters

| Chapter | Title | Contents |
|---------|-------|----------|
| [17.1](01-fraud-fundamentals.md) | Fraud Fundamentals | Definition, impact, types |
| [17.2](02-auto-fraud.md) | Auto Fraud | Staged accidents, exaggerations |
| [17.3](03-property-fraud.md) | Property Fraud | Arson, inflated claims |
| [17.4](04-liability-fraud.md) | Liability Fraud | Slip & fall, injury claims |
| [17.5](05-siu.md) | Special Investigation Unit | SIU structure, referral, investigation |
| [17.6](06-analytics-fraud.md) | Data & Analytics | Predictive models, network analysis |
| [17.7](07-emerging-fraud.md) | Emerging Fraud | Cyber, organised rings, social |

## Learning Objectives

After completing this volume you should be able to:

1. Explain the types and financial impact of insurance fraud.
2. Identify red flags across lines of business.
3. Describe the SIU investigation process.
4. Apply data and analytics to fraud detection.
5. Recognise emerging fraud schemes.

## Suggested Reading

- Start with [17.1 Fraud Fundamentals](01-fraud-fundamentals.md).
- Cross-reference Volume 7 (Claims), Volume 10 (Data), Volume 14 (AI in Insurance).

---

*Part of the Global Insurance Underwriting Handbook — Volume 17*
"""

CHAPTERS = [
    dict(num="1", title="Fraud Fundamentals", file="01-fraud-fundamentals.md",
         intro="Insurance fraud is a deliberate deception to obtain a benefit under an insurance policy or to avoid a premium obligation. It affects every line of business and adds billions to premium costs worldwide.",
         sections=[
            ("Definition", "Fraud is an intentional deception for financial gain", "—"),
            ("Hard fraud", "Fabricated loss — accident never happened", "Criminal prosecution"),
            ("Soft fraud", "Exaggerated claim / misstated application", "Most common form"),
            ("Impact", "Higher premiums, delays, reputational risk", "Fraud prevention investment"),
         ],
         tables=[
            ("Fraud Types", [("Hard fraud", "Fabricated events", "Arson, staged collisions"),
                             ("Soft fraud", "Exaggerated losses", "Inflated estimates"),
                             ("Organised", "Rings with repeated activity", "Mobility, scheme coordination"),
                             ("Opportunistic", "Individual exaggeration", "Applications misstatement")]),
            ("Where Fraud Occurs", [("Application", "Misstatement at quote", "Medical history, garaging"),
                                    ("Claims", "Fabrication, inflation", "Most fraud is in claims"),
                                    ("Premium", "Misclassification", "Payroll, employee count"),
                                    ("Distribution", "Agent/broker schemes", "Premium diversion")]),
         ],
         review="1. Distinguish hard fraud from soft fraud.\\n2. Why is soft fraud more common?\\n3. What are the costs of fraud to insurers?",
         glossary="| Hard fraud | Fabricated loss |\\n| Soft fraud | Exaggerated or misstated claim |",
         takeaways="1. **Fraud is deliberate deception for financial gain.**\\n2. **Most fraud is soft fraud — exaggeration and misstatement.**\\n3. **Fraud raises premiums and requires prevention investment.**",
         next="02-auto-fraud.md", next_title="Auto Fraud",
         prev="index.md", prev_title="Volume 17 Home",
         related="volume-07, volume-10, volume-14"),
    dict(num="2", title="Auto Fraud", file="02-auto-fraud.md",
         intro="Auto insurance fraud includes staged accidents, inflated repair claims, phantom passengers, and paper accidents. Vehicle theft fraud and damage exaggeration are significant cost drivers.",
         sections=[
            ("Staged accidents", "Deliberately caused collisions", "SIU referral"),
            ("Paper accidents", "Claim without accident", "Verify facts, photos"),
            ("Exaggeration", "Inflated injuries or repair costs", "Independent appraisal"),
            ("Theft fraud", "False vehicle theft", "Examine keys, finance"),
         ],
         tables=[
            ("Auto Fraud Schemes", [("Staged collision", "Cars collide intentionally", "Witness inconsistencies"),
                                    ("Phantom passengers", "Fake occupants claim injury", "Occupancy verification"),
                                    ("Inflated estimates", "Repairs exceed damage", "Audit estimates"),
                                    ("Theft fraud", "Vehicle hidden/sold", "Review keys and finance")]),
            ("Auto Red Flags", [("Late reporting", "Accident reported days later", "Check timeline"),
                                ("Multiple claimants", "Common address", "Network analysis"),
                                ("Inconsistent damage", "Damage does not match story", "Examine photographs"),
                                ("Attorney involvement", "Immediate representation", "Monitor patterns")]),
         ],
         review="1. What is a paper accident?\\n2. List three auto fraud red flags.\\n3. How can estimators detect inflated repairs?",
         glossary="| Paper accident | Claim without real accident |\\n| Staged collision | Deliberately caused crash |",
         takeaways="1. **Auto fraud ranges from staged collisions to exaggerated estimates.**\\n2. **Verify accident facts, occupants, and repair costs.**\\n3. **Network analysis identifies organised rings.**",
         next="03-property-fraud.md", next_title="Property Fraud",
         prev="01-fraud-fundamentals.md", prev_title="Fraud Fundamentals",
         related="volume-07, volume-02"),
    dict(num="3", title="Property Fraud", file="03-property-fraud.md",
         intro="Property fraud includes arson, inflated damage claims, pre-existing damage, and inventory inflation. Fire and burglary claims require careful investigation of motive and timing.",
         sections=[
            ("Arson", "Deliberate fire for financial gain", "Financial motive review"),
            ("Inflated claims", "Damage estimate exceeds actual loss", "Independent adjusters"),
            ("Pre-existing damage", "Old damage presented as new loss", "Condition documents"),
            ("Inventory inflation", "Contents claimed not owned", "Documentation review"),
         ],
         tables=[
            ("Property Fraud Indicators", [("Financial stress", "Debt, foreclosure", "Motivation check"),
                                           ("Recently increased cover", "Value jumps before loss", "Policy change review"),
                                           ("Poor documentation", "No receipts", "Require proof"),
                                           ("Overstated valuations", "Values exceed market", "Appraisal")]),
            ("Investigation Actions", [("Scene inspection", "Physical evidence", "Fire/engineers"),
                                       ("Financial review", "Motive assessment", "Credit and records"),
                                       ("Document review", "Proof of ownership", "Receipts, warranties"),
                                       ("Timeline verification", "Activity before loss", "Surveillance/photos")]),
         ],
         review="1. Why is financial motive important in arson investigation?\\n2. How do insurers detect pre-existing damage?\\n3. Why inspect the scene early?",
         glossary="| Arson | Deliberate fire |\\n| Inventory inflation | Overstated contents claim |",
         takeaways="1. **Motive and timing are critical in property fraud.**\\n2. **Evidence deteriorates — inspect scenes early.**\\n3. **Documentation disproves inflated and pre-existing claims.**",
         next="04-liability-fraud.md", next_title="Liability Fraud",
         prev="02-auto-fraud.md", prev_title="Auto Fraud",
         related="volume-07, volume-03"),
    dict(num="4", title="Liability Fraud", file="04-liability-fraud.md",
         intro="Liability fraud involves fabricated or exaggerated bodily injury claims, staged slip and falls, and fraudulent workers' compensation claims. Medical treatment fraud and padded damages are common.",
         sections=[
            ("Slip & fall", "Staged or exaggerated falls", "Scene investigation"),
            ("Injury exaggeration", "Damages exceed injury", "Medical review"),
            ("Workers comp", "False or exaggerated injury", "IME, surveillance"),
            ("Medical fraud", "Unnecessary treatment billing", "BI analytics"),
         ],
         tables=[
            ("Liability Red Flags", [("Inconsistent injury", "Symptoms change", "Medical records"),
                                     ("Delay mismatch", "No contemporaneous report", "Timeline review"),
                                     ("Frequent claimants", "Repeat involvement", "Claimant database"),
                                     ("Treatment escalation", "Unusual medical activity", "Medical network review")]),
            ("Investigation Tools", [("IME / medical review", "Independent assessment", "Credentialed physicians"),
                                     ("Surveillance", "Activity documentation", "Within legal limits"),
                                     ("Statement analysis", "Inconsistency detection", "Recorded statements"),
                                     ("Background check", "Prior claims", "Claimant databases")]),
         ],
         review="1. What is an IME?\\n2. Why are repeat claimants significant?\\n3. How does surveillance support fraud investigation?",
         glossary="| IME | Independent medical examination |\\n| Workers comp | Workers' compensation scheme |",
         takeaways="1. **Liability fraud centres on staged or exaggerated injury.**\\n2. **Medical review and statements identify exaggeration.**\\n3. **Claimant databases uncover repeat fraud.**",
         next="05-siu.md", next_title="Special Investigation Unit",
         prev="03-property-fraud.md", prev_title="Property Fraud",
         related="volume-07, volume-03, volume-02"),
    dict(num="5", title="Special Investigation Unit (SIU)", file="05-siu.md",
         intro="The Special Investigation Unit (SIU) investigates suspicious claims, develops fraud cases, and supports prosecution. SIU works with claims, actuarial, legal, and law enforcement.",
         sections=[
            ("SIU role", "Investigate suspicious claims", "Referral-based"),
            ("Referral criteria", "Red flags trigger referral", "Structured rules"),
            ("Investigation process", "Evidence gathering, analysis", "Documented workflow"),
            ("Outcomes", "Decline, rescission, prosecution", "Evidence briefs"),
         ],
         tables=[
            ("SIU Referral Triggers", [("Claimant patterns", "Repeat claimants", "Claimant database"),
                                       ("Loss inconsistencies", "Conflicting facts", "Statement review"),
                                       ("Organised indicators", "Network links", "Link analysis"),
                                       ("High exposure", "Large or structured claims", "Authority escalation")]),
            ("SIU Investigation Steps", [("Intake", "Claim accepted for review", "Referral form"),
                                         ("Analysis", "Documents, data checked", "Verification"),
                                         ("Fieldwork", "Photos, interviews", "Evidence collection"),
                                         ("Resolution", "Findings documented", "Decision memorandum")]),
         ],
         review="1. What is the purpose of an SIU?\\n2. Give three referral triggers.\\n3. What does an SIU investigation produce?",
         glossary="| SIU | Special investigation unit |\\n| Referral | Claim routed to SIU |",
         takeaways="1. **SIU investigates claims flagged by referral criteria.**\\n2. **Structured process protects evidence and outcomes.**\\n3. **Documentation supports declination and prosecution.**",
         next="06-analytics-fraud.md", next_title="Data & Analytics",
         prev="04-liability-fraud.md", prev_title="Liability Fraud",
         related="volume-07, volume-10, volume-14"),
    dict(num="6", title="Fraud Detection — Data & Analytics", file="06-analytics-fraud.md",
         intro="Predictive models, network analytics, and social media intelligence detect fraud patterns that humans miss. Fraud analytics scores claims, flags networks, and prioritises SIU workloads.",
         sections=[
            ("Predictive scoring", "Model assigns fraud propensity score", "SIU prioritisation"),
            ("Network analysis", "Links claimants, providers, vehicles", "Organised ring detection"),
            ("Link analysis", "Shared attributes reveal collusion", "Shared phone, address"),
            ("Behavioural analytics", "Patterns in claim behaviour", "Anomaly detection"),
         ],
         tables=[
            ("Analytics Methods", [("Fraud score", "Model-scored priority", "ML models"),
                                   ("Network graphs", "Entity relationships", "Graph analytics"),
                                   ("Anomaly detection", "Rare behaviour patterns", "Statistical methods"),
                                   ("Text analytics", "NLP on statements", "Inconsistency flags")]),
            ("Model Development", [("Data", "Claims, policy, claimant", "Structured + unstructured"),
                                   ("Features", "Engineered variables", "Timing, amounts, links"),
                                   ("Training", "Labelled fraud cases", "Supervised learning"),
                                   ("Validation", "Holdout testing", "Precision/recall")]),
         ],
         review="1. What is a fraud score?\\n2. How does network analysis detect organised fraud?\\n3. Why validate fraud models?",
         glossary="| Fraud score | Model propensity score |\\n| Network analysis | Entity relationship detection |",
         takeaways="1. **Analytics scores and prioritises fraud referrals.**\\n2. **Network analysis reveals organised rings.**\\n3. **Validated models balance detection and false positives.**",
         next="07-emerging-fraud.md", next_title="Emerging Fraud",
         prev="05-siu.md", prev_title="Special Investigation Unit",
         related="volume-10, volume-14, volume-05"),
    dict(num="7", title="Emerging Fraud", file="07-emerging-fraud.md",
         intro="Emerging fraud includes digital channel fraud, synthetic identity fraud, cyber claim fraud, and social media-driven schemes. Organised criminal groups increasingly exploit self-service channels.",
         sections=[
            ("Synthetic identity", "Fake identities open policies", "Identity verification"),
            ("Cyber fraud", "Fabricated cyber incidents", "Digital forensics"),
            ("AI-generated claims", "Synthetic photos / documents", "Media forensics"),
            ("Social engineering", "Agent/consumer manipulation", "Behavioural analysis"),
         ],
         tables=[
            ("Emerging Schemes", [("Synthetic identity", "Blend real/fake data", "KYC verification"),
                                  ("Fake documents", "AI-generated evidence", "Forensic tools"),
                                  ("Ghost agents", "Brokers divert premiums", "Agency audits"),
                                  ("Organised mobility", "Rings move across states", "Shared intelligence")]),
            ("Detection Controls", [("Identity verification", "KYC at onboarding", "Biometrics, databases"),
                                    ("Forensic validation", "Media authenticity", "AI media tools"),
                                    ("Fraud intelligence", "Shared alerts", "Consortium data"),
                                    ("Monitoring", "Channel analytics", "Real-time flags")]),
         ],
         review="1. What is a synthetic identity?\\n2. How do AI-generated documents challenge fraud detection?\\n3. Why is cross-company intelligence important?",
         glossary="| Synthetic identity | Blend of real and fake identity data |\\n| KYC | Know your customer |",
         takeaways="1. **Digital channels create new fraud surfaces.**\\n2. **AI-generated evidence requires forensic detection.**\\n3. **Shared intelligence disrupts organised mobility fraud.**",
         next=None, next_title=None,
         prev="06-analytics-fraud.md", prev_title="Data & Analytics",
         related="volume-14, volume-10, volume-11"),
]

(BASE / "index.md").write_text(INDEX, encoding="utf-8")


def render(c):
    intro_lines = "\n".join(f"| {s[0]} | {s[1]} | {s[2]} |" for s in c["sections"])
    tables = ""
    for title, rows in c["tables"]:
        body_rows = "\n".join(f"| {r[0]} | {r[1]} | {r[2]} |" for r in rows)
        tables += f"### {title}\n\n| Indicator | Description | Action |\n|----------|-------------|--------|\n{body_rows}\n\n---\n\n"
    nxt = f"[{c['next_title']}]({c['next']})" if c["next"] else "— (end of volume)"
    prv = f"[{c['prev_title']}]({c['prev']})" if c["prev"] else "Volume 17 Home"
    return f"""# 17.{c['num']} — {c['title']}

> **Learning Objectives**
>
> After completing this chapter you should be able to:
>
> 1. Define {c['title'].lower()} and its fraud types.
> 2. Identify red flags and indicators.
> 3. Describe investigation and detection controls.
> 4. Apply fraud prevention principles.

<!-- Metadata (for RAG / AI knowledge base)
keywords: fraud, {c['title'].lower().replace(' ', '-')}
tags: fraud, volume-17
categories: volume-17
related: {c['related']}
-->

## Executive Summary

{c['intro']}

---

## 17.{c['num']}.1 Key Concepts

| Concept | Description | Significance |
|---------|-------------|--------------|
{intro_lines}

---

## 17.{c['num']}.2 Indicators & Actions

{tables}
## 17.{c['num']}.3 Prevention & Response

| Stage | Action |
|-------|--------|
| Prevention | Application screening, verification |
| Detection | Claims triage, analytics, referral rules |
| Investigation | SIU analysis, evidence collection |
| Resolution | Decline, rescission, referral to authorities |

---

## Review Questions

{c['review']}

---

## Glossary

| Term | Definition |
|------|------------|
{c['glossary']}

---

## Key Takeaways

{c['takeaways']}

---

## References & Further Reading

- Coalition Against Insurance Fraud (US) — public guides
- ABI (UK) — fraud guidance
- NAIC — anti-fraud resources

---

**Previous:** {prv} | **Next:** {nxt}

---

*Part of the Global Insurance Underwriting Handbook — Volume 17*
"""


for c in CHAPTERS:
    (BASE / c["file"]).write_text(render(c), encoding="utf-8")
    print(f"Created {c['file']}")

print("Volume 17 generation complete.")