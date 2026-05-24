# Companion — Medical-devices module full population (v0.9.0 + v0.10.0)

**Dates:** 2026-05-23
**Public commits:** `78ee0db` + `cbaffba` (v0.9.0) + `e6d15a8` + `aa51574` (v0.10.0)
**Range:** `ec188b3..aa51574`
**Spec deltas:** OQ-041, OQ-042, OQ-043, OQ-044, OQ-045, OQ-046, OQ-047 all `:argued → :tested`. All 10 module-tier entries (OQ-040..OQ-049) now `:tested`.

## §1 Computational basis

The medical-devices module went from a partial scaffold (24 clauses across 4 standards) to comprehensive coverage (62 clauses across 11 standards) across two release cycles. v0.9.0 closed 6 module-tier entries; v0.10.0 closed the last one (OQ-044 EU MDR Annex I + Annex XIV).

### v0.9.0 — module 24 → 59 clauses

**Files new (4 templates):**

- `templates/product-dhf/technical-file/TECHNICAL-FILE-INDEX-TEMPLATE.md` — navigable manifest of the device's technical file. Indexes content by EU MDR Annex II section AND ISO 13485 §4.2.3 element. Cross-references the DHF, software lifecycle, and cross-cutting QMS evidence per product. Covers ISO13485-4.2.3 and MDR-AnnexII.
- `templates/qms-sops/AUDIT-PROCEDURE-TEMPLATE.md` — internal audit procedure SOP. Audit program planning, auditor independence, procedure (scoping → opening → evidence → categorization → closing → report → findings disposition → closure), records, management-review integration, regulatory-inspection interface. Covers ISO13485-8.2.4 and CFR820-820.22.
- `templates/product-dhf/usability/USABILITY-ENGINEERING-FILE-TEMPLATE.md` — IEC 62366-1 usability engineering file. Use specification, UI specification, primary operating functions, hazard-related use scenarios, formative + summative evaluation. Bound to the RMF. Covers IEC62366-1-5 (consolidated §5.1-§5.9).
- `templates/product-dhf/packaging/PACKAGING-VALIDATION-TEMPLATE.md` — ISTA packaging validation report. Test plan (conditioning, vibration, drop, compression, atmospheric), sample size, sterile-barrier integrity per ISO 11607, shelf life. Covers ISTA-2A and ISTA-3A.

**Files modified:**

- `modules/medical-devices/module.yaml` — version bumped 0.1.0 → 0.2.0. Standards list 4 → 11 (adds 21 CFR Part 11, EU MDR 2017/745, IEC 62366-1, IEC 60601-1, ISTA 2A, ISTA 3A, MDSAP). **35 new clauses** spanning all 7 added standards plus the missing ISO 13485 / 21 CFR 820 / IEC 62304 clauses identified in the crosswalk. Quality policy template gains 12 cross-cutting bindings; 21 CFR Part 11 §11.50 binds to `signature-meaning.md`; §11.70 + §11.100/200/300 bind to `gpg-signing.md`; §11.10(e) operational checks bind to `release-gate.yml`. CAPA / NCR issue templates bind to §820.90 / §820.100 / IEC 62304 §6 / §9.
- `bundles/example-samd.yaml` — standards list 5 → 12 (adds all 7 new module standards).
- `bundles/example-samd.matrix.json` — regenerated. 35 new in-scope clauses + 3 newly-bound existing artifacts.
- `engine/openqms/{__init__,pyproject.toml}` — 0.8.0 → 0.9.0.

### v0.10.0 — EU MDR Annex I + Annex XIV closure

**Files new (3 templates):**

- `templates/product-dhf/gspr/GSPR-CONFORMITY-CHECKLIST-TEMPLATE.md` — EU MDR Annex I checklist enumerating all 23 GSPRs across the three chapters (general requirements §1-9; design and manufacture §10-22; information supplied §23.1-23.4). Per-GSPR rows for Applicable/NA, standards used, evidence references, notes. Mandatory NA-justification section. Covers MDR-AnnexI.
- `templates/product-dhf/clinical/CLINICAL-EVALUATION-TEMPLATE.md` — EU MDR Annex XIV Part A Clinical Evaluation Report per MDCG 2020-13 / 2020-5 / 2020-6. Plan, data identification (literature / clinical experience / clinical investigations / equivalence), appraisal, analysis, conclusions, PMCF integration, update cadence per risk class. Covers MDR-AnnexXIV-A.
- `templates/product-dhf/clinical/PMCF-PLAN-TEMPLATE.md` — EU MDR Annex XIV Part B PMCF plan per MDCG 2020-7/8. Plan scope and rationale, PMCF methods (registries, surveys, PMS data, literature surveillance, PMCF studies), specific PMCF activity table, statistical considerations, GSPR/CER mapping, RMF integration, schedule per risk class. Covers MDR-AnnexXIV-B.

**Files modified:**

- `modules/medical-devices/module.yaml` — version 0.2.0 → 0.3.0. 3 new clauses (MDR-AnnexI, MDR-AnnexXIV-A, MDR-AnnexXIV-B); 3 new template bindings. Module size: 59 → 62 clauses; 28 → 31 artifacts.
- `bundles/example-samd.matrix.json` — regenerated to absorb the 3 new clauses + 3 new artifacts.
- `engine/openqms/{__init__,pyproject.toml}` — 0.9.0 → 0.10.0.

