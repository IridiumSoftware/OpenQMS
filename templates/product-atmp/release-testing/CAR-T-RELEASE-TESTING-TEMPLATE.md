---
document_id: CART-REL-XXX
title: "[CAR-T Product] [Batch / Patient ID — Pseudonymized] — CAR-T Release Testing Record"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[QC Manager + ATMP Release Coordinator]"
status: draft (pending QA release decision)
approved_by: "[QA Director + (EU) Qualified Person per Annex 16]"
approval_date: YYYY-MM-DD
---

# CART-REL-XXX: CAR-T Release Testing Record

Per EU GMP Annex 2A + FDA CBER guidance for CAR-T cellular products + ICH Q5A(R2) + ICH Q5D + ICH Q6B + 21 CFR 1271 Subpart D Current Good Tissue Practice. CAR-T release testing combines elements of cell-therapy release (viability, identity, sterility), gene-therapy release (vector copy number, transgene expression), and process-related impurity testing. The release decision is risk-based per Annex 2A §11 — autologous products in particular may proceed to administration with rapid risk-based clinical decision in collaboration with the treating physician when full conventional release is not feasible within the patient's clinical window.

## 1. Product + batch identification

- **Product name:** [name]
- **Target antigen + construct:** [e.g., CD19 / CD22 / BCMA / dual-target — with construct identifier]
- **Vector + vector lot:** [lentivirus / retrovirus / non-viral — vector lot ID + lentiviral RCL-tested status]
- **Batch (autologous patient identifier — pseudonymized):** [PATIENT-UDI]
- **Batch (allogeneic donor / lot identifier):** [LOT-ID]
- **Manufacturing site:** [licensed facility]
- **Manufacturing start date:** [YYYY-MM-DD apheresis / collection]
- **Manufacturing end date:** [YYYY-MM-DD final formulation]
- **Cryopreservation date:** [YYYY-MM-DD]
- **Total cell count formulated:** [N cells]
- **Per-bag count:** [N cells × bags]
- **Linked MBR:** MBR-XXX
- **Linked Donor Eligibility Assessment (autologous = patient):** DEA-XXX
- **Linked Tissue/Cell Traceability Record:** TCTR-XXX
- **Linked Viral Safety Evaluation (for vector lot):** VSE-XXX

## 2. Release-test panel

### 2.1 Identity

| Test | Specification | Method | Result | Pass/Fail |
|---|---|---|---|---|
| Cell-population identity | CD3+ ≥ X% of viable cells | Flow cytometry (validated panel) | | |
| CAR expression — % positive cells | ≥ X% CAR+ of CD3+ | Flow cytometry — fluorescent reagent recognizing CAR | | |
| CAR expression — mean fluorescence intensity | Per spec | Flow cytometry MFI | | |

### 2.2 Purity / composition

| Test | Specification | Method | Result | Pass/Fail |
|---|---|---|---|---|
| Viability | ≥ X% (typically ≥ 70%) | Trypan blue exclusion + flow cytometry (live/dead stain) | | |
| CD4 / CD8 ratio (if specified) | [range] | Flow cytometry | | |
| CD3+ purity | ≥ X% of total viable cells | Flow cytometry | | |
| Residual non-T cells (B cells, NK, monocytes) | ≤ Y% | Flow cytometry | | |

### 2.3 Vector copy number (VCN) + transduction efficiency

| Test | Specification | Method | Result | Pass/Fail |
|---|---|---|---|---|
| Vector copy number per transduced cell | ≤ 5 (typical FDA expectation; risk of insertional mutagenesis increases with VCN) | qPCR vs. integration cassette | | |
| Transduction efficiency (% CAR+) | Per identity §2.1 above | Flow cytometry | | |

### 2.4 Replication-Competent Lentivirus (RCL) testing

| Test | Specification | Method | Result | Pass/Fail |
|---|---|---|---|---|
| RCL in vector lot | Not detected | C8166 cell-line based assay per FDA Guidance (3-week amplification) | | |
| RCL in final product (per FDA Guidance — pooled patient material; risk-based) | Not detected | Per protocol | | |

For retroviral vectors: Replication-Competent Retrovirus (RCR) per analogous methodology.

### 2.5 Microbiological safety

| Test | Specification | Method | Result | Pass/Fail |
|---|---|---|---|---|
| Sterility | No growth | USP <71> 14-day OR rapid sterility method (e.g., BacT/ALERT) validated to USP <71> equivalence | | |
| Mycoplasma | Not detected | USP <63> OR rapid PCR-based method | | |
| Endotoxin | ≤ X EU/mL or per dose | LAL per USP <85> | | |

