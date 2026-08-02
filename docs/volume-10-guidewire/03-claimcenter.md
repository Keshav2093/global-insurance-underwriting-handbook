# 10.3 ClaimCenter

## What is ClaimCenter?

**ClaimCenter** is Guidewire's claims management system. It handles the end-to-end claims lifecycle — first notice of loss (FNOL) through investigation, evaluation, negotiation, payment, and subrogation — with guided workflows, workflow automation, and configurable rules.

## Core Capabilities

| Capability | Description |
|---|---|
| **FNOL** | Claim initiation, intake, assignment |
| **Investigation** | Statements, records, evidence, expert assignments |
| **Evaluation** | Reserve setting, coverage analysis, damages |
| **Resolution** | Settlement authority, negotiations, payments |
| **Recovery** | Subrogation, salvage, reinsurance reporting |
| **Litigation** | Suit handling, defense counsel, billing |
| **Fraud** | Referral to SIU, fraud indicators, red flags |

## Claims Lifecycle in ClaimCenter

```
FNOL → Assignment → Investigation → Evaluation → Resolution → Recovery/Close
```

| Stage | Activities |
|---|---|
| **FNOL** | Intake via phone, portal, API; claim created |
| **Assignment** | Auto-assign by adjuster, territory, severity |
| **Investigation** | Coverage verification, liability, damages |
| **Evaluation** | Reserves, exposure analysis, settlement strategy |
| **Resolution** | Negotiation, approval, payment |
| **Closure** | File review, subrogation, recoveries, archive |

## Key Features

### Workflow Automation

- **Activity plans** — mandatory steps per claim type (e.g., auto physical damage)
- **Diary/checklists** — follow-up tasks and deadlines
- **Assignment rules** — route claims by line, state, severity, load

### Reserving

| Feature | Purpose |
|---|---|
| **Reserve types** | Case, expense, salvage/subrogation offsets |
| **Reserve history** | Full audit trail of all changes |
| **Reserve analysis** | Compare case reserves to actuals |
| **Exposure-level reserves** | Reserving at exposure/coverage level |

### Payments

| Feature | Purpose |
|---|---|
| **Check/EFT** | Multiple payment methods |
| **Authority limits** | Approvals by amount and role |
| **Payment history** | Complete payment ledger |
| **Reconciliation** | Integration with BillingCenter/ERP |

### Subrogation & Recovery

- Subrogation tracking with demand letters
- Salvage handling with settlement calculations
- Reinsurance claim reporting
- Third-party recovery workflows

## Coverage & Policy Integration

| Feature | Purpose |
|---|---|
| **Policy lookup** | Retrieve policy, coverage, limits from PolicyCenter |
| **Coverage determination** | Verify coverage and limits in context |
| **Reservation of rights** | Track RoR, coverage counsel referrals |
| **Excess/UM** | Track layers, primary/excess relationship |

## Claim Center User Roles

| Role | Responsibilities |
|---|---|
| **Intake/CSR** | FNOL, initial data capture |
| **Adjuster** | Investigation, evaluation, negotiation |
| **Examiner** | Coverage analysis, reserve authority |
| **Supervisor/Manager** | Approvals, quality reviews, workload |
| **SIU Investigator** | Fraud referrals and investigations |
| **Litigation Specialist** | Suit handling and counsel management |

## Configuration in ClaimCenter

| Concept | Business Impact |
|---|---|
| **Workflows/Activities** | Enforce claims handling standards |
| **Rules** | Auto-assignment, authority, notifications |
| **Forms/Documents** | Automated letters and forms |
| **Reserve codes** | Standardized loss and expense codes |
| **Lookups** | Claim type, cause of loss, status values |
| **Data validation** | Mandatory fields at each stage |

## Analytics & Reporting

- **Claim dashboards** — open inventory, aged claims, reserve adequacy
- **Cycle time reports** — FNOL to assignment, to settlement
- **Severity/frequency analyses**
- **Fraud detection** — out-of-pattern claims (with Data Platform / third-party models)

## Summary

- ClaimCenter digitizes the end-to-end claims process.
- Guided workflows enforce consistent, compliant handling.
- Reserves, payments, and recoveries are fully auditable.
- Integration with PolicyCenter and BillingCenter unifies data.
- Configuration drives most business rule changes.

## Related Chapters

- [10.1 Guidewire Overview](01-guidewire-overview.md)
- [10.2 PolicyCenter](02-policycenter.md)
- [Volume 7 Claims](../volume-07-claims/index.md)