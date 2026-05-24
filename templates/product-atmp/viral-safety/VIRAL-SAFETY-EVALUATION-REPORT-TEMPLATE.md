---
document_id: VSE-XXX
title: "[Cell Substrate / Product] — Viral Safety Evaluation Report"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Virology / Biosafety Lead, Title]"
status: draft
approved_by: "[QA Director + Biosafety Officer + (where applicable) external SME viral-safety reviewer]"
approval_date: YYYY-MM-DD
review_cadence: "On material change to cell substrate / raw materials / manufacturing process; periodic re-review per organization SOP (typically every 3-5 years even without change)"
---

# VSE-XXX: Viral Safety Evaluation Report

Per ICH Q5A(R2) — *Viral Safety Evaluation of Biotechnology Products Derived From Cell Lines of Human or Animal Origin* (Step 4 endorsement 2023). The Q5A(R2) revision (vs. the 1997 original) explicitly extends scope to genetically engineered viral vectors (lentivirus, AAV, etc.), introduces risk-based clarifications for products where traditional viral clearance is not feasible (e.g., live viral vectors themselves), and aligns with modern biotech manufacturing.

Viral safety evaluation has three complementary pillars per Q5A(R2):

1. **Selection + testing of cell lines and other raw materials** for the absence of undesirable viruses — including the Master Cell Bank (MCB), Working Cell Bank (WCB), and End-of-Production cells (EPC), plus all biological raw materials (serum, trypsin, hydrolysates, growth factors).
2. **Assessment of the capacity of the production process to clear infectious viruses** — viral clearance studies using orthogonal mechanisms (size exclusion via filtration; inactivation via chemical / thermal / pH treatments; partitioning via chromatography) and "model viruses" representing diverse viral classes.
3. **Testing the product at appropriate steps** for absence of contaminating infectious viruses.

For **ATMPs that themselves contain a viral vector** (e.g., lentiviral CAR-T transduction; AAV gene therapy), the framework adapts: cell-substrate testing remains; raw-material testing remains; but viral clearance studies against the vector itself are not applicable (the vector IS the product). Q5A(R2) provides specific guidance for vector products including replication-competent virus (RCV / RCL / RCA) testing per product category.

## 1. Product + cell substrate context

- **Product name + classification:** [ATMP product ID + classification — autologous CAR-T / allogeneic CAR-T / iPSC-derived / AAV gene therapy / etc.]
- **Cell line + tier:** [Master Cell Bank (MCB) ID + Working Cell Bank (WCB) ID + End-of-Production (EPC) characterization reference]
- **Species of origin (cell + any animal-derived materials):** [list]
- **Vector(s) used in manufacturing (if applicable):** [lentivirus / AAV / adenovirus / retrovirus / non-viral — with vector reference]
- **Manufacturing process reference (MBR):** MBR-XXX

## 2. Cell substrate viral characterization

### 2.1 Master Cell Bank (MCB) testing

| Test | Method | Result | Pass/Fail | Reference | Lab |
|---|---|---|---|---|---|
| In vivo virus assay (adult + suckling mice + embryonated eggs) | Per ICH Q5A(R2) §3.2.1 | | | | |
| In vitro virus assay (3+ cell lines per Q5A(R2) Table 1) | Per Q5A(R2) §3.2.2 | | | | |
| Mycoplasma | USP <63> / Ph. Eur. 2.6.7 | | | | |
| Sterility (bacterial + fungal) | USP <71> / Ph. Eur. 2.6.1 | | | | |
| Species-specific virus testing per cell origin | Per Q5A(R2) Table 2 (rodent: MAP/MVM/Sendai/Reo etc.; human: HIV/HBV/HCV/EBV/HHV-6/HHV-8/CMV/HTLV/parvovirus B19 etc.) | | | | |
| TEM (Transmission Electron Microscopy) for adventitious agents | | | | | |
| Reverse Transcriptase activity | | | | | |
| **For human-derived MCB:** additional human-specific virus panel | | | | | |
| Tumorigenicity (if relevant per cell type + intended use) | | | | | |

### 2.2 Working Cell Bank (WCB) testing

| Test | Method | Result | Pass/Fail | Reference |
|---|---|---|---|---|

WCB testing per Q5A(R2) §3.2.4 — reduced panel acceptable given MCB characterization.

### 2.3 End-of-Production Cells (EPC) / In-Use Cells characterization

| Test | Method | Result | Pass/Fail | Reference |
|---|---|---|---|---|

EPC testing per Q5A(R2) §3.2.5 — confirms no viral contamination introduced during production scale-up + that latent viruses haven't activated. Genetic stability included.

## 3. Raw materials viral risk assessment

| Raw material | Animal-origin? | Risk assessment | Mitigation | Supplier viral-safety statement |
|---|---|---|---|---|

Particularly for animal-origin materials:
- **Bovine** — TSE / BSE risk per EMA CHMP/410/01 + FDA guidance; suppliers from BSE-negligible-risk countries; appropriate certifications
- **Porcine** — porcine circovirus + porcine parvovirus screening
- **Murine** — full mouse virus antibody panel (MAP) on source colony
- **Human** (e.g., human serum albumin, growth factors) — full RCDA panel + lot release with viral testing

## 4. Viral clearance studies (for non-vector products)

