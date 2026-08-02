# {Module} Guidewire Configuration Template

> **Purpose:** Standard template for documenting Guidewire product, integration, or configuration work items.
> **Product:** PolicyCenter / ClaimCenter / BillingCenter / ContactManager / DataHub / InfoCenter / ProducerEngage / Jutro

---

## 1. Overview

{What this configuration or feature does.}

## 2. Business Requirements

| Requirement ID | Requirement | Source |
|----------------|-------------|--------|
| BR-{001} | {Requirement} | {Stakeholder} |
| BR-{002} | {Requirement} | {Stakeholder} |

## 3. Guidewire Application & Module

| Item | Value |
|------|-------|
| Application | {PolicyCenter / ClaimCenter / etc.} |
| Version | {e.g., 10.x, 11.x} |
| Module | {Module name} |
| Configuration type | {Data model / Rules / Workflow / Integration / Rating / UI} |

## 4. Data Model Changes

### New / Modified Entities

| Entity | Type | Fields Added | Description |
|--------|------|--------------|-------------|
| {Entity} | {New / Modified} | {Field list} | {Description} |

### Field Specifications

| Field | Data Type | Length | Required | Default | Validation |
|-------|-----------|--------|----------|---------|------------|
| {Field} | {Type} | {Len} | {Yes/No} | {Default} | {Rule} |

## 5. Rule Configuration (Gosu / Rules)

```gosu
// Example Gosu rule / trigger
uses gw.api.productmodel.PolicyLinePattern

var linePattern = PolicyLinePattern.getByCode("CATAuto")
```

| Rule | Type | Trigger | Behavior |
|------|------|---------|----------|
| {Rule} | {Validation / Availability / Default / Condition} | {Event} | {Behavior} |

## 6. Workflow & Assignment

| Workflow | Trigger | Steps | Assignment Rule |
|----------|---------|-------|-----------------|
| {Workflow} | {Trigger} | {Steps} | {Assign to} |

## 7. Integrations

| Integration | Direction | Technology | Payload Standard | Error Handling |
|-------------|-----------|------------|------------------|----------------|
| {System} | {In/Out} | {REST/SOAP/MQ} | {ACORD/JSON} | {Retry/Alert} |

## 8. Rating Configuration

| Component | Configuration |
|-----------|---------------|
| Rate table | {Table name} |
| Algorithm | {Algorithm} |
| Factors | {Factor list} |
| Minimum premium | {Amount} |

## 9. Batch Processes

| Batch | Schedule | Purpose | Error Handling |
|-------|----------|---------|----------------|
| {Batch} | {Cron/schedule} | {Purpose} | {Handling} |

## 10. UI / Jutro Changes

| Screen | Change | Component |
|--------|--------|-----------|
| {Screen} | {Change description} | {Component} |

## 11. Testing

### Test Scenarios

| Test ID | Scenario | Expected Result | Actual Result |
|---------|----------|-----------------|---------------|
| TC-{001} | {Scenario} | {Expected} | {Actual} |

### UAT Criteria

- [ ] Business sign-off
- [ ] Integration verified
- [ ] Performance acceptable
- [ ] Documentation updated

## 12. Deployment Notes

| Item | Detail |
|------|--------|
| Environment | {Dev / QA / Staging / Prod} |
| Change ticket | {Ticket number} |
| Rollback plan | {Plan} |

---

*Part of the Global Insurance Underwriting Handbook — Templates*