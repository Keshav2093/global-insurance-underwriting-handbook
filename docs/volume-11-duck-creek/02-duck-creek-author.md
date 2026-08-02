# 11.2 — Duck Creek Author

## 11.2.1 Overview

**Duck Creek Author** is the policy administration system. It manages the end-to-end policy lifecycle: submission → quote → bind → issue → endorsement → renewal → cancellation. Author is designed to be *product-centric*: insurance products are built, configured, and maintained by business users without custom code.

### Core Capabilities

| Capability | Description |
|-----------|-------------|
| **Product configuration** | Policy forms, coverages, limits, deductibles, eligibility |
| **Rating** | Rate tables, formulas, tiering, discounting |
| **Underwriting rules** | Referral rules, validation, conditions, authority limits |
| **Submission management** | Data capture, quote comparison, bind |
| **Policy issuance** | Policy documents, dec pages, endorsements |
| **Renewals** | Automatic renewal generation, rate changes |
| **Cancellations** | Flat, pro-rata, short-rate; notices |
| **Customer/agent portal** | Self-service, e-sign, electronic documents |

---

## 11.2.2 Author Architecture

```
┌─────────────────────────────────────────────┐
│                User Interfaces              │
│   Desktop UI, Portal, API, Mobile           │
├─────────────────────────────────────────────┤
│            Service Layer (REST)             │
├─────────────────────────────────────────────┤
│          Policy Model & Workflow            │
├─────────────────────────────────────────────┤
│         Business Rules Engine               │
├─────────────────────────────────────────────┤
│            Rating Engine                    │
├─────────────────────────────────────────────┤
│           Azure SQL Database                │
└─────────────────────────────────────────────┘
```

### Key Architecture Concepts

| Component | Description |
|-----------|-------------|
| **Policy Model** | The data structure for policy, policy period, risk, coverage |
| **Transaction model** | Audit trail of all policy changes |
| **All-Lines Rating** | Unified rating engine across all lines of business |
| **Workflow engine** | Task and approval management |
| **Rules framework** | Business rules in C# / embedded rules |
| **REST API** | All actions available via API |

---

## 11.2.3 Product Configuration with ProductIX

**ProductIX** is Duck Creek's no-code product configuration tool. Business analysts and product managers use ProductIX to define products.

### What You Configure in ProductIX

| Level | Configuration |
|-------|---------------|
| **Product package** | Lines of business, product combinations |
| **Product** | Auto, Home, Commercial Package, Workers Comp |
| **Policy form** | Coverage forms, endorsements |
| **Coverage** | Coverage types, sub-coverages, limits |
| **Modifier** | Deductibles, surcharges, credits |
| **Rating** | Rate tables, factors, formulas |
| **Eligibility rules** | Who / what qualifies |
| **Document template** | Dec pages, policy booklets, forms |

### ProductIX User Experience

| Feature | Description |
|---------|-------------|
| **No-code drag-and-drop editor** | Build products using visual tools |
| **Versioning** | Every product change versioned and approved |
| **Templates** | Clone products from templates |
| **Market launch** | Deploy product to production from the UI |
| **Reference data** | Managed centrally, shared across products |
| **Collaboration** | Role-based access and approval workflow |

---

## 11.2.4 Policy Lifecycle in Author

### New Business

| Step | Description |
|------|-------------|
| **Submission** | Create submission from portal, agent, or API |
| **Data capture** | General info, locations, vehicles, coverage selection |
| **Rating** | System computes premium using configured rating |
| **Underwriting** | Rules evaluate the risk; referrals triggered as needed |
| **Quote** | Multiple quotes compare options |
| **Bind** | Bind coverage, issue policy |
| **Policy issuance** | Generate documents, send to insured |

### Endorsements (Mid-Term Changes)

| Change Type | Description |
|-------------|-------------|
| **Coverage change** | Add/remove/change coverage, limits, deductibles |
| **Risk change** | Add vehicle, change vehicle, location change |
| **Personal change** | Named insured change, mailing address |
| **Policy change** | Reduce/refund premium, additional interest |

### Renewals

| Step | Description |
|------|-------------|
| **Renewal generation** | System creates renewal period before expiration |
| **Rate change** | Renewal rated at current rates |
| **Underwriting re-evaluation** | Rules re-run; new referrals may trigger |
| **Renewal offer** | Customer accepts, declines, or negotiates |
| **Non-renewal** | Policy not offered; notice issued where required |

### Cancellations

