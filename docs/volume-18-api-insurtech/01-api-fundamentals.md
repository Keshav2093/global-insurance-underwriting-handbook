# 18.1 — API Fundamentals

> **Learning Objectives**
>
> After completing this chapter you should be able to:
>
> 1. Describe api fundamentals and its role in insurance integration.
> 2. Identify standards, patterns, and best practices.
> 3. Apply security and testing controls.
> 4. Integrate with core insurance platforms.

<!-- Metadata (for RAG / AI knowledge base)
keywords: api, insurtech, api-fundamentals
tags: api, insurtech, volume-18
categories: volume-18
related: volume-11, volume-13
-->

## Executive Summary

Insurance systems expose APIs for policy, claims, billing, and reference data. REST and event-driven integration dominate modern core platforms.

---

## 18.1.1 Key Concepts

| Concept | Description | Significance |
|---------|-------------|--------------|
| REST | Resource-oriented HTTP APIs | Most common |
| GraphQL | Flexible query API | Evolving |
| Events | Async messaging, streams | Decoupled integration |
| Versioning | Backward-compatible changes | API lifecycle |

---

## 18.1.2 Details

### API Styles

| Aspect | Description | Detail |
|--------|-------------|--------|
| REST | Resources, verbs, status codes | Most platforms |
| GraphQL | Client-defined queries | Complex aggregations |
| Webhooks | Server to client events | Notifications |
| Message queues | Guaranteed delivery | Core integration |

---

### API Lifecycle

| Aspect | Description | Detail |
|--------|-------------|--------|
| Design | OpenAPI spec | Contract first |
| Deploy | Gateway, versions | Blue/green |
| Monitor | Usage, errors, SLAs | Observability |
| Deprecate | Sunset headers | Migration plan |

---


## 18.1.3 Implementation Considerations

| Consideration | Action |
|---------------|--------|
| Standards | Use OpenAPI contracts |
| Security | Apply identity, transport, and runtime controls |
| Testing | Contract, integration, performance |
| Operations | Monitoring, versioning, deprecation |

---

## Review Questions

1. What are REST API constraints?\n2. When is event-driven integration preferred?\n3. Why is API versioning important?

---

## Glossary

| Term | Definition |
|------|------------|
| REST | Representational state transfer |\n| OpenAPI | API specification standard |

---

## Key Takeaways

1. **REST and events are the dominant integration styles.**\n2. **OpenAPI contracts enable testable, documented APIs.**\n3. **Versioning protects consumers during change.**

---

## References & Further Reading

- OpenAPI Specification — public docs
- ACORD — standards library (public summaries)
- Vendor API documentation (Guidewire, Duck Creek, Majesco)

---

**Previous:** [Volume 18 Home](index.md) | **Next:** [ACORD & Data Standards](02-acord-standards.md)

---

*Part of the Global Insurance Underwriting Handbook — Volume 18*
