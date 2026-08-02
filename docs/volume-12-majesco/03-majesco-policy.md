# 12.3 — Majesco Policy for P&C

## 12.3.1 Overview

**Majesco Policy for P&C** is the policy administration system for personal and commercial lines. It manages the complete policy lifecycle: submission, quote, bind, issue, endorsement, renewal, and cancellation.

### Core Capabilities

| Capability | Description |
|-----------|-------------|
| **Product configuration** | No-code product builder (Product Accelerator) |
| **Rating** | Ratabase rating engine integration |
| **Underwriting rules** | Referral, validation, and decision rules |
| **Submission management** | New business workflow |
| **Policy issuance** | Policy documents, schedules, forms |
| **Endorsements** | Mid-term changes |
| **Renewals** | Automated renewal generation |
| **Cancellations** | Full rule-driven cancellation cycle |
| **Multi-line** | Personal auto, home, package, commercial |

---

## 12.3.2 Policy Lifecycle

### New Business

| Step | Description |
|------|-------------|
| **Submission** | Create from portal, agent, or API |
| **Data capture** | Risk, party, coverage data |
| **Rating** | Compute premium via Ratabase |
| **Underwriting review** | Rules and referral workflow |
| **Quote** | Present quote options |
| **Bind** | Bind and issue |
| **Document generation** | Issue policy documents |

### Endorsements

| Change | Description |
|--------|-------------|
| **Coverage change** | Add/remove/change coverage |
| **Risk change** | Vehicle, property, exposure changes |
| **Party change** | Named insured, address changes |
| **Premium adjustment** | Additional or return premium |

### Renewals

| Step | Description |
|------|-------------|
| **Renewal generation** | Auto-create renewal before expiration |
| **Re-rating** | Current rating at renewal |
| **Underwriting** | Rules and referrals re-run |
| **Offer** | Present to insured |
| **Non-renewal** | Notice rules applied |

### Cancellations

| Type | Description |
|------|-------------|
| **Flat** | No earned premium |
| **Pro-rata** | Proportional return |
| **Short-rate** | Penalty applied |
| **Non-payment** | Cancellation for non-pay |
| **Underwriting** | Risk no longer acceptable |

---

## 12.3.3 Product Configuration (Product Accelerator)

**Majesco Product Accelerator** is the no-code product configuration tool.

### What You Configure

| Level | Configuration |
|-------|---------------|
| **Line of business** | Personal auto, home, commercial |
| **Product** | Named product definitions |
| **Coverage** | Coverage types, limits, deductibles |
| **Eligibility** | Risk eligibility rules |
| **Forms** | Coverage forms, endorsements |
| **Rating** | Rate tables, factors, formulas |
| **Workflow** | Screens, tasks, approval flows |
| **Documents** | Dec pages, policy forms |

### Configuration Features

| Feature | Description |
|---------|-------------|
| **UI-driven** | Build products without code |
| **Versioning** | Versioned product definitions |
| **Testing** | Test configurations before release |
| **Templates** | Reusable product templates |
| **Centralized reference data** | Shared lookups |
| **Approval workflow** | Business sign-off before go-live |

---

## 12.3.4 Rating with Ratabase

**Ratabase** is Majesco's rating engine, used for pricing and rating rules.

### Rating Capabilities

| Capability | Description |
|-----------|-------------|
| **Rate tables** | Flexible rate storage |
| **Formulas** | Premium calculation logic |
| **Tiering** | Classification tiers |
| **Discounts** | Credits and discounts |
| **Surcharges** | Additional charges |
| **Minimum premium** | Minimum premium rules |
| **Multi-company** | Company-specific rates |
| **Multi-state** | State-specific rate sets |
| **Audit** | Full rating trace |

### Sample Rating Flow

```
Base Rate (territory + class)
  × Coverage Factors
  × Tier Adjustments
  − Discounts
  + Surcharges
  + Taxes / Fees
= Total Premium
```

---

## 12.3.5 Underwriting in Policy

### Rule Types

| Rule | Action |
|------|--------|
| **Validation** | Block invalid data |
| **Referral** | Send to underwriter |
| **Requirement** | Document required before bind |
| **Condition** | Add stipulation |
| **Decline** | Auto-decline |
| **Pre-fill** | Populate from data sources |
| **Alert** | Warning message |

### Underwriting Workflow

```
Submission → Data Capture → Rules Evaluation → Auto-Approve | Referral | Decline → Decision
```

| Outcome | Description |
|---------|-------------|
| **Auto-approve** | Risk accepted by rules |
| **Referral** | Underwriter reviews, accepts/declines/conditions |
| **Decline** | Risk not accepted |
| **Suspend** | Awaiting additional information |

---

## 12.3.6 Policy Documents

| Document | Description |
|----------|-------------|
| **Declaration page** | Coverage, limits, premium summary |
| **Policy form** | Terms and conditions |
| **Endorsements** | Policy changes |
| **Renewal notice** | Renewal offer |
| **Cancellation notice** | Cancellation notice |
| **Certificate of insurance** | Proof of coverage |
| **ACORD forms** | Industry-standard forms |
| **Binder** | Evidence of coverage pre-issue |

---

## 12.3.7 APIs and Integration

| API | Examples |
|-----|----------|
| **Submission** | Create, update, quote, bind |
| **Policy** | Search, retrieve, issue, cancel |
| **Rating** | Rate a risk, re-rate |
| **Document** | Generate, retrieve |
| **Party** | Create, search, update parties |
| **Task** | Underwriting tasks and decisions |

### Common Integrations

| System | Purpose |
|--------|---------|
| **Agent portal** | Submission and documentation |
| **MVR** | Driving records |
| **Credit bureau** | Insurance scores |
| **Property data** | Replacement cost |
| **Payment gateway** | Premium collection |
| **Document management** | Policy archive |
| **Analytics** | Policy data feeds |

---

## Key Takeaways

1. **Majesco Policy** manages the complete policy lifecycle across personal and commercial lines.
2. **Product Accelerator** provides no-code product configuration.
3. **Ratabase** delivers flexible, auditable rating.
4. **Underwriting rules** automate decisions and referrals.
5. **Documents** are generated within the system.
6. **APIs** enable portal and partner integration.

---

**Next:** [12.4 Billing & Claims](04-majesco-billing-claims.md)