| Type | Description |
|------|-------------|
| **Flat cancellation** | No earned premium (typically before inception) |
| **Pro-rata cancellation** | Premium returned proportionally to unused time |
| **Short-rate cancellation** | Insured-initiated; penalty applied |
| **Non-payment** | Cancellation for non-payment of premium |
| **Underwriting cancellation** | Risk no longer acceptable; notice requirements |

---

## 11.2.5 Rating in Author

### Rating Components

| Component | Description |
|-----------|-------------|
| **Rate tables** | Base rates, territorial factors, classification factors |
| **Modifiers** | Deductibles, credits, surcharges, discounts |
| **Formulas** | Premium calculation logic |
| **Rating steps** | Order of premium computation |
| **Override rules** | Manual premium override with authority limits |

### Sample Rating Flow (Personal Auto)

```
Base Rate (by territory, coverage)
  × Vehicle Class Factor
  × Driver Class Factor
  × Coverage Selection Factor
  × Deductible Discount
  × Multi-Car Discount
  × Claims-Free Discount
  + Additional Coverages
  + Tax / Fees
= Total Premium
```

### Rating Features

| Feature | Description |
|---------|-------------|
| **All-lines rating** | One rating engine for all products |
| **Multi-company** | Rate by underwriting company |
| **Multi-currency** | Rate in local currency |
| **Audit** | Full rating log with calculation detail |
| **Explainability** | Premium display with all factors |
| **Integration** | External rating via API if needed |

---

## 11.2.6 Underwriting Rules in Author

### What Rules Do

| Rule Type | Action |
|-----------|--------|
| **Validation** | Block submission if data invalid |
| **Referral** | Route to underwriter for review |
| **Condition** | Add stipulation or requirement |
| **Requirement** | Need supporting document before bind |
| **Pre-fill** | Auto-populate fields from data |
| **Alert** | Display warning message |
| **Auto-decline** | Automatically decline risk |

### Example Referral Rules

| Rule | Condition |
|------|-----------|
| **High-value home** | Dwelling > $5,000,000 |
| **Young driver** | Driver under 21 on standard auto |
| **Commercial food service** | Restaurant with liquor service |
| **Large workers comp** | Payroll > $10,000,000 |
| **Sinkhole zone** | Property in designated sinkhole area |
| **Excess liability** | Umbrella limit > $20,000,000 |

### Rule Performance

| Feature | Description |
|---------|-------------|
| **Rule testing** | Test rules before release |
| **Versioning** | Rules versioned with products |
| **Rule priority** | Order of rule evaluation |
| **Rule grouping** | Application by product, LOB, state |
| **Exception handling** | Underwriter overrides logged with authority |

---

## 11.2.7 Documents and Forms

| Document Type | Generated From | Purpose |
|---------------|---------------|---------|
| **Declaration page** | Policy data template | Summary of coverage, limits, premium |
| **Policy booklet** | Form library | Standard policy terms and conditions |
| **Endorsement forms** | Form library | Specific changes to policy |
| **Cancellation notice** | Template | Written notice of cancellation |
| **Renewal notice** | Template | Offer of renewal with premium |
| **Certificate of insurance** | Template | Proof of coverage |
| **ACORD forms** | Form library | Standard industry forms |

---

## 11.2.8 Integration and APIs

### Author API Capabilities

| API Category | Examples |
|--------------|---------|
| **Account** | Create account, search, update |
| **Submission** | Create submission, update data, quote, bind |
| **Policy** | Get policy, search, issue |
| **Rate** | Request rating, compare rates |
| **Document** | Get document, generate document |
| **Rules** | Run rules, get rule results |

### Common Author Integrations

| System | Integration |
|--------|-------------|
| **Agent portal** | Submission, quote, bind, documents |
| **MVR provider** | Driver record retrieval during rating |
| **Credit report** | Insurance score for underwriting |
| **Property data** | Replacement cost, loss history |
| **Payment gateway** | Premium collection |
| **Document management** | Archived policy files |
| **Data warehouse** | Policy extracts for reporting |

---

## Key Takeaways

1. **Author is the policy administration system** covering the full policy lifecycle.
2. **ProductIX enables no-code product configuration** — business users build and maintain products.
3. **Rating is configurable** through rate tables, modifiers, and formulas.
4. **Underwriting rules** automate validation, referral, and decisioning.
5. **Documents and forms** are generated from templates within the platform.
6. **API-first** capabilities enable portal and partner integration.

---

**Next:** [11.3 Duck Creek Billing](03-duck-creek-billing.md)