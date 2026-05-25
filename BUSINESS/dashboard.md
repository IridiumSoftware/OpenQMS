# Dashboard — Open QMS

**Version:** v0.1.0 DRAFT (cumulative through engine v0.24.0)
**Date:** 2026-05-23
**Maintainer:** Aaron Green

Current state + priority stack. Read this first every session. For claim status, see `ENGINE_SPEC.md`. For history, `changelog.md`. For evidence map, `artifact_registry.md`.

---

## Status summary

| Status | Count | Tier breakdown |
|---|---|---|
| `:proved` | 0 | — |
| `:verified` | 0 | — |
| `:verified` | 6 | Invariant (2, OQ-001 + OQ-002) · Architecture (4, OQ-010 + OQ-011 + OQ-013 + OQ-015) |
| `:tested` | 91 | Architecture (5, OQ-012 + OQ-014 + OQ-115 + OQ-116 + OQ-117) · Substrate (3) · Workflow (9) · Module (61, OQ-040..OQ-059 + OQ-072..OQ-079 + OQ-081..OQ-096 + OQ-098 + OQ-101..OQ-114 + OQ-118) · Gap (13, OQ-060 + OQ-061 + OQ-062 + OQ-063 + OQ-064 + OQ-065 + OQ-066 + OQ-067 + OQ-068 + OQ-069 + OQ-080 + OQ-097 + OQ-099 + OQ-100) |
| `:benchmarked` | 0 | — |
| `:argued` | 5 | Invariant (1, OQ-003) · Substrate (2, OQ-022 + OQ-023) · Licensing (2, OQ-070 + OQ-071) |
| `:open` | 0 | — |
| **Total** | **102** | — |

Counts: 6 + 91 + 5 + 0 = 102 ✓. **Latest at v0.50.0**: Final cross-overlay batch (4). OQ-118 NEW `:tested` — completes cross-overlay shape coverage across remaining major vertical intersections. **automotive-supply-chain** (automotive + asil-d + cal-4 + recall-workflow — DIA + CIA + AIAG PPAP + UN R155 + R156 + NHTSA Part 573 + tier-N flow-down). **clinical-trial-multi-region** (pharma + privacy + hipaa + digital-health-multi-region — ICH E6(R3) + EU CTR + 21 CFR 312 + DCT + multi-region PHI + parallel IRB/IEC + RBM + multi-region PV). **banking-resilience** (iso-37301-financial-services + dora + nist-csf + iso-22301 — DORA + FFIEC + NIST CSF backbone + multi-stream incident + TLPT + CTPP). **utility-cybersecurity** (manufacturing + iso-27001 + nist-csf — NERC CIP + TSA SD + CISA 16-sector + EU NIS2 + IEC 62443 + CIRCIA). Registry +5 PUBLIC. Cross-overlay count 8 → 12. Module count 112 → 116. CI +8 validate steps. Spec total 101 → 102. **Polishing pass follows as v0.51.0.**

**Phase 0 round-out complete (v0.2.1 → v0.3.0).** P5, P6, P7 all closed. **Phase 1 mostly closed.** P1.1 at v0.4.0; P1.2 at v0.5.0. Remaining Phase 1: P1.3 (re-resolution on mutation, OQ-015 + OQ-065). P8 (Part 11 §11.50 prototype, OQ-060) and continued module-coverage population remain.

