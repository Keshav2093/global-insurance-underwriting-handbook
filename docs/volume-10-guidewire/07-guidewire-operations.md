# 10.7 — Guidewire Operations

Operating Guidewire in production requires disciplined testing, deployment, upgrade, and cloud operations practices. This chapter covers the operational lifecycle of the platform.

---

## 10.7.1 Testing and Quality Assurance

### Test Environment Strategy

| Environment | Purpose | Data | Refresh Frequency |
|-------------|---------|------|-------------------|
| **Developer (Sandbox)** | Individual development and GitHub integration | Synthetic | Continuous |
| **Integration (SIT)** | Cross-module testing, integration testing | Masked production | Weekly |
| **QA** | Functional and regression testing | Masked production | Per release |
| **UAT** | Business validation, user sign-off | Masked production | Per release |
| **Performance** | Load, stress, volume testing | Synthesized large volume | Per release |
| **Production** | Live system | Production | N/A |

### Test Automation

Guidewire supports automation through multiple tools:

| Tool | Purpose | Used For |
|------|---------|----------|
| **JUnit / TestNG** | Unit testing of Gosu code | Rules, extensions, validations |
| **Guidewire Test Automation Framework** | UI test automation | Screen flows, user journeys |
| **SoapUI / Postman** | API testing | REST/SOAP integrations |
| **JMeter** | Performance testing | Load testing |
| **Selenium** | Browser-based UI testing | End-to-end user flows |
| **Jenkins / GitHub Actions** | CI/CD orchestration | Build and deploy pipelines |

### Test Data Management

| Consideration | Approach |
|---------------|----------|
| **Data masking** | Mask PII, payment card data, medical data |
| **Reference data** | Synchronize lookup tables across environments |
| **Data volumes** | Performance testing needs 10x production volume |
| **Date simulation** | Use Guidewire's time travel feature for renewals, billing |
| **Integration stubs** | Mock external systems during SIT |

---

## 10.7.2 Continuous Integration / Continuous Deployment (CI/CD)

### CI/CD Pipeline Stages

```
Commit → Build → Unit Test → Static Analysis → Package → Deploy to SIT → Integration Test → Deploy to QA → UAT → Deploy to Production
```

### Guidewire DevOps Tools

| Tool | Purpose |
|------|---------|
| **GitHub** | Source control for configuration and extensions |
| **Jenkins** | CI/CD orchestration for builds and deployments |
| **Guidewire Studio** | Development and build environment |
| **Gradle / Ant** | Build automation |
| **Artifactory / Nexus** | Binary repository for built artifacts |
| **SonarQube** | Code quality and security scanning |
| **Deployment Manager** | Guidewire cloud deployment automation |
| **Environment Manager** | Cloud environment provisioning |
| **Release Manager** | Versioning, tagging, release planning |

### Build Management

| Element | Description |
|---------|-------------|
| **Source Control** | Git repository per Guidewire module (PC, CC, BC) |
| **Branching Strategy** | Feature branches → develop → release branches |
| **Versioning** | Semantic versioning (e.g., 1.2.3) |
| **Artifact Naming** | Module + version + build number |
| **Release Notes** | Automated from commit messages |
| **Tagging** | Gold build tags for production release |

---

## 10.7.3 Deployment Management

### Deployment Types

| Type | Description | Downtime | When Used |
|------|-------------|----------|-----------|
| **Standard Deployment** | Configuration and extension deployment | Minimal | Regular releases |
| **Hotfix Deployment** | Emergency fix | Minimal | Production incidents |
| **Upgrade Deployment** | Guidewire product version upgrade | Scheduled downtime | Major upgrades |
| **Patch Deployment** | Single-service patch | None | Micro-fixes |
| **Data Deployment** | Rate table, reference data update | None | Content updates |

### Deployment Checklist

| Phase | Activities |
|-------|-----------|
| **Pre-deployment** | Freeze code, validate artifacts, backup production |
| **Deployment** | Execute deployment plan, monitor progress, verify services |
| **Post-deployment** | Smoke test, data validation, report validation, user notification |
| **Rollback** | Revert to previous version if critical failure |
| **Documentation** | Record deployment results, known issues |

### Smoke Test Checklist After Deployment

| Area | Test |
|------|------|
| **Login** | All user roles can log in |
| **PolicyCenter** | Search policy, open policy, run quote |
| **ClaimCenter** | Open claim, update exposure, record payment |
| **BillingCenter** | View invoice, process payment, run statement |
| **Integrations** | Confirmed API endpoints respond correctly |
| **Reports** | Top 5 critical reports run successfully |
| **Batch** | Scheduled jobs completed without error |

