"""Generate knowledge-base sections: references/, case-studies/, industry-data/."""

from pathlib import Path

BASE = Path("docs")

# ---------- references/ ----------
REF = BASE / "references"
REF.mkdir(exist_ok=True)

(REF / "index.md").write_text("""# References & Further Reading

An index of regulatory frameworks, industry bodies, vendors, and further reading referenced across the Global Insurance Underwriting Handbook volumes.

## Regulatory & Industry Bodies

| Body | Jurisdiction | Focus |
|------|--------------|-------|
| NAIC | USA | State insurance regulation, model laws |
| FCA | UK | Insurance conduct regulation |
| PRA | UK | Prudential regulation, Solvency II |
| EIOPA | EU | Insurance supervision |
| IRDAI | India | Insurance regulation |
| Lloyd's | UK | Specialist insurance market |
| IUMI | International | Marine insurance |
| ACORD | International | Data standards |
| ISO | International | Technical standards (incl. insurance data) |

## Core Documents

- Solvency II Directive (2009/138/EC) — public
- NAIC Model Laws & Regulations — public library
- ACORD Standards Library — public summaries
- Swiss Re sigma reports — public
- Lloyd's Market Association wordings — public guides

## Vendors & Platforms

| Vendor | Product | Volume Reference |
|--------|---------|------------------|
| Guidewire | PolicyCenter / ClaimCenter / BillingCenter | Vol 10 |
| Duck Creek Technologies | DMS / MANO | Vol 11 |
| Majesco | DigitalConnect / CloudInsurer | Vol 12 |
| Verisk / AIR | Catastrophe models | Vol 15 |
| Moody's RMS | Catastrophe models | Vol 15 |

## Professional Bodies

- Chartered Insurance Institute (CII) — UK
- CPCU Society — USA
- Australian & New Zealand Institute of Insurance and Finance (ANZIIF)
- Institute of Actuaries — reserves & pricing
- Association of Certified Fraud Examiners (ACFE) — fraud

---

*Part of the Global Insurance Underwriting Handbook — References*
""", encoding="utf-8")

(REF / "regulatory.md").write_text("""# Regulatory & Industry Bodies

Details of key regulatory and industry organisations referenced in the handbook.

## NAIC (National Association of Insurance Commissioners) — USA

- **Role:** Coordinates insurance regulation across US states
- **Key outputs:** Model laws, annual statements, financial regulation
- **Relevance:** Volumes 1, 5, 8, 15

## FCA (Financial Conduct Authority) — UK

- **Role:** Regulates insurance conduct and markets
- **Key outputs:** Conduct rules (ICOB), Consumer Duty
- **Relevance:** Volumes 1, 9

## PRA (Prudential Regulation Authority) — UK

- **Role:** Prudential regulation of insurers
- **Key outputs:** Solvency II implementation, capital standards
- **Relevance:** Volumes 1, 5, 9

## EIOPA — EU

- **Role:** EU insurance supervision coordination
- **Key outputs:** Solvency II guidelines, ORSA
- **Relevance:** Volumes 1, 9

## IRDAI — India

- **Role:** Indian insurance regulation
- **Key outputs:** IRDAI regulations, filings, reinsurance rules
- **Relevance:** Volumes 1, 15

## Lloyd's of London — UK

- **Role:** Specialist insurance and reinsurance market
- **Key outputs:** Syndicates, policy wordings, market oversight
- **Relevance:** Volumes 1, 9, 16

## IUMI (International Union of Marine Insurance)

- **Role:** Marine insurance association
- **Key outputs:** Market statistics, clauses, guidance
- **Relevance:** Volume 16

## ACORD

- **Role:** Insurance data standards body
- **Key outputs:** ACORD messages, LOB standards, JSON/XML
- **Relevance:** Volumes 10–12, 18

---

*Part of the Global Insurance Underwriting Handbook — References*
""", encoding="utf-8")

