# Companion — v0.48.0 + v0.49.0 + v0.50.0 + v0.51.0 (US-state privacy + engine features + final cross-overlays + polishing)

**Session date:** 2026-05-25 (continuation arc from the v0.46.0+v0.47.0 release-day)
**Engine version transitions:** 0.47.0 → 0.51.0 (4 releases)
**Why combined companion:** four sequential releases sharing one session arc: complete the cross-cutting overlay landscape (v0.48 us-state-privacy), then ship the long-deferred engine adopter-features (v0.49 coverage + crosswalk + jurisdictions-query), then close out the cross-overlay tour with the final batch (v0.50), then polish (v0.51). Combined companion is proportionate to per-release weight; no single release warrants standalone treatment but the combination is substantial.

## §1 Computational basis

Four sequential releases:

| Version | Theme | Public commit | Spec entries |
|---|---|---|---|
| v0.48.0 | US State Privacy Umbrella cross-cutting overlay (26th cross-cutting; VCDPA template family covering ~14 US states) | `ffcfe0b` | OQ-114 NEW `:tested` |
| v0.49.0 | Engine adopter-features — 3 new CLI subcommands | `ffcfe0b` (same release-day commit family) | OQ-115 + OQ-116 + OQ-117 NEW `:tested` |
| v0.50.0 | Final cross-overlay batch (4) — automotive-supply-chain + clinical-trial-multi-region + banking-resilience + utility-cybersecurity | `50ec131` | OQ-118 NEW `:tested` |
| v0.51.0 | Polishing pass — audit + this companion + engine bump | (this commit) | (none) |

**Aggregate deliverables:**

- **5 NEW spec entries** (OQ-114 + OQ-115 + OQ-116 + OQ-117 + OQ-118)
- **5 new modules** (1 cross-cutting + 4 cross-overlays)
- **2 new templates** (us-state-privacy: US-STATE-PRIVACY-MATRIX + DATA-PROTECTION-ASSESSMENT)
- **3 new CLI subcommands** (`coverage` + `crosswalk` + `jurisdictions-query`)
- **6 new registry standards** (v0.48: US State Privacy Laws; v0.50: ICH E6(R3) + EU CTR 536/2014 + NERC CIP + EU NIS2 + FFIEC IT Handbook)
- **Cross-cutting overlay count:** 25 → 26 (+1 at v0.48)
- **Cross-overlay count:** 8 → 12 (+4 at v0.50)
- **Total module count:** 111 → 116 (+5 across arc)
- **Total registry standards:** ~129 → ~135 (+6 across arc)
- **Pytest count:** 116 → 129 (+13 at v0.49.0 for the 3 new subcommands)

**Build commands** (replayable from clean checkout):

```bash
source .venv-engine/bin/activate

# v0.48 — US state privacy
openqms validate --module us-state-privacy
openqms validate --module privacy --module us-state-privacy --module hipaa

# v0.49 — engine features (new subcommands)
openqms coverage --all --threshold 99      # CI regression gate
openqms crosswalk --module privacy --module hipaa --format md
openqms jurisdictions-query --jurisdiction FDA

# v0.50 — final cross-overlays (all 4)
openqms validate --module automotive --module automotive-asil-d --module automotive-cal-4 --module recall-workflow --module automotive-supply-chain
openqms validate --module pharma --module privacy --module hipaa --module digital-health-multi-region --module clinical-trial-multi-region
openqms validate --module iso-37301 --module iso-37301-financial-services --module dora --module dora-non-ctpp --module nist-csf --module nist-csf-tier-3 --module iso-22301 --module banking-resilience
openqms validate --module manufacturing --module iso-27001 --module nist-csf --module nist-csf-tier-3 --module utility-cybersecurity

# Repo-wide invariants
pytest engine/tests -q                                     # 129/129
python3 scripts/lint-module-yaml.py                        # 0 findings
openqms trace --all --output /tmp/trace.json               # 0 orphans
openqms coverage --all --output /tmp/cov.json              # 100.0% aggregate
```

## §2 Results

### v0.48.0 — US State Privacy Umbrella (OQ-114)

