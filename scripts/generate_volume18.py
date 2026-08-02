"""Generate Volume 18 - API & InsurTech Integration handbook chapters."""

from pathlib import Path

BASE = Path("docs/volume-18-api-insurtech")
BASE.mkdir(exist_ok=True)

INDEX = """# Volume 18 — API & InsurTech Integration

Volume 18 covers insurance APIs, integration patterns, and InsurTech: REST and event-driven architectures, ACORD and JSON standards, core platform integration (Guidewire, Duck Creek, Majesco), security, and testing.

## Chapters

| Chapter | Title | Contents |
|---------|-------|----------|
| [18.1](01-api-fundamentals.md) | API Fundamentals | REST, GraphQL, events, versioning |
| [18.2](02-acord-standards.md) | ACORD & Data Standards | ACORD, LOBs, JSON, XML |
| [18.3](03-guidewire-integration.md) | Guidewire Integration | PolicyCenter & ClaimCenter APIs |
| [18.4](04-duck-creek-integration.md) | Duck Creek Integration | DMS, MANO, integration patterns |
| [18.5](05-majesco-integration.md) | Majesco Integration | DigitalConnect, APIs |
| [18.6](06-security.md) | API Security | OAuth2, mTLS, threat controls |
| [18.7](07-testing.md) | API Testing | Contract testing, sandboxes, CI/CD |

## Learning Objectives

After completing this volume you should be able to:

1. Explain insurance API styles and standards.
2. Describe core platform integration patterns.
3. Apply security and identity requirements.
4. Design test and deployment strategies for insurance APIs.

## Suggested Reading

- Start with [18.1 API Fundamentals](01-api-fundamentals.md).
- Cross-reference Volumes 10–12 (platforms), Volume 13 (Business Analyst), Volume 11 (Duck Creek).

---

*Part of the Global Insurance Underwriting Handbook — Volume 18*
"""

