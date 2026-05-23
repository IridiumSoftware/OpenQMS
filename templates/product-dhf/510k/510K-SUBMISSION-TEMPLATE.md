---
document_id: 510K-XXX
title: "[Product Name] — 510(k) Premarket Notification Submission Package"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Regulatory Affairs, Title]"
status: draft
approved_by: "[RA / QA Lead, Title]"
approval_date: YYYY-MM-DD
---

# 510K-XXX: [Product Name] 510(k) Premarket Notification

Per 21 CFR 807 Subpart E. The 510(k) is FDA's substantial-equivalence demonstration submission for most Class II devices. It is **not** an approval — FDA reviews and **clears** a 510(k), allowing the device to be legally marketed in the US. Substantial equivalence is established against a **predicate device** (legally on the US market before 1976 or previously cleared via 510(k)).

This template is the assembly index for the 510(k) submission package. Each section references the controlled documents that constitute the actual submission content; the 510K-XXX record itself is the structured manifest that the FDA's eSubmitter / eSTAR tool ingests.

## 1. General information

- **510(k) number (assigned by FDA on receipt):** [K-XXXXXX]
- **Device trade name:** [trade name]
- **Common name:** [generic name]
- **Classification name:** [per FDA classification regulation]
- **Product code (FDA panel + code):** [e.g. HCY — non-invasive blood pressure system]
- **Regulation number:** [21 CFR 8XX.XXXX]
- **Regulatory class:** [I / II / III]
- **Submission type:** [Traditional / Special / Abbreviated / De Novo (see §6)]
- **Applicant:** [legal name + registered address]
- **US agent (if non-US applicant):** [name + address]
- **FDA establishment registration number:** [FEI #]
- **Linked technical file:** TFI-XXX

## 2. Predicate device(s) — substantial equivalence basis

The 510(k) hinges on demonstrating the device is substantially equivalent to one or more predicate devices.

| Predicate | 510(k) # | Manufacturer | Why predicate |
|---|---|---|---|

### 2.1 Comparison matrix

| Attribute | Subject device | Primary predicate | Same / Different? | If different: rationale for SE |
|---|---|---|---|---|
| Intended use | | | | |
| Indications for use | | | | |
| Operating principle | | | | |
| Energy used / delivered | | | | |
| Patient contact materials | | | | |
| Sterility | | | | |
| Software (if applicable) | | | | |
| Performance (key metrics) | | | | |

## 3. Indications for use (FDA Form 3881)

[Verbatim statement to appear on FDA Form 3881 — the "Indications for Use" statement that defines the legal scope of clearance. Carefully worded; any change requires a new 510(k).]

## 4. 510(k) summary or 510(k) statement (per §807.92 or §807.93)

[Manufacturer chooses one:
- **510(k) summary** — published by FDA on the 510(k) database; succinct summary of substantial equivalence basis.
- **510(k) statement** — certifying that the manufacturer will make the substantial-equivalence determination materials available upon request.]

## 5. Technical sections

### 5.1 Device description
[Reference: TFI-XXX §1]

### 5.2 Performance data (bench, animal, clinical as applicable)
[For most 510(k)s, bench data + biocompat + sterility (if sterile) + EMC + electrical safety + software V&V suffice. Clinical data required only when bench/non-clinical data is insufficient to demonstrate substantial equivalence — e.g. for new indications, new technologies, or new patient populations.]

- Bench testing per applicable consensus standards (FDA recognized): VP-XXX-001
- Biocompatibility (ISO 10993 series): [report]
- Sterility (if sterile): [validation report]
- Software (if applicable): SRS, SAD, STP, SRR, SOUP register
- Animal studies (if applicable): [report]
- Clinical data (if applicable): VAL-XXX-001 / CER-XXX

### 5.3 Special Controls compliance (per the device's product code)
[For Class II devices, FDA defines Special Controls per product code in the classification regulation. Examples: performance standards, special labeling, post-market surveillance, patient registries. The 510(k) demonstrates compliance with each applicable Special Control.]

### 5.4 Labeling
[Proposed labeling — package insert, IFU, package label, professional labeling. Must conform to 21 CFR Part 801 general labeling requirements + any product-code-specific labeling controls.]

## 6. De Novo path (if applicable)

If the device is novel (no predicate) and low-to-moderate risk, submission may be via De Novo (21 CFR 860 Subpart D) rather than 510(k):

- **De Novo request:** [request to classify the device into Class I or II rather than the default Class III]
- **Risk-based classification rationale:** [risks identified, controls proposed]
- **Special Controls proposed:** [for FDA to consider establishing as Special Controls for the new device type]

## 7. Establishment registration & listing

- **Establishment registered (per §807 Subpart B):** [Yes/No, FEI #]
- **Device listing (per §807 Subpart D):** [Yes/No, listing number]
- **Annual registration renewal status:** [current through YYYY-MM-DD]

## 8. Post-clearance commitments

[Documented commitments from FDA clearance letter, if any:]
- Post-market studies
- Post-market surveillance per §822 (if 510(k) cleared device falls in §822 scope)
- Reporting under 21 CFR 803 (FDA MDR for adverse events) — see also `modules/fda-class-iii/` for the equivalent reporting clause

## 9. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Regulatory Affairs Lead | | | |
| QA Lead | | | |
| Clinical Lead (if clinical data) | | | |
| CEO / President (authorized signatory) | | | |

## 10. References

- 21 CFR 807 — Establishment registration and device listing for manufacturers and initial importers of devices.
- 21 CFR 807 Subpart E — Premarket Notification (510(k)).
- 21 CFR 860 — Medical device classification procedures.
- 21 CFR 860 Subpart D — De Novo classification process.
- 21 CFR 803 — Medical Device Reporting (post-clearance adverse-event reporting).
- FDA Guidance: The 510(k) Program: Evaluating Substantial Equivalence.
- FDA Guidance: De Novo Classification Process.
- Linked artifacts: TFI-XXX, VP-XXX-001, VAL-XXX-001 (if applicable), SRS-XXX (if software), labeling spec.

## 11. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