---

## 10.7.4 Upgrade Management

### Upgrade Frequency

Guidewire typically releases:

| Release Type | Frequency | Example |
|--------------|-----------|---------|
| **Major Release** | Annual | Guidewire Cloud 10.x |
| **Minor Release** | Quarterly | 10.1, 10.2 |
| **Service Packs** | Monthly | Security fixes, patches |
| **Data Updates** | Monthly | ISO, NCCI content updates |

### Upgrade Process

| Phase | Duration | Activities |
|-------|----------|-----------|
| **1. Impact Assessment** | 2–4 weeks | Review release notes, identify affected customizations |
| **2. Sandbox Upgrade** | 2–4 weeks | Apply upgrade in sandbox, resolve conflicts |
| **3. Integration Testing** | 2–4 weeks | Test all integrations against upgraded system |
| **4. UAT** | 2–4 weeks | Business validation of upgraded functionality |
| **5. Performance Testing** | 1–2 weeks | Load test upgraded environment |
| **6. Production Upgrade** | 1 weekend | Apply upgrade, run smoke tests |
| **7. Stabilization** | 2–4 weeks | Monitor, fix defects, hypercare |

### Upgrade Conflict Handling

| Conflict Type | Description | Resolution |
|---------------|-------------|-----------|
| **Configuration conflict** | Changes to same configuration element | Merge after review |
| **Extension conflict** | Code changes to same class | Code review, manual merge |
| **API change** | Deprecated or changed API | Rewrite extension |
| **Data model change** | New or changed entity fields | Data migration script |
| **Workflow change** | Modified or removed workflow | Reconfigure workflow |

---

## 10.7.5 Guidewire Cloud Operations

### AWS Cloud Architecture

Guidewire Cloud runs on AWS. Typical architecture:

| Component | AWS Service | Purpose |
|-----------|-------------|---------|
| **Compute** | EC2 instances | Application servers |
| **Database** | RDS (Oracle/PostgreSQL) | PolicyCenter, ClaimCenter, BillingCenter databases |
| **Caching** | ElastiCache (Redis) | Session caching, performance |
| **Storage** | S3 | Document storage, batch files |
| **Networking** | VPC, ALB, Route 53 | Network infrastructure, load balancing |
| **Security** | IAM, KMS, Security Groups | Access control, encryption |
| **Monitoring** | CloudWatch, New Relic | Performance monitoring |
| **Logging** | Splunk, ELK | Application and audit logs |

### Environment Types

| Environment | Purpose | Used By |
|-------------|---------|---------|
| **Production** | Live business operations | All users |
| **DR (Disaster Recovery)** | Failover on regional disaster | Automated |
| **Staging** | Final validation before production | Release team |
| **UAT** | User acceptance testing | Business users |
| **SIT** | Integration testing | QA team |
| **Sandbox** | Development and testing | Developers |

### Cloud Operations Responsibilities

| Function | Guidewire Responsibility | Customer Responsibility |
|----------|--------------------------|-------------------------|
| **Infrastructure** | AWS management, patching, scaling | None |
| **Database** | Backups, recovery, tuning | Point-in-time restore requests |
| **Security** | Platform security, SSO integration | User access management |
| **Monitoring** | Platform monitoring, alerting | Business process monitoring |
| **Upgrades** | Platform upgrades | Configuration testing |
| **Incident Management** | Platform incidents | Report to Guidewire support |
| **Capacity Planning** | Auto-scaling, capacity management | Volume forecasting |

---

## 10.7.6 Incident Management

### Incident Severity Levels

| Severity | Definition | Response Target | Example |
|----------|-----------|-----------------|---------|
| **SEV1** | Production down, no workaround | 15 minutes | All users cannot log in |
| **SEV2** | Major functionality impaired | 1 hour | Policy issuance failing |
| **SEV3** | Minor functionality affected | 4 hours | Report formatting issue |
| **SEV4** | Cosmetic or low impact | Next business day | Field label typo |

### Incident Management Process

```
Detection → Triage → Containment → Resolution → Verification → Post-Mortem
```

| Step | Key Activities |
|------|---------------|
| **Detection** | User report, monitoring alert, batch failure |
| **Triage** | Assess severity, assign resolver group |
| **Containment** | Prevent further impact, apply workaround |
| **Resolution** | Fix root cause, hotfix deployment if needed |
| **Verification** | Confirm resolution, monitor for recurrence |
| **Post-Mortem** | Root cause analysis, corrective actions, timeline review |

