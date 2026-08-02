# 13.5 — BA in Technology Projects

## 13.5.1 Overview

BAs are central to technology projects in insurance — from core system implementations (policy, billing, claims) to integrations, portals, data platforms, and automation. This chapter covers how BAs work across the technology project lifecycle.

---

## 13.5.2 Types of Technology Projects

| Project Type | Example |
|--------------|---------|
| **Core system implementation** | Duck Creek, Guidewire, Majesco rollout |
| **System upgrade** | Platform upgrade or migration |
| **Integration** | Portal, MVR, payment, document integration |
| **New channel** | Agent portal, customer portal, mobile app |
| **Data platform** | Data warehouse, dashboards, AI/ML |
| **Automation** | RPA, workflow automation |
| **Legacy modernization** | Replace legacy policy admin |
| **Cloud migration** | Move systems to cloud |

---

## 13.5.3 Core System Implementation

### BA Role in Core System Projects

| Phase | BA Activities |
|-------|---------------|
| **Discovery** | Current state, target state, scope |
| **Requirements** | Elicit and document business requirements |
| **Fit-gap** | Map requirements to system features |
| **Configuration support** | Review config, clarify requirements |
| **Integration support** | Define data flows and interfaces |
| **Testing** | Test scenarios, UAT facilitation |
| **Migration** | Data requirements, validation |
| **Deployment** | Training, go-live support |
| **Hypercare** | Issue triage, enhancements |

### Fit-Gap Analysis

| Requirement | System Feature | Fit | Gap | Action |
|-------------|---------------|-----|-----|--------|
| New business quote | Submission module | ✔ | — | Configure |
| Complex referral rules | Rules engine | — | Partial | Customize rule |
| Scheduled payments | Billing plans | ✔ | — | Configure |
| Mobile FNOL | Digital channel | — | Gap | Build portal |

---

## 13.5.4 Requirements Management

### Requirements Types

| Type | Description |
|------|-------------|
| **Business requirement** | What the business needs (why) |
| **Functional requirement** | What the system must do (what) |
| **Non-functional requirement** | Performance, security, availability |
| **Data requirement** | Fields, formats, sources |
| **Integration requirement** | Interfaces and data flows |
| **Regulatory requirement** | Compliance constraints |
| **Transition requirement** | Migration and go-live needs |

### Non-Functional Requirements

| Category | Examples |
|----------|----------|
| **Performance** | Response times, batch windows |
| **Availability** | 99.9% uptime, DR recovery |
| **Capacity** | Concurrent users, transaction volume |
| **Security** | Access control, encryption |
| **Integrations** | API throughput, latency |
| **Compliance** | Data retention, privacy |
| **Usability** | Training time, ease of use |
| **Scalability** | Growth capacity |

### Requirements Quality

| Quality | Description |
|---------|-------------|
| **Testable** | Can be verified |
| **Unambiguous** | Single meaning |
| **Complete** | All conditions stated |
| **Traceable** | Linked to source and tests |
| **Prioritized** | Must/Should/Could |
| **Consistent** | No contradictions |
| **Feasible** | Achievable within constraints |

---

## 13.5.5 User Stories

### User Story Format

```
As a [role],
I want [feature],
So that [benefit].
```

### Acceptance Criteria (Given/When/Then)

```
GIVEN a policyholder with a $1M home
WHEN a quote is requested
THEN the submission is referred to a senior underwriter
```

### Epics → Stories Breakdown

| Epic | Stories |
|------|---------|
| New business | Submit quote, validate risk, rate, bind |
| Endorsements | Change address, add vehicle, cancel policy |
| Renewals | Generate renewal, offer, accept, non-renew |

---

## 13.5.6 Vendor Management

### BA Coordination with Vendors

| Activity | BA Role |
|----------|---------|
| **RFP support** | Requirements, scoring criteria |
| **Vendor selection** | Evaluate fit-gap results |
| **Statement of Work** | Scope validation |
| **Requirements handoff** | Provide BRDs and specs |
| **Fit-gap facilitation** | Joint workshops |
| **Change requests** | Assess and approve changes |
| **Defect management** | Triage and validate defects |
| **Acceptance** | Support UAT and sign-off |

---

## 13.5.7 UAT (User Acceptance Testing)

### UAT Plan

| Element | Description |
|---------|-------------|
| Scope | What is tested |
| Testers | Business users, roles |
| Scenarios | End-to-end business flows |
| Environment | UAT environment, data |
| Entry criteria | Ready to start |
| Exit criteria | Sign-off achieved |
| Schedule | Timeline and sessions |
| Defect process | How defects are raised |

### UAT Scenarios by Area

| Area | Scenario |
|------|----------|
| Underwriting | Submit, refer, approve, bind |
| Policy | Issue, endorse, renew, cancel |
| Billing | Invoice, pay, refund, collections |
| Claims | FNOL, investigate, reserve, pay |
| Portal | Submit claim online, view policy |
| Reporting | Run and validate reports |

### UAT Support Activities

| Activity | Description |
|----------|-------------|
| Scenario preparation | Reusable business scenarios |
| Test data | Create realistic test data |
| Defect triage | Classify severity and priority |
| Retesting | Validate fixes |
| Sign-off documentation | Approval evidence |
| Lessons learned | Capture improvements |

---

## 13.5.8 Agile BA in Technology

### BA in Agile

| Ceremony | BA Contribution |
|----------|-----------------|
| Backlog refinement | Story creation, acceptance criteria |
| Sprint planning | Prioritization, scope |
| Daily standup | Answer questions |
| Sprint review | Validate delivered features |
| Retrospective | Process improvement |

### Agile BA Best Practices

| Practice | Description |
|----------|-------------|
| **Just-in-time detail** | Elaborate stories as they approach |
| **Business value focus** | Prioritize by value |
| **Short feedback loops** | Demo and validate frequently |
| **Collaborative workshops** | Co-create requirements |
| **Definition of Ready** | Stories ready for sprint |
| **Definition of Done** | Complete and accepted |

---

## Key Takeaways

1. **Technology projects** range from core implementations to integrations and portals.
2. **Fit-gap analysis** maps requirements to system features.
3. **Requirements must be testable, traceable, and prioritized**.
4. **User stories** with acceptance criteria drive agile delivery.
5. **Vendor coordination** is a core BA responsibility.
6. **UAT** validates delivery against business expectations.

---

**Next:** [13.6 Tools & Techniques](06-ba-tools.md)