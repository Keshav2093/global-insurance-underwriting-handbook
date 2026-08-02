# 14.5 — AI in Claims

## 14.5.1 Overview

AI in claims drives faster triage, accurate damage assessment, fraud detection, and better reserve estimates. It transforms the entire claims lifecycle — from FNOL to closure — while improving customer experience and reducing cost.

---

## 14.5.2 AI Use Cases in Claims

| Use Case | Description | AI Type |
|----------|-------------|---------|
| **FNOL automation** | Extract claim data from calls/text/photos | NLP + computer vision |
| **Claim triage** | Route claims by complexity and severity | Predictive ML |
| **Damage assessment** | Estimate auto/property damage from photos | Computer vision |
| **Fraud detection** | Score claims for SIU referral | Predictive ML |
| **Reserve prediction** | Predict ultimate loss | Regression |
| **Coverage guidance** | Confirm coverage from policy data | NLP + rules |
| **Litigation prediction** | Predict claims likely to litigate | Predictive |
| **Subrogation detection** | Identify recovery opportunities | Predictive |
| **Contractor/vendor selection** | Recommend repair partners | Ranking |
| **Claimant communication** | Chatbot answers, status updates | Generative AI |
| **Notes summarization** | Summarize adjuster notes, medical records | Generative AI |
| **Payment automation** | Auto-approve simple claims | Ensemble |

---

## 14.5.3 Claims Lifecycle with AI

```
FNOL → Triage → Damage Assessment → Coverage → Fraud Check → Reserves → Settlement → Payment → Recovery → Closure
  ↓       ↓            ↓               ↓           ↓           ↓          ↓         ↓          ↓          ↓
NLP    ML route     Computer      Rules +     Fraud      Reserve    Settlement  Auto or   Recovery  Analytics
       + vision     vision        NLP         score      model      guidance    approved   model
```

---

## 14.5.4 FNOL Automation

### FNOL Inputs AI Can Process

| Input | AI Processing |
|-------|---------------|
| Phone call | Speech-to-text, key data extraction |
| Chat message | Intent, entity extraction |
| Web/mobile form | Auto-validate, prefill |
| Photos | Damage detection, claim summary |
| Report/document | OCR extraction |

### FNOL Extraction Example

| Field | Source | AI Method |
|-------|--------|-----------|
| Policy number | Call/chat/form | NLP entity extraction |
| Loss date/time | Call/chat | NLP |
| Location | GPS/call | Geolocation |
| Description | Call/chat | NLP summarization |
| Damage info | Photos | Computer vision |
| Injuries | Call/chat | NLP detection |
| Other party | Call | Named entity recognition |

---

## 14.5.5 Damage Assessment (Computer Vision)

### Auto Claims Example

```
Customer Photos → AI Assessment → Estimate → Claimant Option
                    ↓
              Repair estimate
              (parts, labor)
```

| Step | AI Output |
|------|-----------|
| Photo intake | Images validated and tagged |
| Damage detection | Panel/component damage identified |
| Severity estimation | Damage severity score |
| Repair estimate | Cost estimate |
| Total loss check | Compare to vehicle value |

### Property Claims Example

| Application | Description |
|-------------|-------------|
| Roof damage | Satellite/aerial imagery analysis |
| Structural damage | Photo-based assessment |
| Water damage | Classification by room/extent |
| Hail impact | Hail damage detection |

---

## 14.5.6 Fraud Detection

### Fraud Scoring

| Score Range | Action |
|-------------|--------|
| Low (0–30) | Normal handling |
| Medium (31–60) | Enhanced verification |
| High (61–100) | SIU referral |

### Fraud Indicators ML Models Use

| Category | Indicators |
|----------|-----------|
| Timing | Late claim, claim at policy boundary |
| Circumstances | Inconsistent, impossible scenarios |
| Claimant behavior | Prior suspicious claims, exaggeration |
| Documents | Altered, fabricated documents |
| Network | Same parties across claims |
| History | Claim frequency, payout patterns |

### SIU Workflow

```
Fraud Score → Threshold? → SIU Referral → Investigation → Outcome → Feedback to Model
```

| Outcome | Description |
|---------|-------------|
| Confirmed fraud | Deny, prosecute |
| Unsubstantiated | Close, pay if valid |
| Savings | Track avoided payments |

---

## 14.5.7 Reserve Prediction

### What Reserve Models Predict

| Prediction | Use |
|------------|-----|
| Ultimate loss | Initial reserve |
| Severity | Reserve by claim type |
| Development | Reserve changes over time |
| Litigation cost | Defense expense reserve |

### Input Features

| Category | Examples |
|----------|---------|
| Claim type | BI, PD, collision, theft |
| Injury severity | Type, permanency |
| Liability | Fault determination |
| Policy limits | Coverage limits |
| Claimant attributes | Age, occupation |
| Jurisdiction | State venue |
| Claims history | Prior claims |

### Reserve Model Benefit

| Metric | Traditional | With AI |
|--------|-------------|---------|
| Initial reserve accuracy | Moderate | Improved |
| Reserve adequacy review | Quarterly | Continuous |
| Actuarial workload | High | Reduced |

---

## 14.5.8 Generative AI in Claims

| Use Case | Example |
|----------|---------|
| **Claim summary** | Summarize FNOL, notes, and communications |
| **Coverage opinion** | Draft coverage analysis |
| **Correspondence** | Draft denial, reservation of rights, settlement letters |
| **Claimant inquiry** | Answer status questions via chatbot |
| **Document searches** | Find relevant policies and evidence |
| **Medical codification** | Summarize medical records |
| **Quality review** | Flag missing steps, inconsistent notes |
| **Fraud narratives** | Summarize suspicious patterns |

> **Note:** Generative AI in claims requires human review for significant decisions. Coverage opinions, denials, and settlements should be validated by adjusters and counsel.

---

## 14.5.9 Implementation Considerations

| Consideration | Detail |
|---------------|--------|
| **Data labeling** | Damage, fraud labels needed for training |
| **Explainability** | Adjusters must understand AI decisions |
| **Human oversight** | Significant payments require approval |
| **Regulatory** | Fair claims practices deadlines remain |
| **Bias** | Avoid discriminatory outcomes |
| **Integration** | Embed in claims system (Guidewire, Duck Creek, Majesco) |
| **Monitoring** | Track fraud precision, reserve accuracy |

---

## Key Takeaways

1. **AI accelerates FNOL, triage, assessment, and settlement**.
2. **Computer vision** assesses auto and property damage from photos.
3. **Fraud detection** scores claims and routes suspicious cases to SIU.
4. **Reserve models** improve initial reserve accuracy.
5. **Generative AI** summarizes, drafts, and answers — with human oversight.
6. **Explainability and monitoring** are essential for trust and compliance.

---

**Next:** [14.6 AI Governance & Ethics](06-ai-governance.md)