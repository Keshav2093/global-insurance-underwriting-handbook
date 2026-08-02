# 11.3 — Duck Creek Billing

## 11.3.1 Overview

**Duck Creek Billing** manages premium billing, payment processing, accounts receivable, and collections. It delivers a complete billing lifecycle for new business, endorsements, renewals, and cancellations — with support for multiple payment methods, plans, and collection workflows.

### Core Capabilities

| Capability | Description |
|-----------|-------------|
| **Invoice generation** | Automatic invoicing from policy transactions |
| **Payment plans** | Annual, semi-annual, quarterly, monthly |
| **Payment processing** | ACH, credit card, check, EFT |
| **Receivables management** | Open items, aging, dunning |
| **Collections** | Notices, late fees, cancellation for non-payment |
| **Refunds** | Return premiums, cancellations, endorsements |
| **Distribution** | Agent commissions, MGA statements |
| **1099 reporting** | Produce, vendor, claimant forms |
| **Multi-entity** | Multiple companies, currencies, taxes |

---

## 11.3.2 Billing Lifecycle

### Premium Flow

```
Policy Created → Transaction → Invoice → Payment Plan → Billing → Payment → Reconcile → Archive
```

### Billing Events

| Event | Billing Impact |
|-------|---------------|
| **New business** | Create billing account, set payment plan, generate invoice |
| **Endorsement** | Adjust premium, generate additional/return premium |
| **Renewal** | Generate renewal invoice |
| **Cancellation** | Compute return premium, generate credit |
| **Reinstatement** | Reinstate policy, re-establish payment plan |
| **Audit (WC)** | Final premium audit, additional premium billing |
| **Commission** | Calculate and pay agent commission |

---

## 11.3.3 Payment Plans

### Plan Structure

| Plan Component | Description |
|----------------|-------------|
| **Plan type** | Annual, semi-annual, quarterly, monthly, weekly |
| **Payment mode** | Number of installments |
| **Down payment** | First installment amount (often a percentage) |
| **Installment amount** | Calculated from billed premium |
| **Service fee** | Fee for installment plans |
| **Due dates** | Scheduled from policy effective date |
| **Payment method** | ACH, card, check, EFT per installment |

### Common Plan Examples

| Plan | Down Payment | Installments | Frequency |
|------|--------------|--------------|-----------|
| **Annual** | 100% | 1 | Once |
| **Semi-Annual** | 50% | 2 | Every 6 months |
| **Quarterly** | 25% | 4 | Every 3 months |
| **Monthly** | 1st month | 12 | Every month |
| **Payroll Deduction** | 1st deduction | 12 | Monthly |

### Payment Plan Features

| Feature | Description |
|---------|-------------|
| **Plan switching** | Insured can change plan mid-term |
| **Automatic payment** | Auto-draft on due date |
| **Grace period** | Configurable per plan |
| **Installment forgiveness** | Waive final installment on cancellation |
| **Plan rules** | Business rules per product, state, company |

---

## 11.3.4 Payment Processing

### Payment Methods

| Method | Description | Recurring? |
|--------|-------------|------------|
| **ACH** | Bank transfer, automated clearing | Yes |
| **Credit/Debit card** | Card on file, tokenized | Yes |
| **Check** | Paper or lockbox | No |
| **EFT** | Electronic funds transfer | Yes |
| **Cash** | Counter payments (rare) | No |
| **Wallet** | Digital wallets (Apple Pay, PayPal) | Optional |

### Payment Processing Flow

```
Invoice Due → Payment Initiation → Payment Gateway → Authorization → Posting → Reconciliation
```

| Step | Description |
|------|-------------|
| **Payment initiation** | Auto-draft or manual entry |
| **Gateway** | Process through payment processor |
| **Authorization** | Verify funds/card validity |
| **Posting** | Apply payment to open items |
| **Reconciliation** | Match with bank statement |

### Payment Security

| Measure | Description |
|---------|-------------|
| **Tokenization** | Card data replaced with tokens |
| **PCI DSS** | Compliance with payment card standards |
| **Encryption** | Encryption at rest and in transit |
| **3-D Secure** | Additional cardholder verification |
| **Fraud detection** | Transaction monitoring |

---

## 11.3.5 Invoices and Statements

### Invoice Types