**v0.2.1 transitions:** OQ-062 `:open → :argued` (PHI/PII compartmentalization architecture decided); OQ-069 stays `:tested` (claim reframed; complaint template shipped); OQ-038 notes updated (3 → 4 templates including complaint).
**v0.2.2 transitions:** OQ-023 stays `:argued` (GPG signing guide shipped; mechanism unchanged, doc adopter-actionable).
**v0.3.0 transitions:** OQ-049 NEW `:tested` (ISO 14971 complete coverage); OQ-068 stays `:tested` (claim reframed; 8 of 15 originally-empty subdirs populated); OQ-038 notes updated (4 → 11 templates).
**v0.4.0 transitions:** OQ-011 `:open → :tested` (modules compose under union); OQ-012 `:open → :tested` (cross-cutting overlays compose with vertical); OQ-048 `:argued → :tested` (ISO/IEC 27001 overlay module shipped).
**v0.5.0 transitions:** OQ-014 `:open → :tested` (standards-and-jurisdictions registry shipped at `registry/`; CLI strict-validates and normalizes aliases; module manifests cross-checked).
**v0.6.0 transitions:** OQ-015 `:open → :tested` (re-resolution + Git-reviewable diff shipped as `openqms regenerate` over stored bundle definitions); OQ-065 `:open → :tested` (module-version drift detection via registry `superseded_by` + `--strict-editions`).
**v0.7.0 transitions:** OQ-060 `:open → :tested` (Part 11 §11.50 signature-meaning prototype: commit-trailer convention + parser + CLI `signatures verify/export` + Part 11 JSON audit-trail exporter + dormant CI gate + guide).
**v0.8.0 transitions:** OQ-063 `:open → :tested` (supplier-evaluation workflow: ASL + per-supplier evaluation + issue template + guide; bound to ISO 13485 §7.4 + 21 CFR 820.50); OQ-064 `:open → :tested` (management-review aggregation: meeting record template + issue template + `gh` CLI aggregation-pattern guide; bound to ISO 13485 §5.6 + 21 CFR 820.20(c)). OQ-041 + OQ-042 notes updated for the additional 4 ISO 13485 / 21 CFR 820 clauses now machine-readable.
**v0.9.0 transitions:** OQ-041 + OQ-042 + OQ-043 + OQ-045 + OQ-046 + OQ-047 all `:argued → :tested` (medical-devices module fully populated to 59 clauses across 11 standards; 4 new templates shipped — technical-file index, audit procedure SOP, usability engineering file, packaging validation). OQ-044 stays `:argued` with partial coverage (3 of 5 originally-listed annexes; Annex I GSPRs and Annex XIV CER deferred to device-class overlays). OQ-038 + OQ-068 updated.
**v0.10.0 transitions:** OQ-044 `:argued → :tested` (EU MDR Annex I GSPRs + Annex XIV Part A CER + Part B PMCF templates shipped; 3 new clauses + 3 new template bindings; 2 new template subdirs gspr/ and clinical/). OQ-038 template count 18 → 21. OQ-068 subdirectory count updated. **All 10 module-tier entries (OQ-040..OQ-049) now `:tested`.**
**v0.11.0 transitions:** 4 NEW spec entries — OQ-050 SaMD overlay, OQ-051 implantable overlay, OQ-052 EU MDR Class III overlay, OQ-053 FDA Class III overlay. 5 new standards in registry (IEC 82304-1, ISO 14708-1, 21 CFR 814, 21 CFR 803, IMDRF SaMD N12). 5 new templates. OQ-038 template count 21 → 26. **Spec total grew 46 → 50.**
**v0.12.0 transitions:** 5 NEW spec entries across three commits — Phase A: OQ-054 MDR Class IIb, OQ-055 MDR Class IIa, OQ-056 FDA Class II (510(k)). Phase B: OQ-057 IVD overlay (IVDR + 21 CFR 809 + ISO 15189). Phase C: OQ-058 regulated-AI overlay (NIST AI RMF + EU AI Act + ISO 42001 + ISO 23894). 6 new standards in registry. 5 new templates. OQ-038 template count 26 → 31. **Spec total grew 50 → 55.**
**v0.13.0 transitions:** OQ-001 + OQ-010 + OQ-011 + OQ-013 + OQ-015 `:tested → :verified`; OQ-002 `:argued → :verified`. **First `:verified` entries in the spec.** 11 hypothesis property tests in `engine/tests/test_property.py`; `hypothesis>=6.100` added to dev deps. Test count 97 → 108. OQ-002 was the only `:argued` entry where mechanical verification was achievable; all remaining `:argued` are honest-effort items (manual-by-nature licensing, adopter-org-gated substrate enforcement, SOP-bound architecture decisions).
**v0.14.0 transitions:** OQ-059 NEW `:tested` (aerospace vertical — first non-medical vertical regulatory module). 27 clauses across 9 aerospace standards; 5 new aerospace-specific templates (PSAC / FHA / SSP / FAI Report / Type Cert Pack Index); 3 new jurisdictions (FAA / EASA / TCCA). New `bundles/example-aircraft` with committed baseline matrix; CI extended. Module-tier count grew 19 → 20. Spec total 55 → 56.
**v0.15.0 transitions:** OQ-072 NEW `:tested` (automotive vertical — second non-medical vertical). 28 clauses across 8 automotive standards spanning four discipline tracks (IATF 16949 substrate; ISO 26262 FuSa across all 12 parts with ASIL A-D; ISO/SAE 21434 cyber with CAL 1-4; UN R155 + R156 regulations); 5 new automotive-specific templates (Item Definition / HARA / Safety Concept with Cybersecurity Concept Part C / TARA / PPAP); 4 new jurisdictions (NHTSA / UNECE / KBA / TC-MVS). New `bundles/example-vehicle` with committed baseline; CI extended. Module-tier count grew 20 → 21. Spec total 56 → 57.
**v0.16.0 transitions:** 6 NEW Module-tier entries — OQ-073 (aerospace DAL-A), OQ-074 (DAL-B), OQ-075 (DAL-C), OQ-076 (automotive ASIL-D), OQ-077 (ASIL-B), OQ-078 (CAL-4). Each is a small overlay (~5-7 clauses) encoding the rigor delta vs. the baseline vertical. Composes validated standalone + 5-module mega-composite. CI extended (+7 validate steps). Module-tier count grew 21 → 27. Spec total 57 → 63.
**v0.17.0 transitions:** 9 NEW Module-tier entries completing the class-overlay coverage + adding the 4th vertical — OQ-079 (aerospace DAL-D), OQ-081 (DAL-E), OQ-082 (ASIL-C), OQ-083 (ASIL-A), OQ-084 (QM), OQ-085 (CAL-3), OQ-086 (CAL-2), OQ-087 (CAL-1), OQ-088 (general manufacturing vertical — ISO 9001 only). 21 total class overlays across three regulated verticals (medical 7 + aerospace 5 + automotive 9). 4 total verticals (medical-devices / aerospace / automotive / manufacturing). CI extended (+15 validate steps + 1 regenerate dry-run). Module-tier count grew 27 → 36. Spec total 63 → 72.
**v0.18.0 transitions:** 3 NEW Module-tier entries — OQ-089 (ISO 14001 environmental cross-cutting overlay), OQ-090 (ISO 45001 OH&S), OQ-091 (ISO 50001 energy). Each composes with any vertical (12 composites validated: 3 overlays × 4 verticals). 3 new templates (Environmental Aspects Register / HIRA / Energy Review + EnPIs + EnB Baseline). 3 new registry standards. CI extended (+8 validate steps). Module-tier count grew 36 → 39. Spec total 72 → 75.
**v0.19.0 transitions:** OQ-092 NEW `:tested` (pharma vertical — 5th vertical; ICH + cGMP + EU GMP + PIC/S Annex 1; 23 clauses across 8 standards; 6 new pharma-specific templates — MBR, VMP, Deviation, Change Control, OOS, APQR). First vertical where most cited standards are PUBLIC license. Registry +7 standards + 3 jurisdictions. New example bundle (sterile SVP injection). CI +3 validate steps. Module-tier count 39 → 40. Spec total 75 → 76.
**v0.20.0 transitions:** OQ-093 NEW `:tested` (food-safety vertical — 6th vertical; ISO 22000 + FSSC 22000 v6 + Codex HACCP + FSMA Preventive Controls + Seafood HACCP; 16 clauses across 5 standards; 3 new food-safety-specific templates — HACCP Plan, Prerequisite Programs, Recall + Withdrawal Procedure). Registry +5 standards + 4 jurisdictions. New example bundle (RTE chilled-foods processor). CI +2 validate steps. Module-tier count 40 → 41. Spec total 76 → 77.
**v0.21.0 transitions:** OQ-094 NEW `:tested` (ISO 37001 anti-bribery management overlay — 14 clauses + 1 new template Anti-Bribery Due Diligence); OQ-095 NEW `:tested` (ISO 22301 BCMS overlay — 13 clauses + 1 new template Business Continuity Plan). **Completes the common Annex-SL cross-cutting overlay set: 7 overlays now shipped** (iso-27001 + regulated-ai + iso-14001 + iso-45001 + iso-50001 + iso-37001 + iso-22301). Registry +2 standards. CI +6 validate steps (incl. 8-module ultimate composite — deepest tested). Module-tier count 41 → 43. Spec total 77 → 79.
**v0.22.0 transitions:** OQ-096 NEW `:tested` (ATMP class overlay on pharma — 10 clauses across EU GMP Annex 2A+2B + 21 CFR 1271 + ICH Q5A(R2); 3 new ATMP-specific templates: Donor Eligibility Assessment, Tissue/Cell Traceability Record, Viral Safety Evaluation Report). First pharma class overlay. All cited standards PUBLIC license. Registry +4 standards. New example bundle (autologous CAR-T). CI +3 validate steps + 1 regenerate. **9-module deepest composite validates** (pharma + atmp + 7 cross-cutting — realistic commercial-stage cell-therapy shape). Module-tier count 43 → 44. Spec total 79 → 80.
**v0.23.0 transitions:** OQ-097 NEW `:tested` (Gap-tier — public adopter-surface release closing P10 from original priority stack). README rewritten from v0.7.0-era to v0.22.0+ state; new docs/modules-catalog.md; food-safety + atmp READMEs backfilled; BUSINESS/ un-gitignored. Pure consolidation. Spec total 80 → 81.
**v0.24.0 transitions:** OQ-098 NEW `:tested` (cross-vertical recall-workflow overlay — 11 clauses across NHTSA Part 573/577/579 + FDA 21 CFR 7/806 + CPSIA §15; 2 new templates: Generalized Recall Procedure cross-vertical + NHTSA Part 577 Owner Notification Letter). Composes with ANY vertical. **10-module composite validates** (new depth): automotive + asil-d + cal-4 + recall-workflow + 5 cross-cutting + iso-22301. Registry +6 standards (all PUBLIC). Spec total 81 → 82.
**v0.25.0 transitions:** OQ-099 NEW `:tested` (Gap-tier — standalone template library expansion: 15 templates across Group A cross-vertical management-system / Group B domain-specific registers / Group C pharma + ATMP specialty). Group A: Quality Manual + Process Map + Risk-and-Opportunity Register + Risk Assessment standalone + BIA standalone + IT DR Plan. Group B: Compliance Obligations Register (ISO 14001 §6.1.3 dedicated) + OH&S Legal Register (ISO 45001 §6.1.3) + Energy Objectives Register (ISO 50001 §6.2). Group C: Site Master File + Batch CoA + Stability Protocol (ICH Q1A(R2) full design) + Comparability Protocol (ICH Q5E) + CAR-T release testing + AAV release testing. Templates ship standalone; bindings forward work. Template count 54 → 69. Spec total 82 → 83.
**v0.26.0–v0.35.0 transitions (rolled-up):** 5 NEW Module-tier entries + 1 NEW Gap-tier entry. OQ-100 Gap-tier per-module READMEs backfill (v0.26.0+v0.27.0). OQ-101 pharma class overlay batch ×5 sterile/biologics/IMP/generic-biosimilar/clinical-stage (v0.28.0). OQ-102 food-safety class overlay batch ×5 USDA-FSIS/animal/produce/IA/FSVP (v0.29.0). OQ-103 aerospace+automotive extension + IVDR class overlay batch ×6 defense/commercial-space/auto-defense/motorcycle/IVDR-C/IVDR-D (v0.30.0). OQ-104 cross-cutting overlay batch ×11 (v0.31.0+v0.32.0+v0.33.0 — soc-2 + pci-dss + hitrust-csf + nist-csf + iso-31000 + iso-37301 + dora + eu-gpsr + tisax + defense-cui + cmmc). v0.34.0 template binding pass + v0.35.0 documentation omnibus + catalog refresh. Module-tier count 39 → 50. Spec total 83 → 88. Cross-cutting overlay set 7 → 19. Detailed delta in `companion_v0_24_to_34_omnibus.md`.
**v0.36.0 transitions:** OQ-105 NEW `:tested` (chemicals vertical — 7th vertical; REACH + CLP + GHS + GLP + TSCA; 21 clauses; 4 chemicals-specific templates SDS + REACH dossier + CLP notification + GLP study; all 5 standards PUBLIC license). New example bundle `example-specialty-chemical` (50-100 t/y SVHC-adjacent intermediate). CI extended (+5 validate steps + 1 regenerate). Module-tier count 50 → 51. Spec total 88 → 89.
**v0.37.0 transitions:** OQ-106 NEW `:tested` (chemicals-adjacent standalones — 4 cross-cutting overlays: osha-hcs 29 CFR 1910.1200 HazCom 2024 + transport-hazmat DOT HMR + IMDG + IATA DGR + ADR + RID + eu-biocides BPR 528/2012 + tsca-pfas 40 CFR 705 reporting rule). 4 new templates (HAZCOM-WRITTEN-PROGRAM + SHIPPING-PAPER multi-modal + HMT-TRAINING-RECORD + BPR-AUTHORISATION-APPLICATION + PFAS-REPORTING-FORM). Registry +9 standards (8 PUBLIC; IMDG + IATA DGR commercial). Cross-cutting overlay count: 19 → 23. **13-module composite validates** (new depth record): chemicals + 4 adjacent + 8 cross-cutting. Discharges all 4 chemicals-companion forward-work items. CI extended (+12 validate steps). Module-tier count 51 → 52. Spec total 89 → 90.
**v0.38.0 transitions:** OQ-107 NEW `:tested` (chemicals class overlay batch — 6: chemicals-svhc REACH Article 7(2) + 33(1)/(2) + SCIP database + Annex XV; chemicals-authorisation Title VII Articles 55-66 + Annex XIV; chemicals-tonnage-1 Annex VII baseline; chemicals-tonnage-10 Annex VIII + CSR mandatory; chemicals-tonnage-100 Annex IX + 90-day RDT + reproductive screening; chemicals-tonnage-1000 Annex X + chronic + carcinogenicity + EOGRTS). 3 new templates (SVHC-COMMUNICATION-LETTER + REACH-AUTHORISATION-APPLICATION + SUBSTITUTION-PLAN). Class-overlay count 38 → 44 (chemicals first class-overlay set). **16-module composite validates** (new depth record): chemicals + SVHC + Authorisation + tonnage-1000 + 4 adjacent + 8 cross-cutting. No registry additions (reuses existing EU REACH). Cumulative v0.36-38: 11 chemicals-domain modules. CI extended (+12 validate steps). Module-tier count 52 → 53. Spec total 90 → 91.
**v0.39.0 transitions:** OQ-062 `:argued → :tested` (PHI/PII compartmentalization — 4 new structural property tests at `engine/tests/test_phi_compartmentalization.py` asserting complaint intake template cannot capture PHI by design: (1) YAML loads cleanly; (2) no field id/label matches PHI patterns; (3) PHI-handling warning present; (4) external-record reference present). OQ-067 `:argued → :tested` (repo-wide trace matrix shipped as `openqms trace` CLI subcommand: walks all modules, emits forward + reverse maps + orphan detection per module + aggregate summary; JSON or Markdown output; 4 new tests at `engine/tests/test_trace.py`). Pytest count 108 → 116 (+8). CI extended with `openqms trace --all` step asserting zero-orphan invariant across all modules. At audit time reports 75 modules / 614 clauses / 299 templates / 0 orphaned clauses / 0 orphaned templates. Engine 0.38.0 → 0.39.0. `:argued` count 7 → 5 (only honest-effort-by-nature entries remain).
**v0.40.0 transitions:** Hygiene pass discharging audit F1-F6 + adding YAML linter + v0.39 companion. No spec status changes. (1) OQ-054..OQ-058 registry rows expanded from prior condensed snapshot — A1 coverage gap now zero (91/91). (2) Template count "81+" → exact "87" in README + catalog. (3) Catalog `ivd` re-categorised as sub-vertical (clarifies F6). (4) `scripts/lint-module-yaml.py` added + wired into CI as pre-pytest gate — catches the unquoted-colon-in-template-name failure mode observed during chemicals arc + asserts every clause has id/standard/section/summary + every template addresses entries refer to in-module clauses. Linter clean on all 75 modules. (5) `traceability.yml` job ID renamed `generate-trace-matrix → generate-traceability-snippet` (cosmetic cleanup OQ-067 deferred since v0.1.1). (6) `companion_v0_39_argued_push.md` shipped + indexed.
**v0.41.0 transitions:** OQ-108 NEW `:tested` (privacy cross-cutting overlay — GDPR Regulation 2016/679 + CCPA Cal. Civ. Code §1798.100-199; 21 clauses across principles + lawful bases + Article 9 special categories + data subject rights + controller/processor obligations + ROPA + security + breach + DPIA + DPO + international transfers + CCPA consumer rights + business obligations + CPPA ADMT/Risk/Cybersecurity regulatory regime). 5 new substantial templates: PRIVACY-POLICY (Articles 13-14 + CCPA notice with all 11 CCPA categories + SPI + lawful-basis grid + GPC honoring); DPA (Article 28 + CCPA §7050-7053 + 2021/915 SCCs + Transfer Impact Assessment); DPIA (Article 35 + CCPA Risk Assessment + WP248 rev.01 9-criteria + WP250 consequences); ROPA (Article 30 controller Part A + processor Part B); PERSONAL-DATA-BREACH-NOTIFICATION (Article 33 SA 72h + Article 34 subjects + Article 33(5) documentation + CCPA §1798.150 PRA + US state AG cross-reference + HIPAA + FTC HBNR + SEC Item 1.05 8-K). Both standards PUBLIC license. 24th cross-cutting overlay; **last major management-system gap closed**. Registry +2 standards. **17-module ultimate composite validates** (new depth record beats prior 16-module). CI extended (+11 validate steps). Module-tier count 53 → 54. Spec total 91 → 92.
**v0.42.0 transitions:** OQ-109 NEW `:tested` (sub-overlay batch — 16 sub-overlays splitting monolithic cross-cutting overlays into rigor/scope/tier deltas; new module shape). 3 CMMC levels (cmmc-level-1 FCI / cmmc-level-2 CUI / cmmc-level-3 NS-critical CUI) + 2 SOC 2 types (soc-2-type-i point-in-time / soc-2-type-ii observation-period) + 2 ISO 27001 extensions (iso-27001-cloud 27017 / iso-27001-privacy 27701 PIMS) + 4 NIST CSF Implementation Tiers (nist-csf-tier-1 Partial / tier-2 Risk Informed / tier-3 Repeatable / tier-4 Adaptive) + 5 PCI DSS SAQ types (pci-dss-saq-a / saq-a-ep / saq-d-merchant / saq-d-sp / saq-p2pe). Registry +2 commercial standards (ISO 27017 + ISO 27701); other 14 reuse existing registered standards. Total module count 76 → 92. Cross-cutting overlay count unchanged at 24. **19-module deepest composite validates** (new depth record). CI extended (+23 validate steps). Module-tier count 54 → 55. Spec total 92 → 93.

