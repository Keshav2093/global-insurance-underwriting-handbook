# 5.4 Pricing Techniques

## Overview

Pricing techniques convert historical loss experience and exposure data into an **indicated rate level**. The two classic approaches are the **loss cost method** and the **loss ratio method**. Both are built on the concepts from [5.2 Data & Loss Reserving](02-data-loss-reserving.md).

## The Loss Cost (Pure Premium) Method

```
Step 1: Calculate trended, developed loss cost per exposure
Step 2: Divide by expense + profit allowance
Step 3: Compare to current rate level
Step 4: Apply credibility
Step 5: Set indicated rate change
```

### Worked Example

| Item | Value |
|---|---|
| Developed losses (per exposure) | $45.00 |
| Trend factor (2 years) | 1.10 |
| Trended loss cost | $49.50 |
| Expense ratio target | 30% |
| Profit & contingency | 5% |
| Variable expense allowance | 35% |
| Indicated rate | 49.50 ÷ (1 − 0.35) = $76.15 |
| Current average rate | $70.00 |
| Indicated rate change | (76.15 − 70.00) ÷ 70.00 = +8.8% |

## The Loss Ratio Method

```
Indicated Rate Change = (Experience Loss Ratio − Target Loss Ratio) ÷ Target Loss Ratio × 100%
```

| Item | Value |
|---|---|
| Experience loss ratio (trended, developed) | 72% |
| Target loss ratio | 65% |
| Indicated change | (72 − 65) ÷ 65 = +10.8% |

The loss ratio method compares **actual incurred** to **expected target**, with adjustments for trend, development, and rate level.

## Components of Both Methods

| Adjustment | Purpose |
|---|---|
| **Development** | Bring historical losses to ultimate |
| **Trend** | Project loss costs to the policy period |
| **Rate level adjustment** | Index premiums to current rate levels |
| **Experience period** | Selection of credible years |
| **Credibility** | Blend company data with industry data |

## Credibility

**Credibility (Z)** measures how much weight to give actual experience vs. expected/industry data:

```
Indicated = Z × (Experience-based indication) + (1 − Z) × (Expected/Industry indication)
```

| Z (Credibility) | Interpretation |
|---|---|
| 0.00–0.30 | Low — rely on industry/expected |
| 0.31–0.70 | Partial — blend |
| 0.71–1.00 | High — rely on own data |

Full credibility is typically set where the data volume gives a stable estimate (e.g., a certain number of claims or exposures). **Complementary credibility** uses the industry/prior rate as the complement.

## Simple vs. Weighted

| Method | Use |
|---|---|
| **Simple average** | Equal weight to all years |
| **Weighted average** | More weight to recent years (they are more representative) |
| **Exponential smoothing** | Decay weights |

## Large Loss Treatment

| Approach | Description |
|---|---|
| **Cap/limit losses** | Cap individual losses at a level; add a loading for the excess |
| **Separate modeling** | Model severity distribution for the tail |
| **Reinsurance credit** | Reflect net-of-reinsurance losses |

Large losses (catastrophes, single shocks) are treated separately so they do not distort the attritional loss cost.

## Fit and Rate Level

| Term | Meaning |
|---|---|
| **Loss trend** | Annual change in loss cost (frequency + severity) |
| **Premium trend** | Change in exposure base and rate level |
| **On-level premium** | Premium as if current rates applied historically |
| **Rate level index** | Measure of rate changes over time |

**On-leveling** aligns historical premiums to current rates so that loss ratios are comparable across years.

## Off-Balance and Classification Relativity

- **Off-balance factors** — adjust overall rate level while keeping class relativities constant.
- **Classification relativity** — update relativities (e.g., age, territory) independently of the overall level.

Both must be monitored to preserve **equity** between classes.

## Summary

- **Loss cost method** builds the indicated rate from loss cost per exposure.
- **Loss ratio method** compares experience to target.
- **Development, trend, rate level, and credibility** are the core adjustments.
- **Large losses** are handled separately.
- **On-leveling** makes historical data comparable.
- The output is an **indicated rate change** with a documented basis.

## Related Chapters

- [5.1 Pricing Fundamentals](01-pricing-fundamentals.md)
- [5.2 Data & Loss Reserving](02-data-loss-reserving.md)
- [5.3 Classification & Rating](03-classification-rating.md)
- [5.5 Predictive Analytics](05-predictive-analytics.md)