**Test environment:** unchanged. Test count remains 97 throughout (this work is content not engine code).

## §2 Results

- **Medical-devices module fully populated** across all 11 declared standards.
  - ISO 13485:2016: 11 clauses (§4.1.6, §4.2.3, §4.2.4, §4.2.5, §5.6, §6.3, §7.3, §7.4, §8.2.2, §8.2.3, §8.2.4) — all originally-listed clauses plus 4 extras.
  - 21 CFR 820: 11 sections (§820.20, §820.20(c), §820.22, §820.30, §820.40, §820.50, §820.70, §820.90, §820.100, §820.180, §820.198).
  - 21 CFR Part 11: 10 subclauses (§11.10(a-e), §11.50, §11.70, §11.100, §11.200, §11.300) — full coverage; §11.50 satisfied via OQ-060 trailers, §11.70 + 100/200/300 via OQ-023 GPG guide.
  - EU MDR 2017/745: 6 elements (Article 10(9), Annex I, Annex II, Annex IX, Annex XIV Part A, Annex XIV Part B) — full coverage at v0.10.0.
  - ISO 14971:2019: §4-§10 (already complete at v0.3.0 via OQ-049).
  - IEC 62304:2006+A1:2015: 12 clauses (§5.1, §5.2, §5.3, §5.4, §5.5, §5.6, §5.7, §5.8, §6, §7, §8.1.2, §9).
  - IEC 62366-1:2015+A1:2020: consolidated §5 (5.1-5.9).
  - IEC 60601-1:2005+A1+A2: general safety + essential performance, bound to verification protocol (test reports from external accredited labs).
  - ISTA 2A + 3A: bound to packaging validation template.
  - MDSAP: composite clause noting it composes ISO 13485 + jurisdiction-specific additions; bound to quality-policy + supplier-evaluation.

- **Templates: 11 → 14 (v0.9.0) → 18 (v0.10.0).** Eight new document templates between v0.9.0 (4) and v0.10.0 (3) plus existing template bindings extended.

- **Example bundle exercises the full coverage.** `bundles/example-samd.yaml` now lists 12 standards (10 medical-device + 1 infosec overlay + MDSAP composite); the regenerated matrix contains 46 in-scope clauses across 14 artifacts for the SaMD/iso-27001 composite.

- **Per-class customization noted but not enforced.** GSPR template (v0.10.0) ships with placeholder A/NA values; adopters customize per Annex VIII classification. Device-class overlay sub-modules become the natural next iteration after this milestone (delivered at v0.11.0).

## §3 Verification

| Spec entry | Claim | Evidence type | How |
|---|---|---|---|
| OQ-041 | ISO 13485:2016 coverage (11 clauses) | example-tested | Module manifest contains 11 ISO13485-* clauses; each bound to ≥1 template; validation harness passes; CI `engine-tests.yml` runs validate on every push. |
| OQ-042 | 21 CFR 820 coverage (11 sections) | example-tested | Module manifest contains 11 CFR820-* clauses; each bound; validation passes. |
| OQ-043 | 21 CFR Part 11 full coverage (10 subclauses) | example-tested | All 10 CFR11-* subclauses present; §11.50 binds to `signature-meaning.md` (OQ-060); §11.70 + 11.100/200/300 bind to `gpg-signing.md` (OQ-023); §11.10(e) binds to `release-gate.yml`. |
| OQ-044 | EU MDR coverage (6 elements) | example-tested | All 5 originally-listed annex/article items + Annex XIV split into Parts A/B = 6 clauses; each bound to a template (TFI, GSPR checklist, CER, PMCF, quality-policy, management-review). |
| OQ-045 | IEC 62304 coverage (12 clauses) | example-tested | 12 IEC62304-* clauses bound to SRS / SAD / SOUP / STP / SRR / RMF / CAPA / NCR templates. |
| OQ-046 | IEC 62366-1 + IEC 60601-1 coverage | example-tested | IEC62366-1-5 bound to UEF template; IEC60601-1-general bound to verification protocol. |
| OQ-047 | ISTA 2A/3A + MDSAP coverage | example-tested | ISTA-2A + ISTA-3A bound to packaging template; MDSAP-composite bound to quality-policy + supplier-evaluation. |

## §4 Spec impact

| S-ID | Before | After | Evidence type after |
|---|---|---|---|
| OQ-041 | `:argued` | `:tested` | example-tested |
| OQ-042 | `:argued` | `:tested` | example-tested |
| OQ-043 | `:argued` | `:tested` | example-tested |
| OQ-044 | `:argued` | `:tested` | example-tested |
| OQ-045 | `:argued` | `:tested` | example-tested |
| OQ-046 | `:argued` | `:tested` | example-tested |
| OQ-047 | `:argued` | `:tested` | example-tested |
| OQ-038 | `:tested` (template count notes updated 14 → 21) | `:tested` | example-tested |
| OQ-068 | `:tested` (subdir count notes updated; gspr + clinical subdirs new at v0.10.0) | `:tested` | example-tested |

Status counts at end of v0.10.0: 38 `:tested` · 8 `:argued` · 0 `:open` · total 46.

**All 10 medical-devices module-tier entries (OQ-040 through OQ-049) now `:tested`.** The medical-devices module is comprehensively populated; the natural next iteration is device-class overlay sub-modules to handle per-class GSPR applicability + class-specific submission paths (delivered at v0.11.0).
