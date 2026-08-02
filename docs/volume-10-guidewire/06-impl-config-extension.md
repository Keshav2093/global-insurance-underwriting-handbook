# 10.6 — Implementation, Configuration & Extension

Guidewire implementations follow a structured delivery methodology. Understanding the boundary between configuration (standard), extension (code), and integration (external systems) is critical for business analysts, project managers, and technical teams.

---

## 10.6.1 Implementation Methodology

### Guidewire Delivery Framework

Guidewire prescribes an agile delivery methodology for Cloud and OnPrem implementations:

| Phase | Duration | Key Activities |
|-------|----------|----------------|
| **Discover** | 4–6 weeks | Current-state assessment, future-state design, gap analysis, roadmap |
| **Design** | 6–12 weeks | Business process design, data model design, integration architecture, UI design |
| **Build** | 12–24 weeks | Configuration, extension, integration development, unit testing |
| **Test** | 8–16 weeks | SIT, UAT, performance testing, security testing |
| **Deploy** | 4–6 weeks | Data migration, cutover planning, go-live, hypercare |
| **Optimize** | Ongoing | Tuning, enhancements, upgrades, adoption |

### Implementation Approaches

| Approach | Description | When to Use |
|----------|-------------|-------------|
| **Guidewire Cloud (AWS)** | SaaS deployment managed by Guidewire | New implementations, reduced IT burden |
| **Guidewire OnPrem** | Self-hosted deployment | Regulatory data residency, existing infrastructure |
| **Hybrid** | Cloud core with on-prem integrations | Legacy system coexistence |
| **Replatform** | Move existing Guidewire to cloud | Cloud migration programs |
| **Greenfield** | Net-new implementation on Guidewire | New carriers or digital-first startups |

### Typical Implementation Team

| Role | Responsibility |
|------|---------------|
| Executive Sponsor | Budget, strategic alignment, organizational change |
| Program Manager | Timeline, dependencies, risk management |
| Guidewire Solution Architect | Platform architecture, configuration strategy |
| Business Analyst | Requirements, process design, UAT coordination |
| Configuration Developer | Studio configuration, batch processes, rules |
| Integration Developer | API development, middleware, external system integration |
| Data Migration Lead | Source-to-target mapping, migration scripts, validation |
| Test Manager | Test strategy, test case management, defect tracking |
| Change Management Lead | Training, communication, adoption tracking |

---

## 10.6.2 Configuration vs. Customization

### Configuration (Standard — No Code)

Guidewire configuration uses the **Guidewire Studio** visual development environment. Configuration changes are upgrade-safe and do not require Guidewire Professional Services approval.

**Configurable elements include:**

| Element | Examples |
|---------|---------|
| **Product Definition** | Coverage types, limits, deductibles, eligibility rules |
| **Rate Tables** | Territory, vehicle, driver, coverage, discount tables |
| **Underwriting Rules** | Referral thresholds, authority limits, risk scoring |
| **Status Definitions** | Policy states, claim stages, billing statuses |
| **Document Templates** | Declaration pages, endorsements, letters, notices |
| **Business Rules** | Validation rules, pre-fill rules, workflow routing |
| **Queues & Workflows** | Assignment queues, approval workflows, escalations |
| **Question Sets** | Submission questions, FNOL questions, underwriting questionnaires |

**Guidewire Studio key screens:**

- **Product Model Designer** — Define coverages, modifiers, rating
- **Policy File Designer** — Configure policy data model fields
- **Claim File Designer** — Configure claim data model fields
- **Workflow Designer** — Build step-by-step process flows
- **Business Rules Editor** — Write rules using Gosu language
- **Rate Table Editor** — Maintain rate tables and factor lookups
- **Document Template Manager** — Create and manage output documents

### Customization (Code — Requires Approval)

