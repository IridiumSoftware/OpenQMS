# Companion — Automotive vertical (v0.15.0)

**Session date:** 2026-05-23
**Engine version transition:** 0.14.0 → 0.15.0
**Commits:** `d35fedc` (module + templates + registry + bundle + CI + engine version bump in one commit)

---

## §1 Computational basis

### What was built

A second non-medical vertical regulatory module — **automotive** (road vehicles: passenger cars, light commercial vehicles, heavy duty trucks). Purpose: strengthen the platform-generalization claim from one data point (aerospace v0.14.0) to two. The composition discipline (OQ-011 compose primitive + OQ-014 registry + OQ-013 validation harness + OQ-015 regenerate) handles a substantively different shape of regulated industry without engine code change.

### Files added

| Path | Purpose |
|---|---|
| `modules/automotive/module.yaml` | Vertical module manifest; 28 clauses across 8 automotive standards |
| `modules/automotive/README.md` | Module documentation — scope, composition with overlays, class-overlay forward work, what's out of scope (defense / off-highway / rail / recall), standards licensing |
| `templates/product-dhf/item-definition/ITEM-DEFINITION-TEMPLATE.md` | ISO 26262 Part 3 §5 Item Definition |
| `templates/product-dhf/hara/HARA-TEMPLATE.md` | ISO 26262 Part 3 §6 HARA with full ASIL determination table per Annex B |
| `templates/product-dhf/safety-concept/SAFETY-CONCEPT-TEMPLATE.md` | Combined FSC (Part 3 §7) + TSC (Part 4 §6) + optional Cybersecurity Concept (ISO 21434 §9) |
| `templates/product-dhf/tara/TARA-TEMPLATE.md` | ISO/SAE 21434 §15 TARA with UN R155 Annex 5 coverage matrix |
| `templates/product-dhf/ppap/PPAP-TEMPLATE.md` | AIAG PPAP 4th Ed. 18-element submission |
| `bundles/example-vehicle.yaml` | Example bundle: ExamplePowertrainECU under NHTSA + UNECE + KBA composing automotive + regulated-ai + iso-27001 |
| `bundles/example-vehicle.matrix.json` | Committed baseline matrix for regression detection |

### Files modified

