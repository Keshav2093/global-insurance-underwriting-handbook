# 10.2 PolicyCenter

## What is PolicyCenter?

**PolicyCenter** is Guidewire's policy administration system. It manages the full policy lifecycle — from quote through issuance, endorsements, renewals, and cancellation — with configurable underwriting, rating, forms, and document generation.

## Core Capabilities

| Capability | Description |
|---|---|
| **Quoting** | New business, quote comparison, multi-location |
| **Policy Lifecycle** | NB, renewals, endorsements, cancellations, reinstatements |
| **Underwriting** | Workflows, approval rules, underwriter workbench |
| **Rating** | Rate tables, rating steps, pricing analysis |
| **Forms** | Automated form selection, versioning, state compliance |
| **Documents** | Policy documents, binders, certificates, dec pages |
| **Submissions** | Broker/agent submissions, data capture, status tracking |

## Policy Lifecycle in PolicyCenter

```
Quote → Bind → Issue → Serve → Renew
        │       │      │       │
      (NB)   (Docs)  (Changes) (REN)
```

| Stage | Activities |
|---|---|
| **Submission** | Agent enters application; system validates data |
| **Quote** | Rating engine produces premium; UW reviews |
| **Bind** | Coverage confirmed; binder issued |
| **Issue** | Policies, dec pages, and forms generated |
| **Servicing** | Endorsements, billing changes, cancellations |
| **Renewal** | Renewal offer, re-rating, re-underwriting |

## Underwriting in PolicyCenter

### Underwriter Workbench

- Work queue of submissions requiring review
- Application data, loss history, credit, MVRs (if configured)
- Quote analysis showing rating impact of changes
- Activity notes, diary items, and referral tracking
- Decision capture: accept, refer, decline, quote with conditions

### Approval Rules

| Rule Type | Example |
|---|---|
| **Auto-accept** | Low-risk residential under threshold |
| **Auto-decline** | Felony arson history |
| **Referral** | Premium over authority limit |
| **Conditional** | Accept if sprinkler installed |

## Rating in PolicyCenter

### Rating Engine Features

- **Rating tables** — rates, factors, loss costs, expense provisions
- **Rating steps** — sequence of calculation steps
- **Rating worksheet** — shows every step of the premium build-up
- **Rating factors** — territory, class, limits, deductibles, coverage options
- **Override handling** — UW overrides with audit trail

### Rating Steps Example (Commercial Property)

```
1. Base rate ($ per $100 TIV)
2. Construction factor
3. Protection class factor
4. Occupancy factor
5. Limit-of-insurance factor
6. Deductible credit
7. Loss control credit
8. Expenses + profit load
9. Final premium
```

## Forms Management

| Feature | Purpose |
|---|---|
| **Automatic form selection** | Based on state, line, and product |
| **Form versioning** | Track approved versions over time |
| **Form inference** | Forms added automatically by data values |
| **Form suppression** | Remove irrelevant forms |
| **State compliance** | Match statutory forms to state |

## Integrations

| Integration | Typical System |
|---|---|
| **Rating** | External rate engines, ISO/AAIS data feeds |
| **MVR/CLUE** | Motor vehicle records, loss history |
| **Credit** | Insurance credit scoring |
| **Geography** | Flood zones, fire protection class |
| **Producers** | Agent portals, comparative raters |
| **Billing** | BillingCenter integration for invoicing |
| **Claims** | ClaimCenter integration for policy lookups |

## Configuration Key Concepts

| Concept | Description |
|---|---|
| **Product Model** | Coverage, risk, and policy entities |
| **Data Model** | Extendable entities and fields |
| **Rules** | Validation, rating, and workflow rules |
| **Workflows** | Approval routing, activities, tasks |
| **UI** | Screens, tabs, and widgets |
| **Lookups** | Dropdown values and reference data |

## User Roles

| Role | Access |
|---|---|
| **Agent/Broker** | Submit applications, view quotes, issue (if authorized) |
| **Underwriter** | Review submissions, set conditions, quote decisions |
| **Policy Admin** | Issue, endorse, cancel, renew |
| **Manager** | Work queues, audits, monitoring |
| **Actuary/Product** | Rate tables, product definitions, forms |

## Summary

- PolicyCenter manages the entire policy lifecycle.
- Underwriting workbench centralizes decisions and referrals.
- Rating engine is table-driven with full audit trails.
- Forms automation ensures compliance and accuracy.
- Configuration (rules, forms, UI) drives most business change.

## Related Chapters

- [10.1 Guidewire Overview](01-guidewire-overview.md)
- [10.3 ClaimCenter](03-claimcenter.md)
- [10.4 BillingCenter](04-billingcenter.md)
- [Volume 4 Underwriting](../volume-04-underwriting/index.md)
- [Volume 6 Policy Administration](../volume-06-policy-administration/index.md)