26th cross-cutting overlay; single module covering ~14 US state comprehensive privacy laws using VCDPA template family + state-divergence handling. Distinct from the `privacy` overlay (GDPR + CCPA) because the ~14 non-California state laws use a 2-way GDPR-like controller/processor framework distinct from CCPA's 4-way classification + the VCDPA-template states include unique provisions (right-to-appeal denial; UOOM mandatory in 8 states; Maryland MODPA data-minimization strict-necessity standard).

**Covered states:** Virginia VCDPA (template) + Colorado CPA + Connecticut CTDPA + Utah UCPA + Texas TDPSA + Oregon OCPA + Montana MCDPA + Iowa ICDPA + Delaware DPDPA + NH NHPA + NJ NJDPA + Tennessee TIPA + Minnesota MCDPA + Maryland MODPA + Indiana INCDPA + Florida FDBR.

**Key divergence handling:**
- Maryland MODPA (effective 2025-10-01) — data minimization "strictly necessary" + absolute prohibition on sale of sensitive data + absolute prohibition on targeted advertising to under-18
- Florida FDBR — narrowest US state law; effectively only Google + Meta + Amazon + Apple in scope

### v0.49.0 — Engine adopter-features (OQ-115 + OQ-116 + OQ-117)

Three new Architecture-tier CLI subcommands — first Architecture-tier additions since OQ-067 (`openqms trace`, v0.39.0).

| Subcommand | Purpose | Key output |
|---|---|---|
| `openqms coverage` | per-module + aggregate coverage metrics | aggregate clause-coverage % + per-module orphan lists; `--threshold N` exits 1 if below |
| `openqms crosswalk` | clause-crosswalk between modules | same-(standard, section) overlap groups + per-module shared-vs-own-only counts |
| `openqms jurisdictions-query` | registry standards by jurisdiction | publisher-inference via `_PUBLISHER_TO_JURISDICTIONS` table (30+ publishers); forward-compatible with explicit `jurisdictions:` field |

**CI gates added:**
- Aggregate clause-coverage = 100.0% asserted on every push (regression gate, paired with the OQ-067 zero-orphan invariant)
- Crosswalk smoke (3-module privacy-adjacent triad)
- Jurisdictions-query smoke (FDA + EU MDR both return >0)

At v0.49.0 audit time: aggregate coverage = 100.0% across 112 modules / 838 clauses / 0 orphans; FDA query returns 18 standards.

### v0.50.0 — Final cross-overlay batch (OQ-118)

Four cross-overlays completing the shape's coverage of major vertical intersections:

- **automotive-supply-chain** (automotive + asil-d + cal-4 + recall-workflow) — DIA per ISO 26262-8 §5 + CIA per ISO/SAE 21434-7 + AIAG PPAP 4th-Edition 18-element + 5-level submission + ISO/SAE 21434 §15 supplier management + UN R155 Type-Approval CSMS + R156 SUMS + NHTSA Part 573 5-working-day recall coordination + IATF 16949 §8.4 tier-N flow-down + software-supplier special considerations
- **clinical-trial-multi-region** (pharma + privacy + hipaa + digital-health-multi-region) — ICH E6(R3) GCP (Step 4 2024-01-19) + EU CTR 536/2014 + CTIS + 21 CFR 312 IND + §312.32 Safety Reports + DCT + multi-region PHI coordination + parallel IRB/IEC tracking + RBM + multi-region PV triage
- **banking-resilience** (iso-37301-financial-services + dora + nist-csf + iso-22301) — DORA + FFIEC cross-regime alignment + NIST CSF backbone + multi-stream incident reporting (DORA + 36h CSI + NYDFS + CIRCIA) + TLPT framework alignment (TIBER-EU + CBEST + MAS AASE + iCAST) + CTPP + Lead Overseer + ISO 22301 BIA + ICT BCP
- **utility-cybersecurity** (manufacturing + iso-27001 + nist-csf) — NERC CIP-002 through CIP-014 + TSA Pipeline SD 02 series + CISA 16 Critical Infrastructure Sectors + EU NIS2 + IEC 62443 + CIRCIA + Energy Subsector + ES-C2M2 + ONG-C2M2

