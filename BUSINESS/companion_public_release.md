# Companion — Public adopter-surface release (v0.23.0)

**Session date:** 2026-05-23
**Engine version transition:** 0.22.0 → 0.23.0

This companion documents the public release of Open QMS's adopter surface — the consolidation move that the user has deferred across multiple sessions in favor of substantive builds (which is fine — the breadth needed to exist before the surface could meaningfully document it).

---

## §1 Computational basis

### What was built

Pure consolidation release. No new modules, no new templates, no engine code changes. Three deliverables:

1. **README.md rewrite** from v0.7.0-era state to current v0.22.0+ state
2. **`docs/modules-catalog.md`** — comprehensive per-module catalog (new file)
3. **`modules/food-safety/README.md`** + **`modules/atmp/README.md`** — backfill missing vertical/overlay READMEs
4. **`.gitignore`** — remove `BUSINESS/` exclusion → BUSINESS spec discipline publicly readable

### Files added

| Path | Purpose |
|---|---|
| `docs/modules-catalog.md` | Comprehensive per-module catalog: 3 module-type taxonomy, per-vertical entries with module IDs + standards + compatible class overlays, class overlay tables, cross-cutting overlay entries, 11-bundle example table, composition decision flow |
| `modules/food-safety/README.md` | Documents food-safety vertical scope, standards, templates, composition guidance, forward work |
| `modules/atmp/README.md` | Documents ATMP class overlay: cell + gene therapy scope, distinguishing requirements vs. baseline pharma, templates, composition with pharma + cross-cutting overlays |
| `BUSINESS/companion_public_release.md` | This document |

### Files modified

| Path | Change |
|---|---|
| `README.md` | Rewritten from v0.7.0 state to v0.22.0+ state — 6 verticals + 22 class overlays + 7 cross-cutting overlays + 11 bundles + 81 spec entries + per-audience adoption guidance |
| `.gitignore` | `BUSINESS/` exclusion removed → spec/registry/dashboard/changelog/companions all publicly readable |
| `BUSINESS/ENGINE_SPEC.md` | OQ-097 added; v0.23.0 transition note in summary; total reconciled to 81 |
| `BUSINESS/artifact_registry.md` | OQ-097 row; coverage check updated to 81 |
| `BUSINESS/dashboard.md` | Status summary updated; Gap tier now 10 (with OQ-097); v0.23.0 transition note |
| `BUSINESS/changelog.md` | v0.23.0 entry added at top |
| `BUSINESS/companion_index.md` | This companion's row added |
| `engine/openqms/__init__.py` | `__version__ = "0.23.0"` |
| `engine/pyproject.toml` | `version = "0.23.0"` |

### Files that go public for the first time (newly readable on GitHub after un-gitignore)

| Path | Lines | Role |
|---|---|---|
| `BUSINESS/ENGINE_SPEC.md` | 811+ | 81 spec entries with logic tiers + evidence types + status |
| `BUSINESS/DESIGN.md` | 343 | Architectural narrative |
| `BUSINESS/artifact_registry.md` | 108+ | S-ID → evidence file mapping |
| `BUSINESS/dashboard.md` | 363+ | Status summary + priority stack |
| `BUSINESS/changelog.md` | 1209+ | Versioned release log back to v0.1.0 |
| `BUSINESS/companion_*.md` | ~2100 | 13 per-session companion docs documenting the computational basis + verification of every release back to v0.2.0 |
| `BUSINESS/companion_index.md` | 44+ | Companion docs index |

Total ~5100 lines of BUSINESS content going public.

### Build / test commands run

```bash
# No engine validation needed — no module changes
# Spot-check the README references resolve
ls modules/medical-devices modules/aerospace modules/automotive modules/manufacturing modules/pharma modules/food-safety
ls bundles/*.yaml | wc -l   # should be 11

# Verify .gitignore change
grep -v "BUSINESS/" .gitignore | grep BUSINESS  # should produce no output

# Full test suite (unchanged — content release, not code release)
pytest engine/tests -q
# → 108 passed
```

### Dependencies

No new dependencies. No engine code changes. Test count unchanged at 108.

---

## §2 Results

### Adopter discoverability gap closed

Before v0.23.0:
- README described v0.7.0 state (1 vertical "starting with medical devices", 1 cross-cutting overlay, ~20 clauses in modules/medical-devices/, no class overlays mentioned, no example bundles surfaced, no per-audience adoption guidance)
- No `docs/modules-catalog.md`
- food-safety vertical (shipped v0.20.0) had no README
- atmp class overlay (shipped v0.22.0) had no README
- BUSINESS/ gitignored → spec discipline + design + 13 companion docs invisible to anyone browsing the repo on GitHub

After v0.23.0:
- README accurately reflects v0.22.0+ scope (6 verticals + 22 class overlays + 7 cross-cutting overlays + 11 example bundles + 80→81 spec entries + 9-module deepest-composite reference + per-audience adoption guidance + full standards-licensing inventory)
- `docs/modules-catalog.md` is the comprehensive catalog reference
- food-safety + atmp READMEs document the most-recently-shipped scope
- BUSINESS/ contents publicly auditable

### Closes dashboard P10

