# 11.6 — Implementation & Integration

## 11.6.1 Implementation Methodology

### Duck Creek Delivery Approach

| Phase | Duration | Key Activities |
|-------|----------|----------------|
| **Discover** | 4–8 weeks | Current state, target state, gap analysis, solution blueprint |
| **Build** | 12–20 weeks | Product configuration (ProductIX), rules, API development |
| **Test** | 6–12 weeks | SIT, UAT, performance, security testing |
| **Deploy** | 2–4 weeks | Data migration, cutover, go-live |
| **Hypercare** | 4–8 weeks | Support, stabilization, fixes |

### Cloud Delivery Advantages

| Advantage | Description |
|-----------|-------------|
| **No infrastructure** | No servers, databases, or patching to manage |
| **Rapid provisioning** | Environments provisioned automatically |
| **Disaster recovery** | Built-in Azure regional redundancy |
| **Automatic upgrades** | Platform updates handled by Duck Creek |
| **Scalability** | Auto-scaling to handle peak volumes |
| **Security** | Azure enterprise-grade security |

---

## 11.6.2 Implementation Team

| Role | Responsibility |
|------|---------------|
| **Engagement Manager** | Program delivery, timeline, budget |
| **Solution Architect** | Platform design, integration architecture |
| **Product Analyst** | ProductIX configuration, product build |
| **Rules Developer** | Business rules, workflows |
| **API Developer** | Integration development (.NET) |
| **Data Migration Lead** | Legacy data extraction, transformation, loading |
| **Test Lead** | Test planning, execution, defect management |
| **Business Analyst** | Requirements, process mapping, UAT |
| **Change Manager** | Training, communication, adoption |

---

## 11.6.3 Configuration Approach

### ProductIX Configuration

| Activity | Description |
|----------|-------------|
| **Product scoping** | Define lines, states, products to build |
| **Product build** | Configure coverages, limits, modifiers, rating |
| **Rules configuration** | Entry/exit rules, validation, referrals |
| **Document templates** | Dec pages, forms, notices |
| **Rate tables** | Load base rates, territories, factors |
| **Reference data** | Configure statuses, types, reason codes |
| **Testing** | Product testing against expected results |

### Customization (Code)

