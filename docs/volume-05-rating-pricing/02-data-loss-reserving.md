# 5.2 Data & Loss Reserving

## Overview

Pricing and reserving both depend on **loss data**. Loss reserving estimates the outstanding liability for claims already incurred; pricing uses historical loss data to project expected future losses. Both are built on **claim triangles**.

## Data Quality

| Dimension | Considerations |
|---|---|
| **Completeness** | All claims captured, no gaps |
| **Consistency** | Definitions stable across years |
| **Granularity** | Claim-level detail for analysis |
| **Timeliness** | Data as of evaluation dates |
| **Accuracy** | Correct payments, reserves, recoveries |

Poor data produces unreliable prices and reserves.

## Loss Development Triangles

A triangle tracks cumulative paid or incurred losses by **accident year** (or report year) as they **develop** over time.

| Accident Year | 12 mo | 24 mo | 36 mo | 48 mo | 60 mo |
|---|---|---|---|---|---|
| 2020 | 5,000 | 8,000 | 9,000 | 9,500 | 9,800 |
| 2021 | 5,500 | 9,000 | 10,200 | 10,800 | |
| 2022 | 6,000 | 10,000 | 11,500 | | |
| 2023 | 6,500 | 11,000 | | | |
| 2024 | 7,000 | | | | |

- **Rows** = accident years.
- **Columns** = development periods (evaluation age).
- **Cumulative** — each cell includes all prior payments.
- The **diagonal** (last cell per row) is the current estimate.

## Key Concepts

| Term | Meaning |
|---|---|
| **IBNR** | Incurred But Not Reported — claims not yet reported |
| **IBNER** | Incurred But Not Enough Reported — revisions to known claims |
| **Case reserve** | Estimate for a known open claim |
| **Development factor** | Projection of how losses grow as they mature |
| **Tail factor** | Development beyond the last observed period |
| **Ultimate losses** | Final total cost of claims for a period |

## Reserve Methods

| Method | Use | Strengths |
|---|---|---|
| **Chain Ladder** | Project paid/incurred by development factors | Simple, standard |
| **Bornhuetter-Ferguson (B-F)** | Combine expected ultimate with actual development | Good for immature/volatile data |
| **Expected loss ratio** | Ultimate = expected LR × earned premium | When data insufficient |
| **Frequency-severity** | Project counts and averages separately | More granular |
| **Stochastic methods** | Distributions of outcomes (bootstrapping, Mack) | Range, uncertainty |

### Chain Ladder Example (Illustrative)

- Accident year 2024 losses at 12 months: 7,000.
- Average 12→24 development factor from prior years: 1.60.
- Estimated 24-month: 7,000 × 1.60 = 11,200.
- Continue applying factors to reach ultimate.

## Reserves in the P&L

- **Reserves** are liabilities on the balance sheet.
- **Loss reserve development** — changes in estimates flow through the income statement.
- **IBNR** must be estimated for pricing adequacy; underestimating reserves understates prices.

## Pricing Data Adjustments

For pricing, historical data must be adjusted:

| Adjustment | Reason |
|---|---|
| **Trend** | Inflation, claims cost growth, social inflation |
| **Exposure changes** | Payroll, receipts, values changes |
| **Policy form changes** | Coverage differences across years |
| **Reinsurance** | Net vs. gross analysis |
| **Large losses** | Separate attritional from shock losses |
| **Underlying rate changes** | Rate level movements distort comparisons |

## Summary

- **Triangles and development factors** are the foundation of reserving and pricing.
- **IBNR/IBNER** capture unrealized liabilities.
- **Chain ladder, B-F, and stochastic methods** are the core techniques.
- **Pricing adjustments** (trend, exposure, large loss) turn raw data into projections.
- **Data quality** determines the credibility of everything downstream.

## Related Chapters

- [5.1 Pricing Fundamentals](01-pricing-fundamentals.md)
- [5.4 Pricing Techniques](04-pricing-techniques.md)
- [7.5 Reserving & Settlement](../volume-07-claims/05-reserving-settlement.md)