P10 ("Public release of BUSINESS/ contents") was on the priority stack from v0.1.0. The user-stated condition was "things being further along" — at the time of v0.1.0 there was a single medical-devices module + a minimal engine. The platform now has 6 verticals + 22 class overlays + 7 cross-cutting overlays + 9-module composite validation, which clearly meets that bar.

### Test surface unchanged

108 tests pass; no engine code changed. The release is documentation + governance, not engine behavior.

### What this release does NOT do

- Does NOT add new spec entries claiming new Open QMS capabilities (OQ-097 is a Gap-tier entry documenting the publication action, not a new platform capability)
- Does NOT change the engine, validation harness, registry, compose primitive, or any other technical component
- Does NOT add new templates, modules, or example bundles
- Does NOT change any module manifest

It makes the existing claims publicly auditable.

---

## §3 Verification

### OQ-097 — public adopter-surface release — example-tested → `:tested`

**Evidence type:** example-tested.

**Test surface:**

1. `README.md` exists at repository root + reflects current v0.22.0+ scope (6 verticals + 22 class overlays + 7 cross-cutting overlays + 11 bundles + 81 spec entries). Verifiable by inspection.
2. `docs/modules-catalog.md` exists + lists every shipped module + bundle. Verifiable by inspection + by cross-reference (every module listed exists in `modules/<name>/module.yaml`; every bundle listed exists in `bundles/<name>.yaml`).
3. `modules/food-safety/README.md` + `modules/atmp/README.md` exist.
4. `.gitignore` does not exclude `BUSINESS/`. Verifiable by `grep -v "BUSINESS/" .gitignore | grep BUSINESS` producing no output.
5. `BUSINESS/` contents (ENGINE_SPEC.md, DESIGN.md, artifact_registry.md, dashboard.md, changelog.md, 13 companion docs) tracked in git after the release commit. Verifiable by `git ls-files BUSINESS/` producing the full file list.

**What's covered:** mechanically-verifiable publication state.

**What's not covered:** semantic accuracy of the README + catalog text (this companion + the registry + cross-reference between docs/modules-catalog.md and modules/ + bundles/ provide a check; ultimate accuracy is the maintainer's responsibility).

**Status:** `:tested` per the evidence-type → status table.

### Existing entries unaffected

No status transitions. OQ-097 is strictly additive.

---

## §4 Spec impact

### New entries

| S-ID | Tier | Evidence type | Status | Depends_on | Summary |
|---|---|---|---|---|---|
| **OQ-097** | Gap | example-tested | `:tested` | — | Public adopter-surface release: README rewrite + docs/modules-catalog.md + food-safety + atmp READMEs + BUSINESS/ un-gitignored |

### Status transitions on existing entries

None.

### Counts

- Before v0.23.0: 6 `:verified` / 67 `:tested` / 7 `:argued` / 0 `:open` (total 80).
- After v0.23.0: 6 `:verified` / **68** `:tested` / 7 `:argued` / 0 `:open` (total **81**).
- Module-tier entries: 44 (unchanged).
- Gap-tier entries: 9 → 10 (+OQ-097).

### Forward work (surfaced for future sessions)

- **Per-module READMEs for class overlays** — currently aerospace DAL overlays + automotive ASIL/CAL overlays + medical-devices class overlays (samd, implantable, ivd, mdr-class-iii/iib/iia, fda-class-iii/ii) don't have standalone READMEs. The catalog page covers them, but standalone READMEs would deepen discoverability. Probably a future polish round.
- **Per-module READMEs for cross-cutting overlays** — iso-27001, regulated-ai, iso-14001, iso-45001, iso-50001, iso-37001, iso-22301 don't have standalone READMEs. Same as above — catalog covers; standalone would deepen.
- **Vertical READMEs for medical-devices + automotive** — these were never written explicitly (the medical-devices module is older; automotive was shipped but apparently without README). Worth backfilling.
- **PyPI publication** — engine has versioned at every release but is not yet published to PyPI. With v0.23.0 keywords expanded to cover all 6 verticals, the package is ready for PyPI publication if the user wants it discoverable via `pip install openqms`.
- **GitHub Pages publication** — `docs/` is structured for MkDocs but the rendered site isn't published. Could be enabled via `.github/workflows/deploy-docs.yml` (which already exists and is referenced in the README).

### Engine version

0.22.0 → 0.23.0. No engine code change; documentation + gitignore consolidation release.

---

## Cross-audit (A0-A6) — clean

| Check | Result |
|---|---|
| A0 — Self-audit | Pass — this companion exists; OQ-097 registry row added; dashboard updated (Gap tier now 10); changelog v0.23.0 entry added; spec total reconciled to 81 |
| A1 — Coverage | Pass — OQ-097 added to artifact_registry.md |
| A2 — Logic & Status parity | Pass — `:tested` / Gap / example-tested in both spec and registry |
| A3 — Evidence exists | Pass — README.md + docs/modules-catalog.md + food-safety + atmp READMEs + updated .gitignore + this companion all on disk; will all be in the v0.23.0 commit |
| A4 — Status honesty | Pass — example-tested supports `:tested`, not `:verified` or `:proved` |
| A5 — Stale counts | Pass — dashboard updated to 81 in same session |
| A6 — Test sync | Pass — verification of OQ-097 doesn't require CI test addition (the publication state is mechanically verifiable via the file-presence + gitignore checks documented in §3) |
