# 12.4 — Majesco Billing & Claims

## 12.4.1 Majesco Billing for P&C

### Overview

**Majesco Billing for P&C** manages premium billing, payment processing, accounts receivable, and collections across all billing methods.

### Core Capabilities

| Capability | Description |
|-----------|-------------|
| **Invoice generation** | Auto-invoicing from policy transactions |
| **Payment plans** | Annual, semi-annual, quarterly, monthly |
| **Payment processing** | ACH, card, check, EFT |
| **Receivables** | Open items, aging, dunning |
| **Collections** | Notices, late fees, cancellation |
| **Refunds** | Return premium, credits |
| **Commissions** | Agent commission processing |
| **Multi-entity** | Companies, currencies, taxes |

### Billing Lifecycle

```
Policy → Transaction → Invoice → Payment Plan → Payment → Reconciliation → Archive
```

### Billing Events

| Event | Billing Impact |
|-------|---------------|
| New business | Create account, plan, invoice |
| Endorsement | Additional/return premium |
| Renewal | Renewal invoice |
| Cancellation | Return premium, credit |
| Audit (WC) | Final premium |
| Commission | Agent commission |

### Payment Methods

| Method | Description | Recurring |
|--------|-------------|-----------|
| ACH | Bank transfer | Yes |
| Credit/debit card | Tokenized card | Yes |
| Check | Paper/lockbox | No |
| EFT | Electronic transfer | Yes |
| Wallet | Digital wallet | Optional |

### Collections Workflow

```
Invoiced → Past Due → Notice 1 → Notice 2 → Final Notice → Cancellation → Write-Off
```

| Stage | Action |
|-------|--------|
| Past due | Aging starts |
| Notice 1 | Reminder |
| Notice 2 | Formal demand |
| Final notice | Cancellation warning |
| Cancellation | Cancel for non-payment |
| Reinstatement | Payment restores policy |
| Write-off | Uncollectible after approval |

---

## 12.4.2 Majesco Claims for P&C

### Overview

**Majesco Claims for P&C** manages the end-to-end claims lifecycle: FNOL, investigation, coverage analysis, reserving, settlement, recovery, and closure.

### Core Capabilities

| Capability | Description |
|-----------|-------------|
| **FNOL** | Multi-channel intake |
| **Claim setup** | Exposures, parties, involvement |
| **Coverage analysis** | Policy coverage validation |
| **Investigation** | Tasks, documentation, experts |
| **Reserving** | Authority-based reserve setting |
| **Settlement** | Negotiation, approval, payment |
| **Subrogation** | Recovery identification and pursuit |
| **SIU** | Fraud detection and referral |
| **Litigation** | Counsel and expense management |
| **Mobile** | Field adjuster functionality |

### Claims Lifecycle

```
FNOL → Setup → Coverage Check → Investigation → Evaluation → Settlement → Payment → Subrogation → Closure
```

### FNOL Channels

| Channel | Description |
|---------|-------------|
| Phone | Call center entry |
| Web portal | Self-service FNOL |
| Mobile app | Photo, GPS, filing |
| Agent | Agent-filed |
| API | Partner filing |

### Claim Structure

| Component | Description |
|-----------|-------------|
| **Claim** | Overall occurrence/loss |
| **Exposure** | Coverage/claimant combination |
| **Parties** | All involved parties |
| **Reserves** | Case reserves by type |
| **Transactions** | Payments, recoveries, expenses |
| **Activities** | Tasks, notes, assignments |
| **Documents** | Photos, reports, correspondence |

### Reserving

| Reserve Type | Description |
|--------------|-------------|
| Case reserve | Claim-specific estimate |
| Liability reserve | BI/PD estimate |
| Expense reserve | Investigation/legal costs |
| Recovery reserve | Expected subrogation |

### Authority Matrix

| Level | Authority |
|-------|-----------|
| Adjuster | Up to $10,000 |
| Senior adjuster | $10k–$50k |
| Supervisor | $50k–$250k |
| Manager | $250k–$1M |
| Home office | $1M+ |

### Settlement & Payment

| Method | Description |
|--------|-------------|
| Negotiation | Direct settlement |
| Mediation | Facilitated resolution |
| Arbitration | Binding decision |
| Litigation | Court judgment |

### Subrogation

```
Identify → Evaluate → Pursue → Recover → Distribute
```

| Allocation | Description |
|------------|-------------|
| Indemnity | Recover paid indemnity |
| Expenses | Recover investigation costs |
| Deductible | Return policyholder deductible |

### SIU Red Flags

| Indicator | Description |
|-----------|-------------|
| Late reporting | Long delay to report |
| Inconsistent statements | Changing versions |
| Excessive damages | Damage exceeds loss |
| Staged accident | Suspicious pattern |
| Recent coverage | Coverage added before loss |
| Prior suspicious claims | Questionable history |

---

## Key Takeaways

### Billing

1. **Majesco Billing** manages the full premium lifecycle.
2. **Payment plans** provide flexible installment options.
3. **Collections automation** drives notices and cancellations.
4. **Commissions** are processed and reported.

### Claims

5. **Majesco Claims** covers the full claims lifecycle.
6. **FNOL automation** speeds intake and routing.
7. **Reserve authority levels** provide control and oversight.
8. **Subrogation and SIU** are embedded workflows.

---

**Next:** [12.5 Majesco Data & Analytics](05-majesco-data.md)