**Zero `:open` entries.** Remaining work surface: module-coverage population continues (OQ-041 ISO 13485 5/full; OQ-042 21 CFR 820 5/full; OQ-045 IEC 62304 7/9; OQ-043 / 044 / 046 / 047 still `:argued` with no machine-readable bindings yet).

**Honest read of v0.1.0:** Phase 0 (scaffold + workflows) is substantially `:tested`. Phase 1 (generator engine) is uniformly `:open`. The load-bearing invariant (OQ-001) is `:argued` until Phase 1 lands. The regulatory module pattern is sketched (`:argued`) but the medical-devices module is not yet machine-readable.

---

## Phase 0 → Phase 1 boundary

Phase 0 = **scaffold + workflows**. Today's working CI / templates / setup script. Mostly `:tested`.

Phase 1 = **generator engine**. Bundle resolver, module library with structured clause tables, standards/jurisdictions registry, validation harness, re-resolution-on-mutation. Currently 6 `:open` Architecture entries.

Phase 2+ = **additional regulatory modules** (regulated AI ✓ v0.12.0; aerospace ✓ v0.14.0; automotive ✓ v0.15.0; aerospace class overlays ✓ v0.16.0+v0.17.0 — A/B/C/D/E full set; automotive class overlays ✓ v0.16.0+v0.17.0 — ASIL D/C/B/A/QM + CAL 4/3/2/1 full sets; general manufacturing ✓ v0.17.0; pharma / food / fintech / industrial-machinery functional-safety forward), **digital signatures** build-out ✓ (Part 11 prototype v0.7.0), **PHI/PII compartmentalization** ✓ (architecture v0.2.1), **management-review aggregation** ✓ (v0.8.0).