| Customization | When Needed | Requires Duck Creek Approval |
|---------------|-------------|------------------------------|
| **Server-side rules (C#)** | Complex business logic | Yes |
| **UI customization** | Custom screens | Yes |
| **API extensions** | New endpoints | Yes |
| **External service calls** | Custom integrations | Yes |
| **Scheduled jobs** | Custom batch processes | Yes |

> **Best practice:** Use configuration where possible. Customization increases upgrade risk and cost.

---

## 11.6.4 Integration Architecture

### Integration Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **REST API** | Synchronous HTTP/JSON | Portals, partner systems |
| **Event hub** | Asynchronous event streaming | Real-time data sync |
| **Azure Logic Apps** | Workflow automation | System orchestration |
| **BI reports** | Data extracts | Data warehouse |
| **File transfer** | SFTP/flat files | Batch data exchange |
| **Message queue** | JMS/Service Bus | Async transactions |

### Duck Creek API

| API Feature | Description |
|-------------|-------------|
| **REST endpoints** | All applications expose REST APIs |
| **API gateway** | Centralized endpoint management |
| **Authentication** | OAuth 2.0 / Azure AD |
| **Versioning** | API versioning for backward compatibility |
| **Rate limiting** | Throttle excessive calls |
| **Documentation** | Interactive API docs (Swagger/OpenAPI) |

### Common Integration Scenarios

| Integration | Direction | Pattern |
|-------------|-----------|---------|
| **Agent portal** | Bidirectional | REST API |
| **Customer portal** | Bidirectional | REST API |
| **MVR service** | Outbound | REST |
| **Credit bureau** | Outbound | REST |
| **Property data vendor** | Outbound | REST |
| **Payment processor** | Bidirectional | REST/Event Hub |
| **Document management** | Bidirectional | REST |
| **Data warehouse** | Outbound | Event Hub/Batch |
| **GL/Accounting** | Outbound | Batch |
| **Reinsurance admin** | Outbound | File transfer |

---

## 11.6.5 DevOps and Delivery

### Environment Management (OnDemand)

| Environment | Purpose |
|-------------|---------|
| **Development** | Product configuration, rules development |
| **Testing** | SIT, system testing |
| **UAT** | Business validation |
| **Perf** | Performance testing |
| **Production** | Live operations |
| **DR** | Disaster recovery |

### Release Pipeline

```
Code/Config → Build → Test → Deploy to Test → SIT → QA → UAT → Production
```

### Release Management

| Tool | Purpose |
|------|---------|
| **Azure DevOps** | CI/CD, repos, pipelines |
| **GitHub** | Source control |
| **Duck Creek Administrator** | Environment provisioning, release |
| **Duck Creek QA** | Test case execution |
| **Duck Creek Style** | UI regression testing |
| **ProductIX** | Product release management |

---

## 11.6.6 Data Migration

### Migration Approach

| Step | Activity |
|------|----------|
| **1. Inventory** | Identify source systems and data entities |
| **2. Define scope** | Determine what to migrate (policies, claims, billing) |
| **3. Profile data** | Assess quality, completeness |
| **4. Map fields** | Source-to-target mapping |
| **5. Transform** | Normalize codes, dates, values |
| **6. Load** | Import into Duck Creek via API or file |
| **7. Validate** | Reconcile counts, value checks |
| **8. Cutover** | Final migration before go-live |

### Migration Challenges

| Challenge | Mitigation |
|-----------|-----------|
| **Policy history** | Migrate only active policies where practical |
| **Claims history** | Preserve historical claim data for actuarial use |
| **Terminology** | Map legacy codes to Duck Creek typelists |
| **Data quality** | Cleanse before migration |
| **Volume** | Batch load in stages |
| **Guarantees** | Validate with business sign-off |

---

## 11.6.7 Testing Strategy

### Test Types

| Test | Scope |
|------|-------|
| **Configuration testing** | Products, rates, rules, documents |
| **Integration testing** | API connections, event flows |
| **Functional testing** | End-to-end business processes |
| **Regression testing** | Verify no breakage after changes |
| **Performance testing** | Response times, throughput |
| **Security testing** | Vulnerability, access control |
| **UAT** | Business user acceptance |

### Key Test Scenarios

| Scenario | Modules |
|----------|---------|
| New business quote → bind → issue | Author |
| Endorsement → additional premium → invoice | Author + Billing |
| Renewal → generated → accepted → billed | Author + Billing |
| Cancellation → refund → commission reversal | Author + Billing |
| FNOL → assignment → investigation → payment | Claims |
| Direct bill → installment → payment | Billing |
| Agent bill → statement → commission | Billing |
| Report validation → data warehouse refresh | Insight |

---

## 11.6.8 Operations

### Day-to-Day Operations

| Function | Owner |
|----------|-------|
| **Infrastructure** | Duck Creek (Azure) |
| **Database administration** | Duck Creek |
| **Application monitoring** | Duck Creek + Customer |
| **Security** | Duck Creek + Customer |
| **Data corrections** | Customer |
| **Product changes** | Customer (ProductIX) |
| **User administration** | Customer |
| **Integrations** | Customer + partners |

### Support Model

| Tier | Responsibility |
|------|---------------|
| **Tier 1** | Customer help desk — user issues |
| **Tier 2** | Customer technical team — config/rules issues |
| **Tier 3** | Duck Creek support — platform issues |
| **Vendor** | Third-party integrations |

---

## Key Takeaways

1. **Duck Creek implementations are shorter and cloud-delivered** — no infrastructure to manage.
2. **ProductIX configuration is the primary build activity** — no-code product development.
3. **Customization should be minimized** to reduce upgrade risk.
4. **REST APIs and Event Hubs** enable modern integration.
5. **OnDemand environments** support full delivery lifecycle.
6. **Data migration** requires disciplined mapping, loading, and validation.
7. **Operations** split platform responsibility between Duck Creek and the customer.

---

**Back to:** [Volume 11 Index](index.md)