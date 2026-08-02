# 10.5 Guidewire Data Platform

## What is the Guidewire Data Platform?

The **Guidewire Data Platform** unifies data from PolicyCenter, ClaimCenter, and BillingCenter into a single source of truth for **reporting, analytics, and business intelligence**. It enables insurers to query operational and analytical data without impacting production systems.

## Core Components

| Component | Purpose |
|---|---|
| **InfoCenter** | Reporting and dashboard component for operational metrics |
| **Data Warehouse** | Consolidated, modeled data structures for analytics |
| **Analytics Studio** | Self-service dashboards and visualizations |
| **Data Extract/ETL** | Batch pipelines from core systems into warehouse |
| **Data Access APIs** | Programmatic querying and integration |

## Data Integration Flow

```
PolicyCenter ──┐
ClaimCenter  ──┼──► Data Extract ──► Warehouse ──► InfoCenter / Analytics
BillingCenter ─┘
```

## Common Analytics Use Cases

| Use Case | Example |
|---|---|
| **Executive dashboards** | Premium, loss ratio, combined ratio by line |
| **Underwriting analytics** | Hit ratio, quote conversion, UW profitability |
| **Claims analytics** | Cycle time, reserve adequacy, claim severity |
| **Billing analytics** | Aged receivables, cancellation rates |
| **Regulatory reporting** | Statistical reporting, solvency data extracts |

## InfoCenter vs. Analytics Studio

| Aspect | InfoCenter | Analytics Studio |
|---|---|---|
| Type | Operational reporting | Self-service BI |
| Users | Business users, managers | Analysts, actuaries |
| Data source | Data warehouse | Data warehouse |
| Features | Standard reports, ad-hoc queries | Drag-and-drop dashboards |
| Output | Scheduled reports, exports | Interactive visuals |

## Data Model Considerations

- **Star schemas** — fact and dimension tables optimized for querying
- **Subject areas** — policy, claim, billing, party tracked separately
- **Incremental loads** — nightly/periodic ETL to warehouse
- **Data quality** — validation, deduplication, referential integrity

## Summary

- Data Platform centralizes reporting across all three core systems.
- InfoCenter provides operational reporting; Analytics Studio enables self-service.
- Star-schema warehouse design powers fast, cross-system queries.
- Regular data extracts keep analytics current without production impact.

## Related Chapters

- [10.1 Guidewire Overview](01-guidewire-overview.md)
- [Volume 5 Rating & Pricing](../volume-05-rating-pricing/index.md)
- [Volume 7 Claims](03-claimcenter.md)