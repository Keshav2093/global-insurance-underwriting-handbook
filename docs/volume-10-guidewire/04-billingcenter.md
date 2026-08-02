# 10.4 — BillingCenter

## 10.4.1 Overview

**BillingCenter** is Guidewire's billing and receivables application. It manages the complete premium lifecycle — from invoice generation through payment processing, receivables management, collections, and agent commissions.

### Core Capabilities

| Capability | Description |
|-----------|-------------|
| **Invoice generation** | Automatic invoicing from policy transactions |
| **Payment plans** | Annual, semi-annual, quarterly, monthly |
| **Payment processing** | ACH, credit card, check, EFT |
| **Receivables** | Open items, aging, dunning |
| **Collections** | Notices, late fees, cancellation for non-payment |
| **Refunds** | Return premiums, refunds, credits |
| **Commissions** | Agent commissions and statements |
| **Multi-entity** | Multiple companies, currencies, taxes |
| **Reports** | Aging, cash receipts, unearned premium |

---

## 10.4.2 Billing Lifecycle

### Premium Flow

```
Policy → Transaction → Invoice → Payment Plan → Billing → Payment → Reconciliation → Archive
```

### Billing Events

| Event | Billing Impact |
|-------|---------------|
| **New business** | Create billing account, payment plan, invoice |
| **Endorsement** | Additional or return premium |
| **Renewal** | Renewal invoice generation |
| **Cancellation** | Return premium and credit |
| **Reinstatement** | Reinstate policy and payment plan |
| **Audit** | Workers comp final premium |
| **Commission** | Calculate and disburse agent commission |

---

## 10.4.3 Payment Plans

### Plan Configuration

| Component | Description |
|-----------|-------------|
| **Plan type** | Annual, semi-annual, quarterly, monthly |
| **Installments** | Number and frequency of payments |
| **Down payment** | Percentage or amount due first |
| **Fees** | Installment or service fees |
| **Due dates** | Scheduled from policy effective date |
| **Billing method** | Direct bill, agency bill, list bill |
| **Auto-pay** | Automatic payment on due date |

### Billing Methods

| Method | Description |
|--------|-------------|
| **Direct bill** | Insurer bills the policyholder directly |
| **Agency bill** | Agent collects premium and remits to insurer |
| **List bill** | Summary billing for large accounts |
| **Payroll deduction** | Premium deducted from payroll |

---

## 10.4.4 Payment Processing

### Payment Methods

| Method | Description | Recurring |
|--------|-------------|-----------|
| **ACH** | Automated clearing house bank transfer | Yes |
| **Credit/debit card** | Card on file, tokenized | Yes |
| **Check** | Paper, lockbox | No |
| **EFT** | Electronic funds transfer | Yes |
| **Money order** | Paper instrument | No |

### Payment Flow

```
Invoice Due → Payment Initiation → Gateway → Authorization → Posting → Reconciliation
```

| Step | Description |
|------|-------------|
| **Initiation** | Auto-draft or manual entry |
| **Gateway** | External payment processor |
| **Authorization** | Verify funds / card |
| **Posting** | Apply to open items |
| **Reconciliation** | Match to bank statement |

---

## 10.4.5 Receivables and Collections

### Aging Buckets

| Bucket | Description |
|--------|-------------|
| **Current** | Not yet due |
| **1–30** | First notice |
| **31–60** | Second notice |
| **61–90** | Final notice |
| **90+** | Cancellation stage |

### Collection Workflow

```
Invoiced → Past Due → Notices → Late Fee → Cancellation → Reinstatement / Write-Off
```

| Stage | Action |
|-------|--------|
| **Past due** | Aging begins at due date |
| **Notice 1** | Friendly reminder |
| **Notice 2** | Formal demand |
| **Final notice** | Cancellation warning |
| **Cancellation** | Cancel for non-payment |
| **Reinstatement** | Payment restores policy |
| **Write-off** | Uncollectible balance after approval |

---

## 10.4.6 Refunds and Return Premiums

| Refund Type | Calculation |
|-------------|-------------|
| **Pro-rata** | Unearned premium proportionally |
| **Short-rate** | Unearned premium less penalty |
| **Endorsement** | Premium difference from change |
| **Audit refund** | Excess premium from audit |
| **Overpayment** | Duplicate or excess payment |

---

## 10.4.7 Commissions

| Model | Description |
|-------|-------------|
| **Flat percent** | % of premium |
| **Tiered** | % based on volume |
| **Contingent** | Performance-based |
| **Recurring** | Renewal commissions |

---

## 10.4.8 Reports

| Report | Purpose |
|--------|---------|
| **Aging report** | Open receivables by age |
| **Cash receipts** | Payments by date/method |
| **Premium by policy** | Billed premium detail |
| **Unearned premium** | UPR reserve |
| **Cancellation report** | Non-payment cancellations |
| **Commission report** | Agent commissions |
| **Bank reconciliation** | Matching to bank |

---

## Key Takeaways

1. **BillingCenter** manages the complete premium lifecycle.
2. **Payment plans** offer flexible installment options.
3. **Multiple payment methods** are supported with PCI security.
4. **Collections automation** handles notices, fees, and cancellations.
5. **Refunds** compute automatically for cancellations and endorsements.
6. **Commissions** are calculated and reported for agents.

---

**Next:** [10.5 Guidewire Data Platform](05-data-platform.md)