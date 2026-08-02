# 13.3 — Product & Rating Projects

## 13.3.1 Overview

Product and rating projects are among the most frequent and highest-value work for insurance BAs. These projects include new product launches, coverage changes, rate revisions, and rating logic updates — all of which require deep domain knowledge and disciplined requirements management.

---

## 13.3.2 Types of Product Projects

| Project Type | Example |
|--------------|---------|
| **New product launch** | Launch commercial package in a new state |
| **Product enhancement** | Add a new coverage option |
| **Endorsement change** | Revise a policy endorsement |
| **Rate revision** | Annual rate change |
| **Rule change** | Update eligibility or referral rules |
| **Form change** | Update policy forms |
| **Line expansion** | Add a line of business |
| **State expansion** | File and launch in additional states |

---

## 13.3.3 Product Project Phases

### Phase 1: Feasibility & Scoping

| Activity | BA Deliverable |
|----------|---------------|
| Business case support | Scope definition |
| Stakeholder identification | Stakeholder list |
| Options analysis | Recommendation |
| High-level estimate | Impact assessment |
| Success criteria | Measurable goals |

### Phase 2: Requirements

| Activity | BA Deliverable |
|----------|---------------|
| Product requirements workshop | Product requirements document |
| Rate structure definition | Rating requirements |
| Rule definition | Rule matrix |
| Form/endorsement drafting support | Form requirements |
| Workflow design | Workflow requirements |
| Data requirements | Data dictionary |

### Phase 3: Configuration Support

| Activity | BA Deliverable |
|----------|---------------|
| Clarify requirements | Answers, decisions log |
| Validate logic | Reviewed config specs |
| Coordinate with actuaries | Rate table specs |
| Support developers/configurators | Functional specs |

### Phase 4: Testing

| Activity | BA Deliverable |
|----------|---------------|
| Test scenario creation | Test scenarios |
| Test case review | Reviewed test cases |
| Defect triage | Prioritized defects |
| UAT facilitation | UAT plan and support |
| Sign-off support | UAT sign-off |

### Phase 5: Filing & Deployment

| Activity | BA Deliverable |
|----------|---------------|
| State filing support | Filing documentation |
| User communication | Product bulletins |
| Training support | Training material |
| Go-live coordination | Deployment checklist |
| Post-implementation review | Lessons learned |

---

## 13.3.4 Rating Logic — What the BA Must Understand

### Rating Components

| Component | Description |
|-----------|-------------|
| **Base rate** | Starting premium for a class/territory |
| **Factor** | Multiplier (class, territory, tier) |
| **Modifier** | Adjustment (deductible, discounts) |
| **Step/algorithm** | Order of calculation |
| **Minimum premium** | Floor |
| **Maximum premium** | Cap |
| **Taxes/fees** | Premium taxes, fees |
| **Rounding** | Rounding rule |

### Rating Formula Example (Personal Auto)

```
Premium = Base Rate × Territory Factor × Class Factor × Tier Factor
          × Deductible Modifier × Discount Modifier
          + Additional Coverages
          + Taxes & Fees
```

### Rating Requirements to Document

| Requirement | Example |
|-------------|---------|
| Base rate table | $400 per vehicle per year |
| Territory factor | Zone 1: 1.00, Zone 2: 1.25 |
| Class factor | Age 25–65: 1.00, Under 25: 1.75 |
| Coverage factor | Liability per limit band |
| Deductible modifier | $500: 1.00, $1,000: 0.90 |
| Discounts | Multi-car: −10%, Claims-free: −5% |
| Minimum premium | $150 |
| Taxes | 3.5% state premium tax |

---

## 13.3.5 Rate Filing Support

### State Rate Filing Process (US)

```
Rate Development → Filing Preparation → SERFF Submission → State Review → Approval/Questions → Effective Date
```

| Step | BA Role |
|------|---------|
| Rate development | Coordinate with actuarial |
| Filing preparation | Gather supporting documents |
| SERFF submission | Support filing submission |
| State review | Track status, respond to questions |
| Approval | Prepare implementation |
| Effective date | Coordinate go-live |

### BA Deliverables for Rate Filings

| Deliverable | Description |
|-------------|-------------|
| Rate basis summary | How rates were developed |
| Class/territory plans | Classification definitions |
| Rule changes | Revised rating rules |
| Loss ratio support | Historical experience |
| Impact analysis | Average premium change by segment |
| Competitive analysis | Market rate comparison |
| Implementation plan | System implementation schedule |

---

## 13.3.6 Testing Product & Rating Changes

### Rating Test Cases

| Test Case | Input | Expected Output |
|-----------|-------|----------------|
| Basic rate | Class A, Zone 1 | Base rate × factors |
| Discount application | Multi-car | Rate less discount |
| Minimum premium | Low-risk | Premium ≥ minimum |
| Maximum premium | High-risk | Premium ≤ cap |
| Deductible selection | $1,000 ded. | Modified premium |
| Endorsement | Add coverage | Additional premium |
| Cancellation | Mid-term | Return premium |
| Multi-policy | Package | Combined premium |

### Test Scenario Structure

| Element | Example |
|---------|---------|
| Scenario ID | RATE-015 |
| Description | Home with $1M dwelling value |
| Inputs | Value, territory, deductible |
| Expected premium | $2,450 |
| Calculation steps | Show each step |
| Pass criteria | Calculated = expected +/− $0.01 |

---

## 13.3.7 Product Documentation

### Product Requirements Document Structure

| Section | Contents |
|---------|----------|
| **Overview** | Product description, purpose |
| **Eligibility** | Who/what qualifies |
| **Coverages** | Coverage options, limits, deductibles |
| **Rating** | Rate structure, factors, formulas |
| **Rules** | Referral, decline, validation rules |
| **Forms** | Policy forms, endorsements |
| **Documents** | Dec page, schedules |
| **Workflow** | Screens, tasks, approvals |
| **Regulatory** | State filings, compliance |
| **Implementation** | Config plan, test plan, rollout |

---

## Key Takeaways

1. **Product projects** span new launches, enhancements, rate revisions, and rule changes.
2. **BAs drive the full lifecycle** from scoping through testing and filing.
3. **Rating logic** must be documented precisely — formulas, rules, and factors.
4. **Rate filings** require regulatory coordination and supporting analysis.
5. **Test scenarios** validate every rating path.
6. **Clear product documentation** is essential for configuration and testing.

---

**Next:** [13.4 BA in Claims](04-ba-claims.md)