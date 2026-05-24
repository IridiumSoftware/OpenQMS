# ATMP — Open QMS class overlay (cell + gene therapy on pharma)

Class overlay on top of the **pharma** vertical, encoding the cell + gene therapy specific requirements that don't apply to baseline pharma manufacturing. First pharma class overlay; most-stringent biologics scope.

## Scope

ATMP = Advanced Therapy Medicinal Product. This overlay applies to:

- **Cell-based therapies** — autologous (donor = recipient: CAR-T, TIL, dendritic-cell vaccines) and allogeneic (donor ≠ recipient: iPSC-derived therapies, NK-cell therapies, MSC therapies)
- **Gene therapies** — AAV (Adeno-Associated Virus) gene therapy, lentiviral gene therapy, retroviral gene therapy, plasmid-based gene therapy
- **Ex vivo gene-modified products** — CAR-T (lentiviral-modified T-cells), HSCT gene therapy, ex vivo gene-edited (CRISPR) cell therapy
- **Oncolytic viruses** — engineered viruses that selectively replicate in tumor cells

This overlay covers four standards:

- **EU GMP Annex 2A** — Manufacture of Advanced Therapy Medicinal Products for Human Use. The EU's ATMP-specific GMP guideline.
- **EU GMP Annex 2B** — Manufacture of Biological Active Substances and Medicinal Products for Human Use. The cross-cutting biological-GMP framework.
- **21 CFR 1271** — Human Cells, Tissues, and Cellular and Tissue-Based Products (HCT/Ps). US regulation covering donor eligibility (Subpart C) + Current Good Tissue Practice (Subpart D) + tracking (§1271.290) + reporting (§1271.350).
- **ICH Q5A(R2)** — Viral Safety Evaluation of Biotechnology Products Derived From Cell Lines of Human or Animal Origin. 2023 revision explicitly extends scope to genetically engineered viral vector products.

**All four standards are PUBLIC license** (same character as the parent pharma vertical — adopters can read every cited requirement for free without commercial standards licenses).

10 clauses encoding the substantive ATMP-specific requirements beyond baseline pharma.

## Most distinguishing ATMP requirements vs. baseline pharma

1. **Donor eligibility** — unique to cell-based ATMPs. 21 CFR 1271 Subpart C requires screening + testing for Relevant Communicable Disease Agents (RCDAs) for every donor. Autologous donors get exception per §1271.65(a) but still require documentation. EU equivalent under Directive 2004/23/EC + Directive 2006/17/EC.

2. **Bidirectional donor → product → recipient traceability with EXTREMELY long retention** — 30 years EU per Directive 2004/23/EC Article 8; 10 years US per 21 CFR 1271.270. Outlasts most operational systems → archival + format-stability planning required (PDF/A + CSV + XML; periodic format migration with checksums; vendor independence; multi-person knowledge; organizational-change contractual transfer; encryption-key escrow).

3. **Aseptic processing throughout** — ATMPs typically cannot be terminally sterilized (live cells + viral vectors). PIC/S Annex 1 applies with ATMP-specific adaptations per Annex 2A: closed-system processing preferred; isolator + RABS use where feasible; media-fill APS qualification per ATMP scope.

4. **Limited batch size + N=1 batches for autologous** — quality decisions can't easily "reject" autologous batches because the product is patient-specific (patient typically already conditioned/lymphodepleted). Rapid investigation + risk-based administration decision in collaboration with treating physician is the workflow.

5. **Viral safety per ICH Q5A(R2)** (2023 revision explicitly addresses viral vector products) — cell substrate characterization + raw material viral risk + viral clearance studies (for non-vector products) OR Replication-Competent Virus testing strategy (for vector products: RCL for lentivirus; RCA for adenovirus; RCAAV for AAV).

6. **Comparability after manufacturing changes per ICH Q5E** — ATMP manufacturing changes require demonstration that the post-change product is comparable to the pre-change product. **Particularly challenging for autologous products** because there's no reference standard from the same patient — the comparability analysis must address inherent inter-patient variability.

7. **Adverse-event reporting under HCT/P-specific framework** — 21 CFR 1271.350 deviation reporting + EU Serious Adverse Reaction / Serious Adverse Event reporting per Directive 2004/23/EC Article 11. Distinct from general pharmacovigilance.

## Templates introduced by this overlay

Three new ATMP-specific templates:

- **`templates/product-atmp/donor-eligibility/DONOR-ELIGIBILITY-ASSESSMENT-TEMPLATE.md`** — 21 CFR 1271 Subpart C + EU Directive 2004/23/EC + Directive 2006/17/EC + EU GMP Annex 2A §3. Full RCDA panel (HIV-1/2 + HBV + HCV + HTLV-1/2 + T. pallidum + T. cruzi + WNV + Zika as applicable + reproductive-tissue-specific Chlamydia + Gonorrhea + EU-additional Malaria where risk-based). Specimen-collection-window compliance per §1271.80(b). Exception handling per §1271.65 (autologous; directed donor intimate partner; urgent medical need) with required labeling per §1271.65(c) + recipient informed consent per §1271.65(d). **PHI compartmentalization required** — template captures the eligibility *decision* + non-PHI traceability identifiers; full identifiable PHI lives in a separate access-restricted record per 21 CFR 1271.270 + HIPAA + GDPR Special Category data requirements.

