# 14.6 — AI Governance & Ethics

## 14.6.1 Why Governance Matters

AI decisions in insurance can significantly affect customers — pricing, coverage, claims payments, and fraud referrals. Poor governance can lead to unfair outcomes, regulatory penalties, reputational damage, and loss of trust. Governance ensures AI is **fair, explainable, compliant, and monitored**.

---

## 14.6.2 Core Governance Principles

| Principle | Description |
|-----------|-------------|
| **Fairness** | No unfair discrimination against protected groups |
| **Transparency** | Customers and regulators can understand decisions |
| **Explainability** | Reasons for decisions are available |
| **Accountability** | Clear ownership of model decisions |
| **Human oversight** | Humans can review and override |
| **Privacy** | Personal data protected |
| **Security** | Models and data secure |
| **Auditability** | Decisions can be traced and verified |
| **Robustness** | Models perform reliably |

---

## 14.6.3 Fairness & Bias

### Types of Bias

| Bias Type | Description |
|-----------|-------------|
| **Historical bias** | Past discrimination reflected in data |
| **Sampling bias** | Data not representative |
| **Proxy bias** | Disparate impact via proxy variables |
| **Label bias** | Inconsistent/biased training labels |
| **Algorithmic bias** | Design choices that worsen outcomes |

### Protected Characteristics (Examples)

| Characteristic | Fairness Concern |
|----------------|-----------------|
| Race / ethnicity | Underwriting, pricing |
| Religion | Pricing, coverage |
| National origin | Underwriting |
| Gender | Pricing (where regulated) |
| Age | Pricing, coverage |
| Disability | Claims handling |
| Marital/family status | Pricing, rate filings |
| Sexual orientation | Coverage decisions |

### Fairness Testing

| Test | Description |
|------|-------------|
| **Statistical parity** | Similar rates across groups |
| **Equal opportunity** | Similar true positive rates |
| **Equalized odds** | Similar error rates |
| **Individual fairness** | Similar people treated similarly |
| **Adverse impact** | Disparate impact ratio |

### Fairness Metrics Example

| Group | Approval Rate | Contact Rate | Difference |
|-------|--------------|--------------|------------|
| Group A | 82% | 82% | — |
| Group B | 74% | 82% | 8 pts ⚠️ |
| Group C | 83% | 82% | 1 pt ✔ |

---

## 14.6.4 Explainability

### Why Explainability Matters

| Stakeholder | Need |
|-------------|------|
| **Regulator** | Justify pricing/discrimination tests |
| **Underwriter** | Understand why a risk was scored |
| **Claimant** | Understand why claim was referred |
| **Internal audit** | Verify decisions are consistent |
| **Data science** | Debug and improve models |

### Explanation Levels

| Level | Description |
|-------|-------------|
| **Global** | What factors matter overall |
| **Local** | Why a specific decision was made |
| **Model-agnostic** | Works for any model (SHAP, LIME) |
| **Model-specific** | Built into model (trees, linear) |

### Explanation Example (SHAP)

| Feature | Value | Contribution |
|---------|-------|--------------|
| Claims history | 3 prior claims | +28 points (higher risk) |
| Age | 22 | +15 points |
| Credit score | 620 | +12 points |
| Deductible | $250 | −8 points |
| **Total score** | | **47 / 100** |

---

## 14.6.5 Regulatory Landscape

| Regulation | Region | Key Points |
|-----------|--------|-----------|
| **EU AI Act** | European Union | Risk-based classification, high-risk AI obligations |
| **NAIC AI Principles** | US (NAIC) | Fairness, transparency, governance expectations |
| **State laws (e.g., Colorado SB21-169)** | US states | Discrimination testing for life insurance AI |
| **GDPR** | EU/UK | Data rights, automated decision protection |
| **CCPA/CPRA** | California | Privacy, opt-out |
| **HIPAA** | US | Health data protection |
| **Fair Credit Reporting Act** | US | Credit-based insurance score rules |

### Key Regulatory Themes

| Theme | Expectation |
|-------|-------------|
| Adverse action notice | Explain denial/adverse change |
| Discrimination testing | Prove no unfair discrimination |
| Human review | Customers can request human review |
| Model documentation | Document purpose, inputs, validation |
| Governance program | Formal AI risk management |
| Record keeping | Retain decision logic and data |

---

## 14.6.6 AI Governance Framework

### Governance Structure

```
Board / Executive
    ↓
AI Governance Committee
    ↓
Model Risk Management
    ↓
Data Science Teams
```

### Governance Committee Responsibilities

| Responsibility | Description |
|----------------|-------------|
| Policy setting | AI use policies |
| Approval | Model deployment approvals |
| Risk review | Bias, fairness, operational risk |
| Compliance | Regulatory alignment |
| Monitoring | Model performance and drift |
| Incident response | Model failures, harm events |

---

## 14.6.7 Model Risk Management (MRM)

### MRM Lifecycle

| Stage | Controls |
|-------|----------|
| **Development** | Documentation, validation |
| **Validation** | Independent validation |
| **Approval** | Risk and business sign-off |
| **Implementation** | Controlled rollout |
| **Monitoring** | Performance, drift, bias |
| **Retirement** | Decommission and archive |

### Documentation — Model Card

| Section | Contents |
|---------|----------|
| Model name | Risk score v2 |
| Purpose | Underwriting risk score |
| Inputs | Policy, claims, credit data |
| Output | 0–100 score |
| Performance | AUC 0.84, precision 0.41 |
| Limitations | Sparse data for new products |
| Fairness | Tested across protected groups |
| Contact | Model owner |

---

## 14.6.8 Human Oversight

### Oversight Requirements

| Requirement | Description |
|-------------|-------------|
| **Right to review** | Customers can request human review |
| **Meaningful control** | Humans can override decisions |
| **Training** | Staff understand AI limitations |
| **Escalation** | Clear escalation for disputes |
| **Fallback** | Manual process if model fails |

---

## 14.6.9 AI Ethics in Practice

### Red Lines

| Situation | Principle |
|-----------|-----------|
| Protected class pricing proxy | Prohibited unless justified & compliant |
| Black-box denial without explanation | Require explainability |
| Discriminatory outcome proven | Remediate or retire model |
| Data used beyond consent | Refuse |
| Model failure without oversight | Human fallback required |

### Responsible AI Checklist

| Check | Status |
|-------|--------|
| Bias tested across protected groups | ☐ |
| Explanation available for decisions | ☐ |
| Human review available | ☐ |
| Model documented (model card) | ☐ |
| Compliance reviewed (regulation) | ☐ |
| Privacy assessed | ☐ |
| Monitoring in place (drift/bias) | ☐ |
| Incident response defined | ☐ |
| Owner accountable | ☐ |

---

## Key Takeaways

1. **Governance ensures AI is fair, explainable, and accountable**.
2. **Bias can enter through data, proxies, labels, and algorithms** — must be tested.
3. **Explainability builds trust** and satisfies regulators.
4. **Regulation is evolving** — EU AI Act, NAIC principles, state laws.
5. **Model risk management** governs the full model lifecycle.
6. **Human oversight** remains essential in every AI decision.

---

**Back to:** [Volume 14 Index](index.md)