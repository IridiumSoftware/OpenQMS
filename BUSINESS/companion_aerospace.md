# Companion — Aerospace vertical (v0.14.0)

**Session date:** 2026-05-23
**Engine version transition:** 0.13.0 → 0.14.0
**Commits:** `a480c3a` (module + templates + registry + bundle + CI) · `00de6d0` (engine version bump)

---

## §1 Computational basis

### What was built

A new vertical regulatory module for **civil-aviation aerospace** — the first non-medical vertical in Open QMS. Until v0.14.0 every shipped module was either the medical-devices vertical, a cross-cutting overlay (iso-27001, regulated-ai), or a medical-devices class overlay (samd, implantable, mdr-class-*, fda-class-*). Aerospace's purpose is structural: confirm the platform composition (compose primitive OQ-011, registry OQ-014, validation harness OQ-013, template system) generalizes off the medical-devices substrate.

### Files added

| Path | Purpose |
|---|---|
| `modules/aerospace/module.yaml` | Vertical module manifest; 27 clauses across 9 aerospace standards |
| `modules/aerospace/README.md` | Module documentation — scope (civil aviation under FAA / EASA / TCCA), composition (regulated-ai / iso-27001), forward work (DAL class overlays, defense, commercial space), standards licensing pointer |
| `templates/product-dhf/psac/PSAC-TEMPLATE.md` | DO-178C Plan for Software Aspects of Certification |
| `templates/product-dhf/fha/FHA-TEMPLATE.md` | ARP4761 Functional Hazard Assessment |
| `templates/product-dhf/safety-assessment/SSP-TEMPLATE.md` | ARP4754A + ARP4761 System Safety Plan |
| `templates/product-dhf/fai/FAI-REPORT-TEMPLATE.md` | AS9102 Rev C First Article Inspection Report (Forms 1/2/3) |
| `templates/product-dhf/type-cert/TYPE-CERT-PACK-INDEX-TEMPLATE.md` | 14 CFR Part 21 + EASA Part 21 Type Certificate Pack Index (aerospace analog of medical-devices Technical File Index) |
| `bundles/example-aircraft.yaml` | Example bundle definition: ExampleAvionicsComputer under FAA composing aerospace + regulated-ai + iso-27001 |
| `bundles/example-aircraft.matrix.json` | Committed baseline matrix for regression detection |

### Files modified

| Path | Change |
|---|---|
| `registry/standards.yaml` | +9 standards: ISO 9001:2015, AS9100D, 14 CFR Part 21, EASA Part 21, DO-178C:2011, DO-254:2000, ARP4754A:2010, ARP4761:1996, AS9102 Rev C |
| `registry/jurisdictions.yaml` | +3 jurisdictions: FAA (U.S. Federal Aviation Administration — distinct from medical-devices FDA = Food and Drug Administration), EASA (European Union Aviation Safety Agency), TCCA (Transport Canada Civil Aviation). Each lists its typical `applicable_standards` |
| `.github/workflows/engine-tests.yml` | Validate step extended to cover `aerospace` standalone, `regulated-ai` standalone, and `aerospace + regulated-ai + iso-27001` composite. Regenerate step extended to dry-run both `example-samd` AND `example-aircraft` matrices |
| `engine/openqms/__init__.py` | `__version__ = "0.14.0"` |
| `engine/pyproject.toml` | `version = "0.14.0"`; keywords gained `aerospace`, `as9100`, `do-178c` |

### Build / test commands run

```bash
# Validate aerospace standalone
openqms validate --module aerospace
# → invariant_holds: True

# Validate aerospace + regulated-ai composite
openqms validate --module aerospace --module regulated-ai
# → invariant_holds: True

# Regenerate baseline matrix
openqms regenerate --bundle example-aircraft --write-matrix
# → wrote bundles/example-aircraft.matrix.json (baseline)

# Idempotence check
openqms regenerate --bundle example-aircraft
# → (no changes); exit 0

# Full test suite
pytest engine/tests -q
# → 108 passed in 9.57s (unchanged — module is content, not engine code)
```

### Dependencies

No engine code changes; no new dependencies. Aerospace module is pure content under the existing engine + registry + composition primitive.

### Clause breakdown (27 total)

- **QMS substrate** — AS9100D §§4.4, 5.6 (renumbered to §9.3 in Rev D), 7.1, 7.4, 7.5, 8.1.4 operational risk, 8.4 supplier control, 8.5.1 production with FOD prevention, 8.7 nonconforming output, 9.2 internal audit, 10.2 corrective action (11 clauses).
- **Certification (US + EU)** — 14 CFR Part 21 §§21.31 type design, 21.35 flight tests, 21.50 ICA (3 clauses); EASA Part 21 Subpart B (1 clause). 4 total.
- **Avionics software** — DO-178C:2011 PSAC + §6 verification + §7 config management + §9 lifecycle data + §11 SOIs. 5 clauses.
- **Airborne electronic hardware** — DO-254:2000 PHAC + §6 V&V. 2 clauses.
- **System development** — ARP4754A:2010 §5 process + §6 function allocation. 2 clauses.
- **Safety assessment** — ARP4761:1996 §3 FHA + §§4-5 PASA/PSSA + §6 SSA + §9 CCA. 4 clauses.
- **Production gate** — AS9102 Rev C FAI. 1 clause.

