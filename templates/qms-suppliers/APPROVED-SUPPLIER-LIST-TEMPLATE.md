---
document_id: ASL-001
title: "Approved Supplier List"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Procurement / QA Lead, Title]"
status: draft
approved_by: "[QA / Operations Lead, Title]"
approval_date: YYYY-MM-DD
---

# ASL-001: Approved Supplier List

Per ISO 13485 §7.4.1 and 21 CFR 820.50(a). The Approved Supplier List (ASL) is the controlled record of every supplier qualified to provide a product or service that has a potential impact on product quality. Purchasing from a supplier not on this list is a nonconformance.

## 1. Purpose and scope

[List of approved suppliers across product categories, with classification, qualification status, and re-evaluation schedule. Used by procurement, QA, and operations to ensure all purchases come from qualified sources.]

## 2. Approved supplier register

| ASL ID | Supplier name | Category | Criticality | Qualification date | Re-evaluation due | Status | Evaluation record |
|---|---|---|---|---|---|---|---|
| SUP-001 | [Acme Components] | [Raw materials / Component] | [Critical / Major / Minor] | YYYY-MM-DD | YYYY-MM-DD | Approved | SE-001 |
| SUP-002 | [Beta Manufacturing] | [Contract manufacturer] | [Critical] | YYYY-MM-DD | YYYY-MM-DD | Approved (with conditions) | SE-002 |

**Criticality classification** (per organization's supplier-risk SOP):

- **Critical** — supplier provides components/services that directly affect device safety or essential performance, OR sole-source with no qualified alternative.
- **Major** — supplier provides components/services with moderate impact on quality or design.
- **Minor** — commodity or off-the-shelf items with low risk and qualified alternatives.

## 3. Qualification scope per supplier

For each supplier in §2, document the specific scope of approval (e.g. "Acme Components — approved for resistor models RES-100 through RES-499; not approved for capacitors").

## 4. Disqualified suppliers (with reason and date)

| Former ASL ID | Supplier name | Disqualification date | Reason | Disposition of in-flight orders |
|---|---|---|---|---|

## 5. Procurement gate

All purchase orders for products in scope of this ASL must reference an approved supplier id (SUP-xxx). Procurement is prohibited from issuing POs to suppliers not on this list. Exceptions require a documented supplier-evaluation issue (SE-xxx) opened and closed prior to PO issue, OR an explicit deviation authorization per the organization's deviation-handling SOP.

## 6. Re-evaluation triggers

A supplier is re-evaluated on whichever of these occurs first:

- Scheduled re-evaluation per the cadence column (typically annual for Critical, biennial for Major, triennial for Minor).
- Any nonconformance attributed to the supplier (NCR-xxx).
- Quality concern raised via complaint (COMPLAINT-xxx) linked to a supplier component.
- Change to supplier's quality system (loss of ISO 13485 certification, change of ownership, change of manufacturing site).
- Performance metrics breaching the agreed threshold per the supplier quality agreement.

## 7. References

- ISO 13485:2016 §7.4 — Purchasing.
- 21 CFR 820.50 — Purchasing controls.
- EU MDR Article 10(9)(c) — Resources and supplier responsibility.
- Linked artifacts: SE-xxx supplier-evaluation records; supplier quality agreements; SOP-PROC-001 procurement SOP.

## 8. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
