# 11.4 — Duck Creek Claims

## 11.4.1 Overview

**Duck Creek Claims** manages the end-to-end claims lifecycle: first notice of loss (FNOL), investigation, coverage analysis, reserving, settlement, recovery (subrogation), and closure. It is designed to deliver fast, consistent, and defensible claim outcomes with embedded workflow, automation, and analytics.

### Core Capabilities

| Capability | Description |
|-----------|-------------|
| **FNOL** | Multi-channel intake: phone, web, mobile, agent, API |
| **Claim setup** | Structure claim into exposures, parties, involvement |
| **Coverage evaluation** | Validate coverage against policy |
| **Investigation** | Tasks, assignments, document collection |
| **Reserving** | Set and adjust reserves with authority limits |
| **Settlement** | Negotiate, approve, pay |
| **Litigation management** | Counsel assignment, expense tracking |
| **Subrogation** | Recovery identification and pursuit |
| **Salvage** | Salvage and SIU handling |
| **SIU / Fraud** | Fraud referral, investigation |
| **Adjuster mobile** | Field work, photo capture, inspection |
| **Reports** | Regulatory (ISO, state), management, performance |

---

## 11.4.2 Claims Lifecycle

### Claim Flow

```
FNOL → Claim Setup → Coverage Verification → Investigation → Evaluation & Reserving → Settlement → Payment → Subrogation → Closure
```

| Stage | Description |
|-------|-------------|
| **FNOL** | Report loss, capture first information |
| **Setup** | Create claim structure, assign adjuster |
| **Coverage verification** | Confirm coverage, limits, exclusions |
| **Investigation** | Gather facts, statements, reports, photos |
| **Evaluation** | Determine liability, damages, reserve |
| **Settlement** | Negotiate and settle within authority |
| **Payment** | Disburse payment to insured/third party |
| **Subrogation** | Recover from responsible party |
| **Closure** | Final review, archive, regulatory filing |

---

## 11.4.3 FNOL (First Notice of Loss)

### FNOL Channels

| Channel | Description |
|---------|-------------|
| **Phone** | Call center enters claim |
| **Web portal** | Policyholder self-service FNOL |
| **Mobile app** | Photo capture, GPS, claim filing |
| **Agent** | Agent files on behalf of insured |
| **API** | Partner or third-party filing |
| **Email** | Digital submission |

### FNOL Data Capture

| Category | Data |
|----------|------|
| **Policy** | Policy number, coverage, effective dates |
| **Insured** | Name, contact, relationship |
| **Loss** | Date, time, location, description |
| **Cause** | Cause of loss (fire, theft, collision, liability) |
| **Parties** | Claimant, witnesses, third parties |
| **Vehicle** | Vehicle involved, damage |
| **Property** | Property damaged, extent |
| **Injuries** | Injured party, extent of injury |
| **Report** | Police report, medical treatment |

### FNOL Automation

| Automation | Description |
|-----------|-------------|
| **Policy auto-verify** | Verify coverage automatically against policy |
| **Claim number auto-assign** | Instant claim number generation |
| **Adjuster auto-assign** | Route by territory, line, complexity |
| **Initial reserve delay** | Set initial reserve based on rules |
| **SIU referral** | Auto-refer suspected fraud |
| **Duplicate detection** | Check for duplicate claims |

---

## 11.4.4 Claims Structure

### Claim Components

| Component | Description |
|-----------|-------------|
| **Claim** | The overall occurrence/loss file |
| **Exposure** | Each distinct coverage/claimant combination |
| **Parties** | All involved parties with roles |
| **Involvements** | How each party relates to claim |
| **Reserves** | Case reserves with type (reported, expected) |
| **Transactions** | Payments, recoveries, expenses |
| **Activities** | Tasks, notes, assignments |
| **Documents** | Photos, reports, correspondence |

### Exposure Structure

Each exposure represents a claim against a specific coverage:

| Field | Example |
|-------|---------|
| Coverage | BI, PD, Medical Payments, Collision |
| Claimant | Third party, insured |
| Loss type | Liability, property damage |
| Cause | Rear-end collision |
| Reserve | $25,000 |
| Status | Open/Closed |
| Assignee | Adjuster |
| Litigation | In litigation, counsel |

---

## 11.4.5 Investigation

### Investigation Activities

| Activity | Description |
|----------|-------------|
| **Statement** | Insured, witness, claimant statements |
| **Police report** | Obtain and review |
| **Photos** | Damage photos, scene photos |
| **Medical records** | Obtain and review treatment records |
| **Expert inspection** | Engineer, appraiser, medical expert |
| **Background search** | Claim history, social media |
| **Subrogation evaluation** | Is another party liable? |
| **SIU review** | Fraud indicators investigation |

### Investigation Tools

| Tool | Purpose |
|------|---------|
| **ISO ClaimSearch** | Claims history check |
| **Credit investigation** | Background information |
| **Social network search** | Public information |
| **Field app** | On-site inspection data |
| **Scheduling** | Expert appointment scheduling |
| **Litigation tracking** | Case status, deadlines |

---

## 11.4.6 Coverage Evaluation

### Coverage Analysis Steps

| Step | Description |
|------|-------------|
| **Policy lookup** | Retrieve policy from Duck Creek Author |
| **Coverage confirmation** | Confirm coverage in effect at loss date |
| **Limit review** | Per-occurrence, aggregate limits |
| **Deductible application** | Apply deductible |
| **Exclusion review** | Identify applicable exclusions |
| **Conditions review** | Duty to cooperate, notice, etc. |
| **Coverage opinion** | Formal documented decision |

