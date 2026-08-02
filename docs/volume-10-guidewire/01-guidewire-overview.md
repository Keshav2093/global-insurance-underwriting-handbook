# 10.1 Guidewire Overview

## What is Guidewire?

**Guidewire** (Guidewire Software, Inc.) is the leading provider of cloud-based software for the **property & casualty (P&C) insurance industry**. Its core products digitize the three central insurance operations:

| Product | Function |
|---|---|
| **PolicyCenter** | Policy administration, underwriting, rating, and issuance |
| **ClaimCenter** | Claims management from notification to settlement |
| **BillingCenter** | Billing, receivables, payments, and collections |

## Why Insurers Choose Guidewire

- **Purpose-built for P&C** — not generic enterprise software
- **Unified platform** — one data model across policy, claim, and billing
- **Configurable** — rules, forms, and workflows adapt without rewriting core code
- **Cloud/SaaS** — Guidewire Cloud reduces infrastructure burden
- **Ecosystem** — Guidewire Marketplace integrates 100+ partner solutions

## Product Suite Overview

### Core systems

| Module | Primary Users | Key Capabilities |
|---|---|---|
| **PolicyCenter** | Underwriters, agents, policy admins | Quoting, new business, renewals, endorsements, cancellations, documents |
| **ClaimCenter** | Claims adjusters, examiners, managers | FNOL, investigation, evaluation, reserves, payments, subrogation |
| **BillingCenter** | Billing analysts, customer service | Invoices, installments, payments, delinquencies, collections, refunds |

### Platform & data layers

| Component | Purpose |
|---|---|
| **Guidewire Cloud** | Hosted infrastructure, environments, security, compliance |
| **Data Platform** | Data warehouse, reporting, analytics (InfoCenter, Analytics) |
| **Integration Framework** | APIs and messaging (policy, claim, billing services) |
| **Configuration Tools** | Rules, forms, workflows, data model editors |

## Guidewire Cloud Architecture

```
Channels (Agent Portal, Customer Portal)
        │
PolicyCenter  ClaimCenter  BillingCenter
        │
Data Platform (InfoCenter, Analytics)
        │
Integration Framework (REST/API, Events)
        │
External Systems (DMS, Rating, Payment)
```

## Implementation Model

| Phase | Activities |
|---|---|
| **Discover** | Current state, requirements, gap analysis |
| **Configure** | Data model, rules, forms, workflows, rating tables |
| **Integrate** | APIs, batch interfaces, portals |
| **Test** | Unit, integration, UAT, performance, regression |
| **Deploy** | Production cutover, data migration, hypercare |
| **Run** | Release management, upgrades, monitoring |

**Key principle:** Guidewire is *configured*, not custom-coded. Configuration (rules, UI, forms) is upgrade-safe; customization (code changes) creates upgrade complexity.

## Configuration vs. Customization

| Aspect | Configuration | Customization |
|---|---|---|
| Examples | Rules, screens, forms, workflows, lookups | Core code modifications |
| Upgrade impact | Low (portable) | High (merge conflicts) |
| Best practice | **Preferred** | Only when unavoidable |

## Common Implementation Roles

| Role | Responsibility |
|---|---|
| **Business Analyst** | Requirements, configuration, UAT support |
| **Configuration Analyst** | Rules, forms, workflows, data model |
| **Integrations Engineer** | API/event wiring, batch jobs |
| **QA/Tester** | Test plans, automation, regression |
| **Actuary/Product Lead** | Rating tables, product definitions |
| **Change Manager** | Training, adoption, communication |

## Key Business Value

- **Policy speed** — quoting in minutes, not days
- **Claims efficiency** — guided workflows, automated tasks
- **Billing accuracy** — automated invoicing, faster cash application
- **Data-driven decisions** — real-time dashboards
- **Regulatory compliance** — audit trails, forms versioning

## Summary

- Guidewire is the market-leading P&C insurance platform.
- Core modules: PolicyCenter, ClaimCenter, BillingCenter.
- Cloud-based, configurable, integration-rich.
- Implementation focuses on configuration, integration, and data migration.

## Related Chapters

- [10.2 PolicyCenter](02-policycenter.md)
- [10.3 ClaimCenter](03-claimcenter.md)
- [10.4 BillingCenter](04-billingcenter.md)
- [Volume 6 Policy Administration](../volume-06-policy-administration/index.md)