### Cross-cutting template reuse

Aerospace QMS is structurally similar to medical-devices QMS — both are regulated-product quality systems with substrate (people / processes / equipment / supplier control / corrective action) + product-specific (cert + safety + V&V) extensions. The aerospace module reuses 6 cross-cutting templates already in Open QMS:

- `quality-policy.md` ← bound to AS9100D §5.6 (renumbered §9.3)
- `SOP-TEMPLATE.md` ← bound to AS9100D §§7.5, 8.4, 8.5.1, 8.7, 10.2, 14 CFR §21.50 ICA
- `audit-procedure-SOP.md` ← bound to AS9100D §9.2
- `management-review.md` template ← bound to AS9100D §5.6 + §9.3
- supplier templates ← bound to AS9100D §8.4
- risk management + verification + software test templates ← bound to ARP4754A / ARP4761 / DO-178C verification clauses

Aerospace-specific extensions (cert, safety assessment, FAI) get their own 5 new templates.

---

## §2 Results

### Module validates standalone and in composite

The aerospace module is well-formed per OQ-013 and OQ-014:

- OQ-001 invariant (bidirectional clause-to-artifact traceability) holds: every clause cites at least one artifact, every artifact is reachable from at least one clause.
- All 9 referenced standards resolve through the registry (added in this same commit).
- All clause + template paths in the manifest exist on disk.

Validates clean as `aerospace` standalone, as `aerospace + regulated-ai` (the bundle case for AI/ML-enabled avionics), and as `aerospace + regulated-ai + iso-27001` (full enterprise composite).

### Compose primitive generalizes

The OQ-011 compose primitive — built and verified in medical-devices context — composes aerospace + regulated-ai without modification. ISO 23894 AI risk management and ARP4761 system safety assessment are complementary domain-specific extensions of risk discipline; they share no clauses but their template bindings interleave cleanly in the resolved bundle.

This is the load-bearing structural result of v0.14.0: the OQ-011 + OQ-012 + OQ-013 + OQ-014 + template-system stack handles a substantively different industry without engine code change. Open QMS isn't medical-devices-with-extras; the medical-devices module just happened to be the first vertical built.

### Example bundle resolves end-to-end

`example-aircraft.yaml` defines ExampleAvionicsComputer under FAA composing aerospace + regulated-ai + iso-27001 across 13 standards (9 aerospace + 4 AI/IS). Idempotent regenerate confirmed (`openqms regenerate --bundle example-aircraft` returns "no changes" exit 0 after baseline write).

### Test suite unchanged

