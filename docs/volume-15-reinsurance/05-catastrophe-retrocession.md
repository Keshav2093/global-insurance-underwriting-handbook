# 15.5 — Catastrophe Reinsurance & Retrocession

> **Learning Objectives**
>
> After completing this chapter you should be able to:
>
> 1. Explain catastrophe risk and why catastrophe reinsurance is needed.
> 2. Describe CAT XL structures, event definitions, and reinstatements.
> 3. Explain catastrophe modelling and PML concepts.
> 4. Define retrocession and alternative capital (ILS, cat bonds).

<!-- Metadata (for RAG / AI knowledge base)
keywords: catastrophe, CAT XL, retrocession, cat bond, ILS, PML, modelling
tags: reinsurance, catastrophe
categories: volume-15
related: volume-15-04, volume-01, volume-05
-->

## Executive Summary

Catastrophe reinsurance protects insurers against the financial impact of large natural events — windstorms, earthquakes, floods — that create massive accumulations of loss across a portfolio. CAT XL layers respond per single event and often include reinstatements. Insurers use catastrophe models to quantify probable maximum loss (PML), then transfer the tail risk to reinsurers, retrocessionaires, and capital markets via insurance-linked securities (ILS) such as catastrophe bonds.

---

## 15.5.1 What Is Catastrophe Risk?

**Catastrophe (CAT)** risk is the potential for a single event — or a season of events — to produce losses across many policies simultaneously.

| Element | Description |
|---------|-------------|
| Peril | Windstorm, earthquake, flood, wildfire, freeze, terrorism |
| Event | Defined by cause, time (hours clause), and area |
| Accumulation | Sum of insured exposures in the event zone |
| Correlation | Many policies impacted by one event |
| Severity | Potential losses far exceed normal frequency |

### Major Catastrophe Types

| Peril | Characteristics | Modelling |
|-------|------------------|-----------|
| Windstorm | Wind speed, tracks | Rerun thousands of simulated events |
| Earthquake | Ground motion, soil | Fault lines, shaking intensity |
| Flood | River, coastal, flash | Hydrological models |
| Wildfire | Fuel, wind, interface | Fire spread simulation |
| Severe storm | Hail, tornado, straight-line | Convective storm models |
| Winter storm | Snow, ice | Meteorological models |

---

## 15.5.2 Catastrophe XL Structures

| Element | Description |
|---------|-------------|
| **Layer** | E.g., $250M xs $100M |
| **Event** | One catastrophe occurrence per treaty definition |
| **Hours clause** | E.g., 72 hours continuous for windstorm |
| **Area clause** | E.g., losses within defined region |
| **Limit** | Max recovery per event |
| **Reinstatements** | Usually 1–2, with additional premium |
| **Annual aggregate** | Optional cap on total recoveries |

### Tower of Protection

| Layer | Limit | Attachment | Purpose |
|-------|-------|-----------|---------|
| Working XL | $10M | $5M | Frequent moderate losses |
| Middle layer | $50M | $100M | Severe events |
| Catastrophe layer | $250M | $150M | Top catastrophic risk |
| Retrocession / ILS | $300M | $400M | Tail / capital market |

---

## 15.5.3 Catastrophe Modelling

### Model Components

| Component | Function |
|-----------|----------|
| **Hazard** | Intensity of event at each location |
| **Exposure** | Insured values, construction, occupancy |
| **Vulnerability** | Damage as a function of intensity |
| **Financial** | Policy conditions, deductibles, limits, reinsurance |

### Model Outputs

| Metric | Definition |
|--------|------------|
| **PML (Probable Maximum Loss)** | Loss at a selected return period |
| **OEP (Occurrence Exceedance Probability)** | Probability of loss from one event |
| **AEP (Aggregate Exceedance Probability)** | Probability of annual aggregate loss |
| **AAL (Average Annual Loss)** | Expected loss per year |
| **Return period** | 1 in 100, 1 in 250 for PML |

### PML Illustration

| Return Period | PML (OEP) |
|---------------|-----------|
| 1 in 50 | $80M |
| 1 in 100 | $120M |
| 1 in 250 | $180M |
| 1 in 500 | $250M |