---

## Priority stack

Ordered by load-bearingness. Each item names the S-ID it addresses, the artifact it produces, and the status transition expected.

### ~~P1 — Build the generator engine MVP (CLI bundle resolver)~~ ✓ (closed at v0.2.0)

**Addresses:** OQ-010, OQ-013, OQ-066 closed. OQ-011, OQ-014, OQ-015 deferred to follow-up priorities below.
**Resolution:** v0.2.0 — Python engine at `engine/` (commit `4a72a9f`). `openqms resolve` and `openqms validate` CLIs work end-to-end against the medical-devices module. 15-test pytest suite covering loader, resolver, validation, and a medical-devices integration smoke. CI workflow `.github/workflows/engine-tests.yml` runs on every push touching `engine/`, `modules/`, or `templates/`.
**Status transitions:** OQ-010 `:open → :tested`, OQ-013 `:open → :tested`, OQ-066 `:open → :tested`, OQ-001 `:argued → :tested`, OQ-040 `:argued → :tested`.
**Companion doc:** `BUSINESS/companion_engine_mvp.md`.
**Follow-up priorities split out below as P1.1 (composition), P1.2 (registry), P1.3 (re-resolution).**

### P2 — Convert medical-devices crosswalk into a machine-readable module *(partial at v0.2.0)*

**Addresses:** OQ-040 closed; OQ-041..OQ-048 partial (~15% of the 27-clause full crosswalk machine-readable so far).
**Status at v0.2.0:** `modules/medical-devices/module.yaml` ships with 4 of the 27 crosswalk clauses (ISO 13485 §4.2.4, §7.3; 21 CFR 820 §820.30, §820.40) bound to the 3 artifact templates currently in `templates/`. Validation harness passes.
**Remaining work:** Fold in the remaining 23 clauses as additional artifact templates land. Each clause addition requires: (a) the clause entry in `module.yaml`, (b) at least one artifact template in `templates/` (existing or new) declaring the clause in its `addresses` binding, (c) the validation harness staying green.
**Status transitions for completion:** OQ-041..OQ-048 each move `:argued → :tested` once the full clause set of that standard is in `module.yaml`. Partial mechanization is recorded in each entry's notes, not the status field.

### ~~P1.1 — Multi-module composition~~ ✓ (closed at v0.4.0)

**Addresses:** OQ-011, OQ-012, OQ-048.
**Resolution:** v0.4.0 (commit `2a146ad`) — added `openqms.module.compose(list[Module]) -> Module` as a new primitive (resolver signature unchanged; composition is its own testable function). CLI `--module` is repeatable on both `resolve` and `validate`; multiple modules are composed before the operation. Shipped a minimal ISO/IEC 27001:2022 cross-cutting overlay module at `modules/iso-27001/` (3 clauses bound to 3 existing OpenQMS templates) to exercise the composition primitive end to end. Integration tests confirm the medical-devices + iso-27001 composite validates and resolves with merged template addresses.
**Status transitions:** OQ-011 `:open → :tested`, OQ-012 `:open → :tested`, OQ-048 `:argued → :tested`.

### ~~P1.2 — Standards-and-jurisdictions registry~~ ✓ (closed at v0.5.0)

**Addresses:** OQ-014.
**Resolution:** v0.5.0 (commit `12b6b33`) — registry shipped at `registry/standards.yaml` (15 entries) + `registry/jurisdictions.yaml` (6 entries) + `registry/README.md`. Engine code at `engine/openqms/registry.py` with `Registry`/`StandardEntry`/`JurisdictionEntry` frozen dataclasses, `load_registry()` with dangling-reference cross-check, and `validate_module_against_registry()`. CLI normalizes `--standard` aliases to canonical ids before passing to resolver; rejects unknown standards and jurisdictions with helpful error messages listing registered ids. New subcommand `openqms registry list/show`. Escape hatch `--allow-unregistered-standards` for migration paths (jurisdictions remain strictly validated).
**Status transitions:** OQ-014 `:open → :tested`.

### ~~P1.3 — Re-resolution on mutation~~ ✓ (closed at v0.6.0)

**Addresses:** OQ-015, OQ-065.
**Resolution:** v0.6.0 (commit `3cfec2c`) — shipped `openqms regenerate --bundle <name>` CLI subcommand operating on stored bundle definitions at `bundles/<name>.yaml` and committed matrix files at `bundles/<name>.matrix.json`. The matrix file's Git diff is the regulatory audit trail. New modules `engine/openqms/bundle.py` (loader) and `engine/openqms/diff.py` (`MatrixDiff` + `format_diff`). Edition supersession via `superseded_by` field on registry entries + `--strict-editions` CLI flag on `validate` and `regenerate`. Shipped `bundles/example-samd.{yaml,matrix.json}` as a committed regression baseline; CI runs `regenerate` in dry-run mode on every push touching `engine/`, `modules/`, `registry/`, `templates/`, or `bundles/`.
**Status transitions:** OQ-015 `:open → :tested`, OQ-065 `:open → :tested`.

### ~~P3 — Implement or remove `generate-trace-matrix.sh`~~ ✓ (closed at v0.1.1)

**Addresses:** OQ-067, OQ-031.
**Resolution:** Doc-only fix at v0.1.1. Replaced the broken `./scripts/generate-trace-matrix.sh` reference in `docs/guide/traceability.md` with a "Repository-wide traceability matrix (forward)" subsection pointing at the engine-driven Phase-1 deliverable.
**Status transitions:** OQ-067 `:open → :argued` ✓
**Follow-up observation (not yet ticketed):** the YAML job ID `generate-trace-matrix` in `traceability.yml:43` is the same misleading name. The job's display name ("Generate traceability snippet") is accurate; the YAML ID is not. Renaming touches Actions run history and any branch-protection required-checks configured against the old name, so defer to a deliberate cleanup pass.

### ~~P4 — Tighten training-trigger YAML parsing~~ ✓ (closed at v0.1.2)

**Addresses:** OQ-061.
**Resolution:** v0.1.2 — replaced the regex-based parsing in `.github/workflows/training-trigger.yml` with a Python 3.12 + PyYAML parse step that emits a JSON payload consumed by the issue-creation step. Parses both `docs/qms-config.yml` and per-document frontmatter using `yaml.safe_load`. Behaviour preserved (config-missing → no issues + warning; config-present-but-empty-trainees → issues with placeholder).
**Status transitions:** OQ-035 stays `:tested`; OQ-061 stays `:tested` with the claim reframed (was "is brittle"; now "uses real parser — gap closed").

### ~~P5 — Add complaint issue template (or document why deferred)~~ ✓ (closed at v0.2.1)

