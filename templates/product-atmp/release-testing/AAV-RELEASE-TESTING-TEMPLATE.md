---
document_id: AAV-REL-XXX
title: "[AAV Product] [Batch] — AAV Release Testing Record"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[QC Manager + Vector Release Coordinator]"
status: draft (pending QA release decision)
approved_by: "[QA Director + (EU) Qualified Person per Annex 16]"
approval_date: YYYY-MM-DD
---

# AAV-REL-XXX: AAV (Adeno-Associated Virus) Release Testing Record

Per EU GMP Annex 2A + FDA CBER guidance for AAV gene therapy products + ICH Q5A(R2) (2023 — explicitly extends to viral vector products with vector-specific RCV testing strategy) + ICH Q5D + ICH Q6B + USP <1046> (Cellular and Tissue-Based Products) + USP general chapters as applicable. AAV release testing characterizes the vector product itself (titer, capsid composition, purity, integrity) rather than a downstream cell product.

AAV is the leading delivery vector for in vivo gene therapy (Luxturna RPE65 for inherited retinal dystrophy; Zolgensma SMN1 for SMA; Hemgenix Factor IX for hemophilia B; Elevidys micro-dystrophin for DMD; many investigational programs). Manufacturing typically uses HEK293-based transient transfection (triple-plasmid: AAV ITR-flanked transgene + AAV Rep+Cap + adenoviral helper) OR baculovirus/Sf9 systems. Release testing addresses both common AAV-specific attributes + program-specific transgene attributes.

## 1. Product + batch identification

- **Product name:** [name]
- **AAV serotype + variant:** [e.g., AAV2 / AAV5 / AAV8 / AAV9 / AAVrh10 / engineered variant such as AAV-PHP.eB or AAV.LK03]
- **Transgene cassette:** [promoter + transgene + polyA + regulatory elements]
- **Production system:** [HEK293 triple-transfection / Sf9-baculovirus / stable producer cell line]
- **Batch number:** [BATCH-NUMBER]
- **Manufacturing date:** [YYYY-MM-DD start to YYYY-MM-DD finish]
- **Batch size (vector genomes):** [vg total]
- **Final formulation:** [buffer + volume + concentration]
- **Fill date + container/closure:** [YYYY-MM-DD; vials/bags + closure system]
- **Linked MBR:** MBR-XXX
- **Linked Viral Safety Evaluation:** VSE-XXX
- **Linked production cell-line characterization:** [MCB + WCB references for HEK293 or Sf9]

## 2. Release-test panel

### 2.1 Identity

| Test | Specification | Method | Result | Pass/Fail |
|---|---|---|---|---|
| Capsid identity (serotype confirmation) | Conforms to AAV[serotype] reference | Capsid ELISA OR cryo-EM | | |
| Genome identity (transgene cassette) | Conforms to reference sequence | NGS sequencing (full vector genome including ITRs) | | |
| Restriction digest pattern | Conforms | Diagnostic restriction digest + agarose gel | | |

### 2.2 Vector genome titer + concentration

| Test | Specification | Method | Result | Pass/Fail |
|---|---|---|---|---|
| Vector genome titer (vg/mL) | ≥ X × 10^Y vg/mL | ddPCR (preferred for accuracy) OR qPCR | | |
| Vector genome copy concentration | Within label tolerance | ddPCR | | |

### 2.3 Capsid titer + empty:full ratio

This is critical for AAV — empty capsids do not deliver transgene + may contribute to immunogenicity without therapeutic effect.

| Test | Specification | Method | Result | Pass/Fail |
|---|---|---|---|---|
| Total capsid titer (capsid particles per mL) | Per spec | ELISA-based capsid quantification (e.g., AAV capsid ELISA) | | |
| Empty:full ratio | ≤ X% empty (typical: ≤ 30%; ideal ≤ 10%) | Analytical ultracentrifugation (AUC — gold standard) OR cryo-EM OR charge detection mass spectrometry (CDMS) | | |

### 2.4 Purity

| Test | Specification | Method | Result | Pass/Fail |
|---|---|---|---|---|
| Capsid protein ratio (VP1 : VP2 : VP3) | ~1:1:10 (per AAV biology) | SDS-PAGE / capillary electrophoresis | | |
| Aggregates | ≤ X% | Size-exclusion chromatography | | |
| Process-related impurities — residual host cell protein (HCP) | ≤ X ng/mL or ≤ Y ppm | HCP ELISA (HEK293-specific OR Sf9-specific per production system) | | |
| Process-related impurities — residual host cell DNA | ≤ X ng/dose | qPCR (oncogene-specific OR generic) | | |
| Process-related impurities — residual plasmid DNA (transfection system) | ≤ X ng/dose | qPCR | | |
| Process-related impurities — residual baculovirus (Sf9 system only) | ≤ X infectious particles per dose | TCID50 or qPCR | | |
| Process-related impurities — residual nuclease (Benzonase) | ≤ X ng/mL | ELISA | | |

