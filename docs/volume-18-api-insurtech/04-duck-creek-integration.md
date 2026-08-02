# 18.4 — Duck Creek Integration

> **Learning Objectives**
>
> After completing this chapter you should be able to:
>
> 1. Describe duck creek integration and its role in insurance integration.
> 2. Identify standards, patterns, and best practices.
> 3. Apply security and testing controls.
> 4. Integrate with core insurance platforms.

<!-- Metadata (for RAG / AI knowledge base)
keywords: api, insurtech, duck-creek-integration
tags: api, insurtech, volume-18
categories: volume-18
related: volume-11, volume-12
-->

## Executive Summary

Duck Creek provides a SaaS-native insurance platform with APIs for policy, billing, and claims, plus MANO (modern architecture, API-first) integration patterns.

---

## 18.4.1 Key Concepts

| Concept | Description | Significance |
|---------|-------------|--------------|
| Duck Creek APIs | Cloud-native with Swagger APIs | API-first design |
| MANO | Modern architecture operating model | Agile, product-centric |
| Integration patterns | Sync, async, event-driven | Cloud microservices |
| Data services | Reference and transactional data | MongoDB / APIs |

---

## 18.4.2 Details

### Duck Creek Capabilities

| Aspect | Description | Detail |
|--------|-------------|--------|
| Policy | Product lifecycle | Policy APIs |
| Billing | Invoicing, payments | Billing APIs |
| Claims | FNOL to settlement | Claims APIs |
| Insights | Analytics platform | Data services |

---

### MANO Principles

| Aspect | Description | Detail |
|--------|-------------|--------|
| API-first | Contracts before code | Swagger/OpenAPI |
| Cloud-native | SaaS, microservices | Azure platform |
| Reusable components | Service libraries | Duck Creek APIs |
| CI/CD | Continuous delivery | Integrated tooling |

---


## 18.4.3 Implementation Considerations

| Consideration | Action |
|---------------|--------|
| Standards | Use OpenAPI contracts |
| Security | Apply identity, transport, and runtime controls |
| Testing | Contract, integration, performance |
| Operations | Monitoring, versioning, deprecation |

---

## Review Questions

1. What is MANO?\n2. How do Duck Creek APIs support InsurTech?\n3. What integration patterns does Duck Creek support?

---

## Glossary

| Term | Definition |
|------|------------|
| MANO | Modern architecture operating model |\n| Duck Creek | SaaS insurance platform |

---

## Key Takeaways

1. **Duck Creek is API-first and cloud-native.**\n2. **MANO emphasises product-centric, agile delivery.**\n3. **Event and REST patterns integrate the platform.**

---

## References & Further Reading

- OpenAPI Specification — public docs
- ACORD — standards library (public summaries)
- Vendor API documentation (Guidewire, Duck Creek, Majesco)

---

**Previous:** [Guidewire Integration](03-guidewire-integration.md) | **Next:** [Majesco Integration](05-majesco-integration.md)

---

*Part of the Global Insurance Underwriting Handbook — Volume 18*
