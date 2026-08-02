# 14.4 — AI in Underwriting

## 14.4.1 Overview

AI transforms underwriting by automating data capture, risk assessment, and decision routing — allowing underwriters to focus on complex risks. AI supports the human underwriter rather than replacing them.

---

## 14.4.2 AI Use Cases in Underwriting

| Use Case | Description | AI Type |
|----------|-------------|---------|
| **Automated risk scoring** | Score submissions for acceptance | Predictive ML |
| **Document extraction** | Extract data from applications and reports | NLP/OCR |
| **Submission triage** | Route to correct UW based on complexity | Rules + ML |
| **Referral optimization** | Auto-approve low-risk, refer complex | Predictive + rules |
| **Straight-through processing** | Bind without human review | Ensemble |
| **Pricing recommendation** | Suggest rate/coverage adjustments | Predictive |
| **Fraud/red-flag detection** | Flag suspicious submissions | Predictive |
| **Underwriter assistant** | Summarize submissions, answer questions | Generative AI |
| **Renewal retention** | Predict non-renewal risk | Predictive |
| **Portfolio monitoring** | Track UW performance | Analytics |

---

## 14.4.3 Underwriting Decision Flow with AI

```
Submission
   ↓
Data Capture & Document Extraction (NLP/OCR)
   ↓
Risk Scoring (ML)
   ↓
Rules Engine
   ├── Auto-approve (STP) → Bind
   ├── Referral → Underwriter reviews + AI-assisted summary
   └── Decline
```

| Outcome | AI Contribution |
|---------|-----------------|
| **Auto-approve** | Risk score + rules support binding |
| **Referral** | UW sees score, reasons, supporting data |
| **Decline** | Rule-based decline with rationale |

---

## 14.4.4 Risk Scoring Models

### What They Score

| Model | Target |
|-------|--------|
| **Loss propensity** | Probability of a claim |
| **Severity potential** | Expected severity |
| **Fraud probability** | Likelihood submission is fraudulent |
| **Retention score** | Likelihood to renew |
| **Conversion score** | Likelihood to buy |

### Input Features

| Category | Examples |
|----------|---------|
| Risk attributes | Age, value, location, class |
| Coverage selections | Limits, deductibles |
| Previous losses | Claim counts, types, amounts |
| Credit-based score | Insurance score |
| MVR | Driving violations |
| Property data | Condition, age, construction |
| External | Weather, crime, catastrophe exposure |

### Score Usage

| Score | Action |
|-------|--------|
| Low risk | Auto-approve, standard pricing |
| Medium risk | Refer, price adjustment |
| High risk | Decline or require conditions |

---

## 14.4.5 Document Extraction (NLP/OCR)

### Document Types

| Document | Data Extracted |
|----------|----------------|
| Application | Applicant details, risk info |
| Financial statements | Business financials |
| Inspection reports | Property condition |
| Loss runs | Prior claims |
| State filings | Fleet, liability limits |
| Photos | Damage/condition (vision) |

### Extraction Benefits

| Benefit | Description |
|---------|-------------|
| Speed | Reduction from hours to minutes |
| Accuracy | Consistent extraction |
| STP | No manual rekeying |
| Data quality | Validated structured output |
| Underwriter productivity | Focus on analysis, not data entry |

---

## 14.4.6 Underwriter Assistant (Generative AI)

### Capabilities

| Capability | Example |
|-----------|---------|
| Submission summary | Summarize application and attachments |
| Coverage comparison | Compare requested vs. standard coverage |
| Risk highlight | Surface concerning attributes |
| Draft communication | Draft quotes, conditions, decline letters |
| Knowledge retrieval | Answer from UW guidelines |
| Consistency check | Highlight atypical requests |

### Human-in-the-Loop

| Step | Human Role |
|------|-----------|
| AI draft | Generated summary and suggestion |
| Underwriter review | Validate and adjust decision |
| Approval | Underwriter owns final decision |
| Audit | Decision logged and explainable |

---

## 14.4.7 Implementation Considerations

| Consideration | Detail |
|---------------|--------|
| **Data availability** | Historical submissions and outcomes |
| **Outcome labels** | Define "good" vs. "bad" risk clearly |
| **Model explanation** | Underwriters need reasons, not just scores |
| **Authority preservation** | AI supports, UW retains authority |
| **Fairness** | Bias testing across protected classes |
| **Integration** | Embed in policy admin workflow |
| **Monitoring** | Track approval rates and outcomes |
| **Regulatory** | Compliance with ratings/surplus rules |

---

## 14.4.8 Benefits to Track

| Metric | Before AI | After AI |
|--------|-----------|----------|
| Quote turnaround | 15 min | 5 min |
| STP rate | 40% | 65% |
| Referral rate | 25% | 15% |
| UW capacity | 10 submissions/day | 25/day |
| Data entry errors | 8% | 1% |
| Renegade pricing | Moderate | Reduced |

---

## Key Takeaways

1. **AI automates data capture, scoring, and routing** in underwriting.
2. **Risk scoring models** predict loss propensity, severity, and fraud.
3. **Document extraction** dramatically speeds submission handling.
4. **Generative AI assistants** synthesize information and draft communications.
5. **Human underwriters remain in charge** — AI is decision support.
6. **Explainability, fairness, and monitoring** are essential.

---

**Next:** [14.5 AI in Claims](05-ai-claims.md)