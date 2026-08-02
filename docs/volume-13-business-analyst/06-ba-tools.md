# 13.6 — Tools & Techniques

## 13.6.1 Overview

BAs use a toolkit of documentation, process, and analysis techniques. This chapter covers the most important tools and techniques for insurance BAs: BRDs, process maps, data analysis, SQL, use cases, traceability, and workshop facilitation.

---

## 13.6.2 Business Requirements Document (BRD)

### BRD Structure

| Section | Contents |
|---------|----------|
| **Executive summary** | Purpose, scope, success criteria |
| **Background** | Business context and drivers |
| **Objectives** | Measurable goals |
| **Scope** | In scope / out of scope |
| **Stakeholders** | Roles and interests |
| **Current state** | As-is process and pain points |
| **Future state** | Target process |
| **Requirements** | Functional and non-functional |
| **Assumptions & constraints** | Limitations, dependencies |
| **Approvals** | Sign-off record |

### BRD Quality Checks

| Check | Question |
|-------|----------|
| Complete | Are all requirements captured? |
| Testable | Can each requirement be verified? |
| Unambiguous | Is there only one interpretation? |
| Prioritized | Are must/should/could levels set? |
| Traceable | Can requirements be traced to tests? |
| Approved | Has the business signed off? |

---

## 13.6.3 Process Mapping

### Process Mapping Symbols

| Symbol | Meaning |
|--------|---------|
| Oval | Start / end |
| Rectangle | Activity / task |
| Diamond | Decision |
| Parallelogram | Data / document |
| Arrow | Flow direction |

### Swimlane Diagram

A **swimlane (cross-functional) diagram** shows which role performs each step:

```
          ┌──────────────────────────────────────────┐
Agent     │ Submit → Upload → Respond → (End)        │
          ├──────────────────────────────────────────┤
UW        │ (Start) → Initiate → Refer → Approve     │
          ├──────────────────────────────────────────┤
System    │ Validate → Rate → Notify                 │
          └──────────────────────────────────────────┘
```

### Process Mapping Steps

| Step | Activity |
|------|----------|
| 1. Define scope | Start and end points |
| 2. Identify actors | Roles involved |
| 3. Map as-is | Current process |
| 4. Identify pain points | Bottlenecks, errors, waits |
| 5. Design to-be | Target process |
| 6. Validate | Walk through with stakeholders |
| 7. Document | Final process maps |

---

## 13.6.4 Use Cases

### Use Case Components

| Component | Description |
|-----------|-------------|
| **Actor** | Who interacts with system |
| **Precondition** | State before use case |
| **Main flow** | Normal steps |
| **Alternate flow** | Variations |
| **Exception flow** | Error handling |
| **Postcondition** | State after use case |

### Use Case Example — Submit Claim

| Element | Description |
|---------|-------------|
| Actor | Policyholder (web) |
| Precondition | Policy is active |
| Main flow | 1. Log in, 2. Select policy, 3. Enter loss details, 4. Attach photos, 5. Submit |
| Alternate flow | Claimant (no login) files via public form |
| Exception flow | Policy not found — error displayed |
| Postcondition | Claim number assigned, AOR notified |

---

## 13.6.5 Data Analysis with SQL

### When BAs Use SQL

| Use Case | Example |
|----------|---------|
| Validate data | Check ratings applied correctly |
| Impact analysis | Count affected policies |
| Test data | Identify sample data for UAT |
| Reporting | Extract data for analysis |
| Reconciliation | Verify migration counts |
| Ad-hoc queries | Answer stakeholder questions |

### Basic SQL Commands

```sql
SELECT policy_no, premium, effective_date
FROM policy
WHERE effective_date >= '2026-01-01'
  AND line_of_business = 'HOME';
```

| Command | Purpose |
|---------|---------|
| SELECT | Choose columns |
| FROM | Specify table |
| WHERE | Filter rows |
| JOIN | Combine tables |
| GROUP BY | Aggregate |
| ORDER BY | Sort results |

---

## 13.6.6 Gap Analysis

### Gap Analysis Format

| Item | Current State | Required State | Gap | Action |
|------|--------------|----------------|-----|--------|
| New business | Manual entry | Auto-quote | Process gap | Automate |
| Referrals | Email only | In-system queue | Tool gap | Configure |
| Data capture | 20 fields | 45 fields | Data gap | Add fields |
| Reporting | Monthly Excel | Daily dashboard | Reporting gap | Build dashboard |

### Gap Types

| Type | Description |
|------|-------------|
| Process gap | How work is done |
| Tool gap | System capability |
| Data gap | Information availability |
| Skill gap | People capability |
| Compliance gap | Regulatory requirement |

---

## 13.6.7 Traceability Matrix

### Requirements Traceability Matrix (RTM)

| Req ID | Requirement | Source | Design | Build | Test Case | Status |
|--------|-------------|--------|--------|-------|-----------|--------|
| REQ-001 | Auto-assign claim | Stakeholder | ✓ | ✓ | TC-001 | Pass |
| REQ-002 | Referral rule | UW Director | ✓ | ✓ | TC-002 | Pass |
| REQ-003 | Mobile FNOL | Portal owner | ✓ | ✓ | TC-003 | Pending |

### Why RTM Matters

| Benefit | Description |
|---------|-------------|
| Coverage | Every requirement has a test |
| Impact | Change impact is clear |
| Completion | Track build status |
| Audit | Evidence for sign-off |
| Risk | Uncovered requirements identified |

---

## 13.6.8 Facilitation Techniques

### Workshop Types

| Workshop | Purpose |
|----------|---------|
| Requirements workshop | Elicit and agree requirements |
| Fit-gap workshop | Compare system to needs |
| Process design | Design to-be processes |
| Retrospective | Reflect and improve |
| Prioritization | Rank requirements |

### Workshop Best Practices

| Practice | Description |
|----------|-------------|
| Clear agenda | Purpose, outcomes, timing |
| Right people | Decision-makers present |
| Ground rules | Participation, timing |
| Visual capture | Whiteboard, sticky notes |
| Parking lot | Off-topic items captured |
| Actions & owners | Documented next steps |
| Follow-up | Minutes published promptly |

---

## 13.6.9 Decision Trees

### Decision Tree Format

```
Submission
├── Eligibility Pass? ── No → Decline
└── Yes
    ├── Referral Rule? ── Yes → Send to UW
    │                        ├── Approve → Bind
    │                        ├── Condition → Add stipulation
    │                        └── Decline → Decline
    └── No
        ├── Rating Valid? ── No → Error
        └── Yes → Quote → Bind
```

### When to Use Decision Trees

| Use | Example |
|-----|---------|
| Rule documentation | Referral rules |
| Workflow design | Claims triage |
| Test design | Scenario branches |
| Training | Decision guidance |

---

## Key Takeaways

1. **BRDs capture scope and requirements** in a structured, testable format.
2. **Process maps** (swimlanes) clarify roles and flows.
3. **Use cases** describe actor–system interactions.
4. **SQL and Excel** enable data-driven analysis.
5. **Traceability matrices** ensure requirements are tested.
6. **Facilitation and decision trees** support collaborative, clear analysis.

---

**Back to:** [Volume 13 Index](index.md)