**Addresses:** OQ-069, OQ-062.
**Resolution:** v0.2.1 (commit `2fe3ef6`) — both deliverables in one release:
- `.github/ISSUE_TEMPLATE/complaint.yml` ships with form validation, PHI-redacted intake fields, and required PHI-handling confirmation checkboxes.
- `docs/guide/complaints.md` documents the compartmentalization architecture decision: PHI/PII lives in a sibling access-restricted record (Pattern A: private GitHub repo; Pattern B: external eQMS). The main-repo issue captures only triage metadata.
- Medical-devices module manifest gains ISO 13485 §8.2.2 + 21 CFR 820.198 as clauses, both bound to the new template.
**Status transitions:** OQ-069 stays `:tested` (claim reframed); OQ-062 `:open → :argued`.

### ~~P6 — Populate the high-priority template subdirectories~~ ✓ (closed at v0.3.0)

**Addresses:** OQ-068 (partial — 8 of original 15 dirs populated; 7 intentionally adopter-defined remain); OQ-049 (NEW — ISO 14971 full coverage); OQ-038 (template count 4 → 11).
**Resolution:** v0.3.0 (commit `2625b98`) — eight IEC 62304 / ISO 14971 workhorse templates shipped: `RISK-MANAGEMENT-FILE-TEMPLATE` (ISO 14971 §4-10), `VERIFICATION-PROTOCOL-TEMPLATE`, `VALIDATION-PROTOCOL-TEMPLATE`, `SOFTWARE-REQUIREMENTS-TEMPLATE` (IEC 62304 §5.2), `SOFTWARE-ARCHITECTURE-TEMPLATE` (§5.3), `SOUP-REGISTER-TEMPLATE` (§8.1.2), `SOFTWARE-TEST-PROTOCOL-TEMPLATE` (§5.5 + §5.6 + §5.7), `SOFTWARE-RELEASE-TEMPLATE` (§5.8). Medical-devices module manifest extended with 14 new clauses and 8 new template bindings. Validation harness passes on 20 clauses / 12 artifacts.
**Status transitions:** OQ-049 NEW `:tested`; OQ-068 stays `:tested` (claim reframed); OQ-038 updated.
**Remaining template work (P6.1, low priority):** 7 dirs still placeholder-only: `qms-{capa,forms,training,suppliers,management-review}/` (org-level workflows) and `product-dhf/{design-outputs,technical-file}/` (product-specific). These are intentionally adopter-defined; not on the v0.4 roadmap.

### ~~P7 — Org-level GPG enforcement documented~~ ✓ (closed at v0.2.2)

**Addresses:** OQ-023, OQ-022.
**Resolution:** v0.2.2 (commit `86bda4f`) — `docs/guide/gpg-signing.md` shipped as runnable checklist: pick signing scheme (GPG / SSH / S/MIME), per-individual key registration with HR-attested identity mapping, repository-level "Require signed commits" branch protection, optional org-level defaults, CI workflow snippet for belt-and-suspenders verification, periodic audit habit, and an explicit limitations section noting that GitHub "Verified" badges certify key→account but not account→person, that web edits sign as GitHub, and that signature meaning (§11.50) is out of scope.
**Status transitions:** OQ-023 stays `:argued` — mechanism unchanged, but adopters now have a documented enforcement path. Upgrading to `:tested` would require either monitoring instrumentation outside this repo or an end-to-end test that doesn't compose with the org-level admin perms required.

### ~~P8 — Part 11 §11.50 signature-meaning prototype~~ ✓ (closed at v0.7.0)

**Addresses:** OQ-060.
**Resolution:** v0.7.0 (commit `0b06381`) — shipped commit-trailer convention (`Signature-Meaning:` required; `Signature-Role:` and `Signature-Justification:` optional) plus `engine/openqms/signatures.py` (parser, GPG-status decoder, git-log extractor, Part 11 JSON exporter), CLI `openqms signatures verify|export` subcommand, dormant CI workflow `.github/workflows/signature-check.yml` (active in adopter forks via path filter), and comprehensive guide `docs/guide/signature-meaning.md`. 23 tests cover the round trip from commit through audit-trail export.
**Status transitions:** OQ-060 `:open → :tested`.

### P9 — Module-version drift detection

**Addresses:** OQ-065, OQ-014.
**Produces:** Each `modules/*/manifest.yaml` declares the standard editions it implements; engine refuses to resolve a bundle that references a stale module without explicit operator override.
**Status transitions:** OQ-065 `:open → :tested`. Phase 1+ work, after P1 ships.

### P10 — Public release of BUSINESS/ contents

**Addresses:** governance posture for engaging Open Honest Foundation or other upstream homes (per `~/.claude/.../memory/project_open_honest_konscience_fit.md`).
**Produces:** Move ENGINE_SPEC.md, DESIGN.md, artifact_registry.md, dashboard.md, changelog.md out of `BUSINESS/` (gitignored) and into a public top-level location, OR keep them in BUSINESS/ but with a public-versioned counterpart. Decide before any external standards-body conversation that requires the spec on-disk.

---

## Open gaps (rolled up from ENGINE_SPEC for at-a-glance scan)

| S-ID | Gap | Tier | Priority |
|---|---|---|---|
| ~~OQ-060~~ | ~~Part 11 §11.50 signature meaning binding~~ ✓ closed v0.7.0 | Gap | ~~P8~~ |
| ~~OQ-061~~ | ~~Training-trigger YAML parsing brittle~~ ✓ closed v0.1.2 | Gap | ~~P4~~ |
| OQ-062 | PHI/PII compartmentalization for complaints | Gap | P5 |
| ~~OQ-063~~ | ~~Supplier-evaluation workflow~~ ✓ closed v0.8.0 | Gap | — |
| ~~OQ-064~~ | ~~Management-review aggregation~~ ✓ closed v0.8.0 | Gap | — |
| OQ-065 | Module-version drift detection | Gap | P1.3 |
| ~~OQ-066~~ | ~~Generator validation harness~~ ✓ closed v0.2.0 | Gap | ~~P1~~ |
| ~~OQ-067~~ | ~~Trace-matrix generator script promised but missing~~ ✓ closed v0.1.1 | Gap | ~~P3~~ |
| OQ-068 | Eleven template subdirectories placeholder-only | Gap | P6 |
| OQ-069 | No complaint issue template | Gap | P5 |
| OQ-080 | README disclaimer (gap-as-honesty-bound) | Gap | *(no action required; entry is the assurance)* |

---

## Cross-audit findings (2026-05-22)

A-level checks per the TCE cross-audit protocol, run against this v0.1.0 baseline.

| Check | Finding |
|---|---|
| **A0 — Self-audit** | This document describes Phase 0 + Phase 1 honestly; the spec does not yet describe what is not actually built. ✓ |
| **A1 — Coverage** | 39 / 39 spec entries have registry rows. ✓ |
| **A2 — Logic & Status parity** | Registry status matches spec status for all 39 entries. ✓ |
| **A3 — Evidence exists** | Every non-dash path in the registry exists on disk (verified `git ls-files`). ✓ |
| **A4 — Status honesty** | No entry has a status above what its evidence type supports. No `:proved` entries today. ✓ |
| **A5 — Stale counts** | Counts in this dashboard match ENGINE_SPEC §Status summary (14 / 14 / 11 / 39). ✓ |
| **A6 — Test sync** | All Workflow tier entries (OQ-030..OQ-038) cite a real CI workflow or template that GitHub will execute / validate on appropriate triggers. No standalone Python test suite yet — appropriate for v0.1.0 since the engine is not built. Note for later: when the engine lands, add a `tests/` directory and CI workflow to exercise the validation harness; track that as part of P1. |

**No drift between spec, registry, and dashboard at v0.1.0.** This is the easy state — the discipline gets harder once mutations start happening.

---

## What changed today (2026-05-22)

