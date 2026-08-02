# 18.3 — Guidewire Integration

> **Learning Objectives**
>
> After completing this chapter you should be able to:
>
> 1. Describe guidewire integration and its role in insurance integration.
> 2. Identify standards, patterns, and best practices.
> 3. Apply security and testing controls.
> 4. Integrate with core insurance platforms.

<!-- Metadata (for RAG / AI knowledge base)
keywords: api, insurtech, guidewire-integration
tags: api, insurtech, volume-18
categories: volume-18
related: volume-10, volume-11
-->

## Executive Summary

Guidewire exposes PolicyCenter, ClaimCenter, and BillingCenter APIs plus event messaging through the Integration Framework, enabling InsurTech and core-to-core integration.

---

## 18.3.1 Key Concepts

| Concept | Description | Significance |
|---------|-------------|--------------|
| PolicyCenter APIs | Policy lifecycle endpoints | REST APIs |
| ClaimCenter APIs | Claims data and tasks | REST APIs |
| Integration Framework | Messaging and events | Guidewire integration layer |
| BillingCenter | Billing and payment | APIs and batch |

---

## 18.3.2 Details

### Guidewire APIs

| Aspect | Description | Detail |
|--------|-------------|--------|
| PolicyCenter | Quoting, policies | Core data APIs |
| ClaimCenter | Claims, FNOL | Claims APIs |
| BillingCenter | Invoices, payments | Billing APIs |
| InfoCenter | Reporting | BI extracts |

---

### Integration Points

| Aspect | Description | Detail |
|--------|-------------|--------|
| Fire & forget | Event notifications | Kafka / AMQP |
| Request/reply | Synchronous calls | REST |
| Batch | Bulk extract / load | ETL |
| Screen Extensions | UI integration | Jutro / SPA |

---


## 18.3.3 Implementation Considerations

| Consideration | Action |
|---------------|--------|
| Standards | Use OpenAPI contracts |
| Security | Apply identity, transport, and runtime controls |
| Testing | Contract, integration, performance |
| Operations | Monitoring, versioning, deprecation |

---

## Review Questions

1. What APIs does PolicyCenter expose?\n2. What is the Integration Framework?\n3. When is batch integration preferred?

---

## Glossary

| Term | Definition |
|------|------------|
| Guidewire | Core insurance platform vendor |\n| Integration Framework | Guidewire messaging layer |

---

## Key Takeaways

1. **Guidewire REST APIs cover policy, claims, and billing.**\n2. **Event messaging enables real-time integration.**\n3. **Batch remains essential for high-volume data.**

---

## References & Further Reading

- OpenAPI Specification — public docs
- ACORD — standards library (public summaries)
- Vendor API documentation (Guidewire, Duck Creek, Majesco)

---

**Previous:** [ACORD & Data Standards](02-acord-standards.md) | **Next:** [Duck Creek Integration](04-duck-creek-integration.md)

---

*Part of the Global Insurance Underwriting Handbook — Volume 18*
