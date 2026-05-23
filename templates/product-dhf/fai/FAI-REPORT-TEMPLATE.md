---
document_id: FAI-XXX
title: "[Part Number] — First Article Inspection Report"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[QA / Inspector, Title]"
status: draft
approved_by: "[QA Lead + Customer (where flow-down requires)]"
approval_date: YYYY-MM-DD
---

# FAI-XXX: First Article Inspection Report for [Part Number]

Per AS9102 Rev C. The First Article Inspection (FAI) is a documented, complete, independent, and documented physical and functional inspection process verifying that prescribed production methods have produced an acceptable item per engineering drawings, planning, purchase order, engineering specifications, or other applicable design documents.

**FAI is required for:**
- New parts.
- Significantly changed parts (drawing revision, material, supplier, manufacturing process, location).
- Re-establishing production after a 2-year+ gap.
- Customer-flowed-down requirements.

The FAI is documented on the AS9102 standard forms (Form 1, Form 2, Form 3) which are reproduced in §3, §4, §5 below.

## 1. Part identification

- **Part number:** [PN]
- **Part revision:** [rev]
- **Part name + description:** [name]
- **Customer:** [name]
- **Customer-flowed-down FAI requirement reference:** [contract / PO / spec]
- **Manufacturer:** [legal name + address; FAA CAGE code or EASA POA reference if applicable]
- **FAI type:** [Full FAI / Partial FAI / Delta FAI]
- **If Delta FAI:** [original FAI reference + reason for delta]

## 2. Configuration management context

- **Drawing revision used for inspection:** [rev + date]
- **Planning / process specification revision:** [rev + date]
- **Linked engineering change orders:** [list]
- **Tool revision (where applicable):** [rev]

## 3. AS9102 Form 1 — Part Number Accountability

| Item | Value |
|---|---|
| Part Number | |
| Part Name | |
| Serial Number | |
| FAIR Number | |
| Part Revision Level | |
| Drawing Number | |
| Drawing Revision Level | |
| Additional Changes (deviation, waiver) | |
| Manufacturing Process Reference | |
| Organization Name | |
| Supplier Code | |
| P.O. Number | |
| Detail FAI / Assembly FAI? | |
| Full FAI / Partial FAI? | |
| Reason for Partial FAI (if applicable) | |
| List of Sub-Assemblies (with their FAI numbers) | |
| Signature | |
| Date | |
| FAI Complete (Y/N + date) | |

## 4. AS9102 Form 2 — Product Accountability — Raw Material, Specifications and Special Process(es)

| Material / Process | Spec | Code | Supplier Code | Customer-Approved? | Certificate of Conformance |
|---|---|---|---|---|---|

[List all raw materials with their specs, all special processes (heat treatment, plating, welding, NDT, etc.) with their specs, all sub-suppliers used. Customer-approved special process suppliers per Nadcap or customer's approved-supplier list where applicable.]

## 5. AS9102 Form 3 — Characteristic Accountability, Verification and Compatibility Evaluation

Every characteristic from the drawing / specification is enumerated and verified:

| Char # | Reference Location (drawing zone) | Characteristic Designator (Key / Critical / Major / Minor) | Requirement | Results | Designed Tooling | Non-Conformance Number |
|---|---|---|---|---|---|---|

**Characteristic designators:**

- **Key Characteristic (KC)** — feature whose variation has significant influence on product fit, performance, service life, or manufacturability. Subject to AS9103 variation management.
- **Critical Characteristic** — feature whose failure could cause failure of the product or its safety / serviceability / etc.
- **Major Characteristic** — feature that, if not met, results in failure of part to perform its intended function.
- **Minor Characteristic** — feature that would not result in failure but is a deviation from drawing.

## 6. Results summary

- **Total characteristics:** [N]
- **Conforming characteristics:** [N]
- **Nonconforming characteristics:** [N]
- **Linked NCRs:** [list of NCR-xxx for any nonconformities found]
- **Disposition (for nonconformities):** [accepted under deviation / reworked / scrapped]

## 7. FAI decision

- [ ] **FAI accepted** — production approved; subsequent units may ship.
- [ ] **FAI accepted with conditions** — production approved subject to enumerated conditions.
- [ ] **FAI rejected** — production NOT approved; root cause + corrective action required; FAI re-performed after corrective action.

## 8. Customer concurrence (if flow-down requires)

[Customer-submitted FAI requires customer review / acceptance per the contract. Document the customer acceptance reference here.]

## 9. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Inspector | | | |
| QA Lead | | | |
| Engineering (for KC / Critical characteristics) | | | |
| Customer (where flow-down requires) | | | |

## 10. References

- AS9102 Rev C — Aerospace First Article Inspection Requirement.
- AS9100D §8.4 — Control of externally-provided processes (FAI as supplier-quality gate).
- AS9100D §8.5.1.3 — Production process verification.
- AS9103 — Variation Management of Key Characteristics (where KCs are flagged in §5).
- Linked artifacts: drawing revision; planning revision; NCR-xxx (any nonconformities).

## 11. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
