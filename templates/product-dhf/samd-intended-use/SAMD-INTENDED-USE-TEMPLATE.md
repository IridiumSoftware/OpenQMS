---
document_id: SIU-XXX
title: "[SaMD Name] — SaMD Intended Use Statement"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Clinical Affairs / RA, Title]"
status: draft
approved_by: "[Clinical / RA Lead, Title]"
approval_date: YYYY-MM-DD
---

# SIU-XXX: [SaMD Name] SaMD Intended Use Statement

Per IMDRF SaMD WG/N12FINAL:2014 — Software as a Medical Device: Possible Framework for Risk Categorization. The intended use statement formally categorizes the SaMD on the IMDRF two-axis framework, which drives the rigor of clinical evaluation, post-market surveillance, and risk controls applied across the QMS.

## 1. Device identification

- **SaMD name + version:** [name]
- **Manufacturer:** [legal name + registered address]
- **Software safety class (IEC 62304):** [A / B / C]
- **EU MDR class (Annex VIII Rule 11 typically applies to SaMD):** [I / IIa / IIb / III]
- **FDA classification:** [Class I / II / III; 510(k) / De Novo / PMA / pre-cert]

## 2. SaMD intended use

[Plain-language statement of what the SaMD does, for whom, and in what clinical context. This is the primary input to the IMDRF risk categorization in §3.]

- **What the SaMD does:** [analyze ECG / triage radiology images / etc.]
- **Intended users:** [HCP role, training; consumer/patient if home-use]
- **Intended patient population:** [demographics, condition, severity]
- **Clinical environment:** [hospital ICU / outpatient / home / etc.]
- **Information output to the user:** [diagnosis, alert, recommendation, decision-support, monitoring data]

## 3. IMDRF SaMD risk categorization

The IMDRF framework places SaMD on two axes:

### 3.1 State of Healthcare Situation or Condition

- [ ] **Critical** — accurate / timely diagnosis or treatment is vital to avoid death, long-term disability, or other serious deterioration. (Examples: cancer detection, ICU monitoring.)
- [ ] **Serious** — accurate diagnosis or treatment is of vital importance to avoid unnecessary interventions or timely interventions are important to mitigate long-term irreversible consequences.
- [ ] **Non-serious** — accurate diagnosis or treatment is important but not critical for mitigating long-term irreversible consequences.

[Mark one; justify per the clinical evaluation.]

### 3.2 Significance of Information Provided to Healthcare Decision

- [ ] **Treat or diagnose** — the SaMD provides information that will be used to take immediate or near-term action to diagnose or treat. (Examples: AI-driven cancer detection that drives biopsy; insulin pump dosing algorithm.)
- [ ] **Drive clinical management** — the SaMD provides information that will be used to aid in treatment, aid in diagnosis, triage or identify early signs of a disease.
- [ ] **Inform clinical management** — the SaMD provides information that will not trigger an immediate or near-term action; the information will be aggregated with other sources.

[Mark one; justify per the intended use.]

### 3.3 Resulting SaMD Category (I-IV)

| Healthcare situation \ Significance | Treat/diagnose | Drive clinical mgmt | Inform clinical mgmt |
|---|---|---|---|
| **Critical** | **IV** | III | II |
| **Serious** | III | II | I |
| **Non-serious** | II | I | I |

**SaMD Category:** [I / II / III / IV — derived from §3.1 + §3.2]

## 4. Implications of the SaMD category

| Category | Clinical-evaluation rigor | PMS rigor | Risk-control rigor |
|---|---|---|---|
| IV (highest) | Clinical investigation typically required | Continuous PMS + post-market clinical studies | Highest |
| III | Clinical investigation often required | Active PMS | High |
| II | Literature + equivalence typically sufficient | Active PMS | Moderate |
| I (lowest) | Literature review often sufficient | Routine PMS | Standard |

[Document the specific implications for THIS SaMD per the assigned category — what clinical-evaluation scope, what PMS cadence, what risk-control measures.]

## 5. Mapping to other regulatory classifications

- **EU MDR Annex VIII Rule 11:** [Justify the Class assignment — Rule 11 generally classifies SaMD that provides information for decisions with diagnostic or therapeutic purposes as Class IIa; if the decisions can cause death or irreversible deterioration → Class III; if serious deterioration → Class IIb.]
- **FDA classification:** [510(k) / De Novo / PMA path; cite the device classification panel / product code.]

## 6. References

- IMDRF/SaMD WG/N12FINAL:2014 — Software as a Medical Device: Possible Framework for Risk Categorization.
- IMDRF/SaMD WG/N23FINAL:2015 — SaMD Application of Quality Management System.
- IMDRF/SaMD WG/N41FINAL:2017 — SaMD Clinical Evaluation.
- FDA Pre-Cert Program (informative; pilot status).
- Linked artifacts: SRS-XXX, RMF-XXX-001, CER-XXX, GSPR-XXX.

## 7. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