**v0.1.0 — initial baseline.**
- Created `BUSINESS/` tree with TCE-standard discipline: `ENGINE_SPEC.md` (39 entries), `DESIGN.md`, `artifact_registry.md`, `dashboard.md` (this file), `changelog.md`, `regulatory_modules/medical_devices_crosswalk.md`.
- Added `BUSINESS/` and `.paper-index.json` to `.gitignore` (pushed at `a2c8dec`).
- Cross-audit run; all A0-A6 checks pass.
- Priority stack populated; P1 (build the engine MVP) is the next major build target.

**v0.1.1 — P3 closed.**
- Removed broken `./scripts/generate-trace-matrix.sh` reference from `docs/guide/traceability.md`; replaced with a "Repository-wide traceability matrix (forward)" subsection that points at the engine-driven Phase-1 deliverable.
- OQ-067 reframed and transitioned `:open → :argued`. Status counts: 14 `:tested` / 15 `:argued` / 10 `:open` / 0 `:proved` etc. (Total 39.)
- A0-A6 cross-audit re-run: clean.

**v0.1.2 — P4 closed.**
- Switched `.github/workflows/training-trigger.yml` from regex YAML parsing to Python + PyYAML.
- OQ-061 reframed; status stays `:tested`; the claim now describes the post-fix robust state.
- A0-A6 cross-audit re-run: clean.

**v0.2.0 — P1 closed; P2 partial.**
- Shipped Open QMS engine at `engine/`: types, module loader, bundle resolver, per-module validation harness, argparse CLI. 15-test pytest suite green locally; CI workflow `.github/workflows/engine-tests.yml` will exercise it on every push touching `engine/`, `modules/`, or `templates/`.
- Shipped minimal medical-devices regulatory module at `modules/medical-devices/module.yaml`: 4 clauses (ISO 13485 §4.2.4, §7.3; 21 CFR 820 §820.30, §820.40) bound to the 3 existing artifact templates. Validation harness passes.
- Status transitions: OQ-001 `:argued → :tested`, OQ-010 `:open → :tested`, OQ-013 `:open → :tested`, OQ-040 `:argued → :tested`, OQ-066 `:open → :tested`. New counts: 19 `:tested` / 13 `:argued` / 7 `:open` (total 39).
- Priority stack restructured: P1 closed, P2 marked partial with explicit remaining-work definition, new P1.1 (composition), P1.2 (registry), P1.3 (re-resolution) split out from the original P1.
- Companion doc at `BUSINESS/companion_engine_mvp.md` per the TCE discipline.
- Public commit `4a72a9f`. A0-A6 cross-audit re-run: clean.

**v0.2.1 — P5 closed.**
- Shipped `.github/ISSUE_TEMPLATE/complaint.yml` (PHI-redacted intake with form validation + required confirmation checkboxes) and `docs/guide/complaints.md` (compartmentalization architecture: Pattern A private sibling repo vs. Pattern B external eQMS).
- Medical-devices module extended with ISO 13485 §8.2.2 + 21 CFR 820.198 clauses, both bound to the complaint template.
- Status transitions: OQ-069 stays `:tested` (claim reframed); OQ-062 `:open → :argued`. Counts: 19 / 14 / 6 (total 39).
- Public commit `2fe3ef6`. A0-A6 cross-audit re-run: clean.

**v0.2.2 — P7 closed.**
- Shipped `docs/guide/gpg-signing.md` — runnable checklist for layering required-signed-commits enforcement.
- No spec-status transitions (OQ-023 stays `:argued`; doc closes the actionability gap, not the mechanical-enforcement gap).
- Counts unchanged: 19 / 14 / 6 (total 39).
- Public commit `86bda4f`. A0-A6 cross-audit re-run: clean.

**v0.3.0 — P6 closed (partial template build-out); ISO 14971 full coverage achieved.**
- Shipped 8 IEC 62304 / ISO 14971 workhorse templates (RISK-MANAGEMENT-FILE, VERIFICATION-PROTOCOL, VALIDATION-PROTOCOL, SOFTWARE-REQUIREMENTS, SOFTWARE-ARCHITECTURE, SOUP-REGISTER, SOFTWARE-TEST-PROTOCOL, SOFTWARE-RELEASE).
- Medical-devices module extended with 14 new clauses (ISO 14971 §4-10 and IEC 62304 §5.2, §5.3, §5.5, §5.6, §5.7, §5.8, §8.1.2) and 8 new template bindings. Standards list grows to 4: ISO 13485:2016, 21 CFR 820, ISO 14971:2019, IEC 62304:2006+A1:2015.
- Validation harness passes on the expanded manifest: 20 clauses, 12 artifacts, full bidirectional traceability when all four standards are in scope.
- 8 of original 15 empty template subdirectories populated; 7 remain placeholder-only (intentionally adopter-defined).
- NEW spec entry OQ-049 (ISO 14971 full coverage), `:tested`. OQ-068 reframed; stays `:tested`. OQ-038 updated (3 → 11 templates). Spec total: 39 → 40.
- Counts: 20 `:tested` / 14 `:argued` / 6 `:open` (total 40).
- Public commit `2625b98`. A0-A6 cross-audit re-run: clean.

**Phase 0 round-out complete.** Phase 1 priorities (P1.1 composition, P1.2 registry, P1.3 re-resolution, P8 Part 11 §11.50) are the next major work surface.

**v0.4.0 — P1.1 closed.**
- Added `openqms.module.compose` primitive: unions clauses (conflict raises), template addresses (merged), standards (deduped).
- CLI `--module` made repeatable on both `resolve` and `validate`; composes before operation.
- Shipped first cross-cutting overlay module: `modules/iso-27001/` (3 Annex A clauses bound to 3 existing OpenQMS templates).
- Engine package version bumped 0.2.0 → 0.4.0 to match spec versioning.
- Test count: 15 → 28 (13 new for composition).
- Status transitions: OQ-011 `:open → :tested`, OQ-012 `:open → :tested`, OQ-048 `:argued → :tested`. Counts: 23 / 13 / 4 (total 40).
- Public commit `2a146ad`. A0-A6 cross-audit re-run: clean.