108 tests pass; same count as v0.13.0. Aerospace is content, not engine code — there's nothing new to test at engine level. The aerospace-specific validation is exercised by the CI workflow's validate + regenerate steps (which run the engine's existing OQ-013 / OQ-014 / OQ-015 paths against the new manifest + registry + bundle data).

### Forward work surfaced

- **Aerospace DAL class overlays** — DO-178C / DO-254 Design Assurance Levels A through E. Each DAL mandates increasing rigor of structural coverage analysis (MC/DC for DAL-A, decision coverage for DAL-B, statement coverage for DAL-C, requirements-based testing only for DAL-D, none for DAL-E). Direct analog of the medical-devices class overlay pattern (mdr-class-iii / fda-class-iii / etc.). Triggered by ARP4761 FHA + ARP4754A function allocation; DAL drives DO-178C / DO-254 process rigor.
- **Aerospace-defense overlay** — MIL-STD-882E System Safety Program Plan + ITAR + EAR controlled-technology handling. Strict scope notes apply (Open QMS doesn't redistribute controlled technical data; the overlay covers process discipline, not the data itself).
- **Commercial space scope** — FAA 14 CFR Part 450 (launch / re-entry vehicle licensing). Likely a separate vertical (different regulatory architecture from civil aviation) rather than an aerospace extension.
- **Production-readiness deepening** — Nadcap (NDT, heat treatment, plating, welding qualifications) as an aerospace cross-cutting overlay; AS9145 Advanced Product Quality Planning (APQP); AS9120 (distributors).

---

## §3 Verification

### OQ-059 — aerospace vertical module — example-tested → `:tested`

**Evidence type:** example-tested.

**Test surface:**

1. `openqms validate --module aerospace` exercises the OQ-013 validation harness against the aerospace manifest; harness asserts the OQ-001 invariant on the union of (aerospace clauses, aerospace template bindings). Run locally pre-commit: `invariant_holds: True`.
2. `openqms validate --module aerospace --module regulated-ai` exercises the OQ-011 + OQ-012 + OQ-013 composition path; composed module validates clean.
3. `openqms regenerate --bundle example-aircraft --write-matrix` exercises OQ-014 (registry lookup for 9 aerospace standards + 3 aerospace jurisdictions) + OQ-015 (re-resolution diff). Baseline write succeeds; idempotent re-run yields no diff.
4. CI workflow extension at `.github/workflows/engine-tests.yml` runs both validate paths and the regenerate dry-run on every push touching engine/, modules/, registry/, templates/, or bundles/. Drift in any module/registry/template that affects the aerospace example will fail CI.

**What's covered:** structural well-formedness of the module + its registry citations + its template bindings + its composability with existing overlays + regression detection on the example bundle.

**What's not covered:** semantic correctness of the clause-to-artifact mapping (Open QMS does not adjudicate whether AS9100D §9.2 is appropriately satisfied by `audit-procedure-SOP.md` — that is a human-judgment claim, evidenced by adopter validation per their certification audit). Open QMS's OQ-080 disclaimer already covers this scope boundary across all modules.

**Status:** `:tested` per the evidence-type → status table. Upgrade to `:verified` would require a property test that holds across a generated population of aerospace-shaped modules — not motivated until a second aerospace-like module exists to share invariants with.

### Existing entries unaffected

No status transitions on existing entries. OQ-059 is a strictly additive Module-tier entry; engine code paths (OQ-010, OQ-011, OQ-013, OQ-014, OQ-015) are exercised by the new content but their `:verified` status (from v0.13.0 property tests) is unchanged.

---

## §4 Spec impact

### New entries

| S-ID | Tier | Evidence type | Status | Depends_on | Claim summary |
|---|---|---|---|---|---|
| **OQ-059** | Module | example-tested | `:tested` | OQ-011, OQ-014 | Aerospace vertical at `modules/aerospace/`: 27 clauses across 9 aerospace standards (ISO 9001 / AS9100D / 14 CFR Part 21 / EASA Part 21 / DO-178C / DO-254 / ARP4754A / ARP4761 / AS9102); composes with regulated-ai and iso-27001; 5 new aerospace-specific templates; first non-medical vertical |

### Status transitions on existing entries

None.

### Adjusted entries

- **OQ-038** template count: 31 → 36 (PSAC + FHA + SSP + FAI Report + Type Cert Pack Index).

### Counts

- **Before v0.14.0:** 6 `:verified` / 42 `:tested` / 7 `:argued` / 0 `:open` (total 55).
- **After v0.14.0:** 6 `:verified` / 43 `:tested` / 7 `:argued` / 0 `:open` (total **56**).
- Module-tier entries: 19 → 20 (OQ-040..OQ-059).

### Forward spec entries (not opened, surfaced for future sessions)

- **OQ-XXX aerospace DAL-A class overlay** — DO-178C / DO-254 Design Assurance Level A rigor (MC/DC structural coverage, independence requirements). Triggered when a software / hardware item's DAL assignment per FHA is A.
- **OQ-XXX aerospace DAL-B class overlay** — DAL-B rigor (decision coverage). Triggered when assigned DAL is B.
- **OQ-XXX aerospace DAL-C/D/E class overlays** — Lower-DAL rigor tiers; structurally analogous.
- **OQ-XXX aerospace-defense overlay** — MIL-STD-882E SSPP + ITAR + EAR procedural discipline.
- **OQ-XXX commercial-space vertical** — FAA 14 CFR Part 450; likely separate vertical from civil aviation.

None of these are opened as `:open` spec entries today; they remain in this companion's forward-work note pending an adopter need or a session opening one explicitly.

### Engine version

0.13.0 → 0.14.0. No engine code change; version bump tracks the module addition + the keyword expansion (`aerospace`, `as9100`, `do-178c`) for PyPI surfacing when the engine eventually ships.

---

## Cross-audit (A0-A6) — clean

| Check | Result |
|---|---|
| A0 — Self-audit (does CLAUDE.md / TCE-discipline-this-doc match observable practice?) | Pass — this companion exists, registry row added in same session, dashboard updated, changelog entry added, spec total reconciled to 56 |
| A1 — Coverage (every spec S-ID has a registry row) | Pass — OQ-059 added to artifact_registry.md in same commit-set |
| A2 — Logic & Status parity (registry matches spec) | Pass — OQ-059 `:tested` / Module / example-tested in both |
| A3 — Evidence exists (every Test/Proof + Source file in registry exists) | Pass — all 5 templates exist on disk; module.yaml + README.md exist; engine validate + regenerate runs reference real engine paths |
| A4 — Status honesty (no entry has a status its evidence type can't support) | Pass — example-tested supports `:tested`, not `:verified` or `:proved` |
| A5 — Stale counts (dashboard + CLAUDE.md match spec) | Pass — dashboard updated to 56 in same session; CLAUDE.md doesn't cite total counts (only per-tier breakdowns) |
| A6 — Test sync (every spec entry with a Test/Proof file is exercised by a test that runs in CI) | Pass — CI workflow extended to validate aerospace + regenerate example-aircraft on every push touching the relevant paths |
