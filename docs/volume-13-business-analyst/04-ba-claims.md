# 13.4 — BA in Claims

## 13.4.1 The BA's Role in Claims

BAs support claims organizations through:

1. **Claims system projects** — FNOL changes, reserving workflows, payment automation.
2. **Process improvement** — claims handling efficiency, compliance, customer experience.
3. **Data analysis** — cycle times, reserve adequacy, claim outcomes, SIU referrals.

---

## 13.4.2 Understanding the Claims Process

### Claims Lifecycle

```
FNOL → Claim Setup → Coverage Verification → Investigation → Evaluation & Reserving → Settlement → Payment → Subrogation → Closure
```

### Key Claims Concepts for BAs

| Concept | Description |
|---------|-------------|
| **FNOL** | First notice of loss — initial report |
| **Exposure** | Each coverage/claimant combination |
| **Coverage determination** | Was the loss covered? |
| **Reserve** | Estimate of ultimate claim cost |
| **Authority** | Approval limit by role |
| **Litigation** | Legal defense and management |
| **Subrogation** | Recovery from responsible party |
| **Salvage** | Value recovered from damaged property |
| **SIU** | Special Investigations Unit for fraud |
| **Cycle time** | Time from FNOL to closure |

---

## 13.4.3 Typical Claims Projects

| Project Type | Example |
|--------------|---------|
| **FNOL channel** | Launch mobile app FNOL |
| **Claim triage** | Implement assignment rules |
| **Reserve guidance** | Configure reserve recommendations |
| **Payment workflow** | Automate small-loss payments |
| **Litigation tracking** | Enhance counsel management |
| **Subrogation** | Improve recovery workflows |
| **SIU referral** | Implement fraud referral rules |
| **Regulatory** | Implement new compliance requirements |
| **Reporting** | Build claims dashboards |

---

## 13.4.4 Requirements for FNOL Systems

### FNOL Requirements Consideration

| Requirement Area | Details to Capture |
|------------------|--------------------|
| **Channels** | Phone, web, mobile, agent, API |
| **Data capture** | Fields needed at intake |
| **Validation** | Required fields, data rules |
| **Policy verification** | Auto-check against policy data |
| **Claim number** | Auto-assignment rules |
| **Assignments** | Adjuster routing rules |
| **Initial reserve** | Rules for initial reserve |
| **SIU referral** | Fraud indicator rules |
| **Notice requirements** | Statutory notice rules |
| **Duplicate detection** | Check for duplicate claims |

### FNOL Data Capture Requirements

| Category | Fields |
|----------|--------|
| Policy | Policy number, coverage, dates |
| Insured | Name, contact, relationship |
| Loss | Date, time, location, description |
| Cause | Cause of loss |
| Parties | Claimant, witnesses |
| Property | Damage description |
| Injuries | Injury details |
| Report | Police report, medical |

---

## 13.4.5 Reserving Requirements

### Reserve Setting Logic

| Factor | Consideration |
|--------|---------------|
| Injury severity | Medical, permanency |
| Liability | Fault determination |
| Damage | Repair/replacement costs |
| Litigation | Defense costs |
| Policy limits | Cannot exceed limits |
| Similar claims | Comparable settlements |

### Authority Matrix Requirements

| Level | Authority | Expense Authority |
|-------|-----------|------------------|
| Adjuster | $10,000 | $2,500 |
| Senior adjuster | $50,000 | $10,000 |
| Supervisor | $250,000 | $25,000 |
| Manager | $1,000,000 | $100,000 |
| Home office | Over $1M | Over $100k |

### Reserve Requirements to Document

| Requirement | Description |
|-------------|-------------|
| Reserve types | Indemnity, expense, recovery |
| Reserve timing | When to set reserve |
| Review triggers | When to review/re-adjust |
| Authority limits | Who can set what |
| Approval workflow | Escalation for large reserves |
| Documentation | Reserve rationale required |

---

## 13.4.6 Claims Payment Requirements

### Payment Workflow

```
Payment Proposal → Authority Check → Approval → Disbursement → Reconciliation
```

### Payment Types

| Payment | Example |
|---------|---------|
| Claimant payment | Indemnity to insured/third party |
| Medical | Medical bills |
| Property | Repair/replacement |
| Expense | Expert, investigation, legal |
| Advance | Partial payment |
| Loss of use | Additional living expenses |

### Payment Requirement Areas

| Requirement | Details |
|-------------|---------|
| Approval limits | Authority matrix |
| Payee validation | Validate payee details |
| Payment modes | ACH, check, card |
| Tax reporting | 1099 requirements |
| Deductible handling | Apply policy deductible |
| Subrogation | Track for later recovery |
| Audit trail | Complete payment history |

---

## 13.4.7 Claims Data Analysis

### Common Claims Analyses

| Analysis | Purpose |
|----------|---------|
| **Cycle time** | FNOL to first contact, to payment, to closure |
| **Reserve adequacy** | Initial vs. ultimate reserve |
| **Severity trends** | Average payment by type |
| **Frequency trends** | Claims per 100 policies |
| **SIU outcomes** | Referral to confirmed fraud |
| **Subrogation recovery** | % of potential recovered |
| **Reopen rate** | Claims closed then reopened |
| **Customer satisfaction** | Claims survey results |
| **Litigation rate** | % of claims in litigation |

### Sample: Cycle Time Dashboard

| Metric | Target | Actual |
|--------|--------|--------|
| FNOL to contact | ≤ 24 hrs | 18 hrs |
| FNOL to assignment | ≤ 4 hrs | 3.2 hrs |
| Contact to investigation | ≤ 48 hrs | 36 hrs |
| Investigation to decision | ≤ 30 days | 26 days |
| Decision to payment | ≤ 5 days | 3.8 days |
| FNOL to closure | ≤ 60 days | 52 days |

---

## 13.4.8 Claims Compliance

### Regulatory Requirements BAs Support

| Requirement | Description |
|-------------|-------------|
| **Timely claim handling** | Statutory deadlines per state |
| **Unfair claims practices** | Fair settlement regulations |
| **Notice requirements** | When insurer must respond |
| **Privacy** | Handling of claimant personal data |
| **Record retention** | Claims file retention periods |
| **Bad faith prevention** | Good-faith handling standards |
| **ISO reporting** | Claim data submissions |
| **Adjuster licensing** | Licenses for adjusters |

---

## Key Takeaways

1. **BAs support claims** through system projects, process improvement, and data analysis.
2. **Understand the full claims lifecycle** — FNOL through closure.
3. **FNOL requirements** determine intake channels, data, and routing.
4. **Reserve and payment requirements** follow authority matrices.
5. **Claims analytics** track cycle time, reserve adequacy, and outcomes.
6. **Compliance** is core — deadlines, privacy, and fair handling.

---

**Next:** [13.5 BA in Technology Projects](05-ba-technology.md)