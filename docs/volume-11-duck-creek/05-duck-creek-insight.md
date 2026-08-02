# 11.5 — Duck Creek Insight

## 11.5.1 Overview

**Duck Creek Insight** is the data, analytics, and reporting platform. It ingests data from Duck Creek Author, Billing, and Claims, and provides insurers with:

- Operational and management reporting
- Data visualization and dashboards
- Predictive analytics and AI/ML models
- Data warehousing and data lake capabilities
- Real-time and batch data processing

### Core Capabilities

| Capability | Description |
|-----------|-------------|
| **Data ingestion** | Real-time and batch capture from all Duck Creek applications |
| **Data warehouse** | Structured and analytical data storage |
| **Data lake** | Raw data storage for advanced analytics |
| **Reporting** | Operational, regulatory, and management reports |
| **Dashboards** | Interactive visualizations |
| **Predictive analytics** | AI/ML models embedded in workflows |
| **External data** | ISO, NCCI, third-party data integration |
| **Export/ETL** | Data extracts to external systems |

---

## 11.5.2 Insight Architecture

```
┌─────────────────────────────────────────────┐
│         Power BI / Insight Reports         │
├─────────────────────────────────────────────┤
│       Analytics & ML (Luminos)             │
├─────────────────────────────────────────────┤
│        Data Warehouse (SQL)                │
├─────────────────────────────────────────────┤
│           Data Lake (ADLS)                 │
├─────────────────────────────────────────────┤
│      Ingest from Author, Billing, Claims   │
└─────────────────────────────────────────────┘
```

### Architecture Components

| Component | Description |
|-----------|-------------|
| **Azure Data Lake Storage (ADLS)** | Raw event data storage |
| **Azure SQL Data Warehouse** | Structured analytical data |
| **Data Factory** | ETL orchestration |
| **Event Hubs** | Real-time event streaming |
| **Power BI** | Visualization and dashboards |
| **Azure Machine Learning** | Predictive model deployment |
| **Luminos** | Duck Creek's AI/ML decision platform |

---

## 11.5.3 Data Ingestion

### Data Sources

| Source | Data Captured |
|--------|---------------|
| **Author** | Submissions, quotes, policies, endorsements, cancellations |
| **Billing** | Invoices, payments, receivables, refunds, commissions |
| **Claims** | FNOL, exposures, reserves, payments, recoveries |
| **Distribution** | Producer activity, licensing, appointments |
| **External** | ISO, NCCI, weather, credit, MVR |

### Ingestion Methods

| Method | Description | Use Case |
|--------|-------------|----------|
| **Real-time events** | Event-driven capture | Dashboards, alerts |
| **Batch extract** | Scheduled nightly extracts | Data warehouse refresh |
| **API polling** | Periodic API calls | Third-party data |
| **File upload** | Flat file import | Reference data, external content |

---

## 11.5.4 Reporting

### Report Categories

| Category | Examples |
|----------|---------|
| **Operational** | Daily premium, new business, bind rates, claim counts |
| **Financial** | Written premium, earned premium, loss ratios |
| **Underwriting** | New business by line, loss ratio by class, renewal retention |
| **Claims** | Open claims, reserves, cycle time, severity |
| **Billing** | Aged receivables, cash receipts, cancellations |
| **Producer** | Production by agent, commission, retention |
| **Regulatory** | ISO reports, state filings, bordereaux |
| **Reinsurance** | Ceded premium, recoveries |

### Common Reports

#### Policy Reporting

| Report | Description |
|--------|-------------|
| **New business report** | Policies written in period |
| **In-force report** | Current active policies |
| **Retention report** | Renewal rates |
| **Product mix** | Premium by line of business |
| **Geographic mix** | Premium by state/territory |

#### Claims Reporting

| Report | Description |
|--------|-------------|
| **Loss run** | Policy claim history |
| **Reserve adequacy** | Reserve vs. actual paid |
| **Open claims dashboard** | Current open exposure |
| **Cycle time** | Time from FNOL to closure |
| **SIU referrals** | Fraud referral outcomes |

#### Billing Reporting

| Report | Description |
|--------|-------------|
| **Aged receivables** | Open balances by bucket |
| **Cash receipts** | Payments by method/date |
| **Cancellation report** | Non-payment cancellations |
| **Commission report** | Agent commissions owed |
| **Unearned premium** | UPR calculations |

---

## 11.5.5 Dashboards

### Dashboard Types