(REF / "vendors.md").write_text("""# Platform Vendors & Tools

Summary of core insurance platform vendors referenced across the technology volumes.

| Vendor | Products | Architecture | API/Integration |
|--------|----------|--------------|-----------------|
| Guidewire | PolicyCenter, ClaimCenter, BillingCenter, InfoCenter | Java-based, on-prem/SaaS | REST, Integration Framework, events |
| Duck Creek | Policy, Billing, Claims, Insights | Cloud-native SaaS, MANO | Swagger/OpenAPI, event-driven |
| Majesco | CloudInsurer, DigitalConnect | Cloud/SaaS | DigitalConnect APIs |
| Sapiens | CoreSuite, Persona | Core platform | APIs |
| EIS | Core platform | Cloud | APIs |
| Innoveo / Genius | Digital distribution | SaaS | APIs |

## Selection Considerations

| Criterion | Consideration |
|-----------|---------------|
| Cloud vs on-prem | Deployment flexibility, cost |
| APIs & ecosystem | Ease of InsurTech integration |
| Product support | Line-of-business coverage |
| Total cost of ownership | Licensing, implementation, run |

---

*Part of the Global Insurance Underwriting Handbook — References*
""", encoding="utf-8")

(REF / "terminology.md").write_text("""# Glossary of Regulatory Terms

| Term | Definition |
|------|------------|
| Solvency II | EU prudential regime |
| ORSA | Own Risk and Solvency Assessment |
| ICOBS | Insurance Conduct of Business Sourcebook |
| Consumer Duty | FCA principle requiring good outcomes |
| Model law | NAIC template adopted by states |
| Authorised reinsurer | Approved for credit for reinsurance |

---

*Part of the Global Insurance Underwriting Handbook — References*
""", encoding="utf-8")

print("references/ created")

# ---------- case-studies/ ----------
CS = BASE / "case-studies"
CS.mkdir(exist_ok=True)

(CS / "index.md").write_text("""# Case Studies

Case studies illustrating underwriting, claims, reinsurance, and technology decisions across the handbook volumes.

| Case Study | Volume | Focus |
|------------|--------|-------|
| [Large Commercial Property](property.md) | Vol 3, 4 | Risk survey & rating |
| [Cost-in-Use Pricing](cost-in-use.md) | Vol 5 | Pricing methods |
| [Cyber Claim](cyber-claim.md) | Vol 7 | Cyber claims |
| [Recovery through Reinsurance](reinsurance.md) | Vol 15 | Treaty recoveries |
| [Fraud Network Detection](fraud-network.md) | Vol 17 | Analytics & SIU |
| [API Integration](api-integration.md) | Vol 18 | Core platform integration |

---

*Part of the Global Insurance Underwriting Handbook — Case Studies*
""", encoding="utf-8")

(CS / "property.md").write_text("""# Case Study — Large Commercial Property

## Scenario

A 40,000 m² logistics warehouse with sprinklered racked storage, annual turnover $250M.

## Process

| Step | Action |
|------|--------|
| 1 | Risk survey and protection review |
| 2 | Exposure assessment (sum insured adequate) |
| 3 | Loss scenario testing (fire, flood, BI) |
| 4 | Pricing by exposure and experience |
| 5 | Reinsurance placement for peak risk |

## Outcome

- Property limit: $50M, BI: $20M
- Loss control conditions imposed
- Quota share treaty 40%
- Premium: $120,000 (0.17% of sum insured)

## Lessons

1. **Surveys are essential for commercial property.**
2. **BI exposure often exceeds material damage.**
3. **Reinsurance supports peak capacity.**

---

*Part of the Global Insurance Underwriting Handbook — Case Studies*
""", encoding="utf-8")

(CS / "cost-in-use.md").write_text("""# Case Study — Cost-in-Use Pricing

## Scenario

A fleet insurer evaluates whether Cost-in-Use (CIU) pricing improves lifecycle loss ratios.

## Method

| Element | Description |
|---------|-------------|
| Telematics | Speeds, harsh events, miles |
| Claims integration | Frequency, severity |
| Model | GLM on CIU factors vs traditional |
| Measurement | Loss ratio by policy period |

## Findings

- CIU improves predictability of frequency
- Severity benefits limited without claims integration
- Premium differentiation increased 18% for high-risk groups

## Lessons

1. **Usage data improves risk selection.**
2. **CIU requires telematics coverage.**
3. **Data quality drives model value.**

---

*Part of the Global Insurance Underwriting Handbook — Case Studies*
""", encoding="utf-8")

