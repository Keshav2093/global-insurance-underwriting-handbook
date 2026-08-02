# 5.3 Classification & Rating

## Overview

**Classification** groups risks into classes with similar expected loss. **Rating** applies rates to a specific risk using rating factors. The combination of classification and rating produces the **manual premium** for a risk.

## The Rating Structure

```
Base Rate (per exposure unit)
      × Class/Table Factors
      × Territory Factors
      × Limit / Deductible Factors
      = Manual Premium
      ± Experience / Schedule Adjustments
      = Final Premium
```

## Rating Factors by Line

| Line | Main Classifications |
|---|---|
| **Personal auto** | Age, sex (where lawful), marital status, driving record, vehicle, territory, annual mileage, credit/insurance score |
| **Homeowners** | Construction, protection class, age, territory, deductibles, coverage amounts |
| **Commercial property** | Construction, occupancy, protection, exposure, values |
| **Commercial auto** | Vehicle type/use, radius, fleet size, driver records |
| **General liability** | Class code by operation, receipts/payroll, territory, products exposure |
| **Workers comp** | Class code by occupation, payroll, experience modification |
| **Life/health** | Age, sex, health class, smoker status, occupation, avocation |

## Key Rating Concepts

| Concept | Meaning |
|---|---|
| **Base rate** | Rate for a standard risk before factors |
| **Relativity** | Multiplier reflecting relative risk vs. base (e.g., 1.25 territory) |
| **Limits profile (ILF)** | Increase in loss cost per additional limit; diminishing factor |
| **Increased limits factor (ILF)** | Multiplier for higher policy limits |
| **Deductible credit** | Premium reduction for higher deductibles |
| **Territory** | Geographic rated area |
| **Class code** | Occupation/business classification (WC, GL, workers comp) |
| **Experience modification (E-mod)** | Credibility-weighted loss experience factor for WC |

## Manual Rate

The **manual rate** is the filed rate for a class/territory before individual risk adjustments. Manual rates are built from:

- **Expected loss cost** per exposure × expense/profit loading.
- Adjusted for **trend** and **rate level**.

### Example — Commercial Property

```
Base rate:                     $0.85 per $100 of value
Construction factor (masonry):  0.80
Protection factor (sprinkler):  0.90
Limit factor:                   1.00
Territory factor:               1.10
Manual rate = 0.85 × 0.80 × 0.90 × 1.00 × 1.10 = $0.673/$100
Premium on $1,000,000 = $6,730
```

## Schedule Rating

**Schedule rating** adjusts the manual rate for individual account characteristics beyond the classification:

| Debit/Credit | Basis |
|---|---|
| **Management quality** | Safety programs, training, expertise |
| **Housekeeping/maintenance** | Physical condition evidence |
| **Loss control programs** | Engineering, safety, return-to-work |
| **Claims management** | Cooperation, loss history, mitigation |
| **Financial strength** | Deductible credibility, insolvency risk |
| **Special hazards** | Operations outside the class norm |

Schedule factors apply within a range (e.g., ±25%); they must be **justified and documented**.

## Increased Limits Factors

As limits rise, loss cost rises **less than proportionally**:

| Limit | ILF |
|---|---|
| $100,000 | 1.00 |
| $250,000 | 1.25 |
| $500,000 | 1.45 |
| $1,000,000 | 1.60 |

ILFs are filed and applied consistently; the underwriter does not re-derive them in a standard risk.

## Rating vs. Pricing

| Function | Who | Output |
|---|---|---|
| **Ratemaking** | Actuary | Manual rates, ILFs, schedules |
| **Rating** | System/underwriter | Applied premium for the risk |
| **Pricing** | Underwriter | Final terms: debits, credits, judgment |

The underwriter may make **discretionary** adjustments within authority; large deviations require referral.

## Summary

- **Classification and rating** translate risk characteristics into premium.
- **Factor multiplicatives** (class, territory, ILF, deductible) build the manual rate.
- **Schedule rating** reflects account-specific quality.
- **Experience rating** (E-mod) reflects historical losses (see 5.7).
- **Ratemaking, rating, and pricing** are distinct but connected functions.

## Related Chapters

- [5.1 Pricing Fundamentals](01-pricing-fundamentals.md)
- [5.4 Pricing Techniques](04-pricing-techniques.md)
- [5.6 Rating by Line](06-rating-by-line.md)
- [5.7 Experience Rating](07-experience-rating.md)