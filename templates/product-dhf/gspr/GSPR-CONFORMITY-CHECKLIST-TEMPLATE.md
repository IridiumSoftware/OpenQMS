---
document_id: GSPR-XXX
title: "[Product Name] — GSPR Conformity Checklist"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Regulatory Affairs, Title]"
status: draft
approved_by: "[QA / RA Lead, Title]"
approval_date: YYYY-MM-DD
---

# GSPR-XXX: [Product Name] General Safety and Performance Requirements Checklist

Per EU MDR 2017/745 Annex I. Every General Safety and Performance Requirement (GSPR) applicable to the device is evaluated for conformity, with explicit evidence references. The checklist is a required component of the technical file (per Annex II §4) and is what notified-body reviewers walk to assess GSPR compliance.

**Per-class customization.** The applicability column (`A` / `NA`) is device-class-dependent. SaMD devices may declare NA on many physical / chemical / mechanical GSPRs; implantables typically declare A on most; IVD devices route through IVDR rather than MDR. Adopters customize per-product based on the intended-use statement and classification.

## 1. Device identification

- **Product:** [name + model + risk classification]
- **Intended use:** [as approved]
- **Device class** (MDR Annex VIII): [I / IIa / IIb / III]
- **Classification rule applied:** [rule number from Annex VIII]
- **Linked technical file:** TFI-XXX
- **Linked risk management file:** RMF-XXX-001

## 2. GSPR conformity matrix — Chapter I (General requirements, GSPR 1–9)

| GSPR | Title (paraphrased) | A / NA | Standard(s) used | Evidence | Notes |
|---|---|---|---|---|---|
| 1 | Intended performance | A | [e.g. clinical evaluation; performance testing] | [CER-XXX §N; STP-XXX §N] | |
| 2 | Risk reduction without adverse benefit-risk impact | A | ISO 14971 | RMF-XXX-001 §6 | |
| 3 | State of the art design and manufacture | A | [applicable design standards] | [SAD-XXX §N] | |
| 4 | Risk control order: inherent safety → protective measures → information | A | ISO 14971 §7 | RMF-XXX-001 §3 | |
| 5 | Safe and effective for the intended environment / users | A | [usability + clinical] | UEF-XXX, CER-XXX | |
| 6 | Risk management system established and maintained | A | ISO 14971 | RMF-XXX-001 | |
| 7 | Risk control measures preserve intended function | A | ISO 14971 §7 | RMF-XXX-001 §4 (risk control effectiveness) | |
| 8 | All known and foreseeable risks reduced as far as possible | A | ISO 14971 §7 + §8 | RMF-XXX-001 §3-5 | |
| 9 | Characteristics maintained over device lifetime | A | [reliability + aging studies] | [reliability study; PV-XXX shelf life] | |

## 3. GSPR conformity matrix — Chapter II (Design and manufacture, GSPR 10–22)

| GSPR | Title (paraphrased) | A / NA | Standard(s) used | Evidence | Notes |
|---|---|---|---|---|---|
| 10 | Chemical, physical, biological properties | [A/NA] | [ISO 10993 if biocompat applies] | [biocompat report] | NA for non-contact devices |
| 11 | Infection / microbial contamination | [A/NA] | [ISO 11135 / 11137 if sterile] | [sterility test reports] | NA for non-sterile |
| 12 | Devices incorporating medicinal substances | NA | — | — | NA unless combination product |
| 13 | Devices incorporating biological materials | NA | — | — | NA unless ToA / TSE risk |
| 14 | Construction and environmental properties | A | [applicable env standards] | [env test reports] | |
| 15 | Devices with diagnostic / measuring function | [A/NA] | [IEC standards for measurement accuracy] | [accuracy verification] | A for measurement devices |
| 16 | Protection against radiation | [A/NA] | [IEC 60601-1-3 for medical radiation] | — | NA unless emitting/receiving radiation |
| 17 | Electronic programmable systems and software | A | IEC 62304 + IEC 82304-1 | SRS-XXX, SAD-XXX, STP-XXX, SRR-XXX | |
| 18 | Active devices and connections | [A/NA] | IEC 60601-1 | [test reports] | A for powered devices |
| 19 | Protection against mechanical / thermal risks | [A/NA] | [IEC 60601-1 mechanical/thermal sections] | [test reports] | |
| 20 | Energy / substance delivery devices | [A/NA] | [IEC 60601-2 collateral standards] | [delivery accuracy tests] | A for energy / drug delivery |
| 21 | Self-testing / self-administration devices | [A/NA] | IEC 62366-1 + use-error analysis | UEF-XXX | A for home-use / patient-administered |
| 22 | Lay-person use | [A/NA] | IEC 62366-1 | UEF-XXX | A for consumer / patient use |

## 4. GSPR conformity matrix — Chapter III (Information supplied with the device, GSPR 23)

| GSPR | Title (paraphrased) | A / NA | Standard(s) used | Evidence | Notes |
|---|---|---|---|---|---|
| 23.1 | General requirements for the information supplied | A | [labeling spec] | [labeling spec doc] | |
| 23.2 | Information on the label | A | EU MDR Annex I §23.2 verbatim | [labeling spec; UDI assignment] | UDI-DI required |
| 23.3 | Information in the instructions for use | A | EU MDR Annex I §23.3 verbatim | [IFU doc] | |
| 23.4 | Information for patients with implants (if applicable) | [A/NA] | — | [implant card if applicable] | A only for implantables |

## 5. NA justifications

[For each GSPR marked NA, document why the requirement is not applicable to the device per the intended use and classification. Mandatory per notified-body expectation.]

## 6. Conformity declaration

[Statement that, taken as a whole, the device meets the applicable GSPRs as documented in this checklist. Sign-off by Regulatory Affairs, QA, and (for clinical-evidence-dependent GSPRs) the clinical lead.]

## 7. References

- EU MDR 2017/745 Annex I — General Safety and Performance Requirements.
- EU MDR 2017/745 Annex II §4 — Technical documentation must include the GSPR conformity checklist.
- MDCG 2019-16 (informative) — Guidance on Annex I cybersecurity.
- Harmonized standards list (EU OJ) — current applicable standards.
- Linked artifacts: TFI-XXX, RMF-XXX-001, CER-XXX, PMCF-XXX, UEF-XXX, SRS-XXX, SAD-XXX, STP-XXX, SRR-XXX, PV-XXX.

## 8. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