**v0.15.0 — automotive vertical (second non-medical vertical).**
- Shipped `modules/automotive/` covering ISO 9001:2015 + IATF 16949:2016 (QMS substrate, with automotive-specific additions) + ISO 26262:2018 across all 12 parts (functional safety with ASIL A-D) + ISO/SAE 21434:2021 (cybersecurity engineering with CAL 1-4) + UN R155 (CSMS + per-vehicle-type cyber assessment) + UN R156 (SUMS) + Automotive SPICE 4.0 (process maturity for software development) + AIAG PPAP 4th Ed. (production approval). 28 clauses, 8 standards, four discipline tracks.
- **Why this matters structurally:** aerospace had a single safety-assessment track (ARP4761); automotive has *bifurcated* risk-management discipline — ISO 26262 (FuSa, ASIL A-D) AND ISO/SAE 21434 (cyber, CAL 1-4) — with explicit safety-security interaction analysis required at architecture level. The Safety Concept template models this with FSC + TSC + optional Cybersecurity Concept Part C. Plus type-approval is layered (IATF QMS cert + UN R155 CSMS cert + UN R156 SUMS cert + per-vehicle-type Annex 5 cyber assessment). A stronger composition-discipline test than aerospace.
- 5 new automotive-specific templates: Item Definition (ISO 26262 Part 3 §5), HARA (Part 3 §6; reproduces the S × E × C → ASIL table from Annex B), Safety Concept (FSC Part 3 §7 + TSC Part 4 §6 + Cybersecurity Concept ISO 21434 §9), TARA (ISO 21434 §15 with UN R155 Annex 5 coverage matrix for 32 threats across 7 groups), PPAP (18 elements + Part Submission Warrant).
- 7 new standards in registry. 4 new jurisdictions: NHTSA (US — note: not type-approval; FMVSS framework), UNECE (international WP.29 type-approval forum), KBA (Germany / EU type-approval authority), TC-MVS (Transport Canada Motor Vehicle Safety — distinct id from aerospace's TCCA = Transport Canada Civil Aviation).
- New `bundles/example-vehicle.yaml` (ExamplePowertrainECU under NHTSA + UNECE + KBA composing automotive + regulated-ai + iso-27001 across 12 standards) + committed baseline matrix. Regulated-AI overlay included because predictive battery state-of-health is an ML-driven function under EU AI Act high-risk-AI scope. Idempotent regenerate confirmed.
- CI workflow extended: validate automotive + automotive+regulated-ai+iso-27001 composite; regenerate dry-run for example-samd + example-aircraft + example-vehicle.
- 1 NEW spec entry: OQ-072 `:tested`. Spec total 56 → 57.
- Engine package version 0.14.0 → 0.15.0 (no engine code change; version + keyword expansion).
- Test count unchanged at 108 (module is content, not engine code).
- **Forward work:** ASIL class overlays (ASIL-A through ASIL-D per ISO 26262); CAL class overlays (CAL 1-4 per ISO/SAE 21434); automotive-defense overlay (MIL-STD-882, ITAR, EAR); motorcycle adaptation (ISO 26262 Part 12); NHTSA Part 573 recall workflow as cross-cutting.
- Public commit `d35fedc`. A0-A6 cross-audit re-run: clean.

**v0.14.0 — aerospace vertical (first non-medical vertical).**
- Shipped `modules/aerospace/` covering ISO 9001:2015 + AS9100D (QMS substrate) + 14 CFR Part 21 + EASA Part 21 (cert) + DO-178C (software) + DO-254 (hardware) + ARP4754A (system development) + ARP4761 (safety assessment) + AS9102 (FAI). 27 clauses, 9 standards.
- 5 new aerospace-specific templates: PSAC (DO-178C Plan for Software Aspects of Certification), FHA (ARP4761 Functional Hazard Assessment), SSP (System Safety Plan), FAI Report (AS9102 Forms 1/2/3), Type Cert Pack Index (14 CFR Part 21 + EASA Part 21).
- 9 new standards in registry. 3 new jurisdictions: FAA, EASA, TCCA (note: FAA = Federal Aviation Administration; not the medical-devices FDA).
- New `bundles/example-aircraft.yaml` (avionics computer under FAA, composes aerospace + regulated-ai + iso-27001 across 13 standards) + committed baseline matrix. Idempotent regenerate confirmed.
- CI workflow extended to validate aerospace + aerospace+regulated-ai+iso-27001 composite and to dry-run example-aircraft regenerate for regression-detection.
- 1 NEW spec entry: OQ-059 `:tested`. Spec total 55 → 56.
- Engine package version 0.13.0 → 0.14.0 (no engine code change; version bump tracks the module addition).
- Test count unchanged at 108 (aerospace module is content, not engine code).
- **Forward work:** aerospace DAL class overlays (DAL-A through DAL-E per DO-178C / DO-254); aerospace-defense overlay (MIL-STD-882, ITAR, EAR); commercial space scope (FAA Part 450).
- Public commits `a480c3a` (module + templates + registry + bundle + CI) + `00de6d0` (engine version bump). A0-A6 cross-audit re-run: clean.

**v0.12.0 — additional class overlays + IVD overlay + regulated-AI overlay (three-phase release).**
- **Phase A (commit `f0d48f7`):** 3 additional class overlays — mdr-class-iib (Article 54 expert panel for active drug-delivery + Annex IX procedure + biennial PSUR), mdr-class-iia (Annex XI PQA route + as-needed PMS), fda-class-ii (510(k) submission + Special Controls + De Novo path). 1 new template (510K-SUBMISSION-TEMPLATE). 2 new standards (21 CFR 807, 21 CFR 860).
- **Phase B (commit `361f4ff`):** IVD overlay covering EU IVDR + 21 CFR 809 + ISO 15189. 8 clauses across IVDR (Article 5 + Annex I + Annex II + Annex IX + Annex XIII performance evaluation + Article 56), CFR 809, ISO 15189. 2 new templates (IVDR-GSPR-CHECKLIST + PERFORMANCE-EVALUATION-REPORT). 3 new standards (EU IVDR, 21 CFR 809, ISO 15189). Shipped as cross-cutting overlay; adopters declare MDR clauses NA per IVD scope SOP.
- **Phase C (commit `3e231d5`):** Regulated-AI cross-cutting overlay — composes with any vertical. 13 clauses: NIST AI RMF 4 functions + EU AI Act Articles 9-15 + ISO 42001 AIMS + ISO 23894 AI risk management. 2 new templates (AI-SYSTEM-CARD + AI-IMPACT-ASSESSMENT). Existing templates extended with AI bindings (RMF, quality-policy, SAD, STP, TFI). 1 new standard (ISO 23894).
- 7-module mega-composite (medical-devices + ivd + samd + regulated-ai + mdr-class-iii + fda-class-iii + iso-27001) validates cleanly — demonstrates AI overlay composes with any vertical combination.
- 5 NEW spec entries: OQ-054 (MDR IIb), OQ-055 (MDR IIa), OQ-056 (FDA II), OQ-057 (IVD), OQ-058 (regulated-AI). **Spec total 50 → 55.**
- OQ-038 template count 26 → 31.
- Engine package version 0.11.0 → 0.12.0 (commit `093c35f`).
- Test count unchanged at 97 (all green); each overlay validates standalone + in composite.
- Public commits `f0d48f7` + `361f4ff` + `3e231d5` + `093c35f`.

**v0.11.0 — device-class overlay modules shipped.**
- 4 new overlay modules: `modules/samd/` (SaMD), `modules/implantable/`, `modules/mdr-class-iii/` (EU MDR Class III), `modules/fda-class-iii/` (FDA Class III / PMA path). Each composes with the medical-devices vertical via the OQ-011 compose primitive.
- 5 new templates: SAMD-INTENDED-USE, IMPLANT-CARD, SSCP, EXPERT-PANEL-CONSULTATION, PMA-SUBMISSION.
- 5 new standards in registry: IEC 82304-1 (health software product), ISO 14708-1 (active implantables), 21 CFR 814 (PMA), 21 CFR 803 (FDA MDR adverse-event reporting), IMDRF SaMD N12 (risk categorization framework).
- Example bundle updated to include `samd` overlay (honest about its SaMD identity) + IEC 82304-1 + IMDRF SaMD N12 standards. Matrix regenerated.
- 4 NEW spec entries: OQ-050 (SaMD), OQ-051 (implantable), OQ-052 (MDR Class III), OQ-053 (FDA Class III) — all `:tested`. Spec total grew 46 → 50.
- OQ-038 template count 21 → 26.
- Engine package version 0.10.0 → 0.11.0.
- Class I and Class II overlays deliberately NOT shipped: their "additions" over baseline are subtractions which don't fit the union-based compose primitive. IVD deferred to a separate vertical module (IVDR governs in EU, not overlay-able).
- Public commits `54e93de` (content) + `edfc2f0` (version bump).

**v0.10.0 — OQ-044 closed. All module-tier entries `:tested`.**
- 3 new templates: `GSPR-CONFORMITY-CHECKLIST-TEMPLATE.md` (EU MDR Annex I — all 23 GSPRs across 3 chapters; per-class applicability column), `CLINICAL-EVALUATION-TEMPLATE.md` (Annex XIV Part A CER per MDCG 2020-5/6/13), `PMCF-PLAN-TEMPLATE.md` (Annex XIV Part B PMCF per MDCG 2020-7/8).
- 2 new subdirs: `templates/product-dhf/gspr/` + `templates/product-dhf/clinical/`.
- Module manifest: 3 new clauses (MDR-AnnexI, MDR-AnnexXIV-A, MDR-AnnexXIV-B) + 3 new bindings. Module version 0.2.0 → 0.3.0.
- Templates are device-class-agnostic with explicit per-class customization notes (SaMD declares NA on most physical/mechanical GSPRs; implantables declare A on most; IVD routes through IVDR). Device-class overlay sub-modules remain forward work but are not on the immediate roadmap.
- Spec transitions: OQ-044 `:argued → :tested`. Counts: 38 / 8 / 0 (total 46). All medical-devices standard-coverage entries (OQ-041 through OQ-047) now `:tested`.
- OQ-038 template count updated 18 → 21.
- Engine package version 0.9.0 → 0.10.0.
- Public commits `e6d15a8` (content) + `aa51574` (version bump).

**v0.9.0 — medical-devices module fully populated.**
- 4 new templates shipped: `TECHNICAL-FILE-INDEX-TEMPLATE.md` (ISO 13485 §4.2.3 + EU MDR Annex II), `AUDIT-PROCEDURE-TEMPLATE.md` (ISO 13485 §8.2.4 + 21 CFR 820.22), `USABILITY-ENGINEERING-FILE-TEMPLATE.md` (IEC 62366-1 §5), `PACKAGING-VALIDATION-TEMPLATE.md` (ISTA 2A + 3A).
- Module manifest expanded from 24 clauses across 4 standards to 59 clauses across 11 standards (added 21 CFR Part 11, EU MDR 2017/745, IEC 62366-1, IEC 60601-1, ISTA 2A, ISTA 3A, MDSAP).
- Existing templates gained additional bindings (quality-policy now binds 12 cross-cutting clauses; SOP, verification, architecture, requirements, RMF, CAPA, NCR templates all expanded; release-gate workflow + signature-meaning + gpg-signing guides bound as artifacts where appropriate).
- Example bundle `bundles/example-samd.yaml` expanded to all 12 standards (10 medical + 1 infosec + MDSAP); matrix regenerated as new baseline.
- Spec transitions (6 module-tier entries to `:tested`): OQ-041 (ISO 13485, 11 clauses), OQ-042 (CFR 820, 11 sections), OQ-043 (CFR Part 11, 10 subclauses), OQ-045 (IEC 62304, 12 clauses), OQ-046 (IEC 62366-1 + 60601-1, 2 clauses), OQ-047 (ISTA + MDSAP, 3 clauses). OQ-044 (EU MDR) stays `:argued` — 3 of 5 originally-listed annexes machine-readable; Annex I GSPRs and Annex XIV CER deferred to device-class overlays.
- OQ-068 updated: 11 of 15 originally-empty subdirs populated.
- OQ-038 updated: 14 → 18 document templates.
- Engine package version 0.8.0 → 0.9.0.
- Test count unchanged at 97 (all green); validation harness passes on the expanded manifest.
- Public commits `78ee0db` (content) + `cbaffba` (version bump).

**v0.8.0 — OQ-063 + OQ-064 closed. Zero `:open` entries milestone.**
- Shipped supplier-controls infrastructure (ASL template + per-supplier evaluation template + workflow issue template + guide) and management-review infrastructure (meeting record template + workflow issue template + `gh` CLI aggregation-pattern guide).
- 4 new clauses in `modules/medical-devices/module.yaml`: ISO 13485 §5.6 (management review) + §7.4 (purchasing); 21 CFR 820.20(c) (management review subset) + §820.50 (purchasing controls). 5 new artifact bindings.
- CLI fix: `openqms regenerate --write-matrix` now exits 0 on successful write regardless of diff content (was exiting 1 if the diff was non-empty, which conflated "you accepted the change" with "CI dry-run detected drift").
- Baseline matrix `bundles/example-samd.matrix.json` regenerated to absorb the 4 new clauses + 5 new artifacts. Subsequent `regenerate --bundle example-samd` reports `(no changes)` and exits 0.
- Engine package version 0.7.0 → 0.8.0 (commit `ec188b3`, follow-up to `aedde0b`).
- Test count unchanged at 97 (all green); the regenerate exit-code semantics are exercised by existing tests.
- Status transitions: OQ-063 `:open → :tested`, OQ-064 `:open → :tested`. Counts: 31 / 15 / 0 (total 46). **Zero `:open` entries.**
- OQ-041 + OQ-042 notes updated: ISO 13485 5/full and 21 CFR 820 5/full clause sets now machine-readable.
- OQ-038 template count updated: 11 → 14 document templates.
- Public commits `aedde0b` + `ec188b3`. CI green.

**v0.7.0 — P8 closed.**
- Shipped 21 CFR Part 11 §11.50 signature-meaning prototype.
- `engine/openqms/signatures.py` — commit-trailer parser (lenient regex matching `Signature-*: value`), `signature_from_commit_data()` (9 GPG-status codes), `extract_signatures_from_repo()` (NUL/0x1e-separated `git log` parsing), `export_audit_trail()` (Part 11 JSON records).
- CLI `openqms signatures verify --commit <sha>` / `openqms signatures export --since <ref>` with `--require-gpg` flag.
- CI workflow `.github/workflows/signature-check.yml` — gates PRs on controlled paths (`qms-policy/`, `qms-sops/`, `qms-forms/`, `qms-training/`, `product-*/`); dormant in OpenQMS, active in adopter forks.
- Guide `docs/guide/signature-meaning.md` — §11.50 verbatim, why GPG alone isn't sufficient, trailer convention, CLI surface, CI integration, honest limitations.
- Engine package version 0.6.0 → 0.7.0.
- Test count: 74 → 97 (+23 new — 4 parser, 11 signature/GPG-status parametric, 2 export field structure, 2 tmp-repo integration, 4 CLI subprocess).
- Status transitions: OQ-060 `:open → :tested`. Counts: 29 / 15 / 2 (total 46).
- Public commit `0b06381`. CI run: green.

**v0.6.0 — P1.3 closed. Phase 1 fully closed.**
- Shipped `openqms regenerate --bundle <name>` CLI subcommand operating on stored bundle definitions at `bundles/<name>.yaml` and committed matrix files at `bundles/<name>.matrix.json`.
- New engine modules `openqms.bundle` (loader) and `openqms.diff` (`MatrixDiff` + `format_diff`).
- Shipped `bundles/example-samd.{yaml,matrix.json}` as committed regression baseline (5 standards, 2 modules; idempotent re-resolution confirmed).
- Edition supersession via `superseded_by` field on `StandardEntry` + `--strict-editions` CLI flag.
- CI workflow now triggers on `bundles/**` and runs `regenerate` in dry-run mode on every push as a regression-detection mechanism.
- Engine package version 0.5.0 → 0.6.0.
- Test count: 49 → 74 (+25 new — 8 bundle, 9 diff, 8 regenerate CLI subprocess including 2 supersession, plus the shipped-example regression test).
- Status transitions: OQ-015 `:open → :tested`, OQ-065 `:open → :tested`. Counts: 28 / 15 / 3 (total 46 — reconciled from long-running 40 undercount).
- Public commit `3cfec2c`. A0-A6 cross-audit re-run: clean. Phase 1 complete.

**v0.5.0 — P1.2 closed.**
- Shipped standards-and-jurisdictions registry at `registry/standards.yaml` + `registry/jurisdictions.yaml` (15 standards + 6 jurisdictions seeded from the medical-devices crosswalk and the AI-regulation roadmap).
- Engine `openqms.registry` module: `Registry`/`StandardEntry`/`JurisdictionEntry` frozen dataclasses, `load_registry()` with dangling-reference cross-check, `validate_module_against_registry()`.
- CLI behavior: `--standard` arguments normalized to canonical ids via aliases (`"ISO 13485"` → `"ISO 13485:2016"`); unknown standards / jurisdictions raise with the registered-ids listed. New `openqms registry list/show` subcommand. Escape hatch `--allow-unregistered-standards` for migration paths.
- Engine package version 0.4.0 → 0.5.0.
- Test count: 28 → 49 (21 new for registry — 8 unit, 4 shipped-registry, 2 negative loader, 2 module-vs-registry negatives, 5 CLI subprocess integration).
- CI workflow `engine-tests.yml` now triggers on `registry/**`; validation step runs `validate` against medical-devices, iso-27001, and the composite, plus `registry list` smoke check.
- Status transitions: OQ-014 `:open → :tested`. Counts: 24 / 13 / 3 (total 40).
- Public commit `12b6b33`. A0-A6 cross-audit re-run: clean.