CHAPTERS = [
    dict(num="1", title="API Fundamentals", file="01-api-fundamentals.md",
         intro="Insurance systems expose APIs for policy, claims, billing, and reference data. REST and event-driven integration dominate modern core platforms.",
         sections=[
            ("REST", "Resource-oriented HTTP APIs", "Most common"),
            ("GraphQL", "Flexible query API", "Evolving"),
            ("Events", "Async messaging, streams", "Decoupled integration"),
            ("Versioning", "Backward-compatible changes", "API lifecycle"),
         ],
         tables=[
            ("API Styles", [("REST", "Resources, verbs, status codes", "Most platforms"),
                            ("GraphQL", "Client-defined queries", "Complex aggregations"),
                            ("Webhooks", "Server to client events", "Notifications"),
                            ("Message queues", "Guaranteed delivery", "Core integration")]),
            ("API Lifecycle", [("Design", "OpenAPI spec", "Contract first"),
                               ("Deploy", "Gateway, versions", "Blue/green"),
                               ("Monitor", "Usage, errors, SLAs", "Observability"),
                               ("Deprecate", "Sunset headers", "Migration plan")]),
         ],
         review="1. What are REST API constraints?\\n2. When is event-driven integration preferred?\\n3. Why is API versioning important?",
         glossary="| REST | Representational state transfer |\\n| OpenAPI | API specification standard |",
         takeaways="1. **REST and events are the dominant integration styles.**\\n2. **OpenAPI contracts enable testable, documented APIs.**\\n3. **Versioning protects consumers during change.**",
         next="02-acord-standards.md", next_title="ACORD & Data Standards",
         prev="index.md", prev_title="Volume 18 Home",
         related="volume-11, volume-13"),
    dict(num="2", title="ACORD & Data Standards", file="02-acord-standards.md",
         intro="ACORD standards define common data formats for policy, claims, and billing exchange. JSON, XML, and EDI versions enable insurer and vendor interoperability.",
         sections=[
            ("ACORD", "Global data standards body", "Widely adopted"),
            ("LOB messages", "Line-of-business data models", "Policy and claim messages"),
            ("Formats", "XML, JSON, EDI", "Transmission standard"),
            ("Usage", "Legacy and modern integration", "Platform support varies"),
         ],
         tables=[
            ("ACORD Messages", [("Policy", "Quote, bind, policy issue", "100s series"),
                                ("Claims", "First notice, loss report", "Claims series"),
                                ("Billing", "Payment and statement", "Billing series"),
                                ("Reference", "Parties, locations", "Common data")]),
            ("Format Comparison", [("XML", "Mature, verbose", "Legacy systems"),
                                   ("JSON", "Lightweight, developer-friendly", "Modern APIs"),
                                   ("EDI", "Compact, batch", "Carrier legacy")]),
         ],
         review="1. What is ACORD?\\n2. Why does JSON matter for InsurTech APIs?\\n3. What are ACORD consumer integration (CI) standards?",
         glossary="| ACORD | Association for Cooperative Operations R&D |\\n| LOB | Line of business |",
         takeaways="1. **ACORD standards enable multi-vendor interoperability.**\\n2. **JSON is preferred in modern APIs.**\\n3. **Standardised messages reduce integration cost.**",
         next="03-guidewire-integration.md", next_title="Guidewire Integration",
         prev="01-api-fundamentals.md", prev_title="API Fundamentals",
         related="volume-11, volume-10"),
    dict(num="3", title="Guidewire Integration", file="03-guidewire-integration.md",
         intro="Guidewire exposes PolicyCenter, ClaimCenter, and BillingCenter APIs plus event messaging through the Integration Framework, enabling InsurTech and core-to-core integration.",
         sections=[
            ("PolicyCenter APIs", "Policy lifecycle endpoints", "REST APIs"),
            ("ClaimCenter APIs", "Claims data and tasks", "REST APIs"),
            ("Integration Framework", "Messaging and events", "Guidewire integration layer"),
            ("BillingCenter", "Billing and payment", "APIs and batch"),
         ],
         tables=[
            ("Guidewire APIs", [("PolicyCenter", "Quoting, policies", "Core data APIs"),
                                ("ClaimCenter", "Claims, FNOL", "Claims APIs"),
                                ("BillingCenter", "Invoices, payments", "Billing APIs"),
                                ("InfoCenter", "Reporting", "BI extracts")]),
            ("Integration Points", [("Fire & forget", "Event notifications", "Kafka / AMQP"),
                                    ("Request/reply", "Synchronous calls", "REST"),
                                    ("Batch", "Bulk extract / load", "ETL"),
                                    ("Screen Extensions", "UI integration", "Jutro / SPA")]),
         ],
         review="1. What APIs does PolicyCenter expose?\\n2. What is the Integration Framework?\\n3. When is batch integration preferred?",
         glossary="| Guidewire | Core insurance platform vendor |\\n| Integration Framework | Guidewire messaging layer |",
         takeaways="1. **Guidewire REST APIs cover policy, claims, and billing.**\\n2. **Event messaging enables real-time integration.**\\n3. **Batch remains essential for high-volume data.**",
         next="04-duck-creek-integration.md", next_title="Duck Creek Integration",
         prev="02-acord-standards.md", prev_title="ACORD & Data Standards",
         related="volume-10, volume-11"),
    dict(num="4", title="Duck Creek Integration", file="04-duck-creek-integration.md",
         intro="Duck Creek provides a SaaS-native insurance platform with APIs for policy, billing, and claims, plus MANO (modern architecture, API-first) integration patterns.",
         sections=[
            ("Duck Creek APIs", "Cloud-native with Swagger APIs", "API-first design"),
            ("MANO", "Modern architecture operating model", "Agile, product-centric"),
            ("Integration patterns", "Sync, async, event-driven", "Cloud microservices"),
            ("Data services", "Reference and transactional data", "MongoDB / APIs"),
         ],
         tables=[
            ("Duck Creek Capabilities", [("Policy", "Product lifecycle", "Policy APIs"),
                                         ("Billing", "Invoicing, payments", "Billing APIs"),
                                         ("Claims", "FNOL to settlement", "Claims APIs"),
                                         ("Insights", "Analytics platform", "Data services")]),
            ("MANO Principles", [("API-first", "Contracts before code", "Swagger/OpenAPI"),
                                 ("Cloud-native", "SaaS, microservices", "Azure platform"),
                                 ("Reusable components", "Service libraries", "Duck Creek APIs"),
                                 ("CI/CD", "Continuous delivery", "Integrated tooling")]),
         ],
         review="1. What is MANO?\\n2. How do Duck Creek APIs support InsurTech?\\n3. What integration patterns does Duck Creek support?",
         glossary="| MANO | Modern architecture operating model |\\n| Duck Creek | SaaS insurance platform |",
         takeaways="1. **Duck Creek is API-first and cloud-native.**\\n2. **MANO emphasises product-centric, agile delivery.**\\n3. **Event and REST patterns integrate the platform.**",
         next="05-majesco-integration.md", next_title="Majesco Integration",
         prev="03-guidewire-integration.md", prev_title="Guidewire Integration",
         related="volume-11, volume-12"),
    dict(num="5", title="Majesco Integration", file="05-majesco-integration.md",
         intro="Majesco provides DigitalConnect APIs and cloud solutions across policy, claims, and billing, enabling carriers to integrate distribution channels and InsurTech ecosystems.",
         sections=[
            ("DigitalConnect", "API integration hub", "Majesco APIs"),
            ("Core platforms", "Policy, claims, billing", "Cloud platform"),
            ("InsurTech partner", "Ecosystem integrations", "Partner APIs"),
            ("Modernisation", "Legacy to digital", "Batch + API"),
         ],
         tables=[
            ("Majesco APIs", [("Policy admin", "Lifecycle services", "Policy APIs"),
                              ("Claims", "FNOL and adjustment", "Claims APIs"),
                              ("Digital distribution", "Quoting, bind", "DigitalConnect"),
                              ("Customer", "Self-service", "Customer APIs")]),
            ("Integration Patterns", [("Direct API", "Real-time channel", "REST"),
                                      ("Event streams", "Asynchronous", "Messaging"),
                                      ("File transfer", "Legacy batch", "ETL"),
                                      ("Partner network", "InsurTech SaaS", "Marketplace")]),
         ],
         review="1. What is DigitalConnect?\\n2. How does Majesco support InsurTech partnerships?\\n3. When is batch used in Majesco integration?",
         glossary="| DigitalConnect | Majesco API platform |\\n| Majesco | Insurance software vendor |",
         takeaways="1. **DigitalConnect exposes Majesco platform APIs.**\\n2. **Real-time and partner integrations deepen ecosystems.**\\n3. **Batch remains for legacy and high-volume.**",
         next="06-security.md", next_title="API Security",
         prev="04-duck-creek-integration.md", prev_title="Duck Creek Integration",
         related="volume-12, volume-13"),
    dict(num="6", title="API Security", file="06-security.md",
         intro="Insurance APIs carry sensitive personal and financial data. Security requires strong identity, transport protection, and runtime threat controls.",
         sections=[
            ("OAuth2", "Delegated authorization", "Standard identity"),
            ("mTLS", "Mutual transport authentication", "High trust"),
            ("API keys", "Simple service credentials", "Low risk"),
            ("Threat controls", "Rate limits, validation, logging", "Runtime protection"),
         ],
         tables=[
            ("Security Mechanisms", [("OAuth2/JWT", "Token-based access", "Consumer APIs"),
                                     ("mTLS", "Mutual certs", "Partner/core"),
                                     ("API keys", "Identifier credentials", "Internal tools"),
                                     ("Audit logging", "Access evidence", "Compliance")]),
            ("Threat Controls", [("Rate limiting", "Prevent abuse", "Gateway"),
                                 ("Input validation", "Prevent injection", "Schema validation"),
                                 ("PII controls", "Data minimization", "Tokenization"),
                                 ("Monitoring", "Detect anomalies", "SIEM/alerting")]),
         ],
         review="1. Why is OAuth2 used for insurance APIs?\\n2. What is mTLS and when is it required?\\n3. How do rate limits protect APIs?",
         glossary="| OAuth2 | Authorization framework |\\n| mTLS | Mutual TLS |",
         takeaways="1. **OAuth2 and mTLS secure identity and transport.**\\n2. **Runtime controls prevent abuse and injection.**\\n3. **PII protection is a compliance requirement.**",
         next="07-testing.md", next_title="API Testing",
         prev="05-majesco-integration.md", prev_title="Majesco Integration",
         related="volume-13, volume-11"),
    dict(num="7", title="API Testing", file="07-testing.md",
         intro="API testing covers contract, integration, and performance testing, supported by sandbox environments and CI/CD pipelines in insurance technology programs.",
         sections=[
            ("Contract testing", "Verify API contracts", "Consumer-driven"),
            ("Sandbox", "Developer test environments", "Non-production"),
            ("CI/CD", "Automated pipelines", "Regression safety"),
            ("UAT", "Business acceptance", "Scenario-based"),
         ],
         tables=[
            ("Testing Levels", [("Unit", "Endpoint logic", "Code-level"),
                                ("Contract", "Request/response shape", "Schema checks"),
                                ("Integration", "End-to-end flows", "Real dependencies"),
                                ("Performance", "Load and latency", "Non-functional")]),
            ("Test Data", [("Synthetic", "Generated data", "Development"),
                           ("Masked", "Production-derived", "Realistic"),
                           ("Reference", "Curated test sets", "UAT scenarios")]),
         ],
         review="1. What is contract testing?\\n2. Why are sandboxes important?\\n3. What roles does CI/CD play?",
         glossary="| Contract testing | API schema verification |\\n| Sandbox | Isolated test environment |",
         takeaways="1. **Contract testing catches breaking API changes.**\\n2. **Sandboxes enable developer and partner testing.**\\n3. **CI/CD automates regression and release quality.**",
         next=None, next_title=None,
         prev="06-security.md", prev_title="API Security",
         related="volume-13, volume-10"),
]