- **`templates/product-atmp/traceability/TISSUE-CELL-TRACEABILITY-RECORD-TEMPLATE.md`** — EU GMP Annex 2A §10 + Directive 2004/23/EC Art. 8 + Directive 2006/86/EC + 21 CFR 1271.290. Bidirectional traceability: forward (donor → product → recipient — for recipient adverse-event investigation) + reverse (recipient → product → donor — for donor-source-related adverse events affecting multiple recipients) + recall scope queries (rapid identification of all recipients of product derived from a specific donor or batch). EU Single European Code (SEC) coding per Directive 2015/565. Format + media stability planning for the 30-year EU retention requirement.

- **`templates/product-atmp/viral-safety/VIRAL-SAFETY-EVALUATION-REPORT-TEMPLATE.md`** — ICH Q5A(R2) 2023 three-pillar framework. MCB/WCB/EPC characterization per species-specific virus panel. Raw material viral risk assessment (bovine TSE/BSE per CHMP/410/01; porcine circo+parvovirus; murine MAP; human full RCDA). Viral clearance studies with model-virus panel covering diverse classes (enveloped/non-enveloped × DNA/RNA × ssDNA/dsDNA × range of sizes — typically pseudorabies / X-MuLV / Reo3 / MVM standard panel). Cumulative log reduction calculation. For vector products: vector characterization (titer, purity, capsid-protein ratios for AAV, RCL/RCA/RCAAV per category).

## Composition with other modules

The natural composition is **pharma + atmp + cross-cutting overlays**:

```bash
# Minimal — pharma + atmp standalone
openqms validate --module pharma --module atmp

# Realistic commercial cell-therapy organization (9-module deepest composite tested)
openqms validate \
  --module pharma --module atmp \
  --module iso-27001 --module regulated-ai \
  --module iso-14001 --module iso-45001 --module iso-50001 \
  --module iso-37001 --module iso-22301
```

The 9-module composite represents the realistic shape for a commercial-stage cell-therapy organization pursuing fully-integrated management system certification (PQS + ATMP-specific GMP + IS + AI governance + EMS + OHSMS + EnMS + ABMS + BCMS).

## Example bundle

[`bundles/example-cart.yaml`](../../bundles/example-cart.yaml) — autologous CD19-targeted CAR-T product at US+EU dual-licensed cell therapy facility under FDA + EMA + MHRA.

## What is intentionally NOT in scope

- **Reproductive tissue / gametes** — 21 CFR 1271 reproductive-tissue-specific subprovisions; separate ethical + regulatory framework. Forward overlay if adopter needs.
- **HCT/Ps that are NOT ATMPs** — regulated only under 21 CFR 1270/1271 without IND/BLA pathway (minimum-manipulation + homologous-use criteria per §1271.10 + §1271.15). Different regulatory pathway from drug+biologic. Forward overlay.
- **Veterinary ATMPs** — emerging space; EMA + FDA-CVM have separate frameworks. Forward.
- **In situ gene editing** — CRISPR direct administration without ex vivo cell processing (e.g., CASGEVY base-editing in situ administration). Fundamentally different manufacturing model. Forward.

## Standards licensing

All ATMP-specific standards are **PUBLIC license**:

- EU GMP Annex 2A + 2B — via European Commission
- 21 CFR 1271 — via ecfr.gov / FDA
- ICH Q5A(R2) — via ich.org

This is meaningful for cell-therapy startups + academic spinouts, which typically have limited budgets for commercial standards licenses. The full set of ATMP regulatory documents can be assembled at zero standards-licensing cost.

See repo-root `README.md` "Standards licensing — important" for the broader licensing posture.

## Forward work

- Reproductive tissue / gametes overlay (21 CFR 1271 reproductive-tissue-specific subprovisions)
- HCT/P-only overlay (non-ATMP — products under §1271.10 + §1271.15 minimum-manipulation + homologous-use)
- Veterinary ATMP overlay
- In situ gene editing overlay
- Site Master File for ATMPs — PIC/S Explanatory Notes equivalent + ATMP-specific facility descriptions
- Comparability Protocol template (ICH Q5E — particularly critical for autologous ATMPs without reference standard)
- CAR-T-specific release-testing template (flow cytometry + cytotoxicity assay + vector copy number + integration site analysis + sterility)
- AAV-specific release-testing template (empty/full capsid ratio + vector genome copy number + dose-determination math)
- Additional pharma class overlays — sterile vs. non-sterile + biologics vs. small-molecule + commercial vs. clinical-stage
