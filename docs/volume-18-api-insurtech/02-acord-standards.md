# 18.2 — ACORD & Data Standards

> **Learning Objectives**
>
> After completing this chapter you should be able to:
>
> 1. Describe acord & data standards and its role in insurance integration.
> 2. Identify standards, patterns, and best practices.
> 3. Apply security and testing controls.
> 4. Integrate with core insurance platforms.

<!-- Metadata (for RAG / AI knowledge base)
keywords: api, insurtech, acord-&-data-standards
tags: api, insurtech, volume-18
categories: volume-18
related: volume-11, volume-10
-->

## Executive Summary

ACORD standards define common data formats for policy, claims, and billing exchange. JSON, XML, and EDI versions enable insurer and vendor interoperability.

---

## 18.2.1 Key Concepts

| Concept | Description | Significance |
|---------|-------------|--------------|
| ACORD | Global data standards body | Widely adopted |
| LOB messages | Line-of-business data models | Policy and claim messages |
| Formats | XML, JSON, EDI | Transmission standard |
| Usage | Legacy and modern integration | Platform support varies |

---

## 18.2.2 Details

### ACORD Messages

| Aspect | Description | Detail |
|--------|-------------|--------|
| Policy | Quote, bind, policy issue | 100s series |
| Claims | First notice, loss report | Claims series |
| Billing | Payment and statement | Billing series |
| Reference | Parties, locations | Common data |

---

### Format Comparison

| Aspect | Description | Detail |
|--------|-------------|--------|
| XML | Mature, verbose | Legacy systems |
| JSON | Lightweight, developer-friendly | Modern APIs |
| EDI | Compact, batch | Carrier legacy |

---


## 18.2.3 Implementation Considerations

| Consideration | Action |
|---------------|--------|
| Standards | Use OpenAPI contracts |
| Security | Apply identity, transport, and runtime controls |
| Testing | Contract, integration, performance |
| Operations | Monitoring, versioning, deprecation |

---

## Review Questions

1. What is ACORD?\n2. Why does JSON matter for InsurTech APIs?\n3. What are ACORD consumer integration (CI) standards?

---

## Glossary

| Term | Definition |
|------|------------|
| ACORD | Association for Cooperative Operations R&D |\n| LOB | Line of business |

---

## Key Takeaways

1. **ACORD standards enable multi-vendor interoperability.**\n2. **JSON is preferred in modern APIs.**\n3. **Standardised messages reduce integration cost.**

---

## References & Further Reading

- OpenAPI Specification — public docs
- ACORD — standards library (public summaries)
- Vendor API documentation (Guidewire, Duck Creek, Majesco)

---

**Previous:** [API Fundamentals](01-api-fundamentals.md) | **Next:** [Guidewire Integration](03-guidewire-integration.md)

---

*Part of the Global Insurance Underwriting Handbook — Volume 18*
