# 15.6 — Reinsurance Pricing & Accounting

> **Learning Objectives**
>
> After completing this chapter you should be able to:
>
> 1. Explain the components of reinsurance premium pricing.
> 2. Describe experience vs exposure rating methods.
> 3. Explain key reinsurance accounting entries.
> 4. Describe reporting, reserves, and regulatory treatment.

<!-- Metadata (for RAG / AI knowledge base)
keywords: reinsurance pricing, burning cost, experience rating, accounting, reserves
tags: reinsurance, pricing, accounting
categories: volume-15
related: volume-05, volume-15-04
-->

## Executive Summary

Reinsurance pricing combines the expected loss cost of the coverage (burning cost) with loadings for expenses, capital, and profit. Methods include experience rating (based on the cedent's own loss history) and exposure rating (based on portfolio characteristics). Accounting for reinsurance involves ceded premium, ceding commission, recoveries, and reserves, with treatment governed by solvency frameworks (Solvency II, NAIC, IRDAI).

---

## 15.6.1 Pricing Methods

### Experience Rating

| Element | Description |
|---------|-------------|
| Basis | Cedent's historical losses |
| Process | Trend, develop, apply to current exposure |
| Strengths | Reflects actual portfolio |
| Limitations | Sparse data for large layers |

### Exposure Rating

| Element | Description |
|---------|-------------|
| Basis | Estimated loss cost from exposure profiles |
| Process | Apply severity distributions to exposure |
| Strengths | Works for new/low-frequency layers |
| Limitations | Relies on modelled assumptions |

### Burning Cost Derivation

| Step | Description |
|------|-------------|
| 1 | Extract historic losses subject to the layer |
| 2 | Trend losses to future cost levels |
| 3 | Develop for IBNR / late reporting |
| 4 | Convert to current exposure base |
| 5 | Calculate annual expected loss to layer |
| 6 | Divide by limit to obtain burning cost |

---

## 15.6.2 Pricing Components

| Component | Description | Example |
|-----------|-------------|---------|
| Burning cost | Expected loss to layer | $2.0M |
| Risk load | Uncertainty of loss | $0.5M |
| Capital charge | Return on capital supporting the layer | $0.8M |
| Expense load | Underwriting, administration, brokerage | $0.6M |
| Profit margin | Target return | $0.3M |
| **Technical premium** | **Total** | **$4.2M** |

### Price Monitoring Metrics

| Metric | Formula | Purpose |
|--------|---------|---------|
| Rate on line | Premium ÷ Limit | Price relative to exposure |
| Loss ratio | Loss ÷ Premium | Claims experience |
| Combined ratio | (Loss + Expense) ÷ Premium | Underwriting profitability |
| Return on equity | Profit ÷ Capital | Capital efficiency |

---

## 15.6.3 Accounting — Key Concepts

| Concept | Description |
|---------|-------------|
| **Ceded premium** | Premium transferred to reinsurer |
| **Ceding commission** | Reinsurer's payment to cedent for acquisition cost |
| **Profit commission** | Additional payment when treaty profitable |
| **Deposit premium** | Minimum premium at inception; adjusted later |
| **Provisional premium** | Estimate subject to adjustment |
| **Adjustment premium** | Difference between final and provisional |
| **Recoveries** | Reinsurer's share of paid losses |
| **Outstanding losses** | Reinsurer's share of reserves |

---

## 15.6.4 Accounting Entries — Illustrative

| Transaction | Cedent Debit | Cedent Credit |
|-------------|--------------|---------------|
| Pay ceded premium | Ceded premium expense | Cash / reinsurer |
| Receive ceding commission | Cash | Ceding commission income |
| Receive profit commission | Cash | Profit commission income |
| Recover paid losses | Cash / recoverable | Recovered losses |
| Record outstanding recoverable | Recoverable asset | Reserve offset |

---

## 15.6.5 Reserves & Reporting

| Reserve | Description |
|---------|-------------|
| **Unearned premium reserve (UPR)** | Premium for unexpired risk |
| **Outstanding claims reserve (OCR)** | Reported losses unpaid |
| **IBNR** | Incurred but not reported losses |
| **Reserve for unexpired risk (RUR)** | Additional buffer when UPR insufficient |

### Reporting Cycles

| Report | Content | Frequency |
|--------|---------|-----------|
| Premium bordereau | Ceded risks, premiums | Monthly |
| Loss bordereau | Claims, recoveries | Monthly |
| Technical account | Premium, claims, commissions | Quarterly |
| Annual statement | Full-year account, settlement | Annual |

---

## 15.6.6 Regulatory Treatment

| Framework | Treatment |
|-----------|-----------|
| **Solvency II (UK/EU)** | Credit for reinsurance if collateral/security requirements satisfied |
| **NAIC (US)** | Credit for reinsurance from authorised reinsurers; trust/collateral for others |
| **IRDAI (India)** | Reinsurance program approval; ceding limits |
| **Statutory reporting** | Reinsurer schedule in annual statement |

### Key Regulatory Considerations

| Consideration | Description |
|---------------|-------------|
| Authorised vs unauthorised | Credit allowed only for authorised (or collateralised) reinsurers |
| Security & collateral | Trust funds, letters of credit |
| Retention & cession limits | Minimum retention requirements |
| Disclosure | Reinsurance arrangements in regulatory filings |

---

## 15.6.7 Case Study — Treaty Pricing

> **Scenario:** Portfolio premium $100M; historical losses to a $20M xs $10M layer trended to $1.8M per year.
>
> **Calculation:**
> - Burning cost = $1.8M
> - Risk load + capital + expense + profit = $1.4M
> - Technical premium = $3.2M (ROL = 16% of limit)
>
> **Outcome:** If market ROL is 14%, the treaty is attractively priced; if 20%, the layer may be renegotiated or reduced.

---

## Review Questions

1. Distinguish experience rating from exposure rating.
2. List the components of a technical reinsurance premium.
3. What is a ceding commission and why is it paid?
4. Why does collateral matter for reinsurance credit?
5. What is the difference between UPR and IBNR?

---

## Glossary

| Term | Definition |
|------|------------|
| Burning cost | Expected loss cost of a layer |
| Ceding commission | Reinsurer payment to cedent |
| IBNR | Incurred but not reported |
| Rate on line | Premium ÷ limit |
| UPR | Unearned premium reserve |

---

## Key Takeaways

1. **Experience and exposure methods estimate the expected loss cost.**
2. **Technical premium = loss cost + risk + capital + expense + profit.**
3. **Accounting tracks premium, commissions, recoveries, and reserves.**
4. **Regulatory credit for reinsurance requires security and compliance.**

---

## References & Further Reading

- Solvency II Directive — reinsurance provisions (public)
- NAIC — reinsurance credit model law (public materials)
- IRDAI — reinsurance regulations (public)

---

**Previous:** [15.5 Catastrophe & Retrocession](05-catastrophe-retrocession.md) |
**Next:** [15.7 Claims & Case Studies](07-claims-case-studies.md)

---

*Part of the Global Insurance Underwriting Handbook — Volume 15*