| Dashboard | Audience | Metrics |
|-----------|----------|---------|
| **Executive** | C-suite | Written premium, loss ratio, combined ratio, growth |
| **Underwriting** | Underwriting team | Submission volume, bind ratio, referral aging |
| **Claims** | Claims leadership | Open claims, reserve adequacy, cycle time |
| **Finance** | Finance team | Cash position, aged receivables, refunds |
| **Operations** | Operations managers | Service levels, queue volumes, workload |
| **Agent** | Agency management | Production, loss ratio, retention |

### Dashboard Example — Executive

| Metric | Value | Trend |
|--------|-------|-------|
| Written Premium (MTD) | $45.2M | ▲ 8% |
| Earned Premium (YTD) | $512.4M | ▲ 5% |
| Loss Ratio (YTD) | 62.3% | ▼ 2.1 pts |
| Combined Ratio (YTD) | 94.8% | ▼ 1.4 pts |
| New Policies (MTD) | 12,450 | ▲ 4% |
| Renewal Retention | 86% | ▲ 1 pt |

---

## 11.5.6 Predictive Analytics and AI

### Duck Creek Luminos

**Luminos** is Duck Creek's AI/ML decision platform that embeds predictive models directly into underwriting and claims workflows.

| Capability | Description |
|-----------|-------------|
| **Model deployment** | Deploy ML models to production |
| **Model monitoring** | Track model performance |
| **Model explainability** | Understand why a decision was made |
| **Workflow integration** | Trigger decisions in Author, Billing, Claims |
| **A/B testing** | Compare model versions |

### Common Use Cases

| Use Case | Application |
|----------|-------------|
| **Risk segmentation** | Classify new business risk |
| **Fraud detection** | Score claims for SIU review |
| **Claim triage** | Route claims by complexity |
| **Reserve adequacy** | Predict ultimate loss |
| **Customer retention** | Identify renewal risk |
| **Pricing optimization** | Recommend rate changes |
| **Cross-sell** | Identify coverage gaps |
| **Churn prediction** | Predict policy cancellations |

### Prompt/Decision Flow

```
Insight Model Scores
  → Author/Billing/Claims calls scoring service
  → Model returns score + explanation
  → Business rules use score to drive workflow
  → Decision recorded for audit
```

---

## 11.5.7 Data Warehouse and Data Lake

### Data Warehouse Structure

| Layer | Description |
|-------|-------------|
| **Staging** | Raw extracted data |
| **Integration** | Cleansed, normalized data |
| **Core** | Enterprise data model (subject areas) |
| **Mart** | Department-specific datasets |

### Data Model Subject Areas

| Subject Area | Tables |
|--------------|--------|
| **Policy** | Policy, period, coverage, risk, premium |
| **Billing** | Invoice, payment, receivable, commission |
| **Claims** | Claim, exposure, reserve, payment, recovery |
| **Customer** | Account, contact, relationship |
| **Producer** | Agent, agency, appointment, license |
| **Financial** | GL entries, premium accounting |

### Data Lake Use Cases

| Use Case | Description |
|----------|-------------|
| **Raw data exploration** | Ad-hoc analysis of unstructured data |
| **Model training** | Historical data for ML models |
| **External data enrichment** | Combine internal and third-party data |
| **Long-term retention** | Archive data at low cost |
| **Regulatory compliance** | Preserve data for audits |

---

## 11.5.8 Power BI Integration

### Power BI Capabilities with Duck Creek

| Feature | Description |
|---------|-------------|
| **Direct connection** | Live queries to data warehouse |
| **Dashboards** | Interactive visual reports |
| **Row-level security** | Restrict data by role |
| **Scheduled refresh** | Automated data updates |
| **Mobile** | Dashboards on mobile devices |
| **Export** | Excel/PDF export |

### Typical Power BI Reports

- Executive underwriting dashboard
- Claims performance scorecard
- Billing KPIs
- Agent production report
- Loss ratio trends
- Product performance analysis

---

## 11.5.9 Data Governance

| Function | Description |
|----------|-------------|
| **Data dictionary** | Define standard metrics and definitions |
| **Data quality** | Validation, deduplication, completeness checks |
| **Data lineage** | Track data source to report |
| **Security** | Row/column-level security, role-based access |
| **Retention** | Data lifecycle management |
| **Privacy** | PII protection, masking, consent management |
| **Certification** | Trusted data owner sign-off |

---

## Key Takeaways

1. **Insight is the data and analytics layer** across the Duck Creek suite.
2. **Data flows** from Author, Billing, and Claims through ingestion pipelines.
3. **Reporting** spans operational, financial, underwriting, claims, and regulatory needs.
4. **Dashboards** provide real-time visibility for executives and operations.
5. **Luminos** embeds predictive AI/ML models directly into workflows.
6. **Data governance** ensures metrics are consistent, trusted, and compliant.

---

**Next:** [11.6 Implementation & Integration](06-duck-creek-impl.md)