### Coverage Decisions

| Decision | Description |
|----------|-------------|
| **Accepted** | Coverage applies |
| **Denied** | Coverage excluded or not applicable |
| **Reserved** | Coverage disputed, rights reserved |
| **Partial** | Part of claim covered |
| **Conditional** | Coverage subject to conditions |

---

## 11.4.7 Reserving

### Reserve Types

| Reserve | Description |
|---------|-------------|
| **Case reserve** | Estimate for a specific claim |
| **Reported reserve** | Indemnity cost estimate |
| **Expected reserve** | Total expected including IBNR |
| **Liability reserve** | For BI/PD liability |
| **Expense reserve** | Defense cost, investigation expense |
| **Recovery reserve** | Expected subrogation/salvage |

### Reserve Setting

| Factor | Consideration |
|--------|---------------|
| Injury severity | Medical treatment, permanency |
| Liability determination | Fault percentage |
| Property damage | Repair/replacement cost |
| Litigation potential | Defense costs |
| Policy limits | Reserve cannot exceed limits |
| Comps | Similar claim settlements |
| Authority | Adjuster authority level |

### Reserve Authority Matrix

| Authority Level | Authority Limit |
|-----------------|-----------------|
| **Adjuster** | Up to $10,000 |
| **Senior Adjuster** | $10,000 – $50,000 |
| **Claim Supervisor** | $50,000 – $250,000 |
| **Claim Manager** | $250,000 – $1,000,000 |
| **Home Office** | Over $1,000,000 |

---

## 11.4.8 Settlement and Payment

### Settlement Methods

| Method | Description |
|--------|-------------|
| **Negotiation** | Direct settlement with claimant |
| **Mediation** | Facilitated settlement |
| **Arbitration** | Binding/non-binding decision |
| **Litigation** | Court judgment |
| **Structured settlement** | Periodic payments |

### Payment Types

| Payment | Description |
|---------|-------------|
| **Claimant payment** | Indemnity payment to insured/third party |
| **Medical payment** | Medical bills paid |
| **Property payment** | Repair/replacement payment |
| **Expense payment** | Investigation, expert, legal expense |
| **Advance** | Partial payment before settlement |
| **Loss of use** | Additional living expense |

### Payment Approval Workflow

```
Proposed Payment → Authority Check → Approval → Disbursement → Reconciliation
```

---

## 11.4.9 Subrogation and Recoveries

### Subrogation Process

| Step | Description |
|------|-------------|
| **Identify** | Identify responsible third party |
| **Evaluate** | Liability and collectability |
| **Pursue** | Demand, negotiation, litigation |
| **Recover** | Receive payment |
| **Distribute** | Allocate to claim and policyholder (deductible recovery) |

### Recovery Allocation

| Allocation | Description |
|------------|-------------|
| **Indemnity reimbursement** | Recover indemnity paid |
| **Expense reimbursement** | Recover investigation/litigation costs |
| **Deductible recovery** | Return policyholder deductible |
| **Billing fees** | Attorney contingency |

---

## 11.4.10 Fraud and SIU

### Red Flags

| Indicator | Description |
|-----------|-------------|
| **Late reporting** | Claim reported long after loss |
| **Inconsistent statements** | Version changes between parties |
| **Excessive damages** | Damage exceeds loss plausibility |
| **Staged accident** | Multiple claims same parties |
| **Recent coverage** | Coverage added just before loss |
| **Prior suspicious claims** | History of questionable claims |
| **No witnesses** | No third-party confirmation |

### SIU Referral

```
Suspicion → SIU Referral → Investigation → Finding → Ruling
```

| Finding | Action |
|---------|--------|
| **No fraud** | Release claim to adjuster |
| **Suspected fraud** | Continue SIU investigation |
| **Fraud confirmed** | Deny claim, report to authorities |

---

## 11.4.11 Regulatory Compliance

| Requirement | Description |
|-------------|-------------|
| **ISO filings** | Claim data reported to ISO |
| **State filings** | Required claim reports to state |
| **Privacy** | Data privacy compliance |
| **Record retention** | Claim file retention requirements |
| **Bad faith prevention** | Timely, fair claims handling |
| **Adjuster licensing** | Track adjuster licenses |

---

## 11.4.12 Claims Reporting

| Report | Purpose |
|--------|---------|
| **Open claim report** | Current open exposure |
| **Reserve report** | Case reserve adequacy |
| **Loss run** | Claim history for underwriting |
| **Payment report** | Payments by type, adjuster |
| **Severity report** | Average claim severity |
| **Frequency report** | Claim frequency by LOB |
| **Cycle time report** | FNOL to closure time |
| **Regulatory report** | ISO/state filings |

---

## Key Takeaways

1. **Claims manages the full lifecycle** from FNOL to closure.
2. **FNOL automation** speeds intake and assignment.
3. **Coverage evaluation** is documented and defensible.
4. **Reserving follows authority levels** with clear oversight.
5. **Payments and settlements** flow through approval workflows.
6. **Subrogation** recovers costs and returns deductibles to policyholders.
7. **SIU and regulatory compliance** are built into the workflow.

---

**Next:** [11.5 Duck Creek Insight](05-duck-creek-insight.md)