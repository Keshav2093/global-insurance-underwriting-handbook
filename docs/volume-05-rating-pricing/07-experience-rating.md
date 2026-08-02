# 5.7 Experience Rating

## Overview

**Experience rating** adjusts a risk's premium based on its **own loss history**, rather than class-wide averages. It rewards good risks and penalizes poor ones, and it is most reliable where the insured is large enough to have credible experience.

## When Experience Rating Applies

| Line | Mechanism |
|---|---|
| **Workers comp** | Experience modification (E-mod) — universal |
| **Commercial auto** | Large fleet experience rating |
| **General liability** | Large accounts; schedule/experience |
| **Commercial property** | Large accounts; loss sensitive plans |
| **Package** | Combined experience across lines |

Small risks lack credibility and use **manual rates** only.

## The Experience Modification (E-mod)

The E-mod compares the insured's **actual losses** to **expected losses** for its class, adjusted for credibility.

| Component | Meaning |
|---|---|
| **Primary limit** | Claims up to this amount count fully (e.g., first $X per claim) |
| **Excess ratio** | Claims above primary count with less weight |
| **Ballast** | Stabilizes small accounts |
| **Credibility (Z)** | Weight on actual vs. expected |
| **E-mod value** | 1.00 = average; <1.00 = better; >1.00 = worse |

### E-mod Example (Illustrative)

```
Expected primary losses:     $50,000
Expected excess losses:      $30,000
Actual primary losses:       $40,000
Actual excess losses:        $20,000
Credibility (Z):             0.60

Primary mod = (40,000 / 50,000) = 0.80
Excess mod  = (20,000 / 30,000) = 0.67
E-mod = Z × (0.80) + (1 − Z) × (1.00)  (simplified)
     = 0.6 × 0.80 + 0.4 × 1.00 = 0.48 + 0.40 = 0.88
```

The E-mod is applied to the **manual premium**; a 0.88 E-mod reduces premium 12%.

## Schedule Rating

**Schedule rating** adjusts the manual/E-mod premium for qualitative account factors:

| Debit (+) | Credit (−) |
|---|---|
| Poor housekeeping/maintenance | Strong safety programs |
| High management turnover | Experienced management |
| Lack of training | Training and return-to-work |
| Poor claims cooperation | Engaged claims management |
| Hazardous operations | Loss control engineering |

Schedule adjustments are limited in range (e.g., ±25%) and must be documented.

## Retrospective Rating

**Retrospective rating** ties the final premium to **actual losses** during the policy period:

```
Final Premium = Basic Premium + (Converted Losses × Loss Conversion Factor) ± Tax
```

Where:

- **Basic premium** — fixed expense/profit component.
- **Converted losses** — losses adjusted by the LCF (loss conversion factor covers LAE).
- **Minimum and maximum premiums** — cap the downside and upside.
- **Standard premium** — the manual premium before the retro plan.

### Retro Rating Characteristics

| Feature | Description |
|---|---|
| **Loss sensitive** | Refunds or additional premiums based on losses |
| **Cash flow** | Retained loss fund for self-insured accounts |
| **Minimum/maximum** | Insurer and insured share risk |
| **Used for** | Large risks with credible experience |

## Loss Sensitive Plans

| Plan | Description |
|---|---|
| **Deductible** | Insured pays first losses; insurer administers |
| **SIR (self-insured retention)** | Insured defends and pays up to SIR |
| **Paid loss retro** | Premium adjusts as losses are paid |
| **Qualified plan** | Tax-approved large deductible programs |

## Credibility in Experience Rating

Credibility determines how much weight the insured's own experience receives:

- **Larger accounts** — more credibility, more experience-based pricing.
- **Small accounts** — more weight to class averages.
- **New businesses** — no experience; manual rates only.

## Advantages and Disadvantages

| Aspect | Notes |
|---|---|
| **Fairness** | Rewards good experience, penalizes poor |
| **Incentive** | Encourages loss prevention |
| **Anti-selection** | Prevents good risks from leaving a pooled book |
| **Volatility** | Large claims create premium swings |
| **Complexity** | Requires loss data, thresholds, filings |
| **Small risk limit** | Little credibility for small insureds |

## Summary

- Experience rating ties premium to the **insured's own losses**.
- **E-mod (WC)** compares actual to expected with credibility and primary/excess weighting.
- **Schedule rating** adds qualitative factors.
- **Retrospective rating** adjusts premium based on policy-period losses within min/max bounds.
- **Deductibles and SIRs** transfer loss exposure to the insured.
- Experience rating is credible only for **larger risks**.

## Related Chapters

- [3.5 Workers Compensation](../volume-03-commercial/05-workers-compensation.md)
- [5.3 Classification & Rating](03-classification-rating.md)
- [5.4 Pricing Techniques](04-pricing-techniques.md)
- [5.6 Rating by Line](06-rating-by-line.md)