Per Q5A(R2) §5. Scale-down studies using "model viruses" representing diverse families to demonstrate the production process's capacity to clear infectious viruses. Each step claimed for clearance is challenged with a known viral spike + reduction factor measured.

| Manufacturing step claimed | Mechanism (size / inactivation / partition) | Model virus class | Model virus | Reduction factor (log10) | Confidence interval |
|---|---|---|---|---|---|

### Model virus panel (per Q5A(R2) §5.4)

Standard panel includes representatives of:
- **Enveloped + non-enveloped**
- **DNA + RNA**
- **Single + double-stranded genome**
- **Range of sizes** (typically pseudorabies virus / X-MuLV / Reo3 / MVM as enveloped large / enveloped medium / non-enveloped medium / non-enveloped small)

### Cumulative clearance

| Virus | Step 1 log RF | Step 2 log RF | Step N log RF | Cumulative log RF | Acceptance criterion | Pass/Fail |
|---|---|---|---|---|---|---|

Cumulative log reduction should be ≥ the worst-case potential viral load (calculated per Q5A(R2) §6) for each viral class.

## 5. For ATMPs containing a viral vector

### 5.1 Vector characterization

| Vector attribute | Specification | Test | Result | Reference |
|---|---|---|---|---|
| Vector identity | | | | |
| Vector titer | TU/mL or vg/mL | | | |
| Vector purity (capsid protein ratios for AAV; protein impurities) | | | | |
| Replication-Competent Virus (RCV) — RCL for lentivirus / RCA for adenovirus / RCAAV for AAV | Per FDA Guidance + Ph. Eur. monograph | | LOD: < N per dose | |
| Vector integrity (genome integrity, capsid integrity) | | | | |
| Empty/full capsid ratio (AAV) | | | | |
| Mycoplasma | | | | |
| Sterility | | | | |
| Endotoxin | LAL per USP <85> | | | |
| Bioburden | | | | |

### 5.2 Vector raw materials (helper plasmids, packaging cells)

- **Helper plasmid + packaging cell line characterization** (for transient + stable producer cell systems): [reference]
- **Helper plasmid + packaging cell viral safety per §2.1-§2.2** above: [reference]

### 5.3 Process-related viral safety considerations

- **Replication-Competent Virus emergence risk during manufacturing:** [risk assessment + mitigation]
- **In-process RCV testing strategy:** [where in the process; sample size; sensitivity]
- **Final product RCV testing:** [test + acceptance criterion]

## 6. Final product testing

| Test | Specification | Method | Acceptance criterion |
|---|---|---|---|

## 7. Overall viral safety conclusion

| Pillar | Conclusion |
|---|---|
| Cell substrate characterized for absence of undesirable viruses | [Yes / No + rationale] |
| Raw materials viral risk acceptably mitigated | [Yes / No] |
| Production process viral clearance demonstrated (or N/A for vector products with alternative strategy) | [Yes / No / N/A — strategy] |
| Final product testing supports release | [Yes / No] |
| **Overall — product viral safety supports clinical use** | [Yes / No] |

## 8. Re-evaluation triggers

- Material change to cell substrate (new MCB / WCB / process step)
- Material change to manufacturing process affecting viral clearance
- Material change to raw materials (new supplier / new material)
- Emergence of new viral threat in the donor population or supply chain
- Post-marketing adverse event suggesting viral safety concern
- Regulatory update (Q5A revision / new viral test mandates)
- Periodic re-review per organization SOP (typically 3-5 years)

## 9. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Virology / Biosafety Lead | | | |
| QA Director | | | |
| Biosafety Officer | | | |
| External SME viral-safety reviewer (high-rigor scope) | | | |
| Qualified Person (EU ATMPs — per EU GMP Annex 16) | | | |

## 10. References

- ICH Q5A(R2) — Viral Safety Evaluation of Biotechnology Products Derived From Cell Lines of Human or Animal Origin (Step 4, 2023).
- ICH Q5D — Derivation + Characterisation of Cell Substrates Used for Production of Biotechnological / Biological Products.
- ICH Q5E — Comparability of Biotechnological / Biological Products Subject to Changes in Their Manufacturing Process.
- ICH Q6B — Specifications: Test Procedures + Acceptance Criteria for Biotechnological / Biological Products.
- EU GMP Annex 2A §6-§8 — Manufacture of ATMPs (raw materials + starting materials + cell substrate considerations).
- EMA CHMP/410/01 — Note for guidance on minimising the risk of transmitting animal spongiform encephalopathy agents via human + veterinary medicinal products.
- FDA Guidance for Industry — CMC Information for Human Gene Therapy Investigational New Drug Applications (IND), January 2020.
- FDA Guidance for Industry — Considerations for the Design of Early-Phase Clinical Trials of Cellular and Gene Therapy Products, June 2015.
- Ph. Eur. monographs on viral safety + adventitious agents.
- USP <63> Mycoplasma + USP <71> Sterility + USP <85> Endotoxin.
- Linked: MBR-XXX (Master Batch Record), DEA-XXX (Donor Eligibility — for human-derived cell substrates), TCTR-XXX (traceability), comparability protocols for any post-evaluation manufacturing changes.

## 11. Revision history

| Version | Date | Author | Changes | Linked CC# |
|---|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. | |
