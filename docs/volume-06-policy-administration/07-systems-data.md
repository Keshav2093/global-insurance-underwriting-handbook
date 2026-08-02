# 6.7 Policy Systems & Data

## Overview

Policy administration runs on **systems that store policy data, generate documents, manage billing, and integrate with underwriting, claims, and finance**. Data quality and system controls determine the reliability of the entire insurance operation.

## The Policy Administration System (PAS)

| Function | Description |
|---|---|
| **Policy master** | Core record: insured, coverages, limits, premium |
| **Rating engine** | Calculates premium from rate tables/models |
| **Document generation** | Produces dec pages, forms, endorsements |
| **Billing module** | Generates invoices, tracks payments |
| **Workflow** | Routes tasks (referrals, audits, renewals) |
| **Claims interface** | Policy data for claim setup |
| **Reporting** | Portfolio, regulatory, management reports |
| **Integration** | Underwriting, claims, finance, analytics systems |

## Core Policy Data Model

| Entity | Key Fields |
|---|---|
| **Policy** | Number, period, status, insurer, producer |
| **Insured** | Legal entity, addresses, contacts |
| **Coverages** | Code, limits, deductibles, premiums |
| **Exposures** | Locations, vehicles, payroll, values |
| **Forms** | Policy forms and endorsements |
| **Transactions** | Issuance, endorsements, renewals, cancellations |
| **Premium** | Charges, payments, balances, adjustments |
| **Documents** | Generated and filed versions |

## Data Quality

| Dimension | Risk of Poor Data |
|---|---|
| **Accuracy** | Wrong coverage, premium, or address |
| **Completeness** | Missing exposures or forms |
| **Consistency** | Conflicting definitions across systems |
| **Timeliness** | Stale policy, billing, or claims data |
| **Uniqueness** | Duplicate policies or customers |

### Data Quality Controls

- **Validation rules** at entry (required fields, ranges).
- **Referential integrity** across policy/billing/claims.
- **Duplicate detection** for customers and policies.
- **Reconciliation** between systems (premium, coverage, status).
- **Monitoring** dashboards for error rates and aging.

## Reference Data

| Reference | Example |
|---|---|
| **Rate tables** | Class, territory, factor values |
| **Forms library** | Approved form editions |
| **Class codes** | WC, GL, NAICS/SIC |
| **Area codes** | Territory definitions |
| **Producer codes** | Agency, license, commission |

Reference data must be **versioned and governed** — a change to a rate table affects all future quotes.

## System Interfaces

| Interface | Purpose |
|---|---|
| **Underwriting workbench** | Referrals, decisions, documents |
| **Claims system** | Policy lookup, coverage verification |
| **Finance/GL** | Premium and payments postings |
| **Reinsurance** | Ceded premium/loss reporting |
| **Regulatory reporting** | Data calls, statutory returns |
| **Producer portal** | Quotes, binding, servicing |

## Technology Considerations

| Topic | Consideration |
|---|---|
| **Legacy systems** | Older PAS; data migration risk |
| **Cloud platforms** | Scalability, availability, security |
| **APIs** | Real-time integration with external data |
| **Automation (RPA)** | Document handling, data entry |
| **Security** | Access controls, data protection (GLBA/GDPR) |

## Reconciliation and Control

| Control | Purpose |
|---|---|
| **Policy count reconciliation** | System vs. issued documents |
| **Premium reconciliation** | Billing vs. ledger |
| **Transaction audit trail** | Every change logged |
| **Cut-off controls** | Period-end processing integrity |
| **Suspense accounts** | Unmatched payments cleared |

## Common System Issues

| Issue | Impact |
|---|---|
| Duplicate policy | Double coverage and premium |
| Stale forms | Wrong coverage at claim |
| Untracked endorsements | Missing documents |
| Broken integration | Claims without policy data |
| Data silos | Inconsistent customer view |
| Uncontrolled rate change | Pricing errors |

## Summary

- The **PAS** is the operational heart of policy administration.
- **Data quality and reference data governance** protect correctness.
- **Interfaces** connect underwriting, claims, finance, and regulation.
- **Controls and reconciliation** keep systems in balance.
- Poor data creates **coverage, premium, and compliance** risk.

## Related Chapters

- [4.8 Automation & Data in Underwriting](../volume-04-underwriting/08-underwriting-automation.md)
- [6.1 Policy Lifecycle](01-policy-lifecycle.md)
- [6.2 Policy Issuance & Documentation](02-policy-issuance.md)
- [7.7 Claims Systems & Analytics](../volume-07-claims/07-claims-systems-analytics.md)