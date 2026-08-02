# 4.8 Automation & Data in Underwriting

## Overview

Insurance underwriting is being transformed by **automation, data, and analytics**. Technology does not replace the underwriter — it changes the job:

- Routine, repetitive decisions are **automated** (straight-through processing).
- Complex risks are **augmented** by models, data, and tools.
- The underwriter's role shifts to **judgment, exception handling, and portfolio thinking**.

## Degrees of Automation

| Level | Description |
|---|---|
| **Manual** | The underwriter reviews every submission and prices by judgment |
| **Assisted** | Systems score, flag, and price; underwriter decides |
| **Automated (STP)** | Eligible risks are bound and issued without human review |
| **Fully algorithmic** | The whole decision is made by a model, supervised by rules |

Most personal lines and small commercial benefit from **straight-through processing (STP)**. Large commercial and specialty remain actively underwritten with decision support.

## What Automates Well vs. What Does Not

| Automates Well | Requires Human Judgment |
|---|---|
| Standard personal lines (auto, home) | Complex commercial accounts |
| Small BOP/package | Specialty lines (marine, aviation, surety) |
| Eligibility and rules checks | Moral hazard evaluation |
| Rating and issuance | Coverage design and negotiation |
| Renewal re-pricing | Exception handling |
| Claims triage and data entry | Large loss and coverage disputes |

## Key Technologies

| Technology | Use |
|---|---|
| **Rules engines** | Eligibility, acceptance criteria, referral logic |
| **Predictive models** | Pricing, retention, conversion, fraud |
| **Machine learning** | Claims reserving, propensity models, anomaly detection |
| **Telematics** | Usage-based auto insurance, driver feedback |
| **IoT sensors** | Water leak detection, property risk mitigation |
| **Geospatial data** | Flood, wildfire, wind scoring |
| **Aerial imagery** | Roof condition, property features, exposure |
| **APIs and data exchange** | Instant quoting from external data |
| **RPA (robotic process automation)** | Document processing, data entry, reconciliation |
| **Generative AI** | Summarizing submissions, drafting correspondence, document extraction |
| **Portfolio dashboards** | Real-time concentration and performance |

## The Data-Driven Underwriting Stack

```
Submission Data
      ↓
Enrichment (MVR, CLUE, credit, geospatial)
      ↓
Models & Scores (pricing, risk, fraud)
      ↓
Decision Engine (rules + referral)
      ↓
Underwriter Review (exceptions)
      ↓
Issuance & Monitoring
```

## Telematics and Usage-Based Insurance (UBI)

| Application | How It Works |
|---|---|
| **Personal auto** | App/device records driving; discounts for safe behavior |
| **Commercial fleet** | Driver coaching, route optimization, claim verification |
| **Pay-per-mile** | Premium based on distance driven |
| **Post-crash** | Crash detection and verification |

Telematics **changes the nature of auto insurance**: pricing moves from demographic proxies to **actual driving behavior**, and insurers gain a **loss-prevention** channel.

## IoT and Smart Homes

| Sensor | Use |
|---|---|
| Water leak | Early detection prevents water damage claims |
| Smoke/CO | Faster fire response |
| Security cameras | Theft prevention and claim verification |
| Temperature | Freeze and spoilage prevention |

Loss prevention data directly improves **underwriting and claims**; some insurers offer premium discounts for connected devices.

## Predictive Models in Underwriting

| Model | Purpose |
|---|---|
| **Frequency model** | Expected number of claims |
| **Severity model** | Expected cost per claim |
| **Pricing model** | Indicated premium |
| **Retention model** | Likelihood of renewal |
| **Conversion model** | Likely acceptance of a quote |
| **Fraud model** | Risk of fraudulent claim |
| **Reserving model** | Estimate outstanding liabilities |
| **Propensity model** | Cross-sell potential |

Models are built on historical data; they must be **validated, monitored, and governed** (see Model Risk below).

## Model Risk and Governance

| Risk | Mitigation |
|---|---|
| **Bias** | Fairness testing; prohibited factors excluded |
| **Overfitting** | Holdout validation; backtesting |
| **Data quality** | Data lineage, quality checks |
| **Drift** | Performance monitoring; refresh cycles |
| **Opacity** | Documentation, explainability for decisions |
| **Regulatory** | Approved rate filings; adverse action notices |

A **model governance framework** includes development standards, independent validation, version control, and audit.

## Regulatory Constraints on Data and Automation

| Jurisdiction | Key Rules |
|---|---|
| **US** | FCRA (adverse action), state rate/fairness laws, GLBA privacy |
| **EU/UK** | GDPR, AI Act (high-risk classification), FCA fair value and pricing rules |
| **General** | Prohibited factors (race, religion, gender where barred), transparency, human review for material decisions |

Automation must not create **unfair discrimination** or deny rights that a human process would provide.

## The Changing Role of the Underwriter

| Then | Now / Future |
|---|---|
| Clerical data entry and rating | Judgment, exception handling |
| Manual file review | Model-driven prioritization |
| Silent risk selection | Broker/insured dialogue on exposures |
| After-the-fact portfolio checks | Real-time concentration dashboards |
| Document-based | Data-based with documents for context |

The underwriter's core skills — **risk assessment, judgment, communication, and portfolio thinking** — remain essential, but they are applied to **exceptions and complexity** rather than routine processing.

## Ethics and Fairness in Automated Underwriting

- **Transparency** — applicants should understand the basis of decisions where required.
- **Fairness** — models must not use prohibited factors or proxy them.
- **Explainability** — decisions must be explainable to regulators and consumers.
- **Human oversight** — material adverse decisions should allow human review.
- **Accountability** — there must be clear ownership of model outcomes.

## Summary

- Automation handles **standard, rules-based** decisions; judgment handles **exceptions**.
- **Predictive models, telematics, IoT, and geospatial data** enrich underwriting.
- **Model governance** controls bias, drift, and opacity.
- **Regulation** (FCRA, GDPR, AI Act, FCA) constrains how data and models are used.
- The underwriter's role **shifts to judgment, complexity, and portfolio management**.

## Related Chapters

- [4.1 The Underwriting Process](01-underwriting-process.md)
- [4.2 Information Sources](02-information-sources.md)
- [4.3 Underwriting Principles](03-underwriting-principles.md)
- [5.4 Pricing Techniques](../volume-05-rating-pricing/04-pricing-techniques.md)
- [5.5 Predictive Analytics](../volume-05-rating-pricing/05-predictive-analytics.md)