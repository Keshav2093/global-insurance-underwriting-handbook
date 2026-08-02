# 14.2 — AI & Data

## 14.2.1 Why Data Is the Foundation

AI models learn from data. The quality, breadth, and governance of data determine model accuracy, fairness, and reliability. Insurers that succeed with AI invest in data platforms, data quality, and feature engineering.

---

## 14.2.2 Data Types for Insurance AI

### Structured Data

| Data | Source | Use |
|------|--------|-----|
| Policy data | Policy admin | Risk attributes |
| Claims data | Claims system | Loss experience, fraud |
| Billing data | Billing system | Payment behavior |
| Customer data | CRM | Retention, cross-sell |
| Producer data | Distribution | Channel performance |
| Financial data | GL | Profitability |

### Unstructured Data

| Data | Source | Use |
|------|--------|-----|
| Policy documents | PDFs, dec pages | Document extraction |
| Claims notes | Adjuster notes | NLP analysis |
| Medical records | Providers | Injury assessment |
| Police reports | Authorities | Liability |
| Photos/video | Insured, adjuster | Computer vision |
| Emails/correspondence | Claims files | Communication analysis |
| Social media | Public | Fraud/background |

### External Data

| Data | Vendor | Use |
|------|--------|-----|
| Credit scores | Credit bureaus | Pricing, risk |
| MVR | Motor vehicle records | Auto risk |
| Property data | GIS, satellite | Property risk |
| Weather | Meteorological | Cat risk |
| ISO data | ISO | Fraud, reports |
| Third-party data | Various | Enrichment |

---

## 14.2.3 Data Quality

### Quality Dimensions

| Dimension | Description |
|-----------|-------------|
| **Accuracy** | Values are correct |
| **Completeness** | No missing required data |
| **Consistency** | Same across systems |
| **Timeliness** | Current and available |
| **Validity** | Conforms to rules/formats |
| **Uniqueness** | No duplicates |

### Data Quality Issues in Insurance

| Issue | Example |
|-------|---------|
| Legacy codes | Different systems, different codes |
| Duplicate parties | Same customer multiple records |
| Missing fields | Incomplete risk data |
| Free-text fields | Unstructured, inconsistent |
| Date formats | MM/DD/YYYY vs DD/MM/YYYY |
| Address quality | Invalid or outdated addresses |

---

## 14.2.4 Feature Engineering

**Features** are the inputs a model uses. Feature engineering transforms raw data into meaningful model inputs.

### Feature Examples

| Domain | Raw Data | Engineered Feature |
|--------|----------|-------------------|
| Auto | Driver age | Age band (18–25, 26–65, 65+) |
| Auto | Claims history | Claims-free years |
| Home | Dwelling value | Value per square foot |
| Customer | Policy count | Total policies across products |
| Claims | Injury type | Injury severity score |
| Billing | Payment history | Late payment count, avg days late |

### Feature Types

| Type | Description |
|------|-------------|
| Numerical | Age, value, premium |
| Categorical | Territory, class, coverage |
| Date-based | Tenure, age of risk |
| Ratio | Loss ratio, value ratio |
| Count | Claims count, policy count |
| Text (NLP) | Sentiment, topic, keywords |
| Engineered | Combinations, interactions |

---

## 14.2.5 Data Infrastructure for AI

### Modern Data Platform

```
Applications (Policy, Claims, Billing)
        ↓
   Event Stream / Batch
        ↓
   Data Lake (Raw Data)
        ↓
   Data Warehouse (Curated)
        ↓
   Feature Store
        ↓
   Model Training → Model Registry → Serving
```

### Components

| Component | Purpose |
|-----------|---------|
| **Data lake** | Store raw data at low cost |
| **Data warehouse** | Curated, queryable datasets |
| **Feature store** | Reusable, consistent features |
| **Model registry** | Version models |
| **ML platform** | Train, deploy, monitor |
| **Data quality tools** | Profiling, validation |
| **Governance** | Lineage, access, retention |

---

## 14.2.6 Common Data Challenges

| Challenge | Impact | Mitigation |
|-----------|--------|-----------|
| Silos | Fragmented features | Data platform integration |
| Poor quality | Unreliable models | Data quality program |
| Sparse history | Cold-start models | External data, transfer learning |
| Historical bias | Unfair outcomes | Bias testing, balanced data |
| Class imbalance | Rare event (fraud) | Resampling, cost weighting |
| Data privacy | Regulatory risk | Anonymization, consent |

---

## Key Takeaways

1. **Data is the foundation of AI** — quality matters more than algorithm choice.
2. **Structured, unstructured, and external data** are all valuable.
3. **Feature engineering** converts raw data into model-ready inputs.
4. **A modern data platform** (lake, warehouse, feature store) supports AI at scale.
5. **Data quality** must be actively managed and governed.
6. **Bias and privacy** are managed from the data layer up.

---

**Next:** [14.3 Models & Lifecycle](03-ai-models.md)