(BASE / "index.md").write_text(INDEX, encoding="utf-8")


def render(c):
    intro_lines = "\n".join(f"| {s[0]} | {s[1]} | {s[2]} |" for s in c["sections"])
    tables = ""
    for title, rows in c["tables"]:
        body_rows = "\n".join(f"| {r[0]} | {r[1]} | {r[2]} |" for r in rows)
        tables += f"### {title}\n\n| Aspect | Description | Detail |\n|--------|-------------|--------|\n{body_rows}\n\n---\n\n"
    nxt = f"[{c['next_title']}]({c['next']})" if c["next"] else "— (end of volume)"
    prv = f"[{c['prev_title']}]({c['prev']})" if c["prev"] else "Volume 18 Home"
    return f"""# 18.{c['num']} — {c['title']}

> **Learning Objectives**
>
> After completing this chapter you should be able to:
>
> 1. Describe {c['title'].lower()} and its role in insurance integration.
> 2. Identify standards, patterns, and best practices.
> 3. Apply security and testing controls.
> 4. Integrate with core insurance platforms.

<!-- Metadata (for RAG / AI knowledge base)
keywords: api, insurtech, {c['title'].lower().replace(' ', '-')}
tags: api, insurtech, volume-18
categories: volume-18
related: {c['related']}
-->

## Executive Summary

{c['intro']}

---

## 18.{c['num']}.1 Key Concepts

| Concept | Description | Significance |
|---------|-------------|--------------|
{intro_lines}

---

## 18.{c['num']}.2 Details

{tables}
## 18.{c['num']}.3 Implementation Considerations

| Consideration | Action |
|---------------|--------|
| Standards | Use OpenAPI contracts |
| Security | Apply identity, transport, and runtime controls |
| Testing | Contract, integration, performance |
| Operations | Monitoring, versioning, deprecation |

---

## Review Questions

{c['review']}

---

## Glossary

| Term | Definition |
|------|------------|
{c['glossary']}

---

## Key Takeaways

{c['takeaways']}

---

## References & Further Reading

- OpenAPI Specification — public docs
- ACORD — standards library (public summaries)
- Vendor API documentation (Guidewire, Duck Creek, Majesco)

---

**Previous:** {prv} | **Next:** {nxt}

---

*Part of the Global Insurance Underwriting Handbook — Volume 18*
"""


for c in CHAPTERS:
    (BASE / c["file"]).write_text(render(c), encoding="utf-8")
    print(f"Created {c['file']}")

print("Volume 18 generation complete.")