---
document_id: PV-XXX
title: "[Product Name] — Packaging Validation Report"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Packaging Engineer / QA, Title]"
status: draft
approved_by: "[QA / Engineering Lead, Title]"
approval_date: YYYY-MM-DD
---

# PV-XXX: [Product Name] Packaging Validation Report

Per ISO 13485 §7.5.11 (Preservation of product), 21 CFR 820.130 (Device packaging), ISTA 2A / ISTA 3A / ISTA 6-FedEx / ISTA 6-Amazon as applicable to the distribution channel.

Packaging validation demonstrates that the packaging system protects the device from damage during the foreseeable distribution environment, and that sterile-barrier integrity (for sterile devices) is maintained through the package's labeled shelf life.

## 1. Scope

- **Product:** [name, model, configuration]
- **Packaging configuration:** [primary, secondary, tertiary as applicable; box dimensions; cushioning; sterile barrier system if sterile]
- **Distribution channel(s) validated:** [retail / parcel / cold chain / etc.]
- **Applicable ISTA standard(s):** [2A — Partial Simulation ≤150 lb; 3A — Parcel Delivery System; 6-FedEx; 6-Amazon; etc.]
- **Sterile?** [Yes/No — if yes, ISO 11607 series also applies]

## 2. Test plan

| Test sequence | Method | Acceptance criterion |
|---|---|---|
| Conditioning | [Per ISTA atmospheric pre-conditioning if applicable] | [Achieved per spec] |
| Vibration | [Per ISTA schedule] | [No package failure; device functional] |
| Drop | [Per ISTA drop sequence: heights, faces, edges, corners] | [Sterile barrier intact (if sterile); device functional] |
| Compression | [Per ISTA compression schedule] | [No package collapse; device functional] |
| Atmospheric / climate | [If applicable] | [Per spec] |

## 3. Sample size and justification

- **Sample size:** [n packages per condition; rationale]
- **Sample selection:** [random / worst-case / per AQL plan]
- **Statistical confidence:** [if applicable]

## 4. Results

| Sample ID | Test | Pre-test inspection | Post-test inspection | Device function check | Sterile-barrier integrity (if applicable) | Pass / Fail |
|---|---|---|---|---|---|---|

## 5. Sterile barrier integrity (if applicable)

Per ISO 11607-1 / ISO 11607-2 (sterile barrier systems). Test methods: dye penetration, peel strength, microbial barrier, accelerated and real-time aging.

| Test | Method | Acceptance criterion | Result |
|---|---|---|---|

## 6. Shelf life

- **Labeled shelf life:** [period]
- **Aging study basis:** [accelerated (e.g. ASTM F1980) + real-time]
- **Real-time aging status:** [in progress / complete; current data point]

## 7. Deviations

[Document any deviations from the planned protocol — sample substitutions, instrument variance, environmental condition variance. Each deviation gets impact assessment and disposition.]

## 8. Conclusion

[Statement that the packaging system meets the acceptance criteria for the validated distribution channels and labeled shelf life. Sign-off by packaging engineer, QA, and (if sterile) microbiology.]

## 9. References

- ISO 13485:2016 §7.5.11 — Preservation of product.
- 21 CFR 820.130 — Device packaging.
- ISTA 2A — Packaged-Products Weighing 150 lb (68 kg) or Less (Partial Simulation).
- ISTA 3A — Packaged-Products for Parcel Delivery System Shipment.
- ISO 11607-1 / 11607-2 — Packaging for terminally sterilized medical devices (if applicable).
- ASTM F1980 — Accelerated aging of sterile barrier systems (if applicable).

## 10. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