| Invoice | Trigger |
|---------|---------|
| **Initial invoice** | New business, first installment |
| **Installment invoice** | Each scheduled payment |
| **Endorsement invoice** | Additional premium from change |
| **Return premium invoice** | Credit from endorsement or cancellation |
| **Audit invoice** | Worker comp final audit |
| **Aggregate invoice** | Multiple policies combined on one invoice |

### Invoice Components

| Field | Description |
|-------|-------------|
| Invoice number | Unique identifier |
| Policy number | Related policy |
| Invoice date | Date generated |
| Due date | Payment deadline |
| Premium amount | Billed premium |
| Fees/taxes | Service, installment, premium tax |
| Payment method | How payment is expected |
| Payment history | Prior payments/credits |

### Statements

| Statement | Description |
|-----------|-------------|
| **Billing statement** | Summary of all open items for an account |
| **E-bill** | Electronic invoice delivery |
| **Agent statement** | Commission and premium summary for agents |
| **MGA statement** | Detailed statement for managing general agents |

---

## 11.3.6 Receivables and Collections

### Receivables Aging

| Aging Bucket | Definition |
|--------------|-----------|
| **Current** | Not yet due |
| **1–30 days** | First notice sent |
| **31–60 days** | Second notice sent |
| **61–90 days** | Final notice / demand |
| **90+ days** | Cancellation for non-payment |

### Collections Workflow

```
Invoiced → Past Due → Notice 1 → Notice 2 → Cancellation → Reinstatement / Write-Off
```

| Stage | Action |
|-------|--------|
| **Past due** | Aging starts at due date |
| **Notice 1** | Friendly reminder |
| **Notice 2** | Formal demand |
| **Final notice** | Warning of cancellation |
| **Cancellation** | Cancel policy for non-payment |
| **Reinstatement** | Pay full balance, reinstate policy |
| **Write-off** | Uncollectable balance removed after approval |

### Late Fees

| Element | Configuration |
|---------|---------------|
| **Percent** | Percentage of past-due amount |
| **Flat fee** | Fixed dollar amount |
| **Grace period** | Days before late fee applies |
| **Exemptions** | States/plans where fees are prohibited |

---

## 11.3.7 Refunds and Return Premiums

| Refund Type | Trigger | Calculation |
|-------------|---------|-------------|
| **Pro-rata refund** | Insurer-initiated cancellation | Unearned premium proportionally |
| **Short-rate refund** | Insured-initiated cancellation | Unearned premium less penalty |
| **Endorsement return** | Reduces coverage mid-term | Difference in premium |
| **Audit return** | Final audit lower than deposit | Excess premium returned |
| **Duplicate payment** | Overpayment | Full amount returned |

### Refund Disbursement

| Method | Description |
|--------|-------------|
| **Original payment method** | Refund to card/ACH |
| **Check** | Paper check |
| **Credit balance** | Apply to other open items |
| **Agent credit** | Credit agent account |

---

## 11.3.8 Commissions

### Commission Structure

| Model | Description |
|-------|-------------|
| **Flat percent** | % of written premium |
| **Tiered** | % based on production volume |
| **Contingent** | Extra % based on loss ratio |
| **One-time vs. recurring** | Initial vs. renewal commission |

### Commission Processing

```
Billing Transaction → Commission Calculation → Commission Statement → Payment
```

| Step | Description |
|------|-------------|
| **Commission calculation** | Compute from premium transactions |
| **Aging** | When commission is due |
| **Statement** | Generate agent statement |
| **Payment** | Disburse to agent |
| **1099** | Annual tax reporting |

---

## 11.3.9 Reports

### Billing Reports

| Report | Purpose |
|--------|---------|
| **Aging report** | Open receivables by age |
| **Cash receipts** | Payments received by date |
| **Premium by policy** | Billed premium by policy/LOB |
| **Unearned premium** | Unearned premium reserve |
| **Refund report** | Refunds issued |
| **Commission statement** | Agent commissions |
| **Cancellation report** | Policies cancelled for non-payment |
| **Bank reconciliation** | Payments matched to bank |

---

## Key Takeaways

1. **Billing manages the complete premium life cycle** — invoice, payment, receivables, collections, refunds.
2. **Payment plans** give insureds flexible installment options.
3. **Payment processing** supports ACH, card, check, and EFT with PCI security.
4. **Collections automation** drives notices, late fees, and cancellation workflows.
5. **Refunds** are computed automatically for cancellations and endorsements.
6. **Commissions** are calculated and disbursed to agents and MGAs.

---

**Next:** [11.4 Duck Creek Claims](04-duck-creek-claims.md)