### Common Production Incidents

| Incident | Likely Cause | Immediate Action |
|----------|--------------|------------------|
| **Login failure** | SSO misconfiguration, database connection issue | Check SSO logs, verify DB connectivity |
| **Slow performance** | Database contention, high volume, missing index | Review DB waits, check monitoring |
| **Batch failure** | Data issue, integration outage | Review batch logs, re-run batch |
| **Report failure** | Data model change, report template issue | Check report logs, verify data |
| **Integration failure** | External system down, timeout, authentication | Check integration logs, verify credentials |
| **Document rendering failure** | Template error, data mismatch | Review document logs, test template |

---

## 10.7.7 Monitoring and Alerting

### Key Metrics

| Category | Metric | Alert Threshold |
|----------|--------|-----------------|
| **Availability** | Application uptime | < 99.5% |
| **Performance** | Response time | > 3 seconds average |
| **Performance** | Transaction throughput | Departs from baseline by 20% |
| **Database** | CPU utilization | > 70% sustained |
| **Database** | Connection pool utilization | > 80% |
| **Database** | Lock waits | > 5 minutes |
| **Queue** | JMS queue depth | > 1000 messages |
| **Batch** | Batch job duration | > 2x baseline |
| **Memory** | Heap usage | > 80% sustained |
| **Disk** | Storage utilization | > 85% |
| **Integration** | Error rate | > 5% of transactions |

---

## 10.7.8 Disaster Recovery

### Recovery Objectives

| Tier | RPO (Recovery Point Objective) | RTO (Recovery Time Objective) |
|------|-------------------------------|-------------------------------|
| **Tier 1 (Critical)** | 0–15 minutes | Under 1 hour |
| **Tier 2 (Important)** | 15 minutes – 1 hour | 1–4 hours |
| **Tier 3 (Standard)** | 1–24 hours | 4–24 hours |

### DR Strategy

| Strategy | Description |
|----------|-------------|
| **Backup and Restore** | Periodic backups to S3, restore on failure |
| **Pilot Light** | DR environment on standby, scale up on failover |
| **Warm Standby** | DR environment running at minimal capacity |
| **Multi-Site Active** | Active-active across two AWS regions |

### Backup Strategy

| Data | Backup Frequency | Retention |
|------|------------------|-----------|
| **Database** | Continuous (PITR) + daily | 35 days PITR |
| **Documents** | Continuous sync to S3 | 90 days |
| **Configuration** | Version control (Git) | Indefinite |
| **Batch files** | Daily | 30 days |
| **Audit logs** | Daily | 1 year |

### DR Testing

| Test Type | Frequency | Scope |
|-----------|-----------|-------|
| **Backup restore test** | Monthly | Restore a database to verify integrity |
| **Failover test** | Quarterly | Perform failover to DR region |
| **Full DR exercise** | Annually | Simulate complete regional failure |

---

## 10.7.9 Change Management

### Change Types

| Change Type | Approval | Window | Examples |
|-------------|----------|--------|----------|
| **Standard** | Pre-approved | Business hours | Password reset, data correction |
| **Normal** | Change advisory board | Scheduled | Configuration change, rate update |
| **Emergency** | Emergency CAB | Immediate | Hotfix, security patch |

### Change Advisory Board (CAB)

| Role | Responsibility |
|------|---------------|
| **Change Manager** | Facilitate CAB, schedule changes |
| **Business Representative** | Approve business impact changes |
| **Technical Lead** | Approve technical approach |
| **QA Lead** | Confirm testing completed |
| **Operations** | Assess operational risk |
| **Security** | Assess security impact |

### Change Records Must Include

| Field | Description |
|-------|-------------|
| **Description** | What is changing and why |
| **Risk** | Low, medium, high impact assessment |
| **Rollback plan** | How to revert if needed |
| **Test plan** | What testing was completed |
| **Schedule** | Planned implementation window |
| **Approver** | Who approved the change |

---

## Key Takeaways

1. **Testing** requires a structured environment strategy from developer sandboxes to production.
2. **CI/CD** automates build, test, and deployment for configuration and extensions.
3. **Upgrades** require strict impact assessment and conflict management.
4. **Cloud operations** shifts infrastructure management to Guidewire, but customers retain configuration and business process responsibility.
5. **Incident management** follows defined severities with clear response targets.
6. **Disaster recovery** is verified through regular failover and restore testing.
7. **Change management** ensures all production changes are reviewed, tested, and reversible.

---

**Back to:** [Volume 10 Index](index.md)