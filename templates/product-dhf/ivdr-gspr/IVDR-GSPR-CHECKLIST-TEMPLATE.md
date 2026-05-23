---
document_id: IVDR-GSPR-XXX
title: "[Product Name] — IVDR GSPR Conformity Checklist"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Regulatory Affairs, Title]"
status: draft
approved_by: "[QA / RA Lead, Title]"
approval_date: YYYY-MM-DD
---

# IVDR-GSPR-XXX: [Product Name] IVDR General Safety and Performance Requirements Checklist

Per EU IVDR 2017/746 Annex I. The IVDR GSPRs are analogous in structure to MDR Annex I but IVD-specific in content. Each applicable GSPR is evaluated for conformity with explicit evidence references. The checklist is a required component of the technical documentation per Annex II.

**Per-class customization.** The IVDR uses Class A (lowest risk) through Class D (highest individual + public-health risk) — different from MDR's I/IIa/IIb/III classification. The GSPR applicability and evidence depth scale with class. Adopters customize per-product per Annex VIII classification rules.

## 1. Device identification

- **Product:** [name + model]
- **Intended purpose:** [as approved; per IVDR Article 2(13)]
- **IVDR class** (per Annex VIII rules): [A / B / C / D]
- **Classification rule applied:** [Rule number from Annex VIII]
- **Linked technical file:** TFI-XXX
- **Linked risk management file:** RMF-XXX-001
- **Linked Performance Evaluation Report:** PER-XXX

## 2. IVDR Annex I — Chapter I (General requirements, GSPR 1–8)

| GSPR | Title (paraphrased) | A / NA | Standard(s) used | Evidence | Notes |
|---|---|---|---|---|---|
| 1 | Intended performance — achieve performance per intended purpose | A | [performance evaluation per Annex XIII] | PER-XXX | |
| 2 | Risk reduction without adverse benefit-risk impact | A | ISO 14971 | RMF-XXX-001 §6 | |
| 3 | State of the art design / manufacture / packaging | A | [applicable design standards] | [SAD-XXX, packaging spec] | |
| 4 | Risk control order: inherent safety → protective → information | A | ISO 14971 §7 | RMF-XXX-001 §3 | |
| 5 | Safe and effective for intended use environment / users | A | [usability + clinical performance] | UEF-XXX (if UI), PER-XXX | |
| 6 | Risk management system established and maintained | A | ISO 14971 | RMF-XXX-001 | |
| 7 | Risk control measures preserve intended function | A | ISO 14971 §7 | RMF-XXX-001 §4 | |
| 8 | All known and foreseeable risks reduced as far as possible | A | ISO 14971 §7 + §8 | RMF-XXX-001 §3-5 | |

## 3. IVDR Annex I — Chapter II (Performance, design and manufacturing, GSPR 9–19)

| GSPR | Title (paraphrased) | A / NA | Standard(s) used | Evidence | Notes |
|---|---|---|---|---|---|
| 9 | Performance characteristics — analytical performance + clinical performance + scientific validity | A | ISO 17511 (calibration) + ISO 18113 (labeling); IVDR Annex XIII methodology | PER-XXX | |
| 9.1 | Analytical performance — accuracy, precision, analytical sensitivity, analytical specificity, detection/quantitation limits, linearity, cut-off determination, interfering substances | A | [as above] | PER-XXX §3 | |
| 9.2 | Clinical performance — clinical sensitivity, clinical specificity, positive predictive value, negative predictive value, likelihood ratios | A | [as above] | PER-XXX §4 | |
| 9.3 | Scientific validity — association of the analyte with the clinical condition / physiological state | A | [literature review + clinical studies] | PER-XXX §2 | |
| 10 | Chemical, physical, biological properties — reagent stability, calibrator traceability, sample volume requirements, primary sample matrix considerations | [A/NA] | ISO 17511 (calibration traceability) | [reagent stability study; calibrator characterization] | NA if no reagents |
| 11 | Infection and microbial contamination | [A/NA] | [ISO 11737 series if applicable] | — | Typically NA for IVD reagents in sealed primary packaging |
| 12 | Devices incorporating materials of biological origin | [A/NA] | [ISO 22442 series if applicable] | — | A if uses cell lines, antibodies, etc. |
| 13 | Construction and environmental properties | [A/NA] | [applicable env standards] | [env test reports] | |
| 14 | Devices with measuring function | A | ISO 17511 — calibration traceability | [calibrator characterization, internal calibrator stability] | Almost always A for IVD |
| 15 | Protection against radiation | [A/NA] | [IEC 60601-1-3 if applicable] | — | NA unless device emits/receives radiation |
| 16 | Electronic programmable systems and software | A | IEC 62304 + IEC 82304-1 | SRS-XXX, SAD-XXX, STP-XXX, SRR-XXX | A for software-containing IVD or SaMD-IVD |
| 17 | IVDs designed for self-testing | [A/NA] | IEC 62366-1 + use-error analysis | UEF-XXX | A for home-use / OTC IVD (e.g. pregnancy, COVID home tests) |
| 18 | IVDs designed for near-patient testing | [A/NA] | IEC 62366-1 + use-error analysis | UEF-XXX | A for POCT devices |
| 19 | Protection against mechanical / thermal risks | [A/NA] | [as applicable] | [test reports] | |

## 4. IVDR Annex I — Chapter III (Information supplied with the device, GSPR 20)

| GSPR | Title (paraphrased) | A / NA | Standard(s) used | Evidence | Notes |
|---|---|---|---|---|---|
| 20.1 | Label requirements — name, manufacturer, intended purpose, intended user, intended use environment | A | ISO 18113-1, ISO 18113-2 | [labeling spec] | |
| 20.2 | IFU requirements — analytical performance characteristics, clinical performance characteristics, traceability, specimen type, equipment required, performance limitations | A | ISO 18113-1, ISO 18113-3 | [IFU doc] | |
| 20.3 | Special requirements for IVDs intended for self-testing or near-patient testing — lay-person comprehensibility | [A/NA] | ISO 18113-4 | [self-test labeling] | A for self-test devices |

## 5. NA justifications

[For each GSPR marked NA, document why the requirement is not applicable to the device per the intended purpose and classification. Mandatory per notified-body expectation for Class B/C/D.]

## 6. Conformity declaration

[Statement that, taken as a whole, the device meets the applicable IVDR Annex I GSPRs as documented in this checklist. Sign-off by Regulatory Affairs, QA, and (for Class C/D) clinical lead.]

## 7. References

- EU IVDR 2017/746 Annex I — General Safety and Performance Requirements (IVD).
- EU IVDR 2017/746 Annex II — Technical documentation.
- EU IVDR 2017/746 Annex XIII — Performance evaluation, performance studies, post-market performance follow-up.
- ISO 17511:2020 — In vitro diagnostic medical devices — metrological traceability of values assigned to calibrators.
- ISO 18113 series — In vitro diagnostic medical devices — information supplied by the manufacturer (labeling).
- Linked artifacts: TFI-XXX, RMF-XXX-001, PER-XXX, UEF-XXX (if UI), SRS-XXX (if software).

## 8. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
