---
document_id: PPAP-XXX
title: "[Part Number] — Production Part Approval Process Submission"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Quality Engineering / Supplier Quality Lead, Title]"
status: draft
approved_by: "[QA Lead + Customer Supplier Quality Engineer, Title]"
approval_date: YYYY-MM-DD
---

# PPAP-XXX: Production Part Approval Process Submission for [Part Number]

Per AIAG PPAP 4th Edition. The Production Part Approval Process (PPAP) is the automotive industry's production-readiness gate. It is the automotive analog of the aerospace AS9102 First Article Inspection — but PPAP is broader, with 18 elements covering not just dimensional inspection but the entire production-process readiness (design records, FMEA, control plan, MSA, capability studies, part submission warrant).

PPAP is required for:
- New parts.
- Engineering change to existing parts (design, material, processing source, processing method).
- Re-establishing production after a tooling-disuse period (typically 12+ months).
- Customer-initiated re-PPAP request (e.g., after quality issue + corrective action).

The submission Level (1 through 5) is set by the customer. Level 3 is most common for standard production parts.

## 1. Part identification

- **Part number:** [PN]
- **Part name + description:** [name]
- **Part revision:** [rev]
- **Customer:** [name]
- **Customer part number:** [as different from supplier PN if applicable]
- **Customer Purchase Order:** [PO + line item]
- **Supplier:** [legal name + address; customer-issued Supplier Code]
- **Manufacturing location:** [plant address; multi-plant disclosures if part is produced at >1 location]
- **PPAP Submission Level:** [1 / 2 / 3 / 4 / 5]
- **PPAP type:** [Initial / Annual re-submission / Engineering change / Tooling refresh / Other (specify)]

## 2. PPAP Submission Levels

| Level | What is submitted to customer | What is retained at supplier |
|---|---|---|
| **1** | Part Submission Warrant (PSW) only | All other elements |
| **2** | PSW + product samples + limited supporting data | Most other elements |
| **3** | PSW + product samples + complete supporting data | All other elements available |
| **4** | PSW + as defined by customer | Other elements per customer request |
| **5** | PSW + product samples + complete supporting data available for review at supplier location | All other elements available for review at supplier |

## 3. The 18 PPAP elements

For each element, indicate Submitted (S) / Retained (R) / Not Applicable (NA) based on Level and customer requirements, with file references.

| # | Element | Status | Reference / Notes |
|---|---|---|---|
| 1 | Design Records (drawings) | | |
| 2 | Engineering Change Documents (ECNs / Deviations) | | |
| 3 | Customer Engineering Approval (if required) | | |
| 4 | Design FMEA (DFMEA) | | Required if supplier is design-responsible |
| 5 | Process Flow Diagram | | |
| 6 | Process FMEA (PFMEA) | | |
| 7 | Control Plan | | Living document; references PFMEA + Special Characteristics |
| 8 | Measurement System Analysis (MSA) studies | | GR&R per AIAG MSA reference manual; per measurement system |
| 9 | Dimensional Results | | Per IATF 16949 §8.3.3.3 Special Characteristics; complete dimensional layout |
| 10 | Records of Material / Performance Test Results | | Includes Material Test Reports (MTR), Certificate of Conformance, durability/fatigue/EMC etc. as applicable |
| 11 | Initial Process Studies | | Capability studies (Cpk / Ppk) per AIAG SPC reference manual; per Special Characteristic |
| 12 | Qualified Laboratory Documentation | | Internal labs require ISO/IEC 17025 or customer-recognized equivalent; external labs require accreditation |
| 13 | Appearance Approval Report (AAR) | | If part has appearance requirements |
| 14 | Sample Production Parts | | Per Level — physical samples or photographs |
| 15 | Master Sample | | Retained at supplier for the entire life of the part for dispute resolution |
| 16 | Checking Aids | | Gauges, fixtures, models used in inspection; documented + calibrated |
| 17 | Customer-Specific Requirements (CSR) records | | Customer-flowed-down requirements + how addressed |
| 18 | Part Submission Warrant (PSW) | S | The summary form signed by supplier authorized signatory + accepted by customer |

## 4. Special Characteristics summary

Per IATF 16949 §8.3.3.3. List Key / Critical / Safety Characteristics from the drawing.

| Char # | Description | Designator (KC / CC / SC) | Tolerance | Cpk / Ppk required | Cpk / Ppk achieved | Control method |
|---|---|---|---|---|---|---|

## 5. Capability studies summary (Element 11)

| Characteristic | n samples | Ppk | Cpk | Acceptance criterion | Conforming? |
|---|---|---|---|---|---|

Customer typically requires Ppk ≥ 1.67 (Initial), Cpk ≥ 1.33 (Ongoing) for Critical / Key Characteristics. Per part / supplier / customer-specific.

## 6. MSA summary (Element 8)

| Measurement system | Type (variable / attribute) | GR&R % | EV % (Equipment Variation) | AV % (Appraiser Variation) | NDC | Acceptance |
|---|---|---|---|---|---|---|

Targets per AIAG MSA: GR&R < 10% (acceptable), 10-30% (marginal), >30% (unacceptable).

## 7. PPAP disposition

| Disposition | Notes |
|---|---|
| [ ] **Approved** — full production approved | |
| [ ] **Interim approval** — production approved with conditions + sunset date | Conditions listed below |
| [ ] **Rejected** — production NOT approved; root cause + corrective action + re-PPAP required | NCR-XXX linked |

If Interim Approval:
- **Conditions:** [list]
- **Sunset date for resolution:** [date]
- **Corrective action plan:** [reference]

If Rejected:
- **Linked NCR:** NCR-XXX
- **Linked 8D / CAPA:** CAPA-XXX
- **Re-PPAP plan + date:** [reference]

## 8. Part Submission Warrant (PSW — Element 18)

The PSW is the formal certification by supplier authorized signatory that the part conforms to all customer requirements and that the submission package is complete.

| Field | Value |
|---|---|
| Part Number | |
| Engineering Change Level + Date | |
| Material + Source | |
| Production Location | |
| Reason for Submission | [Initial / ECN / Tooling refresh / Other] |
| Submission Level | [1-5] |
| Customer Tool Code / Property | [where applicable] |
| **Declaration:** I affirm that the samples represented by this warrant are representative of our parts and have been made to the applicable customer drawings and specifications, are made from specified materials on regular production tooling with no operations other than the regular production process, and that I have noted any deviations from this declaration. | |
| Authorized Supplier Signatory | |
| Title | |
| Date | |

## 9. Customer disposition (filled by customer)

| Field | Value |
|---|---|
| Customer Approval (signature + date) | |
| Customer comments / conditions | |

## 10. Sign-off (Supplier-internal)

| Role | Name | Date | Signature |
|---|---|---|---|
| Production Engineering | | | |
| Quality Engineering | | | |
| QA Lead | | | |
| Authorized Signatory (PSW) | | | |

## 11. References

- AIAG PPAP 4th Edition — Production Part Approval Process reference manual.
- AIAG APQP — Advanced Product Quality Planning (PPAP is the gate at APQP Phase 5).
- AIAG PFMEA — reference manual (Element 6).
- AIAG MSA — reference manual (Element 8).
- AIAG SPC — reference manual (Element 11).
- IATF 16949 §8.3.3.3 — Special characteristics.
- IATF 16949 §8.5.1.1 — Control plan (Element 7).
- IATF 16949 §8.7 — Control of nonconforming outputs (linked NCRs).
- Customer-Specific Requirements (CSRs).

## 12. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
