# Chemicals arc companion — v0.36.0 through v0.38.0

**Session date:** 2026-05-24
**Engine version transitions:** 0.35.0 → 0.38.0 (3 releases cumulative)
**Theme:** Build out the chemicals regulatory domain from zero coverage to comprehensive — vertical + adjacent standalones + class overlays. 11 chemicals-domain modules + 12 templates shipped across 3 releases.
**User direction sequence:**
- v0.36.0: "do chemicals, save rest of verticals for future work."
- v0.37.0 + v0.38.0: "do 1 and 2" (1 = chemicals-adjacent standalones, 2 = chemicals class overlays)
- After v0.38.0: "ok let's hold on any more vertical integration for now. what's left?"

## §1 Computational basis

Three sequential releases:

| Version | Date | Theme | Public commit | Spec entry |
|---|---|---|---|---|
| v0.36.0 | 2026-05-24 | Chemicals vertical (7th vertical) — REACH + CLP + GHS + GLP + TSCA | `0b0641a` | OQ-105 |
| v0.37.0 | 2026-05-24 | Chemicals-adjacent standalones (4 cross-cutting overlays) | `08a50d9` | OQ-106 |
| v0.38.0 | 2026-05-24 | Chemicals class overlays (6: SVHC + Authorisation + 4 tonnage bands) | `885142e` | OQ-107 |

**Aggregate deliverables across the arc:**
- 1 vertical (`modules/chemicals/`)
- 4 cross-cutting overlays (`modules/osha-hcs/`, `modules/transport-hazmat/`, `modules/eu-biocides/`, `modules/tsca-pfas/`)
- 6 class overlays (`modules/chemicals-svhc/`, `modules/chemicals-authorisation/`, `modules/chemicals-tonnage-1/10/100/1000/`)
- 12 new templates (4 vertical + 5 adjacent + 3 class-overlay)
- 14 new registry standards (5 vertical + 9 adjacent + 0 class-overlay)
- 1 new example bundle (`bundles/example-specialty-chemical.yaml`)
- 11 chemicals-domain modules total in scope of `openqms validate`
- 16-module deepest composite tested in CI (new project depth record beating prior 11-module)

**Files shipped:**

```
modules/chemicals/{module.yaml,README.md}                                        # v0.36
modules/osha-hcs/{module.yaml,README.md}                                         # v0.37
modules/transport-hazmat/{module.yaml,README.md}                                 # v0.37
modules/eu-biocides/{module.yaml,README.md}                                      # v0.37
modules/tsca-pfas/{module.yaml,README.md}                                        # v0.37
modules/chemicals-svhc/{module.yaml,README.md}                                   # v0.38
modules/chemicals-authorisation/{module.yaml,README.md}                          # v0.38
modules/chemicals-tonnage-{1,10,100,1000}/{module.yaml,README.md}                # v0.38

templates/product-chemicals/sds/SAFETY-DATA-SHEET-TEMPLATE.md                    # v0.36
templates/product-chemicals/reach/REACH-REGISTRATION-DOSSIER-TEMPLATE.md         # v0.36
templates/product-chemicals/clp/CLP-NOTIFICATION-LABEL-TEMPLATE.md               # v0.36
templates/product-chemicals/glp/GLP-STUDY-PLAN-REPORT-TEMPLATE.md                # v0.36
templates/qms-ohs/HAZCOM-WRITTEN-PROGRAM-TEMPLATE.md                             # v0.37
templates/qms-logistics/SHIPPING-PAPER-TEMPLATE.md                               # v0.37
templates/qms-logistics/HMT-TRAINING-RECORD-TEMPLATE.md                          # v0.37
templates/product-chemicals/biocides/BPR-AUTHORISATION-APPLICATION-TEMPLATE.md   # v0.37
templates/product-chemicals/pfas/PFAS-REPORTING-FORM-TEMPLATE.md                 # v0.37
templates/product-chemicals/svhc/SVHC-COMMUNICATION-LETTER-TEMPLATE.md           # v0.38
templates/product-chemicals/authorisation/REACH-AUTHORISATION-APPLICATION-TEMPLATE.md  # v0.38
templates/product-chemicals/authorisation/SUBSTITUTION-PLAN-TEMPLATE.md          # v0.38

bundles/example-specialty-chemical.yaml + .matrix.json                           # v0.36
registry/standards.yaml (+14 standards)                                          # v0.36+0.37
```

**Build commands** (replayable from a clean checkout):

