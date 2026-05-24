---
document_id: MBR-XXX
title: "[Drug Substance or Drug Product Name] — Master Batch Record"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Production Manager / Manufacturing Lead, Title]"
status: draft
approved_by: "[QA Director — release authorization per 21 CFR 211.22 + EU GMP Ch. 2]"
approval_date: YYYY-MM-DD
review_cadence: "On change-control trigger (formulation / process / equipment / material / supplier change) OR every 2 years OR after deviation pattern indicates revision needed"
---

# MBR-XXX: Master Batch Record for [Product Name]

Per 21 CFR 211.186 + EudraLex Vol. 4 Part I Chapter 4 (Documentation). The Master Batch Record (MBR; Master Formula / Master Production Record in some jurisdictions) is the approved authoritative template that defines how every batch of a specific drug substance or drug product is to be manufactured. Each manufactured batch produces a **completed Batch Record** (BR / BMR) by executing this MBR with the batch-specific values + signatures + actual measurements + deviations filled in. The MBR is the spec; the executed BR is the evidence.

QA approval per 21 CFR 211.22 / EU GMP Ch. 2 is mandatory before any batch is manufactured against this MBR.

## 1. Product identification

- **Product / drug substance name:** [name]
- **Strength + dosage form** (drug product) OR **API molecule + grade** (drug substance): [details]
- **NDC** (US drug product) OR **DMF number** (US API) OR **MA number** (EU): [number]
- **Manufacturing site + line:** [site address + line designation]
- **Batch size (range, with justification for range if applicable):** [min..max units OR fixed]
- **Linked SMF** (Site Master File): SMF-XXX
- **Linked VMP** (Validation Master Plan): VMP-XXX
- **Process validation status:** [Stage 1 / Stage 2 / Stage 3 continued process verification per FDA Process Validation Guidance 2011 + EU GMP Annex 15]

## 2. Composition + bill of materials

| Material code | Material name | Grade / Pharmacopoeia | Quantity per batch (target) | Range allowed | Function in formulation | Active / Excipient / Process aid | Specification reference |
|---|---|---|---|---|---|---|---|

Overage rationale, if applicable, documented separately and linked.

## 3. Equipment + utilities

| Equipment ID | Description | Qualification status (IQ/OQ/PQ reference) | Calibration cycle + last calibration | Cleaning validation reference |
|---|---|---|---|---|

| Utility | Specification (e.g., WFI per USP / Ph. Eur.; HVAC class) | Monitoring reference |
|---|---|---|

## 4. Process flow + manufacturing instructions

### 4.1 Step-by-step manufacturing instructions

Each step shall enumerate:

1. **Step #** + concise operation description.
2. **Equipment used** (with ID).
3. **Materials added** (with material code + quantity + tolerance + order of addition).
4. **Process parameters** (temperature, pressure, RPM, time, pH, etc.) with target value + acceptable range + criticality designation (Critical Process Parameter / Key Process Parameter / Process Parameter).
5. **In-process control (IPC)** sampling point + test + acceptance criterion + responsibility (operator vs. QC).
6. **Recording requirement** (operator entry + initial + time; second-person verification where applicable per 21 CFR 211.188).

| Step # | Description | Equipment | Materials added | Process parameters (CPP / KPP) | IPC sampling + tests + acceptance | Performed by | Verified by | Time / Date |
|---|---|---|---|---|---|---|---|---|

### 4.2 Process holds + intermediate storage

- **Permissible hold points:** [enumerated]
- **Hold-time limits:** [per intermediate, with validation reference]
- **Storage conditions during hold:** [temperature, humidity, light, container]

## 5. In-process control sampling plan

| IPC # | Stage | Sample point | Sample size | Test method | Acceptance criterion | Frequency | Reporting |
|---|---|---|---|---|---|---|---|

## 6. Packaging + labeling instructions (drug product only)

- **Primary packaging components:** [container + closure with specs]
- **Secondary packaging:** [carton + insert + label]
- **Labeling text + artwork reference:** [version-controlled artwork ID]
- **Line clearance procedure:** [reference SOP-XXX]
- **Reconciliation calculation method:** [yields + losses + reconciliation acceptance criterion per 21 CFR 211.103]

## 7. Yield calculations + reconciliation

- **Theoretical yield:** [calculation basis]
- **Expected yield range (with justification):** [%]
- **Reconciliation criterion (per 21 CFR 211.103):** [acceptable range; deviation triggers investigation]

## 8. Sampling for QC release testing

| Sample # | Sample point | Stage | Sample size | QC tests required | Acceptance criteria | Reference monograph / method |
|---|---|---|---|---|---|---|

## 9. Deviations + change controls

Any deviation from this MBR during execution shall be documented per the Deviation Report SOP (DEV-XXX) BEFORE batch closure. Categorize per criticality (minor / major / critical). Batch disposition follows deviation investigation outcome.

Permanent changes to this MBR require Change Control (CC-XXX) per ICH Q10. Once approved, the new MBR version supersedes the prior version; existing in-process batches finish under the prior version unless explicit re-validation justifies otherwise.

## 10. Batch release

The completed Batch Record (BR) shall be reviewed by QA per 21 CFR 211.22 / EU GMP Ch. 2 / ICH Q10 §3.2.2.1. The Qualified Person (QP) in EU jurisdictions per Article 51 of Directive 2001/83/EC + EU GMP Annex 16 performs final batch certification before release for distribution.

### Release-decision criteria

- [ ] All manufacturing steps executed per MBR
- [ ] All IPCs within acceptance
- [ ] All QC release tests within specification
- [ ] All deviations investigated + closed
- [ ] Yield reconciliation within criterion
- [ ] All required signatures + dates present
- [ ] Stability protocol active (if first-time-manufactured strength / formulation / site)

## 11. Sign-off (MBR template approval)

| Role | Name | Date | Signature |
|---|---|---|---|
| Author (Manufacturing Engineering) | | | |
| Production Manager | | | |
| QC Manager | | | |
| Validation Lead | | | |
| QA Director (mandatory approval per 21 CFR 211.22) | | | |
| QP (EU jurisdictions, per EU GMP Annex 16) | | | |

## 12. References

- 21 CFR 211.186 — Master production and control records.
- 21 CFR 211.188 — Batch production and control records.
- 21 CFR 211.100 — Written procedures; deviations.
- 21 CFR 211.103 — Calculation of yield.
- 21 CFR 211.22 — Responsibilities of quality control unit (includes batch release).
- EudraLex Vol. 4 Part I Ch. 4 — Documentation.
- EudraLex Vol. 4 Annex 16 — Certification by a Qualified Person and Batch Release.
- ICH Q7 §6 — Documentation and records (API GMP equivalent).
- ICH Q10 §3.2.2.1 — Management responsibility for the PQS (release decision).
- FDA Process Validation Guidance 2011.
- EU GMP Annex 15 — Qualification and validation.
- Linked: SMF-XXX (Site Master File), VMP-XXX (Validation Master Plan), DEV-XXX (Deviation SOP), CC-XXX (Change Control), CoA-XXX (QC release certificate format).

## 13. Revision history

| Version | Date | Author | Changes | Linked CC# |
|---|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. | CC-XXX |