---

## 15.5.4 Pricing Catastrophe Cover

### Components

| Component | Description |
|-----------|-------------|
| Expected loss (AAL to layer) | Modelled loss cost |
| Risk load | Volatility and uncertainty |
| Capital charge | Return on collateral/capital |
| Expense & commission | Costs of placement |
| **Technical premium** | Sum of the above |
| **Market adjustment** | Supply/demand, market hardening/softening |

### Rate on Line

| Layer | Limit | Premium | ROL |
|-------|-------|---------|-----|
| CAT XL | $250M xs $150M | $50M | 20% |

---

## 15.5.5 Retrocession

**Retrocession** is reinsurance purchased by a reinsurer to protect its own portfolio.

| Element | Description |
|---------|-------------|
| Retrocedent | The reinsurer ceding risk |
| Retrocessionaire | The reinsurer assuming the risk |
| Purpose | Reduce net exposure, peak peril risk, capital relief |
| Forms | Proportional or non-proportional retro treaties |
| Linked | Risk follows the original business |

### Retrocession Example

| Entity | Role |
|--------|------|
| Primary insurer | Cedes to reinsurer |
| Reinsurer | Accepts; then cedes a layer to retrocessionaire |
| Retrocessionaire | Assumes share of the reinsurer's risk |

---

## 15.5.6 Alternative Capital & ILS

| Instrument | Description |
|------------|-------------|
| **Catastrophe bond (cat bond)** | Investor principal at risk if trigger level breached |
| **Industry loss warranty (ILW)** | Payment based on industry loss index |
| **Sidecar** | Reinsurance vehicle sharing a book of business |
| **Collateralised reinsurance** | Funds held to secure obligations |
| **Swap / derivative** | Transfer catastrophe risk to capital markets |

### Cat Bond Trigger Types

| Trigger | Description |
|---------|-------------|
| Indemnity | Based on cedent's actual losses |
| Index | Based on modelled or industry index |
| Parametric | Based on physical parameter (e.g., wind speed) |

---

## 15.5.7 Case Study — Large Hurricane

> **Scenario:** An insurer writes 1% of coastal wind exposure with $300M PML at 1-in-100.
>
> **Programme:**
> - Retention: $50M
> - Working XL: $25M xs $25M
> - CAT layer: $200M xs $50M
> - Cat bond: $50M xs $250M
>
> **Outcome:** A 1-in-100 event produces $120M of losses. The insurer retains $50M, recovers $25M from working XL and $45M from CAT layer, leaving large losses within its risk tolerance. The tail is protected by the cat bond.

---

## Review Questions

1. What makes a loss "catastrophic" from a reinsurer's perspective?
2. Define PML, OEP, AEP, and AAL.
3. What is an hours clause and why is it used?
4. Explain the difference between retrocession and reinsurance.
5. How does a catastrophe bond differ from a traditional CAT XL?

---

## Glossary

| Term | Definition |
|------|------------|
| AAL | Average annual loss |
| AEP | Aggregate exceedance probability |
| Cat bond | Capital-market catastrophe protection |
| OEP | Occurrence exceedance probability |
| PML | Probable maximum loss |
| Retrocession | Reinsurance of a reinsurer |

---

## Key Takeaways

1. **CAT risk arises from correlated losses across many policies in one event.**
2. **CAT XL provides per-event recoveries with reinstatements.**
3. **Catastrophe models estimate PML and drive pricing and retention decisions.**
4. **Retrocession and ILS shift the tail risk beyond the traditional reinsurance market.**

---

## References & Further Reading

- AIR, RMS (Moody's), Verisk cat model documentation (public summaries)
- Swiss Re Institute — sigma catastrophe reports
- Insurance Information Institute — catastrophe fundamentals

---

**Previous:** [15.4 Excess of Loss & Stop Loss](04-excess-of-loss-stop-loss.md) |
**Next:** [15.6 Pricing & Accounting](06-pricing-accounting.md)

---

*Part of the Global Insurance Underwriting Handbook — Volume 15*