```bash
source .venv-engine/bin/activate

# Per-module validation
openqms validate --module chemicals
openqms validate --module osha-hcs
openqms validate --module transport-hazmat
openqms validate --module eu-biocides
openqms validate --module tsca-pfas
openqms validate --module chemicals-svhc
openqms validate --module chemicals-authorisation
openqms validate --module chemicals-tonnage-1
openqms validate --module chemicals-tonnage-10
openqms validate --module chemicals-tonnage-100
openqms validate --module chemicals-tonnage-1000

# 16-module deepest composite (chemicals + SVHC + Authorisation + top tonnage + 4 adjacent + 8 cross-cutting)
openqms validate \
  --module chemicals \
  --module chemicals-svhc --module chemicals-authorisation --module chemicals-tonnage-1000 \
  --module osha-hcs --module transport-hazmat --module eu-biocides --module tsca-pfas \
  --module iso-27001 --module regulated-ai --module iso-14001 --module iso-45001 \
  --module iso-50001 --module iso-37001 --module iso-22301 --module iso-31000

# Example bundle (with baseline matrix)
openqms regenerate --bundle example-specialty-chemical

# Engine test suite
pytest engine/tests -q   # 108/108 pass
```

## §2 Results

### v0.36.0 — Chemicals vertical

7th vertical (after medical-devices / aerospace / automotive / manufacturing / pharma / food-safety). Covers chemical substance + mixture manufacturing + import under the four major regulatory regimes: EU REACH (1907/2006), EU CLP (1272/2008), UN GHS Rev. 10, OECD GLP Principles, US TSCA (15 USC §2601 et seq.). 21 clauses across the 5 standards.

Architectural choice: ship as a single vertical rather than splitting per-regulator (e.g., a REACH-only vertical + a TSCA-only vertical). Rationale — chemical industry operations almost always have multi-regional scope; REACH + TSCA + GHS + GLP coexist within a single manufacturer's compliance program and the SDS template in particular reads both REACH Annex II + OSHA HCS Appendix D requirements off the same 16-section structure.

All 5 standards PUBLIC license — first vertical (alongside food-safety partially + pharma) where the entire standards stack costs nothing to acquire. Meaningful adopter-cost reduction for chemical SMEs + startups + academic spinouts.

4 chemicals-specific templates introduced. Each is the highest-leverage artifact of its regime:
- Safety Data Sheet (16-section per GHS + REACH Annex II + CLP + OSHA HCS App D) — the gating artifact for all regulated chemical commerce
- REACH Registration Dossier Outline (Articles 5-6 + 10 + 14 + Annexes VI-X + Annex I CSR) — required dossier scope for EU placing-on-market
- CLP Classification Notification + Label (Articles 4 + 13 + 17 + Annexes II + VI + VIII) — required EU classification + Poison Centre Notification
- GLP Study Plan + Final Report — required for any non-clinical safety study submitted to a regulatory authority

### v0.37.0 — Chemicals-adjacent standalones

4 cross-cutting overlays that compose with chemicals (and with most other verticals) — each one explicitly named as forward work in the `modules/chemicals/module.yaml` scope notes at v0.36.0.

**osha-hcs** — 9 clauses across 29 CFR 1910.1200 HCS 2024 final rule (aligned with UN GHS Rev. 7). Receiver-side complement to chemicals' sender-side SDS authoring; written program + container labels + SDS access during each shift + employee training before assignment. HAZCOM-WRITTEN-PROGRAM template is the required §(e)(1) artifact. Mandatory compliance dates: substance manufacturer/importer 2026-01-19; mixture manufacturer/importer 2027-07-19.