(CS / "cyber-claim.md").write_text("""# Case Study — Cyber Claim Response

## Scenario

Ransomware attack on a healthcare provider. Systems encrypted; patient data exfiltrated.

## Response Process

| Stage | Action |
|-------|--------|
| Notification | Claim within 24 hours |
| Forensics | Determine scope and cause |
| Business interruption | Quantify downtime |
| Ransom & negotiation | Decision per policy terms |
| Regulatory | Notify authorities per requirements |

## Outcome

- Ransom paid within limit
- BI recovery 75% of insured loss
- Forensic and legal costs covered
- Policy renewed with enhanced security conditions

## Lessons

1. **Speed of response reduces loss.**
2. **Forensics inform coverage decisions.**
3. **Regulatory exposure is material.**

---

*Part of the Global Insurance Underwriting Handbook — Case Studies*
""", encoding="utf-8")

(CS / "reinsurance.md").write_text("""# Case Study — Recovery Through Reinsurance

## Scenario

Quota share 50% and per-risk XL $10M xs $5M attach to a property portfolio.

## Events

| Claim | Loss | QS Recovery (50%) | XL Recovery | Cedent Net |
|-------|------|-------------------|-------------|------------|
| Fire | $1M | $0.5M | None | $0.5M |
| Flood | $8M | $4M | $3M | $1M |
| Storm | $6M | $3M | $1M | $2M |

## Outcome

Cedent net exposure reduced materially; capital released by treaty structure.

## Lessons

1. **Proportional treaties share frequency.**
2. **XL layers cap severity.**
3. **Layer design must match retention appetite.**

---

*Part of the Global Insurance Underwriting Handbook — Case Studies*
""", encoding="utf-8")

(CS / "fraud-network.md").write_text("""# Case Study — Fraud Network Detection

## Scenario

An auto insurer detected elevated claim costs in a city region.

## Method

| Step | Action |
|------|--------|
| Analytics | Fraud-scored claims flagged |
| Network analysis | Shared addresses, phones, attorneys |
| SIU referral | Investigated cluster of 40 claims |
| Outcome | Prosecution, declined claims, recoveries |

## Results

- 40 claims declined, $1.2M savings
- Attorney and clinic removed from network
- Ongoing monitoring established

## Lessons

1. **Analytics identifies organised patterns.**
2. **Network analysis connects entities.**
3. **Enforcement deters further fraud.**

---

*Part of the Global Insurance Underwriting Handbook — Case Studies*
""", encoding="utf-8")

(CS / "api-integration.md").write_text("""# Case Study — API Integration Program

## Scenario

A carrier replaces manual new-business entry with API integration between its Duck Creek Policy platform and a broker portal.

## Implementation

| Stage | Action |
|-------|--------|
| Contract | OpenAPI specification agreed |
| Security | OAuth2 + mTLS configured |
| Sandbox | Broker integration tested |
| Production | Rollout with monitoring |

## Outcome

- Quote-to-bind time: 20 minutes → 4 minutes
- Error rate reduced 80%
- New distribution channels enabled

## Lessons

1. **Contracts and security come first.**
2. **Sandboxes de-risk integration.**
3. **Measured rollout protects operations.**

---

*Part of the Global Insurance Underwriting Handbook — Case Studies*
""", encoding="utf-8")

print("case-studies/ created")

# ---------- industry-data/ ----------
ID = BASE / "industry-data"
ID.mkdir(exist_ok=True)

(ID / "index.md").write_text("""# Industry Data

Public domain industry statistics, loss data, and market context supporting underwriting decisions.

## Content

| File | Content |
|------|---------|
| [Loss Ratios](loss-ratios.md) | Illustrative loss ratios by line |
| [Premium Growth](premiums.md) | Market premium context |
| [Catastrophe Data](catastrophes.md) | Major event loss context |
| [Fraud Data](fraud.md) | Fraud prevalence context |
| [Technology Adoption](technology.md) | InsurTech adoption context |

---

*Part of the Global Insurance Underwriting Handbook — Industry Data*
""", encoding="utf-8")