The cross-overlay tour now spans medical-device intersections (combination-product + connected-medical-device + digital-health-multi-region) + pharma intersections (combination-product + cell-therapy-supply-chain + clinical-trial-multi-region) + food intersections (food-pharma-grade + food-allergen-recall) + automotive intersections (automotive-supply-chain) + financial intersections (banking-resilience) + utility intersections (utility-cybersecurity) + defense intersections (defense-aerospace-cyber) + IMS (integrated-management-system).

### v0.51.0 — Polishing pass

- A0-A6 cross-audit complete; zero findings (see `audit_2026-05-25_v0_50.md`)
- This omnibus companion
- companion_index.md updated
- Dashboard "Latest" note refreshed to call out v0.51.0 polishing as the end of the v0.46-v0.50 build arc
- Engine bump 0.50.0 → 0.51.0 (pure bookkeeping)

## §3 Verification

**OQ-114 (us-state-privacy) — example-tested → `:tested`:** `openqms validate --module us-state-privacy` passes; 7-module privacy/healthcare composite validates; YAML linter clean.

**OQ-115 (coverage) — example-tested → `:tested`:** 5 tests in `engine/tests/test_coverage.py` (--all summary + per-module shape + threshold-zero + threshold-99 mixed-result + markdown format); CI gate asserts aggregate clause-coverage = 100.0%.

**OQ-116 (crosswalk) — example-tested → `:tested`:** 4 tests in `engine/tests/test_crosswalk.py` (requires-2-modules error + summary + per-module counts + markdown); CI runs 3-module smoke.

**OQ-117 (jurisdictions-query) — example-tested → `:tested`:** 4 tests in `engine/tests/test_jurisdictions_query.py` (FDA + EU MDR + unknown + text format); CI asserts FDA + EU MDR both return >0 standards.

**OQ-118 (final cross-overlay batch) — example-tested → `:tested`:** All 4 modules pass `openqms validate --module <m>` standalone; 4 vertical-composite validates (automotive 5-module + pharma 5-module + banking 8-module + utility 5-module); YAML linter clean on all 116 modules; zero-orphan trace invariant holds; 100% aggregate coverage; 129/129 pytest pass.

## §4 Spec impact

| S-ID | Tier | Evidence type | Status | Notes |
|---|---|---|---|---|
| OQ-114 | Module | example-tested | `:tested` | us-state-privacy cross-cutting overlay (26th) |
| OQ-115 | Architecture | example-tested | `:tested` | `openqms coverage` CLI subcommand |
| OQ-116 | Architecture | example-tested | `:tested` | `openqms crosswalk` CLI subcommand |
| OQ-117 | Architecture | example-tested | `:tested` | `openqms jurisdictions-query` CLI subcommand |
| OQ-118 | Module | example-tested | `:tested` | Final cross-overlay batch (4) |

Status counts after arc: 6 `:verified` / 91 `:tested` / 5 `:argued` / 0 `:open` (total 102).

## Lessons / observations

- **Cross-overlay shape is mature.** The 12 cross-overlays now cover all the obvious vertical-intersection coordination layers in the regulated-industry landscape Open QMS targets. Future cross-overlays will be additive-by-customer-request rather than gap-filling.
- **Architecture-tier engine features are gap-filling.** The 3 new CLI subcommands (coverage + crosswalk + jurisdictions-query) close longstanding adopter-experience gaps: coverage gives a "how complete is my module?" answer; crosswalk gives a "where do these two modules overlap?" answer; jurisdictions-query gives a "what standards apply to my jurisdiction?" answer. The pattern: build the substrate (modules + clauses + templates), then expose CLI features that surface what's in the substrate from useful angles.
- **YAML linter caught the §164.509 binding regression mid-release at v0.46.0** — the lint-before-pytest CI gate added at v0.40.0 is paying off as expected.
- **Engine version drift caught at v0.46.0** — corrected silently-stuck 0.43.0 → 0.46.0; pattern (parallel-batch Edit failures on subset) now flagged for verification in every release.
- **Polishing-as-release** — v0.51.0 is a pure bookkeeping release (audit + companion + version bump). Worth doing as its own release for changelog clarity even though no functional code changes.