**Sterility consideration for autologous ATMPs:** the 14-day USP <71> sterility cannot complete within the patient's clinical window (typically 7-10 days from apheresis to infusion). Rapid sterility methods (validated to USP <71> equivalence) + risk-based release per Annex 2A §11 with continued sterility monitoring is the typical workflow.

### 2.6 Potency

| Test | Specification | Method | Result | Pass/Fail |
|---|---|---|---|---|
| Cytotoxicity (in vitro killing of target-antigen-expressing cell line) | ≥ X% lysis at E:T ratio Y | Co-culture with target cell line; LDH release or flow-based killing assay | | |
| Cytokine release (IFN-γ ± IL-2 ± TNF-α) | ≥ X pg/mL upon stimulation | ELISA / multiplex | | |

### 2.7 Process-related impurities

| Test | Specification | Method | Result | Pass/Fail |
|---|---|---|---|---|
| Residual magnetic beads (where Dynabeads used for activation) | ≤ X beads / 10^7 cells | Microscopy | | |
| Residual anti-CD3/CD28 antibodies | Below detection | ELISA | | |
| Residual cytokines (IL-2 / IL-7 / IL-15 from culture) | Below release limit | ELISA | | |
| Endotoxin (process-related) | Per §2.5 above | | | |

### 2.8 Product-related characterization

| Test | Specification | Method | Result | Pass/Fail |
|---|---|---|---|---|
| Cell count + viability (final formulated) | ≥ N × 10^6 viable CAR+ cells per bag | NC-200 / Cellometer / Vi-CELL | | |
| Appearance | Per spec | Visual | | |
| Cryopreservation medium composition | Per formulation | Per process | | |

## 3. Integration site analysis (if required per protocol)

For some CAR-T products, integration site analysis may be performed periodically (per-batch + per-lot frequency depending on regulatory commitment):

| Test | Specification | Method | Result |
|---|---|---|---|
| Integration site distribution | No clonal expansion; insertion sites in non-cancer-gene regions | LAM-PCR + NGS | |

## 4. Deviations + investigations

| Deviation # | Description | Disposition | Linked CAPA |
|---|---|---|---|

For OOS results: per OOS-INVESTIGATION-TEMPLATE-XXX. For autologous products, accelerated OOS Phase 1 + Phase 2 timeline given clinical-window constraints.

## 5. Release decision

- [ ] **Released for administration** — all tests within specification + all deviations resolved
- [ ] **Released for administration under risk-based decision** — selected test(s) pending OR out-of-spec but risk-benefit analysis in collaboration with treating physician supports administration (autologous-specific per Annex 2A §11)
- [ ] **Not released** — manufacturing failure / unacceptable risk → patient receives different therapy
- [ ] **On hold** — pending additional information / repeat manufacturing

**Decision:** [Released / Released w/ risk-based exception / Not released / On hold]
**Decision date + time:** [YYYY-MM-DD HH:MM]
**Decided by:** [QA Director + (EU) QP]
**For risk-based release exception:** [treating physician name + acknowledgment date + rationale + post-administration monitoring plan]

## 6. Continued monitoring (post-release)

For autologous risk-based releases:
- Sterility monitoring continues to USP <71> 14-day completion
- Patient observation per protocol
- Any post-release deviation (e.g., late sterility growth) triggers immediate notification to treating physician + Field Alert per 21 CFR 314.81 if applicable

## 7. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| QC Manager | | | |
| Analyst (data review) | | | |
| Vector specialist (VCN + RCL review) | | | |
| QA Reviewer | | | |
| QA Director (release authority) | | | |
| Qualified Person (EU market) | | | |

## 8. References

- EU GMP Annex 2A §6 + §8 + §11 — ATMP-specific manufacturing + QC + release.
- 21 CFR 1271 Subpart D — Current Good Tissue Practice.
- FDA Guidance for Industry — Considerations for the Development of Chimeric Antigen Receptor (CAR) T Cell Products (March 2024).
- FDA Guidance for Industry — Long Term Follow-Up After Administration of Human Gene Therapy Products (January 2020).
- FDA Guidance for Industry — Testing of Retroviral Vector-Based Human Gene Therapy Products for Replication Competent Retrovirus During Product Manufacture and Patient Follow-Up (January 2020).
- ICH Q5A(R2) — Viral Safety Evaluation (vector lot + adventitious agent testing).
- ICH Q5D — Derivation + Characterisation of Cell Substrates.
- ICH Q6B — Specifications: Biotechnological/Biological Products.
- USP <71> + <63> + <85> + <1046> (Cellular and Tissue-Based Products).
- Linked: MBR-XXX, DEA-XXX, TCTR-XXX, VSE-XXX (vector lot viral safety), OOS-INVESTIGATION-XXX where applicable, integration-site-analysis records.

## 9. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
