# 13.2 — BA in Underwriting

## 13.2.1 The BA's Role in Underwriting

BAs support underwriting in three main ways:

1. **Requirements for system change** — product updates, referral rules, workflow changes.
2. **Process improvement** — how underwriters work, tools, and data.
3. **Data and decision support** — analysis of underwriting performance, rules, and outcomes.

---

## 13.2.2 Understanding the Underwriting Process

### Key Underwriting Concepts the BA Must Know

| Concept | Description |
|---------|-------------|
| **Eligibility** | Rules defining who/what can be written |
| **Classification** | Risk categories (class, territory, tier) |
| **Coverage** | What is insured, limits, deductibles |
| **Rating** | How premium is calculated |
| **Referral** | Cases sent to underwriter for review |
| **Authority** | Limits of binding/approval for each role |
| **Condition** | Stipulations added to policy |
| **Decline** | Risk not accepted |
| **Non-renewal** | Policy not offered for renewal |

### Underwriting Workflow (New Business)

```
Submission → Data Capture → Eligibility → Classification → Rating → Referral (if needed) → Decision → Bind
```

| Step | BA Support |
|------|-----------|
| Submission | Requirements for intake forms and channels |
| Data capture | Field definitions, validation rules |
| Eligibility | Rule requirements |
| Rating | Premium logic, rate tables |
| Referral | Referral rule requirements |
| Decision | Decision options, authority matrix |
| Bind | Bind workflow requirements |

---

## 13.2.3 BA Deliverables for Underwriting Projects

### Typical Project: Launch a New Product

| Deliverable | Description |
|-------------|-------------|
| **BRD** | Business need, scope, success criteria |
| **Product requirements** | Coverages, limits, deductibles, rating |
| **Rule requirements** | Eligibility, referral, decline rules |
| **Workflow requirements** | Screens, tasks, approvals |
| **Test scenarios** | Underwriting scenarios and expected results |
| **Rate filing support** | Actuarial inputs, state filing requirements |

### Typical Project: Update Referral Rules

| Deliverable | Description |
|-------------|-------------|
| **Rule matrix** | Condition → action mapping |
| **Authority matrix** | Approver per referral type |
| **Impact analysis** | Affected submissions/quotes |
| **Test cases** | Rule validation scenarios |
| **Data analysis** | Rule impact on bind rates |

---

## 13.2.4 Eliciting Underwriting Requirements

### Elicitation Techniques

| Technique | Application |
|-----------|-------------|
| **Interviews** | Understand UW decisions and logic |
| **Workshops** | Define rules collaboratively |
| **Shadowing** | Observe underwriters in practice |
| **Document review** | UW guidelines, manuals, forms |
| **Data analysis** | Historical decisions, decline rates |
| **Prototyping** | Validate screens and workflows |

### Key Questions to Ask

| Question | Purpose |
|----------|---------|
| What makes this risk acceptable? | Define eligibility |
| What triggers a referral? | Define referral rules |
| Who has authority to approve? | Define authority matrix |
| What conditions would you add? | Define stipulations |
| What data do you need to decide? | Define data requirements |
| What would make you decline? | Define decline criteria |
| What is the turnaround expectation? | Define SLAs |
| What are the regulatory limits? | Define compliance constraints |

---

## 13.2.5 Documenting Underwriting Rules

### Rule Documentation Format

| Field | Example |
|-------|---------|
| Rule ID | REF-001 |
| Rule name | High-value home referral |
| Trigger | Dwelling value > $5,000,000 |
| Condition | Replacement cost estimate ≥ $5,000,000 |
| Action | Referral to Senior Underwriter |
| Priority | High |
| Product | Homeowners |
| State | All |
| Effective date | 01/01/2026 |
| Owner | Personal Lines UW Director |

### Rule Types

| Rule Type | Behavior |
|-----------|----------|
| Validation | Block submission |
| Eligibility | Allow/disallow product |
| Referral | Route to UW |
| Requirement | Document needed |
| Condition | Add stipulation |
| Decline | Auto-decline |
| Pre-fill | Populate data |
| Alert | Warning only |

---

## 13.2.6 Underwriting Data Analysis

### Common Analyses

| Analysis | Purpose |
|----------|---------|
| **Bind rates** | How many submissions become policies |
| **Referral rates** | % of submissions referred |
| **Referral aging** | Time to decision |
| **Decline reasons** | Why risks are declined |
| **Renewal retention** | % renewing |
| **Loss ratio by class** | Profitability by classification |
| **Premium by territory** | Geographic distribution |
| **Rule impact** | Effect of rules on volume/quality |

### Sample: Referral Analysis

| Metric | Value |
|--------|-------|
| Submissions | 10,000 |
| Auto-approved | 8,200 (82%) |
| Referred | 1,800 (18%) |
| Referral accepted | 1,250 (69%) |
| Referral declined | 550 (31%) |
| Avg. referral aging | 2.4 days |
| Goal aging | ≤ 2 days |

---

## 13.2.7 Supporting Rate Changes

### Rate Filing Project

| Step | BA Role |
|------|---------|
| **Scope** | Identify affected products, states, effective dates |
| **Requirements** | Document new rate tables and logic |
| **Configuration** | Support rate implementation in system |
| **Testing** | Validate premium calculations |
| **Filing** | Gather data for regulatory filing |
| **Communication** | Prepare internal/external notices |

### BA Deliverables for Rate Changes

| Deliverable | Description |
|-------------|-------------|
| Rate table requirements | New tables, factors |
| Rating logic changes | Formula updates |
| Test cases | Premium calculation scenarios |
| Impact summary | % of policies affected, average change |
| Filing data | State-required rate filings |
| User communication | Rate change notices |

---

## Key Takeaways

1. **BAs support underwriting** through requirements, process improvement, and data analysis.
2. **Understand the full UW lifecycle** — eligibility, classification, rating, referral, decision.
3. **Rule documentation** must be precise and testable.
4. **Authority matrices** define who approves what.
5. **Data analysis** measures rule effectiveness and portfolio performance.
6. **Rate changes** require close BA support for configuration, testing, and filing.

---

**Next:** [13.3 Product & Rating Projects](03-ba-product.md)