Customization involves writing **Gosu** (Guidewire's Java-based language) or **Java** code that extends the base platform.

| Customization Type | When Needed | Guidewire Approval |
|-------------------|-------------|-------------------|
| **PCFs (PolicyCenter Forms)** | Custom UI screens, non-standard workflows | Required |
| **Extensions** | New entities, new fields, custom logic | Required |
| **Plugins** | Custom rating, underwriting, billing logic | Required |
| **Batch Processes** | New batch jobs, custom reports | Required |
| **API Extensions** | New REST/SOAP endpoints | Required |
| **Integration Manager** | Complex external system integrations | Required |

### The Upgrade Impact Matrix

| Change Type | Upgrade Impact | Testing Required | Approval Needed |
|-------------|---------------|-------------------|-----------------|
| Rate table data change | None | Regression test rates | No |
| Product definition change | Low | Product testing | No |
| Business rule change | Low–Medium | Functional testing | No |
| New document template | None | Document testing | No |
| Workflow change | Medium | End-to-end testing | No |
| New extension (entity/field) | Medium–High | Full regression | Guidewire |
| New PCF (UI screen) | Medium–High | UI + regression | Guidewire |
| New plugin | High | Full regression | Guidewire |
| Java-level customization | Very High | Full regression + upgrade | Guidewire |

---

## 10.6.3 Gosu Programming Language

**Gosu** is Guidewire's proprietary language built on Java. It is used for business rules, extensions, and batch processes.

### Gosu Syntax Basics

```gosu
// Variable declaration
var policyNumber : String = "WC-2024-001"
var premium : Number = 1250.00
var isHighRisk : Boolean = false

// Conditionals
if (riskScore > 80) {
  referralReason = "High risk score requires underwriter review"
} else if (riskScore > 50) {
  referralReason = "Moderate risk — consider additional conditions"
} else {
  referralReason = "Standard risk — approve"
}

// Collections
var coveredVehicles = policy.VehicleLines.first().Vehicles
for (vehicle in coveredVehicles) {
  vehicle.CollisionDeductible = 500
}

// Typelists (enumerations)
var status = PolicyStatus.TC_BOUND
var coverageType = CoverageType.TC_COMPREHENSIVE

// Date operations
var effectiveDate = Date.Today
var expirationDate = effectiveDate.addYears(1)

// Null safety
var contact = policy.Account?.Insured?.ContactName ?: "Unknown"
```

### Common Gosu Patterns in Insurance

| Pattern | Example |
|---------|---------|
| **Referral rule** | `if (newBusinessPremium > 50000) → refer to senior underwriter` |
| **Validation rule** | `if (vehicle.Year < 1980) → error "Vehicle too old for comprehensive"` |
| **Pre-fill rule** | `if (state == "FL") → setPIPRequired = true` |
| **Post-save rule** | `if (policy.status == Bound) → generate dec page` |
| **Batch query** | `SELECT p FROM Policy p WHERE p.Status = TC_BOUND` |

---

## 10.6.4 Integration Architecture

### Integration Patterns

Guidewire supports multiple integration patterns:

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **REST API** | HTTP/JSON endpoints | Digital channels, mobile apps, partner integrations |
| **SOAP API** | XML/SOAP web services | Legacy system integration, enterprise service bus |
| **Messaging (JMS)** | Asynchronous message queues | Batch processing, event-driven integration |
| **Batch (IImport/Export)** | File-based bulk data exchange | Data feeds, reporting, reconciliation |
| **Embedded (PCF plug-in)** | Inline UI integration | Third-party data display within Guidewire screens |
| **Guidewire Marketplace** | Pre-built partner integrations | ISO content, LexisNexis, Verisk |

### Common External Integrations

| System | Direction | Pattern | Purpose |
|--------|-----------|---------|---------|
| **ISO ClaimSearch** | Inbound | REST/SOAP | Claims history lookup |
| **MVR (DMV)** | Inbound | REST/SOAP | Driving record retrieval |
| **CLUE (Verisk)** | Inbound | REST/SOAP | Loss history report |
| **Credit Bureau** | Inbound | REST | Insurance score / credit check |
| **Payment Gateway** | Bidirectional | REST/JMS | Payment processing, ACH, card |
| **Document Management** | Bidirectional | REST | Store/retrieve policy documents |
| **Accounting/GL** | Outbound | Batch/JMS | Premium billing, loss payments |
| **Reinsurance** | Outbound | Batch | Ceded premium, treaty allocation |
| **CRM (Salesforce)** | Bidirectional | REST | Agent/customer relationship data |
| **Regulatory Reporting** | Outbound | Batch | State filings, Bordereaux |
| **Telematics/IoT** | Inbound | REST/Messaging | Usage-based insurance data |

### Guidewire Integration Center

| Component | Purpose |
|-----------|---------|
| **Integration Platform** | Manages all inbound/outbound integrations |
| **API Gateway** | Rate limiting, authentication, versioning |
| **Message Queue** | JMS-based async processing |
| **Integration Workshop** | Design-time tool for building integrations |
| **Integration Tester** | Test integrations in sandbox environment |

---

## 10.6.5 Data Migration

### Migration Process

| Step | Activity |
|------|----------|
| 1 | **Inventory** — Catalog all source systems, data entities, volumes |
| 2 | **Profile** — Assess data quality, completeness, duplicates |
| 3 | **Map** — Create source-to-target field mappings |
| 4 | **Transform** — Write transformation rules (Gosu scripts) |
| 5 | **Extract** — Pull data from legacy systems |
| 6 | **Load** — Import into Guidewire using IImport framework |
| 7 | **Validate** — Reconcile counts, spot-check records, run reports |
| 8 | **Certify** — Business sign-off on migrated data |

### Data Entities Typically Migrated

| Guidewire Entity | Source System | Key Fields |
|-----------------|---------------|------------|
| **Account** | Policy admin system | Account number, name, address, contact |
| **Policy** | Policy admin system | Policy number, term, status, effective dates |
| **PolicyLine** | Policy admin system | Line of business, coverage package |
| **Coverage** | Policy admin system | Coverage code, limit, deductible, premium |
| **Vehicle** | Auto policy system | VIN, make, model, year, garaging |
| **Location** | Property policy system | Address, occupancy, construction, protection |
| **Claim** | Claims system | Claim number, date of loss, cause, reserves |
| **Exposure** | Claims system | Coverage, liability, damage assessments |
| **ClaimPayment** | Claims system | Payee, amount, date, check number |
| **Producer** | Agent management | Agent code, name, license, appointments |
| **BillingAccount** | Billing system | Account number, payment plan, balance |

### Common Migration Challenges

| Challenge | Mitigation |
|-----------|-----------|
| **Data quality** | Profile early, establish data cleansing rules |
| **Orphaned records** | Map relationships before migration |
| **Terminology mismatch** | Create comprehensive cross-reference tables |
| **Volume** | Use parallel processing, migrate in batches |
| **Historical accuracy** | Validate against legacy system for 90 days post-migration |
| **In-flight transactions** | Define cutover rules for pending items |

---

## 10.6.6 Testing Strategy

### Testing Phases

| Phase | Scope | Duration | Entry Criteria |
|-------|-------|----------|----------------|
| **Unit Testing** | Individual configurations, rules, integrations | 4–8 weeks | Build complete |
| **Integration Testing (SIT)** | End-to-end workflows across all modules | 4–8 weeks | Unit testing passed |
| **System Testing** | Full system with all integrations | 2–4 weeks | SIT passed |
| **Performance Testing** | Load, stress, volume testing | 2–4 weeks | System testing passed |
| **User Acceptance Testing (UAT)** | Business validation of all processes | 4–8 weeks | Performance passed |
| **Security Testing** | Vulnerability assessment, penetration testing | 2–4 weeks | System testing passed |
| **Regression Testing** | Verify existing functionality not broken | Ongoing | After each change |

### Key Test Scenarios for P&C

| Scenario | Modules Involved |
|----------|------------------|
| New business submission → quote → bind → issue | PolicyCenter |
| Mid-term endorsement → premium change → dec page | PolicyCenter + BillingCenter |
| Renewal → rate change → non-renew option | PolicyCenter |
| Cancellation → pro-rata refund → notice | PolicyCenter + BillingCenter |
| FNOL → investigation → reserve → payment → close | ClaimCenter |
| Subrogation → recovery → claim closure | ClaimCenter |
| Premium installment → payment → commission | BillingCenter |
| Agent commission → statement → payment | BillingCenter |
| Reinsurance treaty → cession → recovery | PolicyCenter + ClaimCenter |
| Data migration → reconciliation → go-live | All modules |

---

## 10.6.7 Go-Live Checklist

| Category | Item |
|----------|------|
| **Data** | Migration validated, reconciliation complete |
| **Integrations** | All integrations tested in production environment |
| **Security** | SSO configured, roles assigned, audit enabled |
| **Document Templates** | All templates tested with production data |
| **Reporting** | Key reports validated against legacy system |
| **Users** | All users trained, roles assigned, access confirmed |
| **Processes** | Business procedures documented, help desk ready |
| **Cutover** | Cutover plan approved, rollback plan documented |
| **Monitoring** | Dashboards configured, alerts defined |
| **Hypercare** | Support team on standby, escalation paths confirmed |

---

## Key Takeaways

1. **Configuration is preferred** over customization — it is upgrade-safe and lower risk.
2. **Gosu** is Guidewire's language for business rules, extensions, and batch processes.
3. **Integration architecture** must account for all external systems from day one.
4. **Data migration** requires rigorous profiling, mapping, transformation, and validation.
5. **Testing** follows a structured progression from unit to UAT with clear entry/exit criteria.
6. **Go-live** requires coordinated cutover across data, integrations, users, and processes.

---

**Next:** [10.7 Guidewire Operations](07-guidewire-operations.md)