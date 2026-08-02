# 14.3 — Models & Lifecycle

## 14.3.1 ML Model Types Used in Insurance

| Model Type | What It Predicts | Insurance Uses |
|------------|------------------|----------------|
| **Classification** | Category/class | Fraud (yes/no), acceptance, decline |
| **Regression** | Continuous value | Reserve amount, premium, severity |
| **Ranking** | Order of preference | Lead scoring, next-best-offer |
| **Clustering** | Natural groups | Customer segmentation |
| **Time series** | Future values | Claims forecasting, loss trends |
| **NLP** | Text meaning | Document extraction, chat intent |
| **Computer vision** | Image content | Damage detection and estimation |

### Common Algorithms

| Algorithm | Type | Strengths | Use |
|-----------|------|-----------|-----|
| Logistic regression | Classification | Interpretable | Score risk |
| Decision tree | Classification | Explainable | Simple rules |
| Random forest | Classification/regression | Robust | Risk scoring |
| Gradient boosting (XGBoost) | Both | Accurate | Fraud, pricing |
| Neural networks | Both | Complex patterns | Images, deep data |
| XGBoost/LightGBM | Tabular | Best of class | Most tabular tasks |
| LLMs (GPT) | Text | Language tasks | Summarization, Q&A |

---

## 14.3.2 Model Lifecycle

### End-to-End Lifecycle

```
1. Business Problem
2. Data Collection & Prep
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. Validation & Approval
7. Deployment
8. Monitoring
9. Retraining & Governance
```

### Phase Detail

| Phase | Key Activities |
|-------|----------------|
| **1. Business problem** | Define objective, success metrics, decision use |
| **2. Data collection** | Acquire data, assess quality |
| **3. Feature engineering** | Build features, split train/test |
| **4. Training** | Select algorithm, train model |
| **5. Evaluation** | Test accuracy on holdout data |
| **6. Validation** | Business and risk approval |
| **7. Deployment** | Deploy to production API/service |
| **8. Monitoring** | Track drift, performance, bias |
| **9. Retraining** | Refresh with new data periodically |

---

## 14.3.3 Train / Validation / Test Split

| Dataset | Purpose | Typical Split |
|---------|---------|---------------|
| **Training** | Model learns patterns | 70–80% |
| **Validation** | Tune hyperparameters | 10–15% |
| **Test** | Final unbiased evaluation | 10–15% |

---

## 14.3.4 Model Evaluation Metrics

### Classification Metrics

| Metric | Question |
|--------|----------|
| **Accuracy** | Overall correctness |
| **Precision** | Of predicted positives, how many correct |
| **Recall** | Of actual positives, how many caught |
| **F1** | Balance of precision and recall |
| **AUC-ROC** | Discrimination ability |
| **Lift** | Improvement over random |

### Regression Metrics

| Metric | Question |
|--------|----------|
| **MAE** | Average absolute error |
| **RMSE** | Root mean squared error |
| **R²** | Variance explained |

### Confusion Matrix (Fraud Example)

| | Predicted Fraud | Predicted Not Fraud |
|--|-----------------|---------------------|
| **Actual Fraud** | True Positive | False Negative |
| **Actual Not Fraud** | False Positive | True Negative |

| Metric | Value |
|--------|-------|
| Precision | 40% |
| Recall | 60% |
| Accuracy | 95% |
| AUC-ROC | 0.85 |

---

## 14.3.5 Model Deployment

### Deployment Patterns

| Pattern | Description | Use |
|---------|-------------|-----|
| **Batch scoring** | Score in batches | Periodic re-rating, strategies |
| **Real-time API** | Score on request | Quotes, claim triage |
| **Streaming** | Score events in stream | Real-time fraud alert |
| **Embedded** | Native platform model | Duck Creek Luminos, AI on GW |

### Integration with Core Systems

```
Application → Scores → Rules Engine → Action
  Policy:  risk score → approve / refer / decline
  Claims:  fraud score → route to SIU / adjuster
  Billing: payment risk → payment plan offered
```

---

## 14.3.6 Model Monitoring

| Monitor | Description |
|---------|-------------|
| **Data drift** | Input distribution changes over time |
| **Concept drift** | Relationship between inputs and output changes |
| **Performance decay** | Accuracy declines over time |
| **Bias drift** | Fairness metrics worsen |
| **Feature quality** | Missing or invalid inputs increase |

### Drift Detection Example

| Month | AUC | Data Drift Score | Action |
|-------|-----|------------------|--------|
| Jan | 0.85 | Low | — |
| Mar | 0.83 | Low | — |
| Jun | 0.79 | Medium | Investigate |
| Sep | 0.74 | High | Retrain / review |

---

## 14.3.7 Model Governance

| Governance Element | Description |
|--------------------|-------------|
| Model inventory | Registry of all models |
| Approval process | Business and risk sign-off |
| Documentation | Model cards, inputs, limitations |
| Version control | Track model versions |
| Explainability | Understand decisions |
| Fairness testing | Bias assessment |
| Audit trail | Full decision logs |
| Review cadence | Scheduled re-review |

---

## Key Takeaways

1. **Model selection** depends on problem type and data.
2. **The lifecycle** spans problem definition through monitoring and retraining.
3. **Train/validation/test splits** prevent overfitting and ensure unbiased evaluation.
4. **Metrics** (precision, recall, AUC, MAE) measure model quality.
5. **Deployment patterns** range from batch to real-time API.
6. **Monitoring and governance** detect drift, bias, and performance decay.

---

**Next:** [14.4 AI in Underwriting](04-ai-underwriting.md)