### 2.5 Potency

| Test | Specification | Method | Result | Pass/Fail |
|---|---|---|---|---|
| In vitro potency (transgene-specific) | Per spec — typically demonstration of transgene expression upon transduction of permissive cell line | RT-qPCR for transgene mRNA OR Western blot for transgene protein OR functional assay specific to transgene | | |
| Infectious titer (transducing units) | Per spec | TCID50 OR ICCA (infectious center assay) on permissive cell line | | |

The potency assay is the most product-specific test — design depends entirely on the transgene's intended function (e.g., for RPE65 product, in vitro retinal pigment epithelium transduction + RPE65 expression).

### 2.6 Replication-Competent AAV (RCAAV) testing

| Test | Specification | Method | Result | Pass/Fail |
|---|---|---|---|---|
| Replication-Competent AAV | Not detected | Cell-line based amplification per FDA + Ph. Eur. recommendations | | |

### 2.7 Microbiological safety

| Test | Specification | Method | Result | Pass/Fail |
|---|---|---|---|---|
| Sterility | No growth | USP <71> 14-day OR rapid sterility method validated to USP <71> | | |
| Mycoplasma | Not detected | USP <63> OR PCR-based rapid method | | |
| Endotoxin | ≤ X EU/mL or ≤ Y EU/dose | LAL per USP <85> | | |
| Adventitious viruses (per ICH Q5A(R2) — risk-based for vector products) | Not detected at LOD | Per Q5A(R2) §3.2 panel | | |

### 2.8 Physico-chemical characterization

| Test | Specification | Method | Result | Pass/Fail |
|---|---|---|---|---|
| Appearance | Per spec | Visual | | |
| pH | [range] | USP <791> | | |
| Osmolality | [range] | USP <785> | | |
| Particulate matter | Per USP <788> | Light obscuration / membrane microscopy | | |
| Container/closure integrity | Pass | Validated method (CCIT) | | |

## 3. Stability protocol reference

Linked stability protocol: STAB-XXX. Per ICH Q5C — biologics stability programme. Frozen storage typical (-65°C or below for long-term; -20°C for shorter terms; refrigerated for short-term in-use stability).

## 4. Deviations + investigations

| Deviation # | Description | Disposition | Linked CAPA |
|---|---|---|---|

For OOS results: per OOS-INVESTIGATION-TEMPLATE-XXX. AAV manufacturing deviations affecting empty:full ratio OR HCP/DNA impurities are particularly load-bearing on patient safety (immunogenicity).

## 5. Release decision

- [ ] **Released for distribution / clinical use** — all tests within specification
- [ ] **Released with restriction** — specific lot use limited (e.g., specific clinical trial site or dose level)
- [ ] **Rejected** — manufacturing failure → batch destroyed or returned

**Decision:** [Released / Released w/ restriction / Rejected / Quarantined]
**Decision date:** [YYYY-MM-DD]
**Decided by:** [QA Director + (EU) QP]
**Restrictions (if applicable):** [enumerated]

## 6. Patient + lot exposure tracking

For commercial-stage products: linked to Tissue/Cell Traceability Record (TCTR-XXX) AAV-equivalent for forward + reverse traceability (which patients received this batch; which batch did a given patient receive). Per EU GMP Annex 2A §10 + 21 CFR 1271.290 traceability.

## 7. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| QC Manager | | | |
| Analyst (data review) | | | |
| Vector specialist (titer + empty:full + RCAAV review) | | | |
| QA Reviewer | | | |
| QA Director (release authority) | | | |
| Qualified Person (EU market) | | | |

## 8. References

- EU GMP Annex 2A §6 + §8 + §11 — ATMP-specific manufacturing + QC + release.
- 21 CFR 1271 Subpart D — Current Good Tissue Practice.
- ICH Q5A(R2) — Viral Safety Evaluation (2023; explicitly extends to viral vector products).
- ICH Q5D — Derivation + Characterisation of Cell Substrates (production cell lines).
- ICH Q6B — Specifications: Biotechnological/Biological Products.
- FDA Guidance for Industry — Chemistry, Manufacturing, and Control (CMC) Information for Human Gene Therapy Investigational New Drug Applications (INDs) (January 2020).
- FDA Guidance for Industry — Long Term Follow-Up After Administration of Human Gene Therapy Products (January 2020).
- FDA Guidance for Industry — Considerations for the Development of Gene Therapy Products to Treat Hemophilia (March 2023).
- USP <1046> Cell and Gene Therapy Products + applicable USP <71>, <63>, <85>, <788>, <791>, <785>.
- Ph. Eur. 5.14 Gene transfer medicinal products for human use; Ph. Eur. 2.6.16 Tests for extraneous agents.
- Linked: MBR-XXX, VSE-XXX (vector + cell-substrate viral safety per Q5A(R2)), STAB-XXX (stability protocol), TCTR-XXX (traceability for commercial-stage products), OOS-INVESTIGATION-XXX where applicable.

## 9. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