| Path | Change |
|---|---|
| `registry/standards.yaml` | +7 standards: IATF 16949:2016, ISO 26262:2018, ISO/SAE 21434:2021, UN R155, UN R156, Automotive SPICE 4.0, AIAG PPAP 4th Ed. |
| `registry/jurisdictions.yaml` | +4 jurisdictions: NHTSA, UNECE, KBA, TC-MVS (TC-MVS chosen as a distinct id from aerospace's TCCA to avoid collision; both are Canadian regulators but for different transport modes) |
| `.github/workflows/engine-tests.yml` | Validate step extended (automotive standalone + composite); regenerate step extended (example-vehicle dry-run) |
| `engine/openqms/__init__.py` | `__version__ = "0.15.0"` |
| `engine/pyproject.toml` | `version = "0.15.0"`; keywords gained `automotive`, `iatf-16949`, `iso-26262`, `iso-21434` |

### Build / test commands run

```bash
# Validate automotive standalone
openqms validate --module automotive
# → invariant_holds: True

# Validate automotive + regulated-ai + iso-27001 composite
openqms validate --module automotive --module regulated-ai --module iso-27001
# → invariant_holds: True

# Regenerate baseline matrix
openqms regenerate --bundle example-vehicle --write-matrix
# → wrote bundles/example-vehicle.matrix.json (baseline)

# Idempotence check
openqms regenerate --bundle example-vehicle
# → (no changes); exit 0

# Full test suite
pytest engine/tests -q
# → 108 passed in 9.90s (unchanged — module is content, not engine code)
```

### Dependencies

No engine code changes; no new dependencies. Automotive module is pure content under the existing engine + registry + composition primitive.

### Clause breakdown (28 total)

- **QMS substrate (IATF 16949)** — 9 clauses: §4.4, §7.1.5.2.1, §7.5, §8.3.3.3, §8.4, §8.5.1.1, §8.7, §9.2, §10.2.3.
- **Functional safety (ISO 26262)** — 10 clauses: Part 2 + Part 2 §6; Part 3 §5, §6, §7; Part 4; Part 5; Part 6; Part 8; Part 9.
- **Cybersecurity (ISO/SAE 21434)** — 5 clauses: §5, §9, §10, §11, §15.
- **Regulations (UN R155 + R156)** — 3 clauses: R155 CSMS, R155 vehicle-type, R156 SUMS.
- **Process maturity (Automotive SPICE 4.0)** — 2 clauses: SWE group, MAN + SUP groups.
- **Production approval (AIAG PPAP 4th Ed.)** — 1 clause: 18-element submission.

### Cross-cutting template reuse

Automotive QMS shares the substrate structure of medical-devices and aerospace QMS. The automotive module reuses 8 cross-cutting templates already in Open QMS:

- `quality-policy.md` ← IATF-4.4 + IATF-7.5
- `SOP-TEMPLATE.md` ← multi-bound: IATF (calibration / SCs / Control Plan / NCRs), ISO 26262 Part 8 (supporting processes), ISO 21434 §5+§10+§11, UN R155+R156, ASPICE MAN+SUP
- `AUDIT-PROCEDURE-TEMPLATE.md` ← IATF-9.2
- `MANAGEMENT-REVIEW-TEMPLATE.md` ← IATF-4.4
- Supplier templates ← IATF-8.4
- CAPA template ← IATF-10.2.3 (8D entry point)
- NCR template ← IATF-8.7
- `RISK-MANAGEMENT-FILE-TEMPLATE.md` ← ISO 26262 Part 2 + Part 9 (FuSa management + dependent-failure analysis)
- `VERIFICATION-PROTOCOL-TEMPLATE.md` ← ISO 26262 Part 5 HW V&V
- `SOFTWARE-TEST-PROTOCOL-TEMPLATE.md` ← ISO 26262 Part 6 SW V&V + ASPICE SWE

Automotive-specific extensions (concept-phase deliverables, the two parallel risk-analysis disciplines HARA + TARA, the combined Safety Concept, and PPAP) get their own 5 new templates.

---

## §2 Results

### Module validates standalone and in composite

The automotive module is well-formed per OQ-013 and OQ-014:

- OQ-001 invariant (bidirectional clause-to-artifact traceability) holds — every clause cites at least one artifact template; every template-binding addresses at least one clause.
- All 8 referenced standards resolve through the registry (added in this same commit-set).
- All clause IDs in template `addresses:` lists reference clauses defined in this module's `clauses:` section.

Validates clean as `automotive` standalone, as `automotive + regulated-ai + iso-27001` composite (the bundle case for an ML-enabled ECU under UN R155 type-approval scope).

### Compose primitive handles three industries

The OQ-011 compose primitive — built in medical-devices context (v0.4.0), exercised across aerospace (v0.14.0) and now automotive (v0.15.0) — composes all three verticals with the regulated-ai cross-cutting overlay using the same code path. The regulated-ai overlay's NIST AI RMF + EU AI Act + ISO 42001 + ISO 23894 clauses interleave cleanly with each vertical's domain-specific clauses in the resolved bundle.

This is the load-bearing structural result of v0.15.0: the OQ-011 + OQ-012 + OQ-013 + OQ-014 + template-system stack handles three substantively different industries (medical / aerospace / automotive) without engine code change. The medical-devices module was the first vertical built; aerospace tested whether the platform generalized; automotive confirms the generalization works across substantively different shapes of regulated industry.

### Substantively different shape from aerospace

Automotive is not a "second aerospace." The shape of regulation is different:

| Dimension | Aerospace | Automotive |
|---|---|---|
| Risk-management discipline | Single track (ARP4761 system safety assessment) | **Bifurcated**: ISO 26262 (FuSa, ASIL A-D) AND ISO/SAE 21434 (cyber, CAL 1-4), interacting at architecture level |
| Concept-phase deliverable | FHA + PASA / PSSA driving DAL | Item Definition → HARA → FSC → TSC chain driving ASIL |
| Cybersecurity | Not regulated at type-approval level | Mandatory in UNECE jurisdictions since July 2022 (UN R155 CSMS + R156 SUMS) |
| Type-approval | FAA / EASA Type Certificate per aircraft | Layered: IATF cert + UN R155 CSMS cert + UN R156 SUMS cert + per-vehicle Annex 5 cyber assessment + KBA / UNECE type approval |
| Production approval | AS9102 FAI (3 forms, dimensional focus) | PPAP 18 elements (DFMEA + PFMEA + Control Plan + MSA + capability studies + PSW) |
| Process-maturity standard | (not separately mandated) | Automotive SPICE 4.0 (VDA-required for German OEMs) |

The Safety Concept template models the safety-security interaction explicitly (Part C with FSR↔CSR cross-reference table); the TARA template includes the UN R155 Annex 5 coverage matrix (32 threats across 7 categories). These are automotive-specific structural deliverables that don't exist in the aerospace shape.

### Example bundle resolves end-to-end

`example-vehicle.yaml` defines ExamplePowertrainECU under NHTSA + UNECE + KBA composing automotive + regulated-ai + iso-27001 across 12 standards (8 automotive + 4 AI/IS). Idempotent regenerate confirmed. The bundle exercises:
- Multi-jurisdiction handling (3 jurisdictions; CLI accepts repeatable --jurisdiction)
- Standards-cross-reference (12 standards, each appearing in `applicable_standards` of at least one of the 3 jurisdictions)
- Module composition (3 modules — vertical + AI overlay + IS overlay)

### Test suite unchanged

108 tests pass; same count as v0.14.0. Automotive is content, not engine code. The automotive-specific validation surface is exercised by the CI workflow's validate + regenerate steps.

### Forward work surfaced

- **ASIL class overlays** — ASIL-A / ASIL-B / ASIL-C / ASIL-D + QM. Each level encodes the process requirements that scale with ASIL (structural coverage thresholds per Part 6, independence requirements per Part 2 §6, hardware metrics SPFM/LFM/PMHF thresholds per Part 5). Mirrors medical-devices class overlay pattern.
- **CAL class overlays** — CAL 1-4 per ISO/SAE 21434.
- **Automotive-defense overlay** — MIL-STD-882E + ITAR + EAR. Strict scope notes apply (no controlled technical data in Open QMS).
- **Motorcycle adaptation** — ISO 26262 Part 12. Decision on overlay-vs-vertical pending an adopter use case.
- **Heavy commercial vehicle + bus** — same standards apply; operational situations and per-vehicle-type cyber tightness differ.
- **NHTSA Part 573 recall workflow** — cross-cutting; analogous to medical-devices §820.198 complaints + EU MDR vigilance. Likely lands as a `recall` cross-cutting workflow module reusable across automotive + future consumer-product verticals.

---

## §3 Verification

### OQ-072 — automotive vertical module — example-tested → `:tested`

**Evidence type:** example-tested.

**Test surface:**

1. `openqms validate --module automotive` exercises the OQ-013 validation harness against the automotive manifest; harness asserts the OQ-001 invariant on the union of (automotive clauses, automotive template bindings). Run locally pre-commit: `invariant_holds: True`.
2. `openqms validate --module automotive --module regulated-ai --module iso-27001` exercises the OQ-011 + OQ-012 + OQ-013 composition path with three modules (vertical + two overlays); composed module validates clean.
3. `openqms regenerate --bundle example-vehicle --write-matrix` exercises OQ-014 (registry lookup for 7 automotive standards + 4 automotive jurisdictions; the 4 jurisdictions include 3 in this bundle's `jurisdictions:` list — NHTSA + UNECE + KBA — TC-MVS unused but registered for adopters needing it) + OQ-015 (re-resolution diff). Baseline write succeeds; idempotent re-run yields no diff.
4. CI workflow extension at `.github/workflows/engine-tests.yml` runs both validate paths and the regenerate dry-run on every push touching engine/, modules/, registry/, templates/, or bundles/. Drift in any module/registry/template that affects automotive will fail CI.

**What's covered:** structural well-formedness of the module + its registry citations + its template bindings + its composability with existing overlays + regression detection on the example bundle.

**What's not covered:** semantic correctness of the clause-to-artifact mapping (Open QMS does not adjudicate whether IATF 16949 §9.2 is appropriately satisfied by `audit-procedure-SOP.md` — that is a human-judgment claim, evidenced by adopter validation per their certification audit). OQ-080 disclaimer covers this scope boundary.

**Status:** `:tested` per the evidence-type → status table. Upgrade to `:verified` would require a property test holding across a generated population of automotive-shaped modules — not motivated until a second automotive-like module exists to share invariants with.

### Existing entries unaffected

No status transitions on existing entries. OQ-072 is a strictly additive Module-tier entry; engine code paths (OQ-010, OQ-011, OQ-013, OQ-014, OQ-015) are exercised by the new content but their `:verified` status (from v0.13.0 property tests) is unchanged.

---

## §4 Spec impact

### New entries

| S-ID | Tier | Evidence type | Status | Depends_on | Claim summary |
|---|---|---|---|---|---|
| **OQ-072** | Module | example-tested | `:tested` | OQ-011, OQ-014 | Automotive vertical at `modules/automotive/`: 28 clauses across 8 standards (ISO 9001 / IATF 16949 / ISO 26262 / ISO/SAE 21434 / UN R155 / UN R156 / Automotive SPICE 4.0 / AIAG PPAP 4th Ed.); composes with regulated-ai and iso-27001; 5 new automotive-specific templates; second non-medical vertical |

### Status transitions on existing entries

None.

### Adjusted entries

- **OQ-038** template count: 36 → 41 (Item Definition + HARA + Safety Concept + TARA + PPAP).

### Counts

- **Before v0.15.0:** 6 `:verified` / 43 `:tested` / 7 `:argued` / 0 `:open` (total 56).
- **After v0.15.0:** 6 `:verified` / 44 `:tested` / 7 `:argued` / 0 `:open` (total **57**).
- Module-tier entries: 20 → 21 (OQ-040..OQ-059 + OQ-072).

### S-ID numbering note

OQ-072 is the next free S-ID after the existing OQ-040..OQ-059 Module range (now full from medical + aerospace + overlays), the OQ-060..OQ-069 Gap range, and OQ-070..OQ-071 Licensing range. OQ-080 is the only Gap entry above the new Module assignment; numbering remains non-contiguous-but-monotonic per existing project convention.

### Forward spec entries (not opened, surfaced for future sessions)

- **OQ-XXX ASIL-A class overlay** — ISO 26262 ASIL-A rigor (statement coverage; recommended-not-mandatory confirmation review; lower hardware-metric thresholds).
- **OQ-XXX ASIL-B / ASIL-C / ASIL-D class overlays** — progressively stricter rigor.
- **OQ-XXX CAL class overlays** — CAL 1-4 per ISO/SAE 21434.
- **OQ-XXX automotive-defense overlay** — MIL-STD-882E + ITAR + EAR procedural discipline.
- **OQ-XXX motorcycle adaptation** — ISO 26262 Part 12.
- **OQ-XXX NHTSA Part 573 recall workflow** — cross-cutting.

None of these are opened as `:open` spec entries today; pending adopter need or explicit session opening one.

### Engine version

0.14.0 → 0.15.0. No engine code change; version bump tracks the module addition + keyword expansion (`automotive`, `iatf-16949`, `iso-26262`, `iso-21434`).

---

## Cross-audit (A0-A6) — clean

| Check | Result |
|---|---|
| A0 — Self-audit | Pass — this companion exists; registry row added; dashboard updated; changelog entry added; spec total reconciled to 57 |
| A1 — Coverage | Pass — OQ-072 added to artifact_registry.md in same session |
| A2 — Logic & Status parity | Pass — OQ-072 `:tested` / Module / example-tested in both spec and registry |
| A3 — Evidence exists | Pass — all 5 templates exist on disk; module.yaml + README.md exist; engine validate + regenerate runs reference real engine paths; example-vehicle bundle + baseline matrix exist |
| A4 — Status honesty | Pass — example-tested supports `:tested`, not `:verified` or `:proved` |
| A5 — Stale counts | Pass — dashboard updated to 57 in same session; CLAUDE.md doesn't cite total counts (only per-tier breakdowns) |
| A6 — Test sync | Pass — CI workflow extended to validate automotive + regenerate example-vehicle on every push touching the relevant paths |
