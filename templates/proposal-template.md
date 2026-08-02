# {Product} Proposal Form Template

> **Purpose:** Collect the minimum information required to underwrite and rate a {Product} risk.
> **Owner:** Underwriting Department
> **Version:** 1.0

## Form Structure

Each field in the proposal form follows the definition below:

| Field Name | Definition | Required | Mandatory | Validation | Example | Underwriting Importance | Common Errors | Premium Impact | Supporting Documents |
|------------|------------|----------|-----------|------------|---------|-------------------------|---------------|----------------|----------------------|
| {Field} | {What it means} | Yes/No | Yes/No | {Rule} | {Example} | {Why it matters} | {Typical mistake} | {Effect on premium} | {Document} |

---

## Instructions for Use

1. **Section A — General Information:** Complete all fields.
2. **Section B — Risk Description:** Provide accurate business operations detail.
3. **Section C — Coverage Requested:** State limits and deductibles requested.
4. **Section D — Loss History:** Report all losses for the past five years.
5. **Section E — Protection & Loss Control:** Confirm all protection features.
6. **Section F — Declarations:** Sign and date.

---

## Field-Level Detail Table

### A. General Information

| Field Name | Definition | Required | Mandatory | Validation | Example | Underwriting Importance | Common Errors | Premium Impact | Supporting Documents |
|------------|------------|----------|-----------|------------|---------|-------------------------|---------------|----------------|----------------------|
| Legal Name | Registered business name | Yes | Yes | 1–100 chars | "ABC Manufacturing Ltd" | Identifies the insured entity | Spelling errors; DBA confusion | Low | Certificate of Incorporation |
| Trading Name | Name used to trade | Yes | No | 1–100 chars | "ABC" | Links to contracts | Left blank | Low | — |
| Entity Type | Legal structure | Yes | Yes | Enum | "Limited Company" | Determines liability exposure | Wrong structure | High | Formation documents |
| Business Address | Registered office | Yes | Yes | Valid address | "1 High Street, London" | Determines governing law & perils | P.O. Box only | Medium | Lease / deeds |
| Contact Person | Named contact | Yes | Yes | Name | "Jane Smith" | Single point of contact | Out-of-date contact | Low | — |

### B. Risk Description

| Field Name | Definition | Required | Mandatory | Validation | Example | Underwriting Importance | Common Errors | Premium Impact | Supporting Documents |
|------------|------------|----------|-----------|------------|---------|-------------------------|---------------|----------------|----------------------|
| Nature of Business | Principal activity | Yes | Yes | Free text | "Metal fabrication" | Core hazard class | Vague description | High | Company website / brochures |
| NAICS/SIC Code | Industry code | Yes | Yes | Numeric | "332312" | Rating classification | Wrong code | High | — |
| Payroll | Annual remuneration | Yes | Yes | Currency | "£2,500,000" | GL & WC exposure base | Excludes bonuses | High | Payroll report |
| Gross Sales | Annual turnover | Yes | Yes | Currency | "£8,000,000" | Products exposure base | Net vs gross confusion | High | Financial statements |
| Employees | Headcount | Yes | Yes | Integer | "45" | WC & EL exposure | Contractors included | Medium | PAYE records |

### C. Coverage Requested

| Field Name | Definition | Required | Mandatory | Validation | Example | Underwriting Importance | Common Errors | Premium Impact | Supporting Documents |
|------------|------------|----------|-----------|------------|---------|-------------------------|---------------|----------------|----------------------|
| Limit | Amount of cover | Yes | Yes | Positive currency | "£5,000,000" | Sets PML | Unrealistic limit | High | — |
| Deductible | Self-insured amount | Yes | Yes | Positive currency | "£5,000" | Frequency control | Zero deductible | Medium | — |
| Sublimits | Restricted cover amounts | No | No | Currency | "£250,000 fire" | Caps specific perils | Unspecified sublimits | Medium | — |

### D. Loss History

| Field Name | Definition | Required | Mandatory | Validation | Example | Underwriting Importance | Common Errors | Premium Impact | Supporting Documents |
|------------|------------|----------|-----------|------------|---------|-------------------------|---------------|----------------|----------------------|
| Prior Claims | Last 5 years' losses | Yes | Yes | Numeric | "2 claims, £40,000" | Loss ratio projection | Omitting open claims | High | Loss runs |
| Largest Loss | Biggest single claim | Yes | Yes | Currency | "£30,000" | PML check | None | High | Claim files |
| Prior Carrier | Previous insurer | Yes | No | Text | "ABC Insurance" | Referral to peer history | None | Medium | Policy schedule |

---

## Underwriting Decision

| Decision | Criteria |
|----------|----------|
| Accept | Meets appetite, all documents received |
| Refer | Any high-severity exposure, new territory |
| Decline | Outside appetite, adverse loss history |

**Prepared by:** ______________ **Date:** ______________

---

*Part of the Global Insurance Underwriting Handbook — Templates*