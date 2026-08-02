# 12.6 — Implementation & Integration

## 12.6.1 Implementation Methodology

### Majesco Delivery Approach

| Phase | Duration | Key Activities |
|-------|----------|----------------|
| **Discover** | 4–8 weeks | Current state, requirements, blueprint |
| **Configure** | 10–18 weeks | Product accelerator, rules, Ratabase, workflows |
| **Integrate** | 6–10 weeks | APIs, event flows, portals |
| **Test** | 6–10 weeks | SIT, UAT, performance |
| **Deploy** | 2–4 weeks | Data migration, cutover |
| **Hypercare** | 4–8 weeks | Stabilization, support |

### Scenario-Based Delivery

| Scenario | Description | Best For |
|----------|-------------|----------|
| **Select** | Preconfigured industry-ready products | Standard personal lines |
| **Config** | Moderate configuration of platform | Regional, mid-size insurers |
| **Full Build** | Extensive customization | Complex commercial lines |

---

## 12.6.2 Implementation Team

| Role | Responsibility |
|------|---------------|
| **Program Manager** | Delivery, timeline, budget |
| **Solution Architect** | Platform and integration design |
| **Product Configurator** | Product Accelerator configuration |
| **Rating Analyst** | Ratabase rating tables and formulas |
| **Integration Developer** | API and event development |
| **Data Migration Lead** | Legacy data extraction and load |
| **Test Manager** | Test planning and execution |
| **Business Analyst** | Requirements and UAT |
| **Change Manager** | Training and adoption |

---

## 12.6.3 Configuration Approach

### Product Accelerator Configuration

| Activity | Description |
|----------|-------------|
| Product scoping | Lines, states, products |
| Product build | Coverages, limits, deductibles |
| Rating setup | Rate tables, factors, formulas |
| Rules configuration | Validation, referrals |
| Document templates | Dec pages, forms |
| Workflow design | Screens, tasks, approvals |
| Reference data | Types, statuses, reasons |

### Customization Guidelines

| Customization | When Needed | Risk |
|---------------|-------------|------|
| Model extension | New data structures | Medium |
| Custom APIs | Unique integration | Medium |
| Service customization | Complex logic | High |
| UI customization | Custom screens | Medium |
| Batch jobs | Unique processes | Medium |

> **Best practice:** Configuration-first. Customize sparingly to protect upgradeability.

---

## 12.6.4 Integration

### Integration Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| REST API | Sync HTTP/JSON | Portals, partners |
| Event Hub | Async event streaming | Real-time sync |
| Logic Apps | Workflow automation | Orchestration |
| Batch | File/SFTP | Data warehouse, GL |
| Message queue | Async messaging | Transactions |

### Typical Integrations

| Integration | Direction | Pattern |
|-------------|-----------|---------|
| Agent portal | Bidirectional | REST |
| Customer portal | Bidirectional | REST |
| MVR service | Outbound | REST |
| Credit bureau | Outbound | REST |
| Payment processor | Bidirectional | REST/Event |
| Document management | Bidirectional | REST |
| Data warehouse | Outbound | Event/Batch |
| GL/Accounting | Outbound | Batch |

---

## 12.6.5 DevOps and Environment Management

### Environments

| Environment | Purpose |
|-------------|---------|
| Development | Configuration, development |
| System test | Integration testing |
| UAT | Business validation |
| Performance | Load testing |
| Production | Live operations |
| DR | Disaster recovery |

### Release Pipeline

```
Config/Code → Build → Test → Deploy → SIT → QA → UAT → Production
```

### Tools

| Tool | Purpose |
|------|---------|
| Azure DevOps | CI/CD, repos |
| GitHub | Source control |
| Terraform | Infrastructure as code |
| Kubernetes | Container orchestration |
| Azure Monitor | Observability |
| Azure App Insights | Application monitoring |

---

## 12.6.6 Data Migration

### Migration Steps

| Step | Activity |
|------|----------|
| 1. Inventory | Identify source data |
| 2. Scope | Determine entities to migrate |
| 3. Profile | Assess data quality |
| 4. Map | Source-to-target mapping |
| 5. Transform | Normalize codes, values |
| 6. Load | Import via API/batch |
| 7. Validate | Reconcile counts, values |
| 8. Cutover | Final migration |

### Migration Challenges

| Challenge | Mitigation |
|-----------|-----------|
| Policy history | Migrate active policies |
| Claims history | Preserve for actuarial |
| Terminology | Map legacy codes |
| Data quality | Cleanse before load |
| Volume | Batch in stages |
| Guarantees | Business validation |

---

## 12.6.7 Testing

### Test Types

| Test | Scope |
|------|-------|
| Configuration testing | Products, rates, rules |
| Integration testing | APIs, events |
| Functional testing | End-to-end processes |
| Regression testing | No breakage |
| Performance testing | Load, response times |
| Security testing | Vulnerability, access |
| UAT | Business sign-off |

### Key Test Scenarios

| Scenario | Modules |
|----------|---------|
| Quote → bind → issue | Policy |
| Endorsement → premium | Policy + Billing |
| Renewal → billed | Policy + Billing |
| Cancellation → refund | Policy + Billing |
| FNOL → payment | Claims |
| Direct bill → installment | Billing |
| Agent commission | Billing |

---

## 12.6.8 Operations

### Responsibility Split

| Function | Owner |
|----------|-------|
| Infrastructure | Majesco (Azure) |
| Database | Majesco |
| Platform monitoring | Majesco + Customer |
| Security | Shared |
| Data corrections | Customer |
| Product changes | Customer (Accelerator) |
| User admin | Customer |
| Integrations | Customer + Partners |

### Support Model

| Tier | Responsibility |
|------|---------------|
| Tier 1 | Customer help desk |
| Tier 2 | Customer technical team |
| Tier 3 | Majesco platform support |
| Vendor | Third parties |

---

## Key Takeaways

1. **Majesco scenarios** (Select, Config, Full Build) tailor implementation effort.
2. **Product Accelerator configuration** is the primary build activity.
3. **REST + Event Hub** drive modern integration.
4. **Cloud DevOps** manages environment, release, and testing.
5. **Data migration** requires structured mapping and validation.
6. **Operations** are shared between Majesco and customer.

---

**Back to:** [Volume 12 Index](index.md)