(ID / "loss-ratios.md").write_text("""# Illustrative Industry Loss Ratios

The figures below are illustrative percentages used for education, based on public market commentary. They are not official statistics.

| Line | Illustrative Incurred Loss Ratio |
|------|----------------------------------|
| Private auto | 70–85% |
| Commercial auto | 75–95% |
| Homeowners | 60–80% (excluding CAT years) |
| Commercial property | 55–75% |
| General liability | 70–90% |
| Workers compensation | 70–85% |
| Marine cargo | 55–70% |
| Aviation | 50–70% |
| Reinsurance (property CAT) | Highly volatile |

## Use in Underwriting

| Purpose | Use |
|---------|-----|
| Pricing benchmarking | Compare against own targets |
| Portfolio review | Identify emerging trends |
| Reserving | Context for reserve levels |

---

*Part of the Global Insurance Underwriting Handbook — Industry Data*
""", encoding="utf-8")

(ID / "premiums.md").write_text("""# Premium Growth Context

Illustrative global insurance premium context by region (approximate, educational).

| Region | Non-Life Premium (approx) | Growth Context |
|--------|---------------------------|----------------|
| North America | Largest share | Mature, tech adoption |
| Europe | Major share | Solvency II, regulatory |
| Asia-Pacific | Fastest growth | Emerging middle class |
| Latin America | Growing | Inflationary pressure |
| Africa & Middle East | Small but growing | Expanding access |

## Drivers

- GDP growth and asset accumulation
- Regulatory reform (e.g., India liberalisation)
- Climate and cyber awareness
- Distribution digitisation

---

*Part of the Global Insurance Underwriting Handbook — Industry Data*
""", encoding="utf-8")

(ID / "catastrophes.md").write_text("""# Catastrophe Loss Context

Illustrative context on natural catastrophe losses (educational; exact figures vary by source and year).

| Event Class | Magnitude Context |
|-------------|-------------------|
| Hurricane (US) | Multi-billion single events |
| Earthquake (global) | Severe losses in high-exposure regions |
| Flood (pluvial/fluvial) | Increasing frequency |
| Wildfire | Growing severity in interface zones |
| Winter storm | Smaller but frequent |

## Underwriting Use

| Use | Description |
|-----|-------------|
| Exposure limits | Cap concentration by zone |
| Reinsurance purchase | Size program by PML |
| Pricing | Load for CAT perils |
| Modelling | Validate with vendor models |

---

*Part of the Global Insurance Underwriting Handbook — Industry Data*
""", encoding="utf-8")

(ID / "fraud.md").write_text("""# Fraud Prevalence Context

Illustrative context on insurance fraud (educational).

| Measure | Illustrative Range |
|---------|--------------------|
| Claims suspected of fraud | 5–15% depending on line |
| Soft fraud share | Majority of detected fraud |
| Detectable fraud | Increases with analytics adoption |
| Cost impact | Adds to premium burden |

## Detection Levers

| Lever | Impact |
|-------|--------|
| Analytics scoring | Higher detection |
| Shared databases | Repeat offender visibility |
| SIU staffing | Investigation capacity |
| Consumer education | Deterrence |

---

*Part of the Global Insurance Underwriting Handbook — Industry Data*
""", encoding="utf-8")

(ID / "technology.md").write_text("""# InsurTech Adoption Context

Illustrative technology adoption context (educational).

| Technology | Adoption State | Business Impact |
|------------|----------------|-----------------|
| Cloud core platforms | Growing | Agility, cost |
| APIs & ecosystem | Growing | Distribution speed |
| AI/ML underwriting | Emerging | Efficiency, accuracy |
| Telematics | Growing | Usage-based pricing |
| Low-code / no-code | Emerging | Faster product builds |
| Blockchain/DLT | Pilot | Trust & transparency |

## Adoption Drivers

- Customer expectations for digital service
- Cost pressure and efficiency
- Regulator encouragement of innovation
- Investor appetite for InsurTech

---

*Part of the Global Insurance Underwriting Handbook — Industry Data*
""", encoding="utf-8")

print("industry-data/ created")