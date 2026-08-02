# 5.5 Predictive Analytics

## Overview

Predictive analytics uses statistical and machine-learning models to estimate loss propensity, pricing, retention, and fraud. In pricing, models replace many manual classification tables with **continuous, data-driven risk scores**.

## Models in Insurance Pricing

| Model Type | Use |
|---|---|
| **Generalized Linear Model (GLM)** | The workhorse: frequency, severity, pure premium |
| **Decision trees / gradient boosting** | Non-linear interactions, fraud, retention |
| **Random forests** | Ensemble robustness, feature importance |
| **Neural networks / deep learning** | Complex patterns (claims triage, imagery) |
| **Cluster analysis** | Risk segmentation |
| **Survival models** | Lapse, claim duration, tail |

## The GLM in Pricing

The GLM models the expected value of the response (e.g., claim count, severity) as a function of predictors:

```
E(Y) = g⁻¹(β₀ + β₁X₁ + ... + βₖXₖ)
```

| Choice | Common Option | Why |
|---|---|---|
| **Distribution** | Poisson / negative binomial (frequency), Gamma (severity) | Counts and positive-skewed severity |
| **Link** | Log link | Multiplicative factors, positivity |
| **Offset** | log(exposure) | Rate per unit exposure |

### GLM Output

- Coefficients become **rating relativities**.
- Model can be validated on holdout data.
- Interactions can be added if supported by data and credible.

## The Modeling Pipeline

```
1. Data assembly (claims, exposures, policy, external)
2. Feature engineering (transformation, missing values, encoding)
3. Split data (train / validation / test)
4. Model fitting
5. Model validation (lift, AIC, holdout performance)
6. Implementation (rating factors, score)
7. Monitoring (drift, fairness, performance)
```

## Validation and Selection

| Metric | Purpose |
|---|---|
| **AIC / BIC** | Model comparison (lower is better) |
| **Lift / gain chart** | How well the model separates risk |
| **Gini coefficient** | Discrimination of the score |
| **Holdout performance** | Out-of-sample accuracy |
| **Calibration** | Predicted vs. actual ratios |

A model must be **predictive, explainable, and stable**.

## Telematics and Usage-Based Pricing

| Source | Feature Examples |
|---|---|
| **GPS** | Distance, time of day, road type, route |
| **Accelerometer** | Hard braking, acceleration, cornering |
| **Phone use** | Distraction indicators |
| **Crash data** | Impact detection and verification |

Telematics pricing shifts from **proxies** (age, territory) toward **actual behavior**. It also enables **pay-per-mile** or **pay-how-you-drive** products.

## IoT, Imagery, and External Data

| Data | Pricing Use |
|---|---|
| **IoT sensors (water, smoke, temp)** | Property risk, loss prevention discounts |
| **Aerial imagery** | Roof condition, vegetation, wildfire proximity |
| **Geospatial analytics** | Flood, wind, wildfire, crime scoring |
| **Social media / web** | Limited and regulated; mostly avoidance |
| **Credit / insurance scores** | Where lawful, personal lines |

## Fairness and Governance

| Risk | Mitigation |
|---|---|
| **Proxy discrimination** | Test for indirect use of prohibited factors |
| **Bias in training data** | Review, reweight, document |
| **Opacity** | Explainability tools; human review for decisions |
| **Regulatory** | Filed rates, adverse action, fair value |

### Model Governance Framework

- Standards for development and documentation.
- Independent validation.
- Version control and approval gates.
- Ongoing monitoring for drift and fairness.
- Audit trail for regulatory review.

## Implementation into Pricing

| Step | Description |
|---|---|
| **Scoring** | Model produces a predicted pure premium |
| **Rating structure** | Map scores to rating factors where suitable |
| **Filed rates** | Where required, submit with justification |
| **Underwriter override** | Judgment adjustments within authority |
| **Monitoring** | Compare actual to predicted; revisit model |

## The Future of Predictive Pricing

- **Real-time pricing** — instant quotes using live data.
- **Continuous underwriting** — telematics updates mid-term.
- **Personalized products** — microsegmentation and tailored terms.
- **Explainable AI** — regulatory pressure for transparency.
- **Fairness-aware models** — constraints to prevent prohibited outcomes.

## Summary

- **GLMs and machine learning** replace manual tables with data-driven scores.
- The **pipeline** (data → features → fit → validate → implement → monitor) governs quality.
- **Telematics, IoT, and external data** enrich predictors.
- **Fairness and governance** are mandatory for regulatory acceptance.
- Pricing moves toward **personalization and real-time** underwriting.

## Related Chapters

- [4.8 Automation & Data in Underwriting](../volume-04-underwriting/08-underwriting-automation.md)
- [5.2 Data & Loss Reserving](02-data-loss-reserving.md)
- [5.4 Pricing Techniques](04-pricing-techniques.md)
- [5.9 Pricing Governance](09-pricing-governance.md)