**transport-hazmat** — 17 clauses across 5 modes covering US DOT HMR (PUBLIC), IMDG Code (commercial; sea), IATA DGR (commercial; air; CBTA per ICAO TI Doc 9284 effective 2023-01-01), ADR 2025 (PUBLIC; EU road), RID 2025 (PUBLIC; EU rail). Two new templates: a multi-modal Multimodal Dangerous Goods Form (per IMO/ILO/UNECE Guidelines — covers all five regimes' shipping-paper requirements in one form) + a multi-regime training record covering DOT four-component training + IATA CBTA + ADR driver vocational + DGSA.

Critical scope-creep observation: transport-hazmat applies broadly across nearly every vertical — automotive (UN3480 Li-ion + UN0503 airbag pyrotechnics) / aerospace (UN3480 batteries + UN0354 ejection-seat pyrotechnics + cryogenics) / medical-devices (UN3373 Biological Substance Cat B specimens) / pharma / manufacturing — not just chemicals.

**eu-biocides** — 10 clauses across EU BPR 528/2012 product-on-market authorisation route (Articles 4-9 active substance approval; Articles 17-23 product authorisation; Article 19(1) conditions; Articles 49-50 + Article 95 supplier list; Article 56 R&D notification; Article 58 treated articles; Articles 69-72 biocide-specific C+L+P; Annex V 22 product types in 4 main groups; Annex VI Common Principles for evaluation). BPR-AUTHORISATION-APPLICATION template covers Article 17 full application with pathway selection (national / MR-parallel / MR-sequence / Union / simplified) + Article 19(1) conditions check + efficacy + HHRA + ERA dossier framework + Annex dossier index.

Critical adopter gotcha: Article 95 supplier list — biocidal products containing active substances whose supplier is not Article-95-listed cannot be placed on EU market post-2015-09-01. Small suppliers without Letter of Access face existential commercial risk.

**tsca-pfas** — 7 clauses across 40 CFR Part 705 TSCA Section 8(a)(7) PFAS Reporting and Recordkeeping (final rule October 2023). Critical scope-creep dimensions: no de minimis exemption; no exemption for substances already in commerce; no exemption for impurities or byproducts; articles in scope per preamble "knowability" standard. ~1,400+ substances meet broad PFAS structural definition per §705.5(b). PFAS-REPORTING-FORM template includes a common-article-categories due-diligence checklist catching non-obvious PFAS imports across textile / semiconductor / cookware / cosmetics / automotive / medical-device / outdoor-gear / aerospace verticals.

### v0.38.0 — Chemicals class overlays

6 class overlays — the first chemicals class-overlay set. Two are obligation-overlays (SVHC + Authorisation); 4 are tonnage-band scaling overlays.

**chemicals-svhc** — 5 clauses across REACH SVHC supply-chain + ECHA notification obligations. Article 7(2) ECHA notification for SVHC in articles >1 t/y AND >0.1% w/w. Article 33(1) communication to recipients. Article 33(2) consumer 45-day response. Waste Framework Directive (EU) 2018/851 Article 9(1)(i) SCIP database notification (effective 2021-01-05). Annex XV identification dossier. SVHC-COMMUNICATION-LETTER template covers all three communication paths + SCIP cross-reference. *FCD* CJEU C-106/14 judgment captured: >0.1% threshold applies per-component (smallest article incorporated), not per total mass of complex object.

**chemicals-authorisation** — 6 clauses across REACH Title VII Articles 55-66 + Annex XIV. Two new templates: REACH-AUTHORISATION-APPLICATION (Article 62 full application with Adequate Control vs. Socio-Economic route selection per substance properties — Adequate Control NOT available for non-threshold CMR/PBT/vPvB) + SUBSTITUTION-PLAN (Article 60(4)(c) 10-action timetable with risk-management transition + contingencies + reporting cadence).

**chemicals-tonnage-{1,10,100,1000}** — 4 dossier-scaling overlays. Each encodes the incremental Annex VII/VIII/IX/X data requirements at the corresponding tonnage threshold.

| Overlay | Annex | Incremental clauses | Typical cost impact |
|---|---|---|---|
| chemicals-tonnage-1 | VII | Baseline (phys-chem + tox screening + ecotox screening) | €50-150k per substance; CSR NOT required |
| chemicals-tonnage-10 | VIII | 28-day RDT + repro screening + toxicokinetics + short-term fish + activated sludge | **Major cost cliff** — CSR mandatory (€30-100k) + 28-day RDT (€40-80k) + eSDS distribution |
| chemicals-tonnage-100 | IX | 90-day RDT + repro screening + long-term Daphnia + long-term fish + soil + sediment + bird ecotox | 90-day RDT €200-500k; vertebrate test proposals + 45-day public consultation; multi-year regulatory timeline |
| chemicals-tonnage-1000 | X | Chronic 12-month + carcinogenicity bioassay + EOGRTS full Cohorts + dev. second species + chronic multi-species ecotox | €1.5-3M carcinogenicity + €1-2M EOGRTS; SIEF joint submission essentially mandatory |

Tonnage-band semantics — in practice, bands are mutually exclusive per substance (each higher band supersedes-and-includes lower bands). Open QMS module-union semantics correctly allow either compose-and-validate (16-module composite for documentation purposes) or adopt-only-current-band (3-module composite chemicals + chemicals-svhc + chemicals-tonnage-10 typical for SMEs at the CSR-mandatory threshold).

### Composition + depth records

- v0.36.0 — 9-module composite: chemicals + 8 cross-cutting (osha-hcs not yet shipped at v0.36)
- v0.37.0 — **13-module composite** (new depth record at the time): chemicals + 4 adjacent + 8 cross-cutting
- v0.38.0 — **16-module composite** (current depth record): chemicals + chemicals-svhc + chemicals-authorisation + chemicals-tonnage-1000 + 4 adjacent + 8 cross-cutting

Each composite validates `openqms validate --module ... --module ...` with `invariant_holds: True`. OQ-011 compose primitive (built v0.4.0, unchanged across 33+ subsequent releases) continues to handle compositions of arbitrary depth.

## §3 Verification

Per TCE evidence-type discipline:

| OQ-NNN | Evidence type | Justification |
|---|---|---|
| OQ-105 chemicals vertical | example-tested | `openqms validate --module chemicals` passes; composite with 4 cross-cutting overlays validates; `bundles/example-specialty-chemical` baseline matrix written + idempotent regenerate verified; 108/108 pytest pass. **Honest framing**: example-tested. Each clause is a structured reference to a published regulation; module-coverage population is the verification surface, not a mathematical proof of clause completeness vs. the underlying regulation. |
| OQ-106 chemicals-adjacent batch | example-tested | All 4 modules validate standalone + pairwise with chemicals + 13-module deepest composite validates; 108/108 pytest pass. Same framing as OQ-105 — `example-tested` is the ceiling for module-population claims under TCE's evidence-type rules. |
| OQ-107 chemicals class overlays | example-tested | All 6 modules validate standalone + composite with chemicals + 16-module deepest composite validates; 108/108 pytest pass. Same framing. |

**Verification status of underlying chemicals-domain knowledge.** Module clauses cite specific regulatory text by Article/Section/Annex number with one-paragraph summaries. No claim is made that the summaries are exhaustive or legally authoritative — clauses are navigation pointers + structural index. Adopters reference the regulatory text itself (PUBLIC for 13 of 14 new standards via EUR-Lex / ecfr.gov / UNECE / OTIF; commercial for IMDG + IATA DGR) for compliance determinations. README forward-work sections enumerate known scope-gaps + further refinements that would benefit deeper Open QMS coverage.

**No upgrade to `:verified` available**: chemicals-domain modules cannot meaningfully become `:verified` under TCE rules — the evidence ceiling for module-coverage entries is `example-tested` by nature (no mathematical property can capture "all relevant clauses are populated"). This is consistent with the rest of the module-tier corpus.

## §4 Spec impact

3 NEW Module-tier entries shipped:

**OQ-105 — Chemicals vertical module (7th vertical)**
- Tier: Module
- Evidence type: example-tested
- Status: :tested
- Depends_on: OQ-011, OQ-012, OQ-014
- Shipped: v0.36.0

**OQ-106 — Chemicals-adjacent standalone overlay batch (4)**
- Tier: Module
- Evidence type: example-tested
- Status: :tested
- Depends_on: OQ-011, OQ-012, OQ-014, OQ-105
- Shipped: v0.37.0

**OQ-107 — Chemicals class overlay batch (6)**
- Tier: Module
- Evidence type: example-tested
- Status: :tested
- Depends_on: OQ-011, OQ-105
- Shipped: v0.38.0

**Cumulative counts post-arc:**
- Spec total: 88 → 91 (+3)
- Status counts: 6 `:verified` / 78 `:tested` / 7 `:argued` / 0 `:open`
- Vertical count: 6 → 7
- Class-overlay count: 38 → 44 (chemicals first class-overlay set)
- Cross-cutting overlay count: 19 → 23
- Registry standards: ~105 → ~114
- Document templates: 73 → 81
- Example bundles: 11 → 12
- Total modules: 64 → 75
- Deepest CI composite: 11 → 16 modules

**Discharged forward-work commitments:**
- All 4 chemicals-companion (OQ-105 module.yaml scope notes) forward-work items: OSHA HCS + DOT HazMat + EU Biocides + TSCA PFAS — closed at v0.37.0
- 2026-05-22 dashboard candidate "chemicals vertical" — closed at v0.36.0
- chemicals-svhc + chemicals-authorisation + tonnage-banded dossier structure named in `modules/chemicals/README.md` forward work — closed at v0.38.0

## §5 Notes on what was deliberately NOT shipped

User direction "save rest of verticals for future work" + "ok let's hold on any more vertical integration for now" — explicit scope-limit per release. Other candidate verticals deferred:

- Cosmetics — EU Regulation 1223/2009 + US MoCRA
- Pesticides — FIFRA (US) + EU Plant Protection Products Regulation 1107/2009
- Nuclear / radiological — 10 CFR + IAEA standards + Euratom
- Oil-and-gas — API standards + OSHA PSM 29 CFR 1910.119 + EPA SPCC
- Construction — OSHA 29 CFR 1926 + ISO 9001 sector
- Textiles + apparel — OEKO-TEX + GOTS + REACH textile-specific
- Mining — MSHA 30 CFR
- Electrical equipment — IEC 60601 (already covered for medical) + RoHS + WEEE
- Chemicals-adjacent forward work named in v0.37 README forward sections:
  - UK COSHH (Control of Substances Hazardous to Health Regulations 2002)
  - Germany GefStoffV (Gefahrstoffverordnung)
  - Canada WHMIS 2015
  - EU CAD + CMRD
  - Canada TDG
  - ICAO Technical Instructions standalone
  - IMSBC Code (bulk solid cargoes)
  - IGC + IGF Codes (LNG + low-flashpoint fuels)
  - EU REACH SVHC → Annex XIV migration tracking
  - ECHA SCIP IUCLID 6 dossier template
  - Per-PT Annex II data-requirements detailed templates for BPR
  - Universal PFAS Restriction proposal tracking (ECHA/RAC/SEAC ongoing)
  - Maine LD 1503 + state-level intentionally-added PFAS rules

These are catalogued for future-release planning — not forgotten.

## §6 Lessons + observations

1. **3-release sprint pattern**. The vertical + adjacent + class-overlay arc cleanly decomposes into 3 distinct release shapes. Each release shipped clean with own commit + push. Reusable pattern for future verticals if the user re-opens vertical work.

2. **YAML colon-in-template-name failure mode (recurrent)**. v0.37.0 had a YAML parse failure on `transport-hazmat/module.yaml` template name `Dangerous Goods Shipping Paper (multi-modal: DOT/IMDG/IATA/ADR/RID-compatible ...)` — unquoted colon broke parse. Resolved by quoting the string. Same failure mode hit earlier releases; persistent gotcha. Consider engine-side stricter YAML-friendliness validation OR linter pre-commit hook.

3. **Cumulative chemicals-domain weight**. 11 modules + 12 templates + 14 standards added in 3 releases without any per-release companion. Choosing to backfill via this single companion (matching v0.34/v0.35 omnibus pattern) keeps cadence high while preserving discipline.

4. **README template scaling**. Per-module README pattern (scope / standards / clauses / templates / composition / when-to-use / forward-work) holds at depth — chemicals + 4 adjacent + 6 class-overlay each have a README following the standard structure. ~12 READMEs added in the arc with consistent shape, no boilerplate scaffolding required.

5. **Pre-existing CI drift caught at v0.36.0**. While shipping v0.36.0 the regenerate dry-run step revealed 4 baseline matrices (machine-shop / drug-product / food-processor / cart) had drifted at the v0.34.0 template-binding pass without being refreshed. Refresh shipped in v0.36.0 commit alongside chemicals; CI now green on master. Pattern to watch: template-binding changes downstream of bundle baselines need matrix refresh in the same commit.

6. **No new example bundles for adjacent + class overlays**. Only `example-specialty-chemical` shipped at v0.36.0. Adopters can hand-roll composite bundles using existing patterns. Forward-work candidate: example bundles for high-tonnage REACH registrant + treated-articles-importer scenarios.

7. **OQ-068 template-subdirectory count**. Originally 15 subdirs with 8 of 15 populated, then 11 of 15, then 13 of 15. Status not refreshed during this arc despite ~12 new template subdirs introduced (product-chemicals/{sds,reach,clp,glp,biocides,pfas,svhc,authorisation} + qms-ohs/{HAZCOM-WRITTEN-PROGRAM} + qms-logistics). Audit candidate.

## §7 Acceptance + close-out

Three releases shipped + pushed. 108/108 pytest pass. All 8 bundle baselines clean post-refresh. CI green. Spec total 88 → 91 with zero `:open` entries maintained. User-confirmed scope after v0.38.0: "ok let's hold on any more vertical integration for now" — chemicals arc closed as a complete domain build-out.

Next session direction (per user "do 2 then 1"): cross-audit (OQ-097 dashboard last A0-A6 findings doc 2026-05-22, now 11 spec entries + 4 releases stale) follows this companion doc.

---

*Companion doc per TCE evidence-discipline; omnibus pattern matches `companion_v0_24_to_34_omnibus.md`. Update `companion_index.md` to add chemicals-arc row.*
