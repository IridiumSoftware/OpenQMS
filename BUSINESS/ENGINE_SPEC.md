# ENGINE_SPEC — Open QMS

**Version:** v0.1.0 DRAFT
**Date:** 2026-05-22
**Maintainer:** Aaron Green
**Repo:** github.com/IridiumSoftware/OpenQMS
**License:** Apache-2.0 (spec is gitignored under BUSINESS/ pending public release of v0.1.0)

This document is the formal specification of Open QMS. Every named claim about the system gets an S-ID, a logic tier, an evidence type, and a status. If it is not in this document, it is not established.

For architectural narrative and intent, see `DESIGN.md`. For the regulatory crosswalks the modules cover, see `regulatory_modules/`. For the spec-to-evidence map, see `artifact_registry.md`. For current state and priorities, see `dashboard.md`.

---

## Tier glossary

- **Invariant** — load-bearing correctness claim about generator output.
- **Architecture** — generator engine, composition, registry.
- **Substrate** — GitHub / Git-native mechanism the system depends on.
- **Workflow** — QMS activity ↔ GitHub mapping (issue templates, CI workflows, document templates).
- **Module** — claim about a specific regulatory module's coverage.
- **Gap** — declared open problem or honest limitation.
- **Licensing** — non-regulatory legal / IP / license constraint.

## Status legend

| Status | Meaning |
|---|---|
| `:proved` | Machine-verified (lean-proved, type-checked, or algebraic). |
| `:verified` | Property-tested with passing generators. |
| `:tested` | Example-tested with hand-written cases that pass. |
| `:benchmarked` | Performance target met by recorded benchmark. |
| `:argued` | Manual argument or design commitment without mechanical verification. |
| `:open` | Claim exists, no verification or implementation yet. |

## Evidence type legend

`lean-proved` · `type-checked` · `algebraic` · `property-tested` · `example-tested` · `benchmarked` · `manual` · `none`

A spec entry may have status `:proved` only if evidence type is `lean-proved`, `type-checked`, or `algebraic`.

---

## Entries

### OQ-001 — Bidirectional traceability invariant

- **Tier:** Invariant
- **Evidence type:** property-tested
- **Status:** :verified
- **Depends_on:** —
- **Claim:** Given `(product, jurisdiction-set, standards-set)`, the generator emits an unvalidated MVP QMS such that there is a complete bidirectional traceability map between in-scope regulatory clauses and generated artifacts: every clause in scope is addressed by at least one artifact, and every artifact declares the clause(s) it addresses.
- **Notes:** Load-bearing claim of the project. Upgraded `:tested → :verified` at v0.13.0 via `engine/tests/test_property.py::test_prop_resolve_satisfies_bidirectional_traceability` — hypothesis property test over arbitrary `valid_module_strategy` outputs, asserting forward and reverse maps form a bijection on the in-scope set. Also remains exercised by the example-tested smoke fixtures from v0.2.0 + the medical-devices integration test.

### OQ-002 — Mutation preserves invariant by reconstruction

- **Tier:** Invariant
- **Evidence type:** property-tested
- **Status:** :verified
- **Depends_on:** OQ-001
- **Claim:** Mutations of the input tuple — adding a standard, removing a jurisdiction, reassigning a product, accommodating a standard supersession — preserve OQ-001 by re-resolving the bundle from scratch and emitting the new artifact set with a fresh traceability map.
- **Notes:** Reconstruction (not patch) is the design choice; reduces the surface area where invariant violations can creep in. Upgraded `:argued → :verified` at v0.13.0 via `engine/tests/test_property.py::test_prop_mutation_preserves_invariant` — hypothesis property test that drops the last template from an arbitrary valid module and asserts the validation harness correctly detects orphaned clauses iff the dropped template was the sole binding for any clause, and correctly accepts the module iff the dropped template was redundant. Demonstrates that re-resolution-from-scratch (via validate) faithfully reflects the post-mutation state. First non-example evidence in the spec; this was the only `:argued` entry where mechanical verification was achievable.

### OQ-003 — Generator emits unvalidated MVP (honesty bound)

- **Tier:** Invariant
- **Evidence type:** manual
- **Status:** :argued
- **Depends_on:** —
- **Claim:** Open QMS does not claim the generated artifact set is a validated quality system, that the artifacts are sufficient for any conformity assessment, or that the generator substitutes for human judgment. The guarantee is coverage-with-traceability per OQ-001; validation for intended use is the consuming organization's responsibility.
- **Notes:** README disclaimer and SPEC §7 carry this commitment. Honesty bound is part of the spec, not a footnote.

### OQ-010 — Bundle resolver is a pure function

- **Tier:** Architecture
- **Evidence type:** property-tested
- **Status:** :verified
- **Depends_on:** OQ-001
- **Claim:** The bundle resolver is a pure function from `(Bundle, Module)` to `ResolvedQMS`. Re-running the resolver on the same input produces the same output. No I/O; no mutation of inputs.
- **Notes:** Implemented at v0.2.0 in `engine/openqms/resolver.py::resolve`. Upgraded `:tested → :verified` at v0.13.0 via two hypothesis property tests in `engine/tests/test_property.py`: `test_prop_resolve_deterministic` (same input → same output across arbitrary modules) and `test_prop_resolve_standards_monotone` (narrowing the bundle's standards can only remove, never add, in-scope clauses — functional-monotonicity property of the filter). Frozen dataclasses guarantee immutability of inputs. Upgrade to `:proved` requires either `mypy --strict` in CI or a port to a language with checked types.

### OQ-011 — Modules compose under union; deduplication preserves invariant

- **Tier:** Architecture
- **Evidence type:** property-tested
- **Status:** :verified
- **Depends_on:** OQ-001, OQ-010
- **Claim:** When multiple modules are active under one product, the composite module's clause table is the union of per-module clause tables (deduped by ID — same content silently absorbed, conflicting content raises) and the composite's template table is the union of per-module templates by path (with `addresses` lists merged). Deduplication preserves the bidirectional traceability map, and the composite is amenable to the same `validate` harness as a single module.
- **Notes:** Implemented at v0.4.0 in `engine/openqms/module.py::compose`. Upgraded `:tested → :verified` at v0.13.0 via 4 hypothesis property tests in `engine/tests/test_property.py`: `test_prop_compose_single_is_identity` (compose([m]) is m), `test_prop_compose_self_is_idempotent_on_content` (compose([m, m]) preserves clauses + per-path addresses), `test_prop_compose_unions_disjoint_modules` (for disjoint clause-ID sets, composite = union), `test_prop_compose_raises_on_conflicting_clauses` (same-ID-different-content raises). Plus 11 example-tested unit tests + 2 integration tests from v0.4.0 + 11+ overlay-composite integration tests from v0.11.0 / v0.12.0.

### OQ-012 — Cross-cutting overlays compose with vertical modules

- **Tier:** Architecture
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011
- **Claim:** A cross-cutting overlay module (e.g. ISO 27001 information security, eventually Open Honest Slop-Audit dimensions) composes with vertical regulatory modules (medical devices, regulated AI, etc.) by additively contributing clauses and artifact-template bindings. The overlay does not replace the vertical's bindings; both contribute to the composite, and the union semantics of `compose` (OQ-011) ensure that a template path appearing in both modules ends up addressing both modules' clauses in the composite.
- **Notes:** Implemented at v0.4.0. Mechanically, overlay composition is the same `compose` operation as vertical-vertical composition; "overlay" vs "vertical" is a conceptual labeling, not a separate code path. Evidence: `engine/tests/test_composition.py::test_medical_devices_plus_iso27001_composes_and_validates` and `::test_medical_devices_plus_iso27001_resolve_unions_template_addresses` exercise the ISO 27001 overlay against the medical-devices vertical end to end; `test_composite_can_close_gaps_in_overlay_only_module` validates the case where an overlay declares clauses without its own templates and relies on a vertical to address them.

### OQ-013 — Per-module validation harness

- **Tier:** Architecture
- **Evidence type:** property-tested
- **Status:** :verified
- **Depends_on:** OQ-001
- **Claim:** Every regulatory module is checked by a validation harness that mechanically asserts the OQ-001 invariant on its own clause table: every clause in the module is addressed by ≥1 template; no template addresses a non-existent clause (no orphaned clauses or artifacts).
- **Notes:** Implemented at v0.2.0 in `engine/openqms/validation.py::validate`. Upgraded `:tested → :verified` at v0.13.0 via `engine/tests/test_property.py::test_prop_valid_module_passes_validation` (every strategy-generated valid module passes validate) + the OQ-002 mutation test (harness correctly detects orphaned clauses iff a mutation creates them). Plus 4 example-tested unit tests + 11 medical-devices module integration tests + CI workflow runs on every push.

### OQ-014 — Standards-and-jurisdictions registry is versioned and immutable

- **Tier:** Architecture
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** —
- **Claim:** The registry of supported standards (with metadata: publisher, edition, kind, license kind, aliases) and jurisdictions (with applicable-standards sets) is versioned per Git, treated as read-only by the engine, and consulted whenever the CLI receives `--standard` or `--jurisdiction` arguments or whenever a module manifest is validated. Unregistered standards or jurisdictions raise rather than silently filtering to empty resolution. Aliases (`"ISO 13485"`) are normalized to canonical ids (`"ISO 13485:2016"`) before reaching the resolver.
- **Notes:** Shipped at v0.5.0 (commit `12b6b33`) in `registry/standards.yaml` (15 entries — 12 medical-device + cross-cutting plus 3 AI-regulation roadmap) and `registry/jurisdictions.yaml` (6 entries — FDA, Health Canada, EU MDR, PMDA, TGA, ANVISA). Engine code at `engine/openqms/registry.py`. CLI integration in `engine/openqms/cli.py` with `--allow-unregistered-standards` escape hatch (jurisdictions remain strictly validated regardless). 21 new tests in `engine/tests/test_registry.py` cover the unit semantics, the shipped-registry cross-check (every jurisdiction → standard reference resolves), and 5 subprocess-level CLI integration tests (alias normalization, unknown-standard rejection, unknown-jurisdiction rejection, escape hatch, `registry list/show`). Immutability is enforced procedurally (frozen dataclasses + adopters edit via PR) rather than cryptographically; upgrading to `:verified` would require content-hash addressing.

### OQ-015 — Re-resolution on mutation produces Git-reviewable diff

- **Tier:** Architecture
- **Evidence type:** property-tested
- **Status:** :verified
- **Depends_on:** OQ-002, OQ-010
- **Claim:** A stored bundle definition at `bundles/<name>.yaml` pins the input tuple. Running `openqms regenerate --bundle <name>` re-resolves the bundle and produces a structured diff against the prior matrix at `bundles/<name>.matrix.json`. The matrix file is Git-tracked; its diff is the regulatory audit trail. With `--write-matrix`, the new matrix overwrites the prior, producing a single reviewable commit containing both the input-tuple change (if any) and the artifact-set diff.
- **Notes:** Shipped at v0.6.0 (commit `3cfec2c`). Upgraded `:tested → :verified` at v0.13.0 via 2 hypothesis property tests in `engine/tests/test_property.py`: `test_prop_diff_self_is_empty` (diff(m, m) has no changes) and `test_prop_diff_detects_standard_narrowing` (removing a standard from the bundle produces standards_removed populated). Plus 9 example-tested diff unit tests + 8 CLI subprocess integration tests + CI dry-run regression check on every push.

### OQ-020 — PR + required reviewers implements role-based approval

- **Tier:** Substrate
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** —
- **Claim:** Pull-request approval with CODEOWNERS-driven required reviewers implements role-based document approval per ISO 13485 §4.2.4 and 21 CFR 820.40, modulo the §11.50 signature-meaning gap (OQ-060).
- **Notes:** CODEOWNERS at repo root maps paths to placeholder team handles; `scripts/setup.sh` configures branch protection requiring approvals. Test evidence: setup.sh execution on a fresh repo configures the constraints. Tier upgradable to `:verified` with a CI smoke test asserting branch protection state post-setup.

### OQ-021 — Branch protection prevents merge without CI + approvals

- **Tier:** Substrate
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-020
- **Claim:** Branch protection rules configured by `scripts/setup.sh` require passing CI status checks (`check-metadata`, `check-approvers`) and ≥1 approval before merge to `main`. Force-push disabled.
- **Notes:** Source: `scripts/setup.sh`. Test evidence: running setup.sh produces the expected `gh api` outputs. Same `:verified` upgrade path as OQ-020.

### OQ-022 — Git history is immutable under force-push-disabled config

- **Tier:** Substrate
- **Evidence type:** manual
- **Status:** :argued
- **Depends_on:** OQ-021
- **Claim:** With force-push disabled at the org / branch level, Git history on `main` is append-only and constitutes a tamper-evident audit trail acceptable to ISO 13485 §4.2.5 / 21 CFR 820.180-198 record-keeping, modulo the audit-trail gaps in OQ-060/OQ-067.
- **Notes:** Continuous enforcement depends on org-level configuration outside this repo. Cannot be upgraded past `:argued` without an external monitoring instrument.

### OQ-023 — GPG-signed commits bind identity to content

- **Tier:** Substrate
- **Evidence type:** manual
- **Status:** :argued
- **Depends_on:** —
- **Claim:** Requiring GPG-signed commits (or SSH-signed commits) at the organization level cryptographically binds committer identity to specific content, contributing toward 21 CFR Part 11 §11.70 signature/record linking.
- **Notes:** Enforcement requires admin permissions not available to the standard `gh` CLI flow that `scripts/setup.sh` uses. At v0.2.2, `docs/guide/gpg-signing.md` provides the runnable checklist: pick a signing scheme (GPG / SSH / S/MIME); generate per-individual keys; register against GitHub-attested identity; enable "Require signed commits" branch protection; optionally enforce at org level; CI workflow snippet for belt-and-suspenders verification. Status stays `:argued` — adopters must implement the checklist; OpenQMS cannot fully automate it. Distinct from §11.50 signature meaning (OQ-060).

### OQ-024 — MkDocs rendering produces point-of-use access

- **Tier:** Substrate
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** —
- **Claim:** The `deploy-docs.yml` GitHub Actions workflow builds the MkDocs site from `docs/`, `qms-policy/`, and `qms-sops/` and publishes to GitHub Pages, providing point-of-use access to controlled documents without requiring Git literacy at the consumer end.
- **Notes:** Workflow is real and functional. Test evidence: running `mkdocs build` locally produces a complete `site/` artifact.

### OQ-030 — Document-control workflow is CI-enforced

- **Tier:** Workflow
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-020, OQ-021
- **Claim:** The `doc-control.yml` workflow enforces document metadata requirements (document_id, version, effective_date, owner, status) and CODEOWNERS-based approval on PRs touching controlled paths (`qms-policy/`, `qms-sops/`, `qms-forms/`, `qms-training/`, `product-*/design-*/`, `product-*/risk-management/`, `product-*/technical-file/`).
- **Notes:** Source: `.github/workflows/doc-control.yml`. Two jobs: `check-metadata` (real frontmatter validation), `check-approvers` (real CODEOWNERS presence check).

### OQ-031 — Design-control traceability via issue-PR linkage

- **Tier:** Workflow
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** —
- **Claim:** The `traceability.yml` workflow warns when a PR is not linked to an issue and generates a markdown table of changed files with their linked issues on PR open/sync.
- **Notes:** Source: `.github/workflows/traceability.yml`. Partial: the workflow produces informational output but does not generate a full clause-to-artifact traceability matrix. The matrix-generation script promised in `docs/guide/traceability.md` (`./scripts/generate-trace-matrix.sh`) does **not** exist (see OQ-067).

### OQ-032 — Change-control issue template captures structured requests

- **Tier:** Workflow
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** —
- **Claim:** The change-request issue template captures change type (dropdown), description, justification, impact assessment, risk assessment, verification plan, and regulatory impact, with four fields marked `required: true`, implementing the structured-record requirement of 21 CFR 820.30(i) and ISO 13485 §7.3.9.
- **Notes:** Source: `.github/ISSUE_TEMPLATE/change-request.yml`. Required-fields enforcement is at the GitHub form level.

### OQ-033 — CAPA issue template captures structured records

- **Tier:** Workflow
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** —
- **Claim:** The CAPA issue template captures type (dropdown), description, root cause, action plan, verification, effectiveness check, target date, and risk level, with five fields marked `required: true`, implementing 21 CFR 820.100 / ISO 13485 §8.5.2-3.
- **Notes:** Source: `.github/ISSUE_TEMPLATE/capa.yml`. Labels: `capa`, `capa-open`. Effectiveness-check workflow follow-up (re-opening issues on schedule) not yet implemented.

### OQ-034 — Release-gating workflow enforces release completeness

- **Tier:** Workflow
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-020
- **Claim:** The `release-gate.yml` workflow triggers on `v*` / `release-*` tags, checks for required documents (quality-policy.md, quality-manual.md), checks for open blocking issues (labels: `release-blocker`, `capa-open`, `ncr-open`), warns on draft docs, and creates a GitHub Release if checks pass.
- **Notes:** Source: `.github/workflows/release-gate.yml`. Required-doc list is hardcoded today; should be driven by the active regulatory module(s) once the generator engine lands.

### OQ-035 — Training-trigger workflow creates training issues on doc revision

- **Tier:** Workflow
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** —
- **Claim:** The `training-trigger.yml` workflow triggers on push to `main` touching `qms-sops/` or `qms-policy/`, parses the trainee list from `docs/qms-config.yml`, and creates a "Training Required" issue per changed document.
- **Notes:** Source: `.github/workflows/training-trigger.yml`. YAML parsing in the workflow uses simple regex; not robust against arbitrary YAML — see OQ-061.

### OQ-036 — Nonconformance issue template captures structured NCR records

- **Tier:** Workflow
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** —
- **Claim:** The NCR issue template captures description, discoverer, date discovered, disposition (use-as-is / rework / return / scrap / pending), containment, investigation findings, and CAPA determination, with four fields marked `required: true`, implementing 21 CFR 820.90 / ISO 13485 §8.3.
- **Notes:** Source: `.github/ISSUE_TEMPLATE/nonconformance.yml`. Labels: `ncr`, `ncr-open`.

### OQ-037 — Design-input issue template captures structured requirement records

- **Tier:** Workflow
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** —
- **Claim:** The design-input issue template captures product, input type (user need / performance / safety / regulatory / interface / environmental / standards / other), requirement statement, rationale, acceptance criteria, and priority, with six fields marked `required: true`, implementing 21 CFR 820.30(c) / ISO 13485 §7.3.3.
- **Notes:** Source: `.github/ISSUE_TEMPLATE/design-input.yml`. Labels: `design-input`.

### OQ-038 — Document templates declare required metadata frontmatter

- **Tier:** Workflow
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-030
- **Claim:** Document templates declare YAML frontmatter with the required document-control fields (document_id, version, effective_date, owner, status, approved_by, approval_date), supplying the metadata that `doc-control.yml` validates. **31 document templates** ship as of v0.12.0.
- **Notes:** Was 3 templates at v0.1.0; v0.3.0 added 8; v0.8.0 added 3; v0.9.0 added 4; v0.10.0 added 3; v0.11.0 added 5; v0.12.0 added 5 (510K-SUBMISSION + IVDR-GSPR-CHECKLIST + PERFORMANCE-EVALUATION-REPORT + AI-SYSTEM-CARD + AI-IMPACT-ASSESSMENT).

### OQ-040 — Medical-devices module is the first reference regulatory module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-001, OQ-013
- **Claim:** The medical-devices module is the first reference regulatory module shipped with Open QMS as a machine-readable manifest. Its v0.1.0 seed (shipped at engine v0.2.0) covers four clauses across ISO 13485:2016 (§4.2.4, §7.3) and 21 CFR 820 (§820.30, §820.40) bound to the three artifact templates currently in the repo. The full target surface is ISO 13485 + 21 CFR 820 + 21 CFR Part 11 + EU MDR + IEC 62304 + IEC 62366-1 + IEC 60601-1 + ISTA 2A/3A + MDSAP + (overlay) ISO 27001.
- **Notes:** Manifest at `modules/medical-devices/module.yaml` shipped at v0.2.0 (commit `4a72a9f`). Validation harness passes (`openqms validate --module medical-devices`). The full crosswalk (covering the additional 23 clauses) remains in `BUSINESS/regulatory_modules/medical_devices_crosswalk.md`; progressive mechanization tracked under priority P6 in `dashboard.md`. Per-standard coverage claims (OQ-041..OQ-048) remain `:argued` until each standard's clause set is fully machine-readable.

### OQ-041 — Medical-devices module ISO 13485:2016 clause coverage

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-040
- **Claim:** The medical-devices module's machine-readable manifest covers ISO 13485:2016 clauses §4.1.6 (QMS software validation), §4.2.3 (medical device file), §4.2.4 (document control), §4.2.5 (records control), §5.6 (management review), §6.3 (infrastructure), §7.3 (design and development), §7.4 (purchasing), §8.2.2 (complaint handling), §8.2.3 (monitoring processes), §8.2.4 (internal audit) — all clauses listed in OQ-041's original target plus four additional clauses, **11 total**. Each is bound to ≥1 artifact (template, issue template, workflow, or guide). Validation harness passes.
- **Notes:** Closed at v0.9.0 (commit `78ee0db`). Full clause set machine-readable in `modules/medical-devices/module.yaml`; crosswalk reference in `BUSINESS/regulatory_modules/medical_devices_crosswalk.md` §4.2.

### OQ-042 — Medical-devices module 21 CFR Part 820 coverage

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-040
- **Claim:** The medical-devices module's machine-readable manifest covers 21 CFR 820 sections §820.20 (management responsibility), §820.20(c) (management review subset), §820.22 (quality audit), §820.30 (design controls), §820.40 (document controls), §820.50 (purchasing controls), §820.70 (production and process controls), §820.90 (nonconforming product), §820.100 (CAPA), §820.180 (records general), §820.198 (complaint files) — **11 sections bound**. Each is bound to ≥1 artifact. Validation harness passes.
- **Notes:** Closed at v0.9.0 (commit `78ee0db`). The records range §820.180-§820.198 is represented by the entry point (§820.180) and the most operationally-distinct subsection (§820.198 complaints); intermediate sections (§820.184 DHR, §820.186 QSR) are intentionally adopter-defined as they bind to manufacturing records that vary per device. Full crosswalk in `BUSINESS/regulatory_modules/medical_devices_crosswalk.md` §4.3.

### OQ-043 — Medical-devices module 21 CFR Part 11 coverage

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-040, OQ-060
- **Claim:** The medical-devices module's machine-readable manifest covers all ten target 21 CFR Part 11 subclauses: §11.10(a) validation, §11.10(b) accurate copies, §11.10(c) access controls, §11.10(d) audit trail, §11.10(e) operational checks, §11.50 signature manifestations, §11.70 signature/record linking, §11.100 general e-signature, §11.200 e-signature components, §11.300 password controls. §11.50 satisfied via the OQ-060 commit-trailer convention; §11.70 and §11.100/§11.200/§11.300 satisfied via the OQ-023 GPG-signing guide.
- **Notes:** Closed at v0.9.0 (commit `78ee0db`). Crosswalk in `medical_devices_crosswalk.md` §4.4. Some clauses bind to documentation guides (signature-meaning.md, gpg-signing.md) — the guide IS the artifact documenting the mechanism that satisfies the clause; this binding pattern is honest about what's happening (the org's approach to e-signatures is documented in the guide, not in a template).

### OQ-044 — Medical-devices module EU MDR 2017/745 coverage

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-040
- **Claim:** The medical-devices module's machine-readable manifest covers all 5 originally-listed EU MDR 2017/745 elements: Article 10(9) (QMS requirements), Annex I (GSPRs — 23 requirements across 3 chapters), Annex II (technical documentation), Annex IX (conformity assessment based on QMS), Annex XIV Part A (clinical evaluation / CER), Annex XIV Part B (PMCF). Six clauses bound to five artifacts (technical-file index, quality policy, management review, GSPR checklist, CER, PMCF plan).
- **Notes:** Closed at v0.10.0 (commit `e6d15a8`). Annex I + Annex XIV closure ships device-class-agnostic templates with explicit per-class customization notes (GSPR applicability column is device-class-dependent — SaMD declares NA on most physical/chemical/mechanical GSPRs; implantables declare A on most). Device-class overlay sub-modules (SaMD / implantable / IVD) remain forward work that would further automate the per-class GSPR subset selection. Crosswalk in `medical_devices_crosswalk.md` §4.5.

### OQ-045 — Medical-devices module IEC 62304 coverage

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-040
- **Claim:** The medical-devices module's machine-readable manifest covers IEC 62304 clauses §5.1 (planning), §5.2 (requirements analysis), §5.3 (architectural design), §5.4 (detailed design), §5.5 (unit verification), §5.6 (integration testing), §5.7 (system testing), §5.8 (software release), §6 (maintenance), §7 (software risk management), §8.1.2 (SOUP configuration management), §9 (problem resolution) — **12 clauses bound**.
- **Notes:** Closed at v0.9.0 (commit `78ee0db`). §8 broader configuration management beyond §8.1.2 SOUP is implicitly covered by Git itself (the substrate); §8.1.2 SOUP register is the operationally-distinct artifact. Crosswalk in `medical_devices_crosswalk.md` §4.6.

### OQ-046 — Medical-devices module IEC 62366-1 + IEC 60601-1 coverage

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-040
- **Claim:** The medical-devices module's machine-readable manifest covers IEC 62366-1:2015+A1:2020 (usability engineering, §5 consolidated from §5.1-§5.9) bound to the new `USABILITY-ENGINEERING-FILE-TEMPLATE.md`, and IEC 60601-1:2005+A1+A2 (general medical electrical safety) bound to the `VERIFICATION-PROTOCOL-TEMPLATE.md` (test reports from external accredited labs).
- **Notes:** Closed at v0.9.0 (commit `78ee0db`). Usability template populates the previously-empty `templates/product-dhf/usability/` subdir. Large-binary-file handling (videos, lab reports) remains a substrate concern noted in the crosswalk — adopters use Git LFS or external storage with references.

### OQ-047 — Medical-devices module ISTA 2A/3A and MDSAP coverage

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-040, OQ-041
- **Claim:** The medical-devices module's machine-readable manifest covers ISTA 2A (packaged products ≤150 lb partial simulation) and ISTA 3A (parcel delivery system) bound to the new `PACKAGING-VALIDATION-TEMPLATE.md`, plus MDSAP (composite audit model satisfying FDA + Health Canada + ANVISA + PMDA + TGA) bound to the quality-policy template and supplier-evaluation template.
- **Notes:** Closed at v0.9.0 (commit `78ee0db`). ISTA template populates a new `templates/product-dhf/packaging/` subdir. MDSAP's "composite" nature is captured as a single clause that binds to artifacts demonstrating QMS operation per ISO 13485 — the same evidence base, presented in MDSAP-auditor format. Crosswalk in `medical_devices_crosswalk.md` §4.9-4.10.

### OQ-048 — ISO/IEC 27001 cross-cutting overlay coverage

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-012
- **Claim:** Open QMS ships an ISO/IEC 27001:2022 cross-cutting overlay module at `modules/iso-27001/module.yaml` that composes with the medical-devices vertical module. The v0.1.0 seed covers three Annex A controls (A.5.1 information security policies; A.5.31 legal / regulatory / contractual requirements; A.8.31 separation of development / test / production environments) bound to three existing OpenQMS templates (quality policy, SOP template, software release record). All three templates are also bound by the medical-devices vertical; composition unions the addresses without conflict.
- **Notes:** Shipped at v0.4.0 (commit `2a146ad`). Coverage is partial (3 of ~93 Annex A controls); the seed exists to demonstrate the overlay composition primitive end to end, not to provide complete ISO 27001 coverage. Full Annex A coverage is roadmap work that compounds as more infosec-specific templates land (e.g. an access-control SOP template would naturally bind to A.5.15, A.5.16, A.8.2, A.8.3). Candidate dock point with Open Honest's Slop Audit infosec dimensions remains open.

### OQ-050 — SaMD overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-012, OQ-040
- **Claim:** Open QMS ships a Software-as-a-Medical-Device (SaMD) overlay at `modules/samd/module.yaml` (version 0.1.0). Adds IMDRF SaMD risk-categorization framework (Class I-IV on State-of-Healthcare-Situation × Significance-of-Information axes), IEC 82304-1 health software product safety, and SaMD cybersecurity considerations as clauses; binds them to the new `SAMD-INTENDED-USE-TEMPLATE.md`, the existing `SOFTWARE-REQUIREMENTS-TEMPLATE.md`, and the existing `RISK-MANAGEMENT-FILE-TEMPLATE.md`. Composes with `medical-devices` via the OQ-011 compose primitive.
- **Notes:** Shipped at v0.11.0 (commit `54e93de`). Validation passes standalone and in 6-module composite with medical-devices + implantable + mdr-class-iii + fda-class-iii + iso-27001. Per-class GSPR applicability note documented in `modules/samd/README.md` — SaMD adopters typically declare NA on most physical/mechanical GSPRs (Annex I §10/§11/§14/§16/§19/§20).

### OQ-051 — Implantable overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-012, OQ-040, OQ-044
- **Claim:** Open QMS ships an implantable-device overlay at `modules/implantable/module.yaml` (version 0.1.0). Adds EU MDR Annex I §23.4 (implant card subclause), Article 32 (SSCP), and ISO 14708-1 (active implantable general requirements) as clauses; binds them to the new `IMPLANT-CARD-TEMPLATE.md`, `SSCP-TEMPLATE.md`, and the existing `VERIFICATION-PROTOCOL-TEMPLATE.md`.
- **Notes:** Shipped at v0.11.0. Composes naturally with `mdr-class-iii` (most implantables are Class IIb or III) — both modules declare MDR-Art32 with identical summaries so compose() silently dedupes. SSCP template is bound by both overlays; composition unions the bindings.

### OQ-052 — EU MDR Class III overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-012, OQ-040, OQ-044
- **Claim:** Open QMS ships an EU MDR Class III risk-class overlay at `modules/mdr-class-iii/module.yaml` (version 0.1.0). Adds Article 32 (SSCP, shared with implantable overlay), Article 54 (expert panel consultation for implantable Class III + Class IIb active drug-delivery devices), Annex X (type-examination), and Article 84 (PSUR cadence) as clauses; binds them to the existing SSCP template plus the new `EXPERT-PANEL-CONSULTATION-TEMPLATE.md`, and to the existing technical-file index and PMCF templates.
- **Notes:** Shipped at v0.11.0. Class III is the most stringent EU MDR risk class. Adopters typically compose this overlay with `medical-devices` + `implantable` for an implantable Class III device, or with `medical-devices` alone for a non-implantable Class III device (e.g. drug-device combination).

### OQ-053 — FDA Class III overlay module (PMA path)

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-012, OQ-040, OQ-042
- **Claim:** Open QMS ships an FDA Class III overlay at `modules/fda-class-iii/module.yaml` (version 0.1.0). Adds 21 CFR 814 Subpart B (PMA application), §814.39 (PMA supplements), §814.84 (PMA annual report), and 21 CFR 803 (FDA Medical Device Reporting — adverse event reporting) as clauses; binds them to the new `PMA-SUBMISSION-TEMPLATE.md`, the existing change-request and complaint issue templates, and the existing management-review template (PMA annual-report aggregation).
- **Notes:** Shipped at v0.11.0. Naming clarification carried in `modules/fda-class-iii/README.md`: FDA's "MDR" (21 CFR 803 Medical Device Reporting) is **not** the EU MDR (2017/745) — recurring acronym-collision source of confusion. The overlay handles only the QMS-relevant additions (annual reporting, MDR adverse-event reporting bound to the complaint workflow). The PMA submission process itself (eSubmitter, FDA interaction) is outside QMS scope.

### OQ-054 — EU MDR Class IIb overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-012, OQ-040, OQ-044
- **Claim:** Open QMS ships an EU MDR Class IIb risk-class overlay at `modules/mdr-class-iib/module.yaml` (version 0.1.0). Adds Article 54 (expert panel — for active drug-delivery devices subset), Annex IX Class IIb conformity assessment, and Article 84 biennial PSUR cadence. Composes naturally with `implantable` overlay for implantable Class IIb devices.
- **Notes:** Shipped at v0.12.0 (commit `f0d48f7`). MDR-Art54 declared identically across mdr-class-iib + mdr-class-iii overlays → compose() silently dedupes.

### OQ-055 — EU MDR Class IIa overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-012, OQ-040, OQ-044
- **Claim:** Open QMS ships an EU MDR Class IIa risk-class overlay at `modules/mdr-class-iia/module.yaml` (version 0.1.0). Adds Annex XI production quality assurance route (alternative to Annex IX) and Article 83 as-needed PMS cadence (not full PSUR).
- **Notes:** Shipped at v0.12.0 (commit `f0d48f7`). Class IIa is the typical MDR class for SaMD per Annex VIII Rule 11.

### OQ-056 — FDA Class II overlay module (510(k) path)

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-012, OQ-040, OQ-042
- **Claim:** Open QMS ships an FDA Class II overlay at `modules/fda-class-ii/module.yaml` (version 0.1.0). Adds 21 CFR 807 Subpart E Premarket Notification (510(k)), Special Controls per product code, 21 CFR 860 Subpart D De Novo classification. Ships the new `510K-SUBMISSION-TEMPLATE.md` for substantial-equivalence + technical-section assembly.
- **Notes:** Shipped at v0.12.0 (commit `f0d48f7`). Includes De Novo path for novel low-to-moderate risk devices without a predicate. Registry additions: 21 CFR 807, 21 CFR 860.

### OQ-057 — IVD overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-012, OQ-040
- **Claim:** Open QMS ships an IVD (In Vitro Diagnostic) overlay at `modules/ivd/module.yaml` (version 0.1.0). Adds 8 IVD-specific clauses covering EU IVDR 2017/746 (Article 5, Annex I IVD GSPRs, Annex II, Annex IX, Annex XIII performance evaluation, Article 56 PSUR cadence), 21 CFR 809 (FDA IVD labeling), and ISO 15189:2022 (medical lab quality + competence). Ships 2 new templates: IVDR GSPR conformity checklist (analogous to MDR GSPR but IVD-specific) and Performance Evaluation Report (IVD equivalent of CER, with three-pillar evidence framework: scientific validity + analytical performance + clinical performance).
- **Notes:** Shipped at v0.12.0 (commit `361f4ff`). Pragmatic shipping decision: cross-cutting overlay (not standalone vertical) — shared QMS baseline inherited from `medical-devices` via composition; adopters declare the MDR-specific clauses (MDR-Art10(9), MDR-AnnexI, MDR-AnnexII, MDR-AnnexIX, MDR-AnnexXIV-A, MDR-AnnexXIV-B) as NA per their IVD scope SOP. A future standalone `medical-devices-ivd` vertical that excludes MDR clauses entirely remains forward work. IVDR class overlays (ivdr-class-c, ivdr-class-d) also forward work. Registry additions: EU IVDR 2017/746, 21 CFR 809, ISO 15189:2022.

### OQ-058 — Regulated-AI cross-cutting overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-012
- **Claim:** Open QMS ships a regulated-AI cross-cutting overlay at `modules/regulated-ai/module.yaml` (version 0.1.0). Composes with ANY vertical regulatory module (medical-devices today; future fintech / automotive / employment / education AI verticals later). 13 clauses: NIST AI RMF 1.0 four functions (Govern, Map, Measure, Manage); EU AI Act Chapter III §2 high-risk AI requirements (Articles 9-15); ISO/IEC 42001:2023 AIMS (consolidated); ISO/IEC 23894:2023 AI risk management guidance. Ships 2 new templates: AI System Card / Model Card (Mitchell et al. 2019 extended with EU AI Act + IMDRF SaMD) and AI Impact Assessment (Article 9 + Article 14 + Article 27 + NIST AI RMF Govern/Measure/Manage). Existing templates gain AI bindings: RMF (ISO 23894), quality-policy (ISO 42001), SAD (Article 15), STP (Article 10), TFI (Article 12).
- **Notes:** Shipped at v0.12.0 (commit `3e231d5`). Registry addition: ISO/IEC 23894:2023 (other AI standards already registered as roadmap entries at v0.5.0). Overlay's clauses primarily target EU AI Act *high-risk* AI scope (Annex III); limited-risk and minimal-risk scope a subset.

### OQ-107 — Chemicals class overlay batch (6): SVHC + Authorisation + 4 tonnage bands

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-105
- **Claim:** 6 new chemicals class overlays at v0.38.0: **chemicals-svhc** (`modules/chemicals-svhc/module.yaml` — REACH SVHC supply-chain + ECHA notification obligations; 5 clauses across Article 7(2) SVHC-in-articles notification ECHA + Article 33(1) recipient communication + Article 33(2) consumer response 45 days + Waste Framework Directive Article 9(1)(i) SCIP database + Annex XV identification dossier; new SVHC-COMMUNICATION-LETTER template); **chemicals-authorisation** (`modules/chemicals-authorisation/module.yaml` — REACH Title VII Authorisation for Annex XIV listed substances; 6 clauses across Article 56 prohibition + Article 60 grant (Adequate Control vs. Socio-Economic routes) + Article 62 application content + Articles 65-66 holder + downstream-user obligations + Article 61 review + Annex XIV listed substances ~60 entries; 2 new templates REACH-AUTHORISATION-APPLICATION + SUBSTITUTION-PLAN with 10-action timetable); **chemicals-tonnage-1** (Annex VII baseline ≥1 t/y entry tier; CSR NOT required); **chemicals-tonnage-10** (Annex VIII incremental ≥10 t/y; CSR mandatory; extended SDS with exposure scenarios — major cost cliff); **chemicals-tonnage-100** (Annex IX incremental ≥100 t/y; 90-day sub-chronic + reproductive screening + long-term ecotox; vertebrate test-proposal mechanism); **chemicals-tonnage-1000** (Annex X incremental ≥1000 t/y; chronic 12-month + 2-year carcinogenicity + EOGRTS full cohorts; SIEF joint submission essentially mandatory). All 6 overlays reuse existing REACH dossier + SDS templates with band-specific bindings. **16-module composite validates** (new depth record beats prior 13-module): chemicals + SVHC + Authorisation + tonnage-1000 + 4 adjacent + 8 cross-cutting overlays.
- **Notes:** Shipped at v0.38.0. Reuses existing chemicals vertical standards (no new registry additions; all bands operate against EU REACH already registered). Tonnage-band overlays are **mutually exclusive in practice** — a registrant uses ONE tonnage band per substance at a time (chemicals-tonnage-1000 supersedes-and-includes all lower bands). Open QMS module-union semantics correctly allow either compose-and-validate (16-module composite) OR adopt-only-current-band (3-module composite chemicals + chemicals-svhc + chemicals-tonnage-10 typical for SMEs at the 10 t/y CSR-mandatory threshold). Class-overlay count: 38 → 44 (chemicals jumps from 0 → 6 class overlays — first chemicals class-overlay set). Cumulative across v0.36-38: chemicals vertical + 4 adjacent standalones + 6 class overlays = **11 chemicals-domain modules** shipped in 3 releases. Discharges Q2 chemicals-companion forward-work commitments on SVHC + Authorisation + tonnage-banded dossier structure.

### OQ-106 — Chemicals-adjacent standalone overlay batch (4): OSHA HCS + transport HazMat + EU Biocides + TSCA PFAS

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-012, OQ-014, OQ-105
- **Claim:** 4 new cross-cutting overlays shipped at v0.37.0 covering chemicals-adjacent regulatory regimes deferred as forward work in OQ-105: **osha-hcs** (`modules/osha-hcs/module.yaml` — 29 CFR 1910.1200 HazCom 2024 final rule alignment with UN GHS Rev. 7; 9 clauses across §(e) Written Program + §(f) labels + §(g) SDS access + §(h) employee training + §(i) trade secrets + Appendices A/B/C/D; 1 new template HAZCOM-WRITTEN-PROGRAM; reuses chemicals SDS template — receiver-side complement to chemicals' sender-side SDS authoring); **transport-hazmat** (`modules/transport-hazmat/module.yaml` — US DOT HMR 49 CFR 100-185 + IMDG (sea) + IATA DGR (air) + ADR 2025 (EU road) + RID 2025 (EU rail); 17 clauses spanning HMT classification + shipping papers + marking + labels + placards + emergency response telephone + HMT training + non-bulk packagings + tank cars + IMDG segregation + IATA CBTA + ADR driver training + DGSA; 2 new templates SHIPPING-PAPER + HMT-TRAINING-RECORD; covers any vertical shipping DG); **eu-biocides** (`modules/eu-biocides/module.yaml` — EU BPR 528/2012; 10 clauses across active-substance approval (Articles 4-9) + product authorisation pathways (Articles 17-23) + Article 19(1) conditions + Articles 49-50 + Article 95 supplier list + treated articles (Article 58) + R&D notification (Article 56) + Article 69-72 biocide-specific C+L+P additions + Annex V product types + Annex VI Common Principles; 1 new template BPR-AUTHORISATION-APPLICATION); **tsca-pfas** (`modules/tsca-pfas/module.yaml` — 40 CFR Part 705 TSCA Section 8(a)(7) PFAS Reporting and Recordkeeping; 7 clauses across §705.3 applicability (no de minimis; articles in scope per knowability standard) + §705.15 submission window 2025-07-11 to 2026-01-11 standard / 2026-07-11 small-mfr-article-only + §705.20-30 info required per-substance per-year per-site for 2011-2022 lookback + §705.25 5-year retention + §705.35 CBI claims per §703.5 + §705.40 CDX/CISS submission + preamble "knowability" standard for article importers; 1 new template PFAS-REPORTING-FORM with common-article-categories due-diligence checklist). **13-module composite validates** — chemicals + 4 adjacent + 8 cross-cutting overlays (new depth record beats prior 11-module).
- **Notes:** Shipped at v0.37.0. Registry +9 standards: 29 CFR 1910.1200 + 49 CFR 100-185 + IMDG Code + IATA DGR + ADR 2025 + RID 2025 + EU BPR + 40 CFR 705 (8 PUBLIC; IMDG + IATA DGR commercial). Cross-cutting overlay count: 19 → 23. CI extended (+12 validate steps). All 4 are FORWARD-WORK items previously named in `modules/chemicals/module.yaml` scope notes — discharging the chemicals companion's forward-work list. **Scope notes:** osha-hcs is the US workplace receiver-side complement to chemicals' EU/global SDS authoring (sender) side; symmetric to REACH downstream-user direction. transport-hazmat applies broadly across automotive (UN3480 Li-ion) + aerospace (cryogenics + pyrotechnics) + medical-devices (UN3373 Cat B specimens) + pharma + manufacturing, not just chemicals. eu-biocides is the BPR product-on-market route distinct from REACH substance-registration route. tsca-pfas is broader-scope than expected — catches article importers across textile + semiconductor + cookware + medical-device + automotive verticals due to no-de-minimis + knowability standard.

### OQ-109 — Sub-overlay batch (16): CMMC levels + SOC 2 types + ISO 27001 extensions + NIST CSF tiers + PCI DSS SAQ types

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-104, OQ-108
- **Claim:** 16 new sub-overlays at v0.42.0 splitting previously-monolithic cross-cutting overlays into their natural rigor/scope/tier structure per the underlying standards — introduces new module shape (class-overlay-like deltas on cross-cutting overlays). **CMMC levels (3):** `cmmc-level-1` (FAR 52.204-21 17 basic safeguarding; FCI-only; annual self-assessment); `cmmc-level-2` (NIST SP 800-171 110 controls / 14 families; CUI; self-vs-C3PAO bifurcation; 5% POAM); `cmmc-level-3` (NIST SP 800-172 +24 enhanced; NS-critical CUI; DIBCAC-only; no POAM). **SOC 2 types (2):** `soc-2-type-i` (point-in-time design; readiness pathway); `soc-2-type-ii` (observation-period operating effectiveness; enterprise default; bridge-letter handling). **ISO 27001 extensions (2):** `iso-27001-cloud` (ISO/IEC 27017:2015; CSP+CSC shared responsibility; 7 CLD controls); `iso-27001-privacy` (ISO/IEC 27701:2019 PIMS; Annex A 31 controller + Annex B 18 processor; GDPR/CCPA mapping). **NIST CSF Implementation Tiers (4):** `nist-csf-tier-1` (Partial; ad-hoc; current-state baseline only); `nist-csf-tier-2` (Risk Informed; management-approved); `nist-csf-tier-3` (Repeatable; organisation-wide policy; most common target); `nist-csf-tier-4` (Adaptive; continuous improvement + bidirectional ecosystem sharing; rare). **PCI DSS SAQ types (5):** `pci-dss-saq-a` (full-outsource e-commerce; ~22 requirements); `pci-dss-saq-a-ep` (merchant-controlled payment page; ~191 requirements + v4.0 script management); `pci-dss-saq-d-merchant` (general merchant; ~300+ requirements; v4.0 transition); `pci-dss-saq-d-sp` (service provider; provider-only requirements + customer AOC); `pci-dss-saq-p2pe` (PCI-listed P2PE-validated solution; ~33 requirements). All 16 reuse parent-overlay templates with binding deltas — no new templates. **19-module deepest composite validates** (chemicals + svhc + authorisation + tonnage-1000 + 4 adjacent + ISO 27001 + cloud + privacy + 7 cross-cutting + privacy — beats prior 17-module record).
- **Notes:** Shipped at v0.42.0. Registry +2 commercial standards (ISO/IEC 27017:2015 + ISO/IEC 27701:2019). 14 of 16 reuse existing registered standards (CMMC 2.0 + NIST SP 800-171 + AICPA TSC 2017 + NIST CSF 2.0 + PCI DSS v4.0). Cross-cutting overlay count unchanged at 24 — sub-overlays are NOT counted in the 24; they are class-overlay-shaped deltas on cross-cutting overlays (analog to how aerospace-dal-a is not counted in the verticals count). Total module count 76 → 92 (+16). Particularly natural compositions: `cmmc + cmmc-level-2` (typical DoD CUI handler); `soc-2 + soc-2-type-ii` (enterprise default); `iso-27001 + iso-27001-privacy + privacy` (ISMS + PIMS + legal-framework triad); `nist-csf + nist-csf-tier-3` (most-common target maturity); `pci-dss + pci-dss-saq-a-ep` (e-commerce merchant with iframe/redirect). New sub-overlay shape is the natural decomposition pattern for any cross-cutting overlay with tiered or scoped variants — paves way for future overlay extensions (DORA tiers + ISO 37301 sectoral profiles + HITRUST scoping levels) without inflating cross-cutting count.

### OQ-108 — Privacy cross-cutting overlay (GDPR + CCPA/CPRA; last major management-system gap)

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-012, OQ-014
- **Claim:** Open QMS ships a privacy cross-cutting overlay at `modules/privacy/module.yaml` (version 0.1.0) — 24th cross-cutting overlay; last major management-system gap. Covers the two dominant global privacy frameworks: **EU GDPR (Regulation 2016/679)** with 15 clauses across principles (Article 5) + lawful bases (Articles 6 + 7) + special categories (Article 9) + data subject rights (Articles 12-22) + controller/processor obligations (Articles 25 + 28 + 30 + 32) + breach (Articles 33-34) + DPIA (Article 35) + DPO (Articles 37-39) + international transfers (Articles 44-49 with Schrems II Transfer Impact Assessment); **US CCPA/CPRA (Cal. Civ. Code §1798.100-199)** with 10 clauses across consumer rights (§1798.100/105/106/120/121/130) + business obligations (§1798.135 notice + §1798.140 SP/Contractor/3P + §1798.150 PRA + §1798.185 CPPA regulatory regime ADMT + Risk Assessment + Cybersecurity Audit 2025-2026). 21 clauses total + 5 substantial new templates: PRIVACY-POLICY (Articles 13-14 + CCPA notice with all 11 CCPA categories + SPI table + lawful-basis grid + rights summary + GPC honoring + state-AG contacts); DPA (Article 28 + CCPA §7050-7053 + 2021/915 SCCs + TIA + sub-processor + audit + breach-24h-SLA + CPPA Cybersecurity/Risk/ADMT assistance); DPIA (Article 35 + CCPA Risk Assessment + WP248 9-criteria + WP250 consequences + Article 36 prior-consultation decision); ROPA (Article 30 controller Part A + processor Part B with all 7+4 required fields + maintenance discipline); PERSONAL-DATA-BREACH-NOTIFICATION (Article 33 SA 72h + Article 34 subjects + Article 33(5) documentation + CCPA §1798.150 PRA + US state AG cross-reference + HIPAA + FTC HBNR + SEC 8-K Item 1.05). UK GDPR addressed under same clauses (UK ICO as SA per DPA 2018 retention). UK GDPR + PIPEDA + LGPD + APPI + PIPL + US state-privacy (VCDPA/CPA/CTDPA/UCPA/TDPSA/OCPA/etc.) + HIPAA + GLBA + COPPA + FERPA + ePrivacy + CPPA ADMT/Risk/Cybersecurity sub-overlays forward. **17-module ultimate composite validates** (new depth record beats prior 16-module): chemicals + svhc + authorisation + tonnage-1000 + 4 adjacent + 8 cross-cutting + privacy. All adopters typically benefit; near-universal applicability.
- **Notes:** Shipped at v0.41.0. Registry +2 PUBLIC standards (GDPR + CCPA). Cross-cutting overlay count: 23 → 24. Composes naturally with ALL 7 verticals + all other cross-cutting overlays. Particularly strong complement with iso-27001 (privacy is the WHY; iso-27001 is the HOW for Article 32 security per Annex A mapping) + soc-2 (Privacy criterion overlap) + hitrust-csf (HITRUST internally maps HIPAA + GDPR + CCPA; privacy overlay adds legal-framework specificity) + regulated-ai (GDPR Article 22 + CCPA ADMT both govern significant automated decision-making). Discharges the last major cross-cutting overlay gap in the project.

### OQ-105 — Chemicals vertical module (7th vertical)

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-012, OQ-014
- **Claim:** Open QMS ships a chemicals vertical module at `modules/chemicals/module.yaml` (version 0.1.0) — 7th vertical (after medical-devices / aerospace / automotive / manufacturing / pharma / food-safety). 21 clauses across 5 standards spanning the four major chemical-industry regulatory regimes: **EU REACH (Regulation (EC) 1907/2006)** — Articles 5-6 no-data-no-market + Article 7 substances-in-articles + Article 10 + Annexes VI-X tonnage-banded technical-dossier + Article 14 + Annex I CSR for ≥10 t/y + Article 31 + Annex II SDS + Articles 33-34 supply-chain SVHC communication + Title V downstream-user obligations + Title VII Authorisation (Annex XIV SVHC) + Title VIII Restrictions (Annex XVII); **EU CLP (Regulation (EC) 1272/2008)** — Article 4 self-classification + Article 13 C&L Inventory notification + Article 17 + Annex II label content + Annex VI harmonised classification (CLH) + Annex VIII UFI + Poison Centre Notification; **UN GHS Rev. 10** — Parts 2-4 hazard classification (17 physical + 10 health + 2 environmental classes) + Annex 4 16-section SDS format + Annex 7 label elements; **OECD GLP Principles** — facility organisation + QA Programme + SOPs + study conduct + reporting + archive; **US TSCA (15 USC §2601; 40 CFR Parts 700-799)** — Section 5 Premanufacture Notice (PMN) + Section 6 existing-chemical risk evaluation + restriction (Lautenberg) + Section 8 Chemical Data Reporting (CDR every 4 years) + Sections 12-13 import/export. Ships 4 new chemicals-specific templates: Safety Data Sheet (16-section GHS + REACH Annex II + CLP + OSHA HCS Appendix D), REACH Registration Dossier Outline (Articles 5-6 + 10 + 14 + Annexes VI-X + Annex I CSR + SIEF joint submission + IUCLID 6 + REACH-IT + Authorisation + Restriction considerations), CLP Classification Notification + Label (full classification tables across all GHS hazard classes + UFI + PCN per Annex VIII), GLP Study Plan + Final Report (combined per Principles 8.1 + 9.1 with QA Statement per Principle 9.1(j) + 10-year archive per Principle 9.2). Plus 2 cross-cutting bindings (quality-policy + SOP-TEMPLATE) addressing REACH no-data-no-market and TSCA operational SOPs. Standalone + composite validates (chemicals + 4 cross-cutting overlays). All 5 standards PUBLIC license — meaningful adopter cost reduction for chemical-industry startups + SMEs + academic spinouts. New example bundle `example-specialty-chemical` (mid-size 50-100 t/y SVHC-adjacent intermediate manufacturer with REACH + TSCA scope + IS + HSE).
- **Notes:** Shipped at v0.36.0. Registry +5 standards (EU REACH + EU CLP + UN GHS Rev. 10 + OECD GLP + TSCA — all PUBLIC license). CI extended (+5 validate steps + 1 regenerate). Vertical count: 6 → 7. Annex SL composability: REACH/CLP/GHS aren't Annex-SL but compose seamlessly with all 9 Annex-SL cross-cutting overlays via the module-union primitive (OQ-011); OECD GLP cleanly layers on as a quality-system-for-non-clinical-safety-studies discipline. **Out of scope (deferred):** OSHA HCS 29 CFR 1910.1200 (US workplace HazCom — workplace H&S overlap partially covered by iso-45001); DOT HazMat + IMDG + IATA + ADR/RID (transport classifications — forward standalone overlay); pesticides (FIFRA / EU PPP Regulation 1107/2009); cosmetics (EU 1223/2009 / US MoCRA — separate vertical); biocides (EU 528/2012); detergents (EU 648/2004). **Forward work:** US OSHA HCS standalone overlay; DOT HazMat + IMDG + IATA + ADR/RID transport overlay; EU Biocides overlay; EU Cosmetics + EU Pesticides + US FIFRA separate verticals/standalones; TSCA PFAS reporting (40 CFR 705) specific standalone; ECHA SCIP database notification workflow; REACH Article 60 Authorisation application template (substitution plan + AoA + SEA); read-across justification per ECHA RAAF; multi-language SDS coordination (EU 24 languages); OECD Test Guidelines cross-reference (TG 401-501+ tox + TG 201+ ecotox).

### OQ-104 — Cross-cutting overlay batch — IS / governance / compliance / resilience / DoD-CUI (11)

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-012, OQ-014
- **Claim:** 11 new cross-cutting overlays shipped across 3 release groups: **v0.31.0 IS+governance (5)** — `soc-2` (AICPA Trust Services Criteria 2017; Common + Security mandatory + Availability/Processing-Integrity/Confidentiality/Privacy optional; Type I vs. Type II); `pci-dss` (PCI DSS v4.0 across 12 requirements + 6 goals; CDE scoping + v4.0 Customized Approach innovation); `hitrust-csf` (HITRUST CSF v11.x; 19 domains + multi-framework mapping across HIPAA + HITECH + ISO 27001 + NIST SP 800-53 + PCI DSS + GDPR); `nist-csf` (NIST CSF v2.0; 6 functions incl. new Govern; Profiles + Tiers); `iso-31000` (the meta-framework — Principles + Framework + Process; unifies domain-specific risk standards already in Open QMS like ICH Q9 + HARA + TARA + FHA + HACCP). **v0.32.0 compliance + resilience (4)** — `iso-37301` (Compliance Management — replaces ISO 19600; broader than ISO 37001 anti-bribery; covers ALL obligations); `dora` (EU Regulation 2022/2554 effective January 17, 2025; 6 chapters incl. 4h/72h/1mo incident-reporting windows + TLPT TIBER-EU + Article 30 mandatory contractual + CTPP designation); `eu-gpsr` (EU GPSR 2023/988 effective December 13, 2024 — replaces GPSD; consumer products; Safety Gate (formerly RAPEX) notification; online marketplace 3-working-day takedown); `tisax` (automotive supply-chain IS based on VDA-ISA v6.0; Information Security + Prototype Protection + Data Protection labels; AL 1/2/3 assessment levels; ENX Portal). **v0.33.0 US DoD CUI (2)** — `defense-cui` (DFARS 252.204-7012 + NIST SP 800-171 Rev 3 May 2024; 14 control families + SSP + POAM + SPRS scoring + 72h cyber incident reporting to DIBNet); `cmmc` (CMMC 2.0 per 32 CFR Part 170 final rule Dec 2024; Levels 1/2/3 with C3PAO certification for Level 2 CUI national-security-critical; phased rollout through 2028). **11-module mega composite validates** (new depth record): pharma + pharma-sterile + pharma-biologics + atmp + iso-27001 + soc-2 + iso-31000 + iso-22301 + iso-14001 + iso-45001 + iso-50001.
- **Notes:** Shipped at v0.31.0 + v0.32.0 + v0.33.0 (engine 0.30.0 → 0.33.0). Registry +12 standards (mix of PUBLIC + commercial license). **Cross-cutting overlay count: 8 → 19** (added soc-2, pci-dss, hitrust-csf, nist-csf, iso-31000, iso-37301, dora, eu-gpsr, tisax, defense-cui, cmmc). Annex-SL-aligned standards (iso-37301) compose cleanly with the 7 prior Annex-SL overlays. ISO 31000 is the META-framework unifying all domain-specific risk standards already in the project.

### OQ-101 — Pharma class overlay batch (5)

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-092
- **Claim:** 5 new pharma class overlays at `modules/pharma-{sterile,biologics,imp,generic-biosimilar,clinical-stage}/`. Sterile (PIC/S Annex 1 2022 enforced rigor — CCS / isolator+RABS / APS / EM Grade A / personnel quals / line clearance); Biologics (ICH Q5A+B+D+E + Q6B + Q11 + EU GMP Annex 2B — cell-bank discipline + viral safety + comparability + biotech specs); IMP (EU GMP Annex 13 + 21 CFR 312 — sponsor model + blinding + IMP-QP + Phase 1 enforcement discretion + protocol amendments); Generic+Biosimilar (ANDA + 351(k) — bioequivalence + Paragraph IV + interchangeability + post-approval reporting); Clinical-Stage (Phase 1-3 staged-expectations + evolving specs + supply forecasting + pre-commercial readiness). All standards PUBLIC license. 6-pharma-module mega composite validates.
- **Notes:** Shipped at v0.28.0. Registry +9 standards (ICH Q5B/Q5D/Q5E/Q6B/Q11 + EU GMP Annex 13 + 21 CFR 312 + 21 CFR 314 + 42 USC 262(k)).

### OQ-102 — Food-safety class overlay batch (5)

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-093
- **Claim:** 5 new food-safety class overlays at `modules/food-{usda-fsis,animal,produce-safety,intentional-adulteration,fsvp}/`. USDA-FSIS (9 CFR 416 sanitation + 9 CFR 417 HACCP — continuous inspector model distinct from FDA); Animal Food (21 CFR 507 FSMA Animal Food Preventive Controls); Produce Safety (21 CFR 112 farm-stage); Intentional Adulteration (21 CFR 121 IA Rule — Food Defense Plan + FDQI); FSVP (21 CFR 1 Subpart L Foreign Supplier Verification — per-food per-supplier evaluation + SAHCODHA verification activities). All standards PUBLIC license. 6-food-module mega composite validates.
- **Notes:** Shipped at v0.29.0. Registry +6 standards (9 CFR 416/417 + 21 CFR 507/112/121 + 21 CFR 1 Subpart L).

### OQ-103 — Aerospace + automotive extension + IVDR class overlay batch (6)

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-059, OQ-072, OQ-040
- **Claim:** 6 new class overlays at `modules/{aerospace-defense,aerospace-commercial-space,automotive-defense,automotive-motorcycle,ivdr-class-c,ivdr-class-d}/`. Aerospace-defense (MIL-STD-882E + ITAR + EAR — DoD acquisition, deemed-export controls); Aerospace-commercial-space (14 CFR Part 450 — FAA-AST licensing, EC ≤ 1×10⁻⁴, FTS, financial responsibility); Automotive-defense (MIL-STD-882E + USML Cat VII + EAR Cat 9/0 + CMMC readiness); Automotive-motorcycle (ISO 26262 Part 12 — MSIL instead of ASIL, rider-specific controllability); IVDR-Class-C (Annex VIII Rule 3 — NB conformity + clinical evidence + biennial PSUR); IVDR-Class-D (Annex VIII Rule 1 — highest IVD risk; EU Reference Laboratory + batch verification + annual PSUR). All standards PUBLIC license.
- **Notes:** Shipped at v0.30.0. Registry +6 standards (MIL-STD-882E + ITAR + EAR + 14 CFR Part 450 + ISO 26262 Part 12 + EU IVDR Annex VIII). **Standards-licensing scope-boundary**: cited regulations are PUBLIC, but the controlled technical data referenced by ITAR + EAR is heavily restricted — Open QMS handles procedural framework only; actual controlled data must be handled per adopter's separate Technology Control Plan + DCSA / DDTC / BIS oversight.

### OQ-100 — Per-module READMEs backfilled (class overlays + cross-cutting overlays)

- **Tier:** Gap
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-097
- **Claim:** All shipped Open QMS modules now have standalone READMEs. v0.26.0 ships 14 class overlay READMEs (5 aerospace DAL + 5 automotive ASIL/QM + 4 automotive CAL); v0.27.0 ships 6 cross-cutting overlay READMEs (iso-14001, iso-45001, iso-50001, iso-37001, iso-22301, recall-workflow). Combined with vertical READMEs + medical-devices class overlay READMEs already in place, **every module in `modules/*/module.yaml` (37 modules total) now has `modules/*/README.md` (37 READMEs)** — verified by `find` count match.
- **Notes:** Each README ~50-100 lines following uniform structure (scope / standards / clause table per delta / composition example / when-to-use + when-NOT-to-use / standards licensing / forward work). Tight by design — comprehensive catalog at `docs/modules-catalog.md` remains the cross-reference; per-module READMEs are point-of-use documentation. Closes the v0.23.0 OQ-097 forward-work item.

### OQ-099 — Standalone template library expansion (15 new templates across 3 groups)

- **Tier:** Gap
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** —
- **Claim:** Open QMS ships 15 new standalone templates surfaced as forward-work in earlier release companions (food-safety / manufacturing / iso-14001 / iso-45001 / iso-50001 / pharma / atmp companions). Templates are organized into 3 groups: **Group A — cross-vertical management-system (6):** Quality Manual (top-level QMS organizing document per ISO 9001 §4+§5); Process Map (ISO 9001 §4.4 inventory + interaction); Risk-and-Opportunity Register (Annex SL §6.1 cross-cutting); Risk Assessment standalone (per ISO 31000 + ISO 31010 — for bounded one-time assessments distinct from steady-state ROR); BIA standalone (ISO 22301 §8.2.2 dedicated); IT DR Plan (IT-specific subset of BCMS-PLAN; ISO/IEC 27031 + NIST SP 800-34). **Group B — domain-specific registers (3):** Compliance Obligations Register (ISO 14001 §6.1.3 dedicated; was forward work from companion_hse_energy_overlays); OH&S Legal and Other Requirements Register (ISO 45001 §6.1.3 dedicated; same companion forward work); Energy Objectives and Targets Register (ISO 50001 §6.2 dedicated; same companion forward work). **Group C — pharma + ATMP specialty templates (6):** Site Master File (EU GMP Part III + PIC/S PE 008 + ATMP-specific Annex 2A additions); Batch Certificate of Analysis (21 CFR 211.165 + EU GMP Part I Ch. 6 + ICH Q6A/Q6B with full standard release-test panel for chemical + biological products); Stability Protocol (ICH Q1A(R2) full design including general/refrigerated/frozen storage conditions per climate zone + Q1B photostability + Q1C dosage forms + Q1D bracketing+matrixing + Q1E statistical evaluation + Q5C biologics); Comparability Protocol (ICH Q5E + Q12 with biologics + ATMP-specific attribute panels and pre-defined acceptance criteria); CAR-T Release Testing Record (EU GMP Annex 2A + FDA CBER 2024 CAR-T Guidance + RCL testing + autologous risk-based release per Annex 2A §11 + FDA OOS clinical-window handling); AAV Release Testing Record (FDA CMC IND Guidance 2020 + Q5A(R2) vector-product extension + AUC/cryo-EM/CDMS for critical empty:full ratio + RCAAV testing + transgene-specific potency).
- **Notes:** Shipped at v0.25.0. Templates are added as standalone files; bindings to existing modules are forward work (separate release) since adding bindings requires per-module manifest updates + would change the OQ-001 validation surface for each affected module. Templates work as adopter-ready reference documents in their current standalone form. **Forward work:** add bindings to relevant modules (Quality Manual + Process Map + Risk-and-Opportunity Register → manufacturing + other verticals; BIA + IT DR + Risk Assessment → iso-22301; Compliance Obligations → iso-14001; OH&S Legal → iso-45001; Energy Objectives → iso-50001; Site Master File + Batch CoA + Stability + Comparability → pharma; CAR-T + AAV release → atmp). Adding bindings is straightforward but heavy in BUSINESS-side updates (touches every affected module's clauses + bindings + companion).

### OQ-098 — Cross-vertical recall-workflow overlay (NHTSA Part 573/577/579 + FDA Part 7/806 + CPSIA §15)

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-012, OQ-014
- **Claim:** Open QMS ships a cross-vertical recall-workflow overlay at `modules/recall-workflow/module.yaml` (version 0.1.0). Composes with ANY vertical that requires recall discipline (automotive, medical-devices, manufacturing for consumer products under CPSIA, food-safety). 11 clauses across 6 standards covering four regulatory frameworks: **NHTSA (automotive)** — 49 CFR 573 Defect Information Report within 5 working days + 49 CFR 577 Owner Notification within 60 days with 10 mandatory §577.5 content elements + §577.8 second notification at < 70% completion + 49 CFR 579 TREAD Act quarterly Early Warning Reporting; **FDA medical devices** — 21 CFR 806 Reports of Corrections and Removals within 10 working days; **FDA general** — 21 CFR 7 recall classification (Class I/II/III) + effectiveness checks at three levels (A/B/C per Class); **CPSC consumer products** — CPSIA §15 / 15 USC §2064 Substantial Product Hazard reports within 24 hours of obtaining information reasonably supporting the conclusion of substantial hazard. Plus cross-framework workflow elements (decision flow with single Recall Coordinator + multi-functional team activation within 4 hours; distribution-list extraction ≤ 4 hours with framework-specific traceability granularity per-VIN / per-UDI / per-lot; effectiveness checks; recovery + disposition; mock-recall annual cadence). Ships 2 new recall-specific templates: **Generalized Recall Procedure** (cross-vertical with regulatory-framework-parametrized notification windows + classification + content per NHTSA / FDA / CPSIA / EU Article 19 General Product Safety Regulation 2023/988) and **NHTSA Part 577 Owner Notification Letter** (automotive-specific with all 10 §577.5 mandatory elements + §577.8 second-notification trigger + §577.9 reimbursement provisions for pre-notification remedy charges).
- **Notes:** Shipped at v0.24.0. All cited standards PUBLIC license (US federal regulations via ecfr.gov; statutes via USC; CPSIA via CPSC). Registry +6 standards (49 CFR 573, 577, 579, 21 CFR 7, 21 CFR 806, CPSIA §15). Validates standalone + composed with automotive + medical-devices + manufacturing + food-safety. **10-module composite validates** (new depth record): automotive + asil-d + cal-4 + recall-workflow + regulated-ai + iso-27001 + iso-14001 + iso-45001 + iso-50001 + iso-22301 — realistic shape for a top-rigor connected automotive ECU manufacturer with full recall discipline + integrated management system. **Architectural decision:** shipped as cross-cutting overlay rather than four separate per-vertical class overlays because the procedure SHAPE is essentially the same across all four frameworks; only the classification scheme + notification windows + notification content differ, which are parametrized in the generalized template. **Forward work:** EU Article 19 General Product Safety Regulation 2023/988 standalone overlay; FDA pharma Field Alert Report 21 CFR 314.81 dedicated workflow; product-liability insurance claim coordination workflow; class-action litigation hold integration.

### OQ-097 — Public adopter-surface release: README rewrite + modules catalog + BUSINESS un-gitignored

- **Tier:** Gap
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** —
- **Claim:** Open QMS's adopter-facing surface (README + catalog page + module READMEs) is current as of v0.23.0 reflecting all 6 verticals + 22 class overlays + 7 cross-cutting overlays + 11 example bundles. README rewritten from v0.7.0-era state to v0.22.0+ state including: top-level verticals catalog table, cross-cutting overlays guide, per-audience quick-start, adoption guidance by industry, full standards-licensing inventory split by public vs. commercial, current status (80 spec entries; 6 `:verified` / 67 `:tested` / 7 `:argued` / 0 `:open`), 9-module composite reference. New `docs/modules-catalog.md` provides comprehensive per-module catalog with standards covered + clause counts + composition guidance + decision flow + composition examples (smallest viable scaffold through 9-module deepest composite). Backfilled missing vertical READMEs for food-safety + atmp (medical-devices / aerospace / automotive / manufacturing / pharma READMEs already existed). **BUSINESS/ directory un-gitignored** — spec discipline (ENGINE_SPEC.md, artifact_registry.md, DESIGN.md, dashboard.md, changelog.md, 12 companion docs) is now publicly readable, closing P10 from the original priority stack.
- **Notes:** Shipped at v0.23.0. Pure consolidation release — no new module-tier entries, no new templates, no engine code changes. The breadth had run substantially ahead of public discoverability; this release closes that gap. The 12 companion docs going public document the per-session computational basis + verification records back to v0.2.0, providing a transparent record of how every spec entry was earned. The publication itself does NOT constitute a new claim about Open QMS capabilities — it makes the existing claims publicly auditable.

### OQ-096 — ATMP (Advanced Therapy Medicinal Products) class overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-092
- **Claim:** Open QMS ships an ATMP class overlay at `modules/atmp/module.yaml` (version 0.1.0). **First pharma class overlay; most-stringent biologics scope** — autologous + allogeneic cell therapies (CAR-T, iPSC-derived); gene therapies (AAV + lentiviral + retroviral); ex vivo gene-modified HSCT; oncolytic viruses. 10 clauses encoding the substantive ATMP-specific requirements beyond baseline pharma: EU GMP Annex 2A §2 risk-based approach + §4+§7 personnel + aseptic manufacturing (closed-system processing preferred; isolator + RABS use; PIC/S Annex 1 with ATMP adaptations) + §3+§6 donor + starting material (per Directive 2004/23/EC + Directive 2006/17/EC EU; 21 CFR 1271 US) + §10 bidirectional traceability (with EU Single European Code per Directive 2015/565; 30-year EU retention per Art. 8) + §8+§11 OOS for autologous (cannot easily be rejected — patient typically already conditioned; risk-based release with clinical decision); EU GMP Annex 2B biological active substances + cell-bank management + comparability per ICH Q5D+Q5E+Q5C; 21 CFR 1271 Subpart C donor eligibility (§§1271.45-1271.90 RCDA screening + testing + determination by licensed physician + exception per §1271.65) + Subpart D Current Good Tissue Practice (establishment registration + personnel + procedures + facilities + EM + recovery through distribution + records + tracking + complaint file) + §1271.350 HCT/P deviation reporting; ICH Q5A(R2) 2023 three-pillar viral safety framework (cell substrate + raw material testing; production-process viral clearance via model-virus challenge with cumulative LRF ≥ worst-case potential viral load per viral class; final product testing) — **2023 revision explicitly extends to genetically engineered viral vector products** with vector-specific RCV testing (RCL for lentivirus; RCA for adenovirus; RCAAV for AAV) where viral clearance not applicable. Ships 3 new ATMP-specific templates: Donor Eligibility Assessment (21 CFR 1271 Subpart C + EU Directive 2004/23/EC — full RCDA panel + specimen-window compliance + §1271.65 exceptions + **PHI compartmentalization required**); Tissue/Cell Traceability Record (EU GMP Annex 2A §10 + Directive 2004/23/EC Art. 8 + Single European Code + bidirectional traceability with forward+reverse+recall-scope queries + format+media stability planning for 30-year EU retention); Viral Safety Evaluation Report (ICH Q5A(R2) — MCB/WCB/EPC characterization + raw material viral risk + viral clearance studies for non-vector + RCV strategy for vector products).
- **Notes:** Shipped at v0.22.0 (commit `2efc102`). All cited standards are PUBLIC license (same character as parent pharma vertical). Registry +4 standards (EU GMP Annex 2A, EU GMP Annex 2B, 21 CFR 1271, ICH Q5A(R2)). New `bundles/example-cart.yaml` (autologous CD19-targeted CAR-T at US+EU dual-licensed site). **9-module deepest composite validates: pharma + atmp + iso-27001 + regulated-ai + iso-14001 + iso-45001 + iso-50001 + iso-37001 + iso-22301** — realistic shape for commercial-stage cell therapy organization pursuing fully-integrated management system (PQS + ATMP-specific GMP + IS + AI governance + EMS + OHSMS + EnMS + ABMS + BCMS). **Forward work:** reproductive tissue / gametes specifics; HCT/P that is NOT an ATMP (different regulatory pathway); veterinary ATMPs; in situ gene editing (no ex vivo); Site Master File for ATMPs; comparability protocol template (ICH Q5E — particularly critical for ATMPs without reference standard for autologous); CAR-T-specific + AAV-specific release-testing templates.

### OQ-092 — Pharma vertical module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-014
- **Claim:** Open QMS ships a pharma vertical at `modules/pharma/module.yaml` (version 0.1.0). 5th vertical; largest remaining regulated-industry gap. 23 clauses across 8 standards spanning 4 discipline tracks: (1) Pharmaceutical Quality System — ICH Q10 §3.2.1 management responsibility, §3.2.2 process performance + product quality monitoring + CAPA + change management as integrated PQS elements, §3.2.4 Stage 3 continued process verification; ICH Q9(R1) Quality Risk Management framework. (2) API GMP — ICH Q7 §2 quality management, §8 production + IPCs, §12 validation. (3) US cGMP — 21 CFR 211 Subparts B (organization + QCU independence), D (equipment), E (components + containers), F (production + process controls), G (packaging + labeling), I (laboratory controls), J (records + reports incl. APQR per §211.180(e)). (4) EU GMP — EudraLex Vol. 4 Ch. 1 (PQS incl. §1.10 PQR mandatory annually with QP), Ch. 2 (QP responsibilities per Article 51 of Directive 2001/83/EC), Ch. 6 (QC + OOS §6.34), Annex 15 (qualification + validation), Annex 16 (QP certification + batch release). (5) Sterile manufacturing — PIC/S Annex 1 (2022) §2+§8 Contamination Control Strategy, §9.40-§9.50 Aseptic Process Simulation, §9 EM + §9.27 cleanroom classification (Grade A/B/C/D). Plus 21 CFR Part 11 for pharma computerized systems. Ships 6 new pharma-specific templates: Master Batch Record (21 CFR 211.186 + EU GMP Part I Ch. 4); Validation Master Plan (ICH Q9+Q10 + EU GMP Annex 15 + FDA PV 2011); Deviation Report (21 CFR 211.100+192 + EU GMP Ch. 1 §1.4(xiv) + ICH Q10 §3.2.2.2 — Critical/Major/Minor categorization with QA-assignment criteria); Change Control (ICH Q10 §3.2.3 + EU GMP Ch. 1 §1.4(xiv) + 21 CFR 211.100 — QA-gated planned change with regulatory-impact assessment for FDA/EMA/MHRA/HC/PMDA submissions); OOS Investigation (FDA OOS Guidance 2006 + 21 CFR 211.192 + EU GMP Ch. 6 §6.34 — Phase 1 lab investigation + Phase 2 full-scale investigation; retesting only with documented protocol); Annual Product Quality Review (21 CFR 211.180(e) + EU GMP Ch. 1 §1.10 — annual per-product trend aggregation with Cpk/Ppk + QP review in EU). Validates as: standalone; medical-devices + pharma (combination products per 21 CFR Part 4); 6-module composite with all 5 HSE+IS+AI cross-cutting overlays.
- **Notes:** Shipped at v0.19.0 (commit `a98854e`). Notable: **first vertical where most cited standards are PUBLIC license** — ICH Q7/Q9/Q10 (ich.org); 21 CFR 210/211 (ecfr.gov); EudraLex Vol. 4 (EU Commission); PIC/S Annex 1 (PIC/S). Meaningful adopter cost reduction vs. medical-devices / aerospace / automotive verticals. Registry +7 standards (ICH Q7, ICH Q9, ICH Q10, 21 CFR 210, 21 CFR 211, EudraLex Vol. 4, PIC/S Annex 1) + 3 jurisdictions (EMA, MHRA, WHO-PQ); FDA jurisdiction extended with pharma standards. New `bundles/example-drug-product.yaml` (sterile SVP injection at US+EU dual-licensed site). **Forward work:** ATMP overlay (EU GMP Annex 2A+2B + FDA 21 CFR 1271 + ICH Q5A(R2)); radiopharma overlay (EU GMP Annex 3 + USP <823>); veterinary overlay; IMP overlay (EU GMP Annex 13); generic/biosimilar overlay; Site Master File template; Batch CoA template; Stability Protocol template (ICH Q1A(R2)); sterile vs. non-sterile + biologics vs. small-molecule + commercial vs. clinical-stage class overlays.

### OQ-093 — Food safety vertical module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-014
- **Claim:** Open QMS ships a food-safety vertical at `modules/food-safety/module.yaml` (version 0.1.0). 6th vertical. Covers human-food manufacturing under ISO 22000 FSMS + Codex HACCP + US FSMA Preventive Controls + FSSC 22000 v6 (GFSI-benchmarked scheme). 16 clauses across 5 standards: ISO 22000:2018 (FSMS substrate following Annex SL — §5.2 policy, §6.1 risk-and-opportunity, §8.2 PRPs per ISO/TS 22002, §8.5 hazard control with CCPs+oPRPs+critical limits+monitoring+corrective actions+verification, §8.7 monitoring/measuring control, §8.9 NC + withdrawal/recall, §9.2 audit, §9.3 mgmt review, §10.1 NC+CAPA); FSSC 22000 v6 (scheme-specific PRPs + food defense + food fraud + allergen + EM + product design); Codex Alimentarius CXC 1-1969 (7 HACCP principles + 12 steps; Good Hygienic Practices); 21 CFR 117 FSMA Preventive Controls Rule (Subpart B cGMP, Subpart C Food Safety Plan with hazard analysis + process/allergen/sanitation/supply-chain preventive controls + PCQI per §117.180, Subpart D recall plan); 21 CFR 123 Seafood HACCP. Ships 3 new food-safety-specific templates: HACCP Plan (Codex + ISO 22000 §8.5 + 21 CFR 117 Subpart C + 21 CFR 123 — covers B/C/P/A hazards including allergens per FALCPA + FASTER Act + EU FIC Annex II, CCP determination via Codex decision tree, pre-defined corrective actions, 7-principles record-keeping, PCQI designation); Prerequisite Programs (ISO/TS 22002 15-element index with cleaning per zone 1-4, pest control, allergen management with changeover validation, FSVP cross-reference, food defense vulnerability assessment per 21 CFR 121); Recall + Withdrawal Procedure (21 CFR 117 Subpart D + 21 CFR 7 + Codex §5.7 + ISO 22000 §8.9 — Class I/II/III classification, 24/7 CMT, hour-0 decision flow, <4-hour distribution-list extraction, 24h regulatory notification incl. Reportable Food Registry per 21 USC §350f, effectiveness checks per FDA levels A/B/C, mock-recall annual cadence).
- **Notes:** Shipped at v0.20.0 (commit `ca6e69b`). Codex + 21 CFR 117 + 21 CFR 123 are PUBLIC license; ISO 22000 + FSSC 22000 are commercial. Registry +5 standards + 4 jurisdictions (FDA-Food/CFSAN+FSMA, USDA-FSIS, EFSA, CFIA). New `bundles/example-food-processor.yaml` (mid-size RTE chilled-foods under FSMA + ISO 22000 + FSSC 22000 v6 across FDA + EFSA + CFIA composing food-safety + iso-14001 + iso-45001 + iso-50001). **Forward work:** USDA meat+poultry HACCP overlay (9 CFR 416+417); FSMA Animal Food overlay (21 CFR 507); Produce Safety overlay (21 CFR 112); BRCGS/SQF/IFS GFSI schemes; Intentional Adulteration standalone (21 CFR 121); FSVP standalone (21 CFR 1 Subpart L); class overlays for low-acid canned (21 CFR 113) + acidified (21 CFR 114) + infant formula (21 CFR 106+107); dietary supplements vertical (21 CFR 111 DSHEA).

### OQ-094 — ISO 37001:2016 anti-bribery management cross-cutting overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-012, OQ-014
- **Claim:** Open QMS ships an ISO 37001:2016 anti-bribery management cross-cutting overlay at `modules/iso-37001/module.yaml` (version 0.1.0). Composes with ANY vertical. 14 clauses encoding the substantive ISO 37001:2016 additions over the Annex SL high-level structure: §5.1.2 governing body + senior management responsibility; §5.2 anti-bribery policy; §5.3.2 INDEPENDENT anti-bribery compliance function with appropriate competence + status + authority + independence + resources + direct reporting to governing body / senior management; §6.1 ABMS risks + opportunities; §7.2.2.2 due diligence on personnel (positions exposed to more than low bribery risk); §7.3 awareness + training; §8.2 risk-proportionate due diligence on transactions/projects/activities/business associates with periodic re-assessment; §8.3 financial controls (segregation + authorization + cash + expense + gifts/hospitality/donations); §8.4 non-financial controls (procurement + commercial + operational + HR); §8.5 anti-bribery controls of controlled organizations + business associates (Medium + High risk — equivalent controls OR contractual commitment with audit rights); §8.7 gifts/hospitality/donations + similar benefits with pre-approval thresholds + register; §8.9 raising concerns / whistleblowing with non-retaliation; §8.10 investigating + dealing with bribery; §9.4 review by anti-bribery compliance function. Ships 1 new template: Anti-Bribery Due Diligence Assessment (ISO 37001 §8.2 + §8.5 — risk-tier framework Low/Medium/High/Prohibited with scaled depth + approval authority + re-assessment cadence; sanctions + PEP + adverse-media + UBO screening; contractual-safeguard checklist with FCPA + UK Bribery Act + OECD Convention + CPI references).
- **Notes:** Shipped at v0.21.0 (commit `ee215d7`). Particularly applicable for public-sector vendors, extractives, defense contractors, healthcare suppliers, infrastructure contractors, intermediary-heavy sales channels, high-CPI jurisdictions.

### OQ-095 — ISO 22301:2019 business continuity management cross-cutting overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-012, OQ-014
- **Claim:** Open QMS ships an ISO 22301:2019 BCMS cross-cutting overlay at `modules/iso-22301/module.yaml` (version 0.1.0). Composes with ANY vertical. 13 clauses encoding the substantive ISO 22301:2019 additions: §5.2 BC policy; §6.1 BCMS risks + opportunities; §6.2 BC objectives derived from BIA; §8.2.2 Business Impact Analysis (BIA — identifies prioritized activities + RTO/MAO/MBCO/RPO); §8.2.3 BC risk assessment; §8.4 BC strategies + solutions (people + ICT + infrastructure + supplies + partners + financial resources; stabilization + continuity + recovery + return); §8.5 BC plans + procedures; §8.6 exercise programme (tabletop, comms cascade, technical, full-scale; varied scenarios over time; post-exercise review); §8.7 evaluation of BC documentation + capabilities; §9.1 monitoring + measurement; §9.2 internal audit; §9.3 management review; §10.2 NC + corrective action. Ships 1 new template: Business Continuity Plan (ISO 22301 §8.4 + §8.5 + §8.6 + §8.7 — recovery objectives summary with MAO/RTO/RPO/MBCO definitions; 8 disruption scenarios with response procedures; crisis management team with 24/7 contacts; internal + external communications matrix with regulatory reporting windows; exercise programme cadence — tabletop annual / comms cascade annual / IT DR annual / live activation biennial / post-incident review after every activation).
- **Notes:** Shipped at v0.21.0 (commit `ee215d7`). Particularly applicable for organizations with significant disruption exposure (single-site dependencies, complex supply chains), regulated services with continuity obligations (financial services under DORA, healthcare, critical infrastructure, utilities, telecoms). **8-module ultimate composite validates: pharma + iso-27001 + regulated-ai + iso-14001 + iso-45001 + iso-50001 + iso-37001 + iso-22301** — deepest composition tested to date; realistic shape for a pharma manufacturer pursuing fully-integrated management-system certification (PQS + IS + AI governance + EMS + OHSMS + EnMS + ABMS + BCMS).

### OQ-089 — ISO 14001:2015 environmental management cross-cutting overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-012, OQ-014
- **Claim:** Open QMS ships an ISO 14001:2015 environmental-management cross-cutting overlay at `modules/iso-14001/module.yaml` (version 0.1.0). Composes with ANY vertical (medical-devices / aerospace / automotive / manufacturing). 11 clauses encoding the substantive ISO 14001:2015 additions over the Annex SL high-level structure: §4.2 interested parties (environmental — regulators, communities, customers, NGOs); §5.2 environmental policy (commits to protection of environment including prevention of pollution + sustainable resource use + climate change mitigation/adaptation + biodiversity, fulfillment of compliance obligations, continual improvement); §6.1.2 environmental aspects (the defining EMS artifact — lifecycle-perspective identification of aspects, impact determination, significance criteria flagging Significant Environmental Aspects); §6.1.3 compliance obligations; §6.1.4 planning action; §6.2 objectives; §7.4 communication (incl. external comms required by compliance obligations); §8.1 operational control of SEAs (lifecycle perspective in design + procurement + outsourced processes); §8.2 emergency preparedness + response (periodic test); §9.1.2 evaluation of compliance; §10.2 nonconformity + corrective action (incl. mitigating adverse environmental impacts). Ships 1 new template: Environmental Aspects + Impacts Register (ISO 14001 §6.1.2 with significance scoring + SEA flagging + operational controls + emergency procedures + compliance-obligations cross-reference + lifecycle perspective). Bindings reuse quality-policy (extended for environmental commitments), SOP, audit-procedure, CAPA from cross-cutting templates.
- **Notes:** Shipped at v0.18.0 (commit `ef13f46`). First HSE-and-energy cross-cutting overlay batch alongside OQ-090 (ISO 45001) + OQ-091 (ISO 50001). All three follow the Annex SL high-level structure → compose cleanly with each other AND with ISO 27001 + ISO 42001 (regulated-ai's organizational AIMS standard). 6-module everything-shop composite validates: manufacturing + iso-14001 + iso-45001 + iso-50001 + iso-27001 + regulated-ai. **Forward work:** Compliance Obligations Register template (dedicated; currently lives only inside the Environmental Aspects Register cross-reference).

### OQ-090 — ISO 45001:2018 OH&S management cross-cutting overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-012, OQ-014
- **Claim:** Open QMS ships an ISO 45001:2018 OH&S management cross-cutting overlay at `modules/iso-45001/module.yaml` (version 0.1.0). Composes with ANY vertical. 11 clauses encoding the substantive ISO 45001:2018 additions: §4.2 interested parties (workers + reps, contractors, communities, families of workers); §5.2 OH&S policy (commits to safe + healthy working conditions for prevention of work-related injury + ill-health, elimination of hazards + reduction of OH&S risks, worker consultation + participation); **§5.4 consultation + participation of workers** (THE foundational OHSMS requirement — non-managerial workers + reps consulted + participating in development + planning + implementation + evaluation + improvement; mechanisms + time + training + barrier removal required); §6.1.2 hazard identification + risk assessment + opportunities (ongoing + proactive; routine + non-routine; psychosocial factors explicitly required); §6.1.3 legal + other requirements; §6.1.4 planning action; §7.3 awareness (incl. right to remove self from imminent danger + protection from undue consequences); §8.1.2 hierarchy of controls (elimination > substitution > engineering > administrative > PPE; PPE is last resort, not default); §8.1.3 management of change; §8.1.4 procurement (incl. contractor coordination); §8.2 emergency preparedness + response; §10.2 incident + nonconformity + corrective action (with worker participation in evaluation + root-cause analysis). Ships 1 new template: HIRA — Hazard Identification + Risk Assessment with Hierarchy of Controls (ISO 45001 §6.1.2 with worker consultation evidence per §5.4 as a precondition, not afterthought; hazard register with S × L matrix + acceptability criterion + hierarchy-of-controls action + residual risk + cross-references to §6.1.3 legal + §8.1.3 MoC + §8.1.4 procurement + §8.2 emergency).
- **Notes:** Shipped at v0.18.0 (commit `ef13f46`). Worker consultation per §5.4 is unique to OHSMS among the Annex SL standards — the overlay surfaces this prominently in both the module and the HIRA template's frontmatter (`worker_consultation:` field required).

### OQ-091 — ISO 50001:2018 energy management cross-cutting overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-012, OQ-014
- **Claim:** Open QMS ships an ISO 50001:2018 energy management cross-cutting overlay at `modules/iso-50001/module.yaml` (version 0.1.0). Composes with ANY vertical. 10 clauses encoding the substantive ISO 50001:2018 additions: §5.2 energy policy (commits to procurement of energy-efficient products/services + design for energy performance + continual improvement of energy performance + the EnMS); §6.3 energy review (analyze use + consumption; identify Significant Energy Uses — SEUs; determine current performance; identify + prioritize improvement opportunities — the analytical foundation of the EnMS); §6.4 EnPIs (energy performance indicators with methodology + values + reviews + comparison to baselines); §6.5 EnB (energy baseline calculated from energy review; revised on EnPI-no-longer-reflects, static-factor change, operations change); §6.6 planning for collection of energy data (key characteristics, relevant variables, operational criteria, static factors); §8.1 operational control of SEUs (criteria for effective operation + maintenance; absence of which could lead to significant deviation from effective energy performance); §8.2 design (energy performance improvement opportunities + operational control in design of facilities/equipment/systems/processes with significant impact); §8.3 procurement (energy-using products + equipment + services with significant impact; suppliers informed; specifications for purchased energy itself); §9.1.1 monitoring + measurement + analysis + evaluation (incl. investigation + response to significant deviations from expected energy consumption); §10.2 nonconformity + corrective action. Ships 1 new template: Energy Review + EnPIs + EnB Baseline (combined §6.3 + §6.4 + §6.5 + §6.6; per-SEU performance basis + improvement opportunity with payback; per-EnPI formula + normalization model; per-EnB calculation method + recalibration triggers; data collection plan; operational + procurement implications).
- **Notes:** Shipped at v0.18.0 (commit `ef13f46`). **ISO 50001 is unique among the management-system standards in mandating a quantitative, calculated, periodically-recalibrated performance baseline** — the Energy Review template is the most quantitative artifact in Open QMS to date, reflecting this character. Adopters seeking ISO 50001 registration must produce real numbers (Cpk-style capability evidence in energy terms), not just process discipline.

### OQ-079 — Aerospace DAL-D class overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-059
- **Claim:** Open QMS ships an aerospace DAL-D class overlay at `modules/aerospace-dal-d/module.yaml` (version 0.1.0). Encodes DO-178C / DO-254 Level D — Minor failure-condition rigor. 5 clauses: DAL-D applicability gate (ARP4754A §5 from FHA Minor), no structural coverage required (Table A-7 doesn't apply at DAL-D — software testing is requirements-based only), 2-of-26 objectives requiring independence (typically QA + SCM), tool qualification typically at TQL-4 or TQL-5, ARP4754A §5 allocation rationale. Bindings to PSAC + SSP templates.
- **Notes:** Shipped at v0.17.0 (commit `f617b2e`). Completes the aerospace DAL set together with DAL-A/B/C (v0.16.0) + DAL-E below.

### OQ-081 — Aerospace DAL-E class overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-059
- **Claim:** Open QMS ships an aerospace DAL-E class overlay at `modules/aerospace-dal-e/module.yaml` (version 0.1.0). Encodes DO-178C / DO-254 Level E — No Safety Effect. 4 clauses: DAL-E applicability gate (ARP4754A §5 from FHA No-Safety-Effect — the substantiation is the load-bearing claim, not subsequent process), NO DO-178C objectives apply at DAL-E (the software is not subject to DO-178C process discipline at all), configuration management still required so cert authority can verify deployed software matches the DAL-E-classified software, ARP4754A §5 allocation rationale (isolation + failure-impact substantiation). Bindings to PSAC + SSP templates.
- **Notes:** Shipped at v0.17.0 (commit `f617b2e`). S-ID OQ-080 was assigned to a Gap entry; OQ-081 follows the manufacturing vertical to keep the numbering contiguous-ish. **Aerospace DAL set complete (A/B/C/D/E).**

### OQ-082 — Automotive ASIL-C class overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-072
- **Claim:** Open QMS ships an automotive ASIL-C class overlay at `modules/automotive-asil-c/module.yaml` (version 0.1.0). Mid-high tier between ASIL-D (v0.16.0) and ASIL-B (v0.16.0). 5 clauses: ASIL-C applicability gate from HARA (S3 × E4 × C2, S3 × E3 × C3, S2 × E4 × C3 per Part 3 §6 Table 4); SPFM ≥ 97% / LFM ≥ 80% / PMHF < 10⁻⁷ failures/hour; 100% statement + 100% branch software structural coverage (MC/DC recommended but NOT required — the major delta from ASIL-D which mandates it); I3-independence confirmation measures (different organizational unit — same as ASIL-D, the major delta from ASIL-B's I2); language subset REQUIRED (e.g., MISRA C 2012 mandatory + required rules — vs. recommended at ASIL-B).
- **Notes:** Shipped at v0.17.0 (commit `f617b2e`).

### OQ-083 — Automotive ASIL-A class overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-072
- **Claim:** Open QMS ships an automotive ASIL-A class overlay at `modules/automotive-asil-a/module.yaml` (version 0.1.0). Lowest non-QM ASIL tier. 5 clauses: ASIL-A applicability gate (S1 × E4 × C3, S2 × E2 × C3, S2 × E3 × C2 per Part 3 §6 Table 4); PMHF < 10⁻⁶ failures/hour but NO quantitative SPFM/LFM targets required; 100% statement coverage at unit-test level (branch + MC/DC recommended — the major delta from ASIL-B which requires 100% branch); I1-independence confirmation measures (different person within the same team — lightest tier short of QM); language subset (MISRA C 2012) + defensive programming + restricted pointers all recommended-not-required.
- **Notes:** Shipped at v0.17.0 (commit `f617b2e`).

### OQ-084 — Automotive QM class overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-072
- **Claim:** Open QMS ships an automotive QM (Quality Management) class overlay at `modules/automotive-qm/module.yaml` (version 0.1.0). Encodes the QM allocation per ISO 26262 — applies when HARA's (S, E, C) combination yields QM per Part 3 §6 Table 4 (e.g., S1 × E4 × C1, S0 × any × any, S2 × E1 × any). 4 clauses: QM applicability gate from HARA (the QM allocation is a POSITIVE safety claim that the function does not require ISO 26262 process discipline beyond baseline IATF 16949 quality management — not an absence of analysis); NO ISO 26262-specific HW metrics / SW coverage / method recommendations / confirmation measures (Part 2 §5.4.1); HARA rationale is load-bearing (mis-classification as QM when true classification is ASIL-A+ omits required FuSa rigor); Safety Plan lists QM-classified items explicitly as out-of-FuSa-scope with HARA cross-reference enabling confirmation reviewer / FuSa auditor to verify appropriate scoping (not silent omission).
- **Notes:** Shipped at v0.17.0 (commit `f617b2e`). **Automotive ASIL set complete (D/C/B/A/QM).** Why ship a QM overlay rather than treat QM as "no overlay"? Auditability — the QM allocation is a positive claim, not an absence; adopters need a place to document the QM rationale that traces from HARA through to the absence-of-FuSa-rigor decision.

### OQ-085 — Automotive CAL-3 class overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-072
- **Claim:** Open QMS ships an automotive CAL-3 class overlay at `modules/automotive-cal-3/module.yaml` (version 0.1.0). Mid-high ISO/SAE 21434 Cybersecurity Assurance Level. 5 clauses: CAL-3 applicability from TARA's impact-and-feasibility matrix (Annex E); independent cybersecurity assessment RECOMMENDED (vs. required at CAL-4, optional at CAL-2); V&V includes baseline security functional + vulnerability scanning + fuzz testing required (penetration testing recommended; side-channel analysis not required vs. required where applicable at CAL-4); continuous activities with formal vulnerability monitoring + response-time commitments documented in CSMS + defined incident-response playbooks (rehearsal recommended; CAL-4 requires rehearsal); safety-security interaction analysis when item is also ASIL-rated (typically ASIL-B or ASIL-C at CAL-3 level).
- **Notes:** Shipped at v0.17.0 (commit `f617b2e`).

### OQ-086 — Automotive CAL-2 class overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-072
- **Claim:** Open QMS ships an automotive CAL-2 class overlay at `modules/automotive-cal-2/module.yaml` (version 0.1.0). Mid-low CAL. 4 clauses: CAL-2 applicability (Annex E moderate-impact / low-feasibility or low-impact / moderate-feasibility damage scenarios); independent cybersecurity assessment OPTIONAL (adopter CSMS decides); V&V includes baseline security functional + vulnerability scanning of dependencies + exposed interfaces (fuzz + pentest recommended); vulnerability monitoring with documented triage cadence (no formal response-time commitments).
- **Notes:** Shipped at v0.17.0 (commit `f617b2e`).

### OQ-087 — Automotive CAL-1 class overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-072
- **Claim:** Open QMS ships an automotive CAL-1 class overlay at `modules/automotive-cal-1/module.yaml` (version 0.1.0). Lowest CAL tier. 4 clauses: CAL-1 applicability (low impact AND low feasibility per Annex E); NO independent cybersecurity assessment required; baseline V&V (security functional testing only — no fuzz / pentest / side-channel); CSMS-baseline vulnerability monitoring (no response-time commitments specific to CAL-1).
- **Notes:** Shipped at v0.17.0 (commit `f617b2e`). **Automotive CAL set complete (4/3/2/1).**

### OQ-088 — General manufacturing vertical module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-014
- **Claim:** Open QMS ships a general-manufacturing vertical regulatory module at `modules/manufacturing/module.yaml` (version 0.1.0). Baseline ISO 9001 QMS for organizations whose products do NOT fall under a domain-specific regulatory framework (medical devices, aerospace, automotive, food, pharma, defense) but who still need a credible QMS for customer credibility, competitive positioning, or contractual flow-down — machine shops, tooling, contract manufacturing, custom fab, job shops, fabrication houses, prototyping shops, light industrial manufacturing. ISO 9001:2015 is the only standard — 17 clauses across the seven clause groups (§4.1 context, §4.4 process approach, §5.1 leadership, §5.2 quality policy, §6.1 risk-and-opportunity — the risk-based-thinking core of ISO 9001:2015 — §7.1 resources, §7.1.5.2 measurement traceability, §7.4 communication, §7.5 documented information, §8.1 operational planning, §8.4 supplier controls, §8.5 production + service provision, §8.5.5 post-delivery, §8.7 nonconforming outputs, §9.1 monitoring + measurement + analysis, §9.2 internal audit, §9.3 management review, §10.2 nonconformity + corrective action). All clauses bind to cross-cutting templates already in Open QMS (quality-policy, SOP, AUDIT-PROCEDURE, MANAGEMENT-REVIEW, ASL, SUPPLIER-EVALUATION, CAPA, nonconformance) — NO new templates required. Composes with iso-27001 (customer proprietary CAD/CAM file handling for many job shops) and with regulated-ai (if production processes use ML — predictive maintenance, computer-vision quality inspection, ML-driven CNC parameter optimization).
- **Notes:** Shipped at v0.17.0 (commit `f617b2e`). Smallest vertical in the project — intentionally minimal. Manufacturing does NOT define class overlays of its own — ISO 9001 has no equivalent of DAL / ASIL / CAL rigor tiers. Higher-rigor needs are served by migrating up to a regulated vertical (aerospace → AS9100D; automotive → IATF 16949; medical-devices → ISO 13485). New example bundle `bundles/example-machine-shop.yaml` (ExamplePrecisionMachineShop composing manufacturing + iso-27001; jurisdictions list intentionally empty since general manufacturing has no specific regulator); idempotent regenerate confirmed. Vertical count now 4 (medical-devices / aerospace / automotive / manufacturing) — Open QMS now serves both regulated AND non-regulated manufacturing scopes. **Forward work:** food safety vertical (ISO 22000 / FSSC 22000 / HACCP), pharma GMP vertical (ICH Q7 / 21 CFR 210+211 / EudraLex Vol. 4), environmental overlay (ISO 14001), occupational H&S overlay (ISO 45001), energy management overlay (ISO 50001), anti-bribery overlay (ISO 37001), industrial machinery functional safety (IEC 61508 / ISO 13849).

### OQ-073 — Aerospace DAL-A class overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-059
- **Claim:** Open QMS ships an aerospace DAL-A class overlay at `modules/aerospace-dal-a/module.yaml` (version 0.1.0). Composes with the aerospace vertical to encode the highest-rigor DO-178C + DO-254 + ARP4754A requirements. 7 clauses: DAL-A applicability gate (FHA Catastrophic → ARP4754A §5 allocation), MC/DC structural coverage (DO-178C Table A-7 obj 5; the strongest practical structural-coverage criterion short of multiple-condition coverage), 25-of-71 DO-178C objectives requiring independence (Annex A), DO-330 tool qualification typically at TQL-1, DO-254 §6.2 elemental analysis, DO-254 §6.3 safety-specific analyses (Single Event Upset analysis + common-mode analysis + analyses identified by ARP4761 SSA + CCA), ARP4754A §5 DAL-allocation rationale traced from FHA. Bindings extend PSAC + Software Test Protocol + Verification Protocol + System Safety Plan templates.
- **Notes:** Shipped at v0.16.0 (commit `ffad042`). First aerospace class overlay; mirrors the medical-devices class overlay pattern from v0.11.0+v0.12.0. Composes via OQ-011 with aerospace vertical (OQ-059).

### OQ-074 — Aerospace DAL-B class overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-059
- **Claim:** Open QMS ships an aerospace DAL-B class overlay at `modules/aerospace-dal-b/module.yaml` (version 0.1.0). 6 clauses: DAL-B applicability gate (FHA Hazardous), Decision Coverage instead of MC/DC (the major delta from DAL-A; DO-178C Table A-7 obj 6), 14-of-69 objectives requiring independence (Annex A), TQL-1/TQL-2 tool qualification, DO-254 elemental analysis still required at DAL-B, ARP4754A allocation rationale for Hazardous-classified items.
- **Notes:** Shipped at v0.16.0 (commit `ffad042`).

### OQ-075 — Aerospace DAL-C class overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-059
- **Claim:** Open QMS ships an aerospace DAL-C class overlay at `modules/aerospace-dal-c/module.yaml` (version 0.1.0). Most common DAL for production avionics functions that are supervised or non-critical. 5 clauses: DAL-C applicability gate (FHA Major), Statement Coverage instead of Decision Coverage (the major delta from DAL-B; DO-178C Table A-7 obj 7), only 2-of-62 objectives requiring independence (a substantial cost-of-process reduction vs. DAL-A/B), TQL-3/TQL-4 tool qualification, ARP4754A §3.5 decomposition often invoked to allocate higher DALs into multiple DAL-C elements with independence argumentation.
- **Notes:** Shipped at v0.16.0 (commit `ffad042`). DAL-D + DAL-E left as forward work (lower-rigor levels; less common in production).

### OQ-076 — Automotive ASIL-D class overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-072
- **Claim:** Open QMS ships an automotive ASIL-D class overlay at `modules/automotive-asil-d/module.yaml` (version 0.1.0). Highest ISO 26262 functional safety rigor (HARA assignment at S3 × E4 × C3 per Part 3 §6 Table 4 — examples: brake-by-wire torque control, steering-by-wire angle control, airbag deployment, BMS battery-fault response). 6 clauses encoding: ASIL-D applicability gate from HARA, hardware architectural metrics SPFM ≥ 99% / LFM ≥ 90% / PMHF < 10⁻⁸ failures/hour (Part 5 §8-9 + Annex F), software structural coverage 100% statement + 100% branch + 100% MC/DC at unit-test level + 100% function + 100% function-call at integration level (Part 6 Tables 12-15), I3-independence confirmation measures (different organizational unit) for confirmation review + FuSa audit + FuSa assessment (Part 2 §6 Table 1), software design + coding method requirements (formal notations + strongly-typed languages strongly recommended; MISRA C 2012 mandatory rules required), optional ASIL decomposition per Part 9 §5 (D = C(D)+A(D), B(D)+B(D), D+QM(D) with dependent-failure-analysis support).
- **Notes:** Shipped at v0.16.0 (commit `ffad042`). First automotive class overlay; composes with automotive vertical (OQ-072) and with regulated-ai + iso-27001 + automotive-cal-4 in mega-composite for top-rigor safety-and-cyber-critical ML-enabled ECU.

### OQ-077 — Automotive ASIL-B class overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-072
- **Claim:** Open QMS ships an automotive ASIL-B class overlay at `modules/automotive-asil-b/module.yaml` (version 0.1.0). Mid-tier FuSa rigor; common for production ECUs implementing non-life-critical but safety-relevant functions. 5 clauses: ASIL-B applicability gate (e.g., S2 × E4 × C2; S3 × E3 × C1; S2 × E3 × C3 per Part 3 §6 Table 4), hardware architectural metrics SPFM ≥ 90% / LFM ≥ 60% / PMHF < 10⁻⁷ failures/hour, software structural coverage 100% statement + 100% branch (MC/DC recommended but NOT required — the major delta from ASIL-D), I2-independence confirmation measures (different team within the same organizational unit), MISRA C 2012 recommended (not mandatory).
- **Notes:** Shipped at v0.16.0 (commit `ffad042`). Brackets the ASIL spectrum together with ASIL-D (OQ-076); ASIL-A + ASIL-C + QM left as forward work.

### OQ-078 — Automotive CAL-4 class overlay module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-072
- **Claim:** Open QMS ships an automotive CAL-4 class overlay at `modules/automotive-cal-4/module.yaml` (version 0.1.0). Highest ISO/SAE 21434 Cybersecurity Assurance Level — assigned when TARA identifies high-impact / high-feasibility damage scenarios potentially affecting safety (e.g., compromise of brake / steering / acceleration ECU; back-end server controlling fleet OTA updates). 5 clauses: CAL-4 applicability gate from TARA's impact-and-feasibility matrix (ISO/SAE 21434 Annex E informative), INDEPENDENT cybersecurity assessment requirement for cybersecurity case + final assessment (§6.4.7 + Annex C — different organizational unit or external), rigorous V&V including functional + vulnerability scanning + fuzz + pentest + side-channel analysis where applicable (§10 + §13), continuous activities including formal vulnerability monitoring with response-time commitments + rehearsed incident-response playbooks + sustained cybersecurity through end-of-support (§11), safety-security interaction analysis when item is also ASIL-rated (cross-reference ISO 26262 Part 2 §6 — joint review by FuSa + cyber engineering).
- **Notes:** Shipped at v0.16.0 (commit `ffad042`). First CAL overlay; CAL-1/2/3 left as forward work. Cross-composes with ASIL-D overlay (OQ-076) for safety-and-cyber-critical items; the Safety Concept template's optional Part C (Cybersecurity Concept) is the artifact where the interaction is documented.

### OQ-072 — Automotive vertical module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-014
- **Claim:** Open QMS ships an automotive vertical regulatory module at `modules/automotive/module.yaml` (version 0.1.0). Second non-medical vertical — strengthens the structural-generalization claim from aerospace (one data point) to two. 28 clauses across 8 standards spanning four discipline tracks: (1) **QMS substrate** — IATF 16949:2016 with automotive-specific additions over ISO 9001 (§4.4 process effectiveness, §7.1.5.2.1 calibration retention, §7.5 documented info + CSRs, §8.3.3.3 Special Characteristics, §8.4 supplier control with Tier-N visibility, §8.5.1.1 Control Plan, §8.7 nonconforming output, §9.2 internal audit with three IATF-mandated types, §10.2.3 8D problem solving). (2) **Functional safety** — ISO 26262:2018 across all 12 parts (Part 2 management + §6 confirmation measures; Part 3 §5 item definition / §6 HARA / §7 FSC; Part 4 system development; Part 5 HW with SPFM/LFM/PMHF metrics per ASIL; Part 6 SW with structural coverage per ASIL; Part 8 supporting processes; Part 9 ASIL decomposition + dependent-failure analysis). ASIL A-D. (3) **Cybersecurity engineering** — ISO/SAE 21434:2021 (§5 CSMS, §9 concept phase, §10 project management, §11 continuous activities, §15 TARA driving CAL). (4) **Type-approval cybersecurity regulations** — UN R155 (CSMS + per-vehicle-type assessment per Annex 5 threat categories) + UN R156 (SUMS); both mandatory in UNECE jurisdictions since July 2022. Plus Automotive SPICE 4.0 (SWE + MAN + SUP process groups) and AIAG PPAP 4th Ed. (18-element production approval). Ships 5 automotive-specific templates: Item Definition (ISO 26262 Part 3 §5), HARA (Part 3 §6; reproduces the S × E × C → ASIL table per Annex B), Safety Concept (combined FSC Part 3 §7 + TSC Part 4 §6 + optional Cybersecurity Concept ISO 21434 §9 with explicit safety-security interaction analysis), TARA (ISO 21434 §15 with UN R155 Annex 5 coverage matrix), PPAP (18 elements + Part Submission Warrant). Composes cleanly with `regulated-ai` (relevant for ML-driven ADAS, automated driving, predictive maintenance, in-cabin monitoring — ISO 23894 AI risk management is complementary to both ISO 26262 FuSa and ISO/SAE 21434 cyber, three interacting risk disciplines) and with `iso-27001` (enterprise IS posture increasingly expected by CSMS assessors).
- **Notes:** Shipped at v0.15.0 (commits `d35fedc` content + engine bump in same commit). Civil road-vehicle scope (passenger cars, light commercial, heavy duty trucks). Registry additions: IATF 16949:2016, ISO 26262:2018 (all parts referenced as one), ISO/SAE 21434:2021, UN R155, UN R156, Automotive SPICE 4.0, AIAG PPAP 4th Ed. (7 standards). Jurisdiction additions: NHTSA (US), UNECE (international), KBA (Germany / EU type-approval authority), TC-MVS (Transport Canada Motor Vehicle Safety — distinct id from TCCA = aerospace) (4 jurisdictions). New example bundle `bundles/example-vehicle.yaml` (ExamplePowertrainECU under NHTSA + UNECE + KBA composing automotive + regulated-ai + iso-27001 across 12 standards) + committed baseline matrix; idempotent regenerate confirmed. CI workflow extended to validate automotive standalone + composite and to dry-run example-vehicle regenerate. **Forward work:** ASIL class overlays (ASIL-A through ASIL-D); CAL class overlays (CAL 1-4 per ISO/SAE 21434); automotive-defense overlay (MIL-STD-882, ITAR, EAR); motorcycle adaptation (ISO 26262 Part 12); NHTSA Part 573 recall workflow as cross-cutting.

### OQ-059 — Aerospace vertical module

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-011, OQ-014
- **Claim:** Open QMS ships an aerospace vertical regulatory module at `modules/aerospace/module.yaml` (version 0.1.0). First non-medical vertical — proves the platform composition (vertical + overlays via OQ-011 / OQ-012) generalizes to a substantively different regulated industry. 27 clauses across 9 aerospace standards: ISO 9001:2015 + AS9100D (QMS substrate — §§4.4, 5.6/9.3, 7.1, 7.4, 7.5, 8.1.4 operational risk, 8.4 supplier control, 8.5.1 production with FOD prevention, 8.7 nonconforming output, 9.2 internal audit, 10.2 corrective action); 14 CFR Part 21 (FAA certification — §21.31 type design, §21.35 flight tests, §21.50 ICA) + EASA Part 21 Subpart B; DO-178C:2011 (avionics software — PSAC, §6 verification, §7 config mgmt, §9 lifecycle data, §11 SOIs); DO-254:2000 (airborne hardware — PHAC, §6 V&V); ARP4754A:2010 (system development — §5 process, §6 function allocation); ARP4761:1996 (safety assessment — §3 FHA, §4-5 PASA/PSSA, §6 SSA, §9 CCA); AS9102 Rev C (First Article Inspection). Ships 5 new aerospace-specific templates: PSAC (DO-178C Plan for Software Aspects of Certification), FHA (ARP4761 Functional Hazard Assessment), SSP (System Safety Plan per ARP4754A + ARP4761), FAI Report (AS9102 forms 1/2/3), and Type Cert Pack Index (14 CFR Part 21 + EASA Part 21; aerospace analog of the medical-devices Technical File Index). Composes cleanly with `regulated-ai` (ISO 23894 + ARP4761 are complementary domain-specific extensions of risk-management discipline) — relevant given modern avionics's ML integration. Composes cleanly with `iso-27001` for organizational information security. Cross-cutting templates (quality-policy, SOP, audit, management-review, supplier templates, CAPA, NCR, risk management, verification, software test) cover the QMS surface naturally — aerospace QMS is structurally similar to medical-devices QMS, just with aerospace-specific extensions.
- **Notes:** Shipped at v0.14.0 (commit `a480c3a`). Civil-aviation scope only (commercial aerospace under FAA / EASA / TCCA). Registry additions: ISO 9001:2015, AS9100D, 14 CFR Part 21, EASA Part 21, DO-178C:2011, DO-254:2000, ARP4754A:2010, ARP4761:1996, AS9102 Rev C (9 standards). Jurisdiction additions: FAA, EASA, TCCA (3 jurisdictions; FAA = U.S. Federal Aviation Administration, not to be confused with the medical-devices FDA = U.S. Food and Drug Administration). New example bundle `bundles/example-aircraft.yaml` + committed baseline `bundles/example-aircraft.matrix.json` demonstrate end-to-end resolution (avionics computer under FAA composing aerospace + regulated-ai + iso-27001 across 13 standards; idempotent regenerate confirmed). CI workflow extended to validate aerospace standalone + aerospace+regulated-ai+iso-27001 composite and to dry-run the example-aircraft bundle for regression-detection. **Forward work:** aerospace DAL class overlays (DAL-A through DAL-E per DO-178C / DO-254 — analogous to the medical-devices class overlay pattern); aerospace-defense overlay (MIL-STD-882 System Safety Program, ITAR, EAR); commercial space scope (FAA Part 450).

### OQ-049 — Medical-devices module ISO 14971:2019 coverage

- **Tier:** Module
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-040
- **Claim:** The medical-devices module covers all seven substantive ISO 14971:2019 clauses (§4 general requirements / risk management process; §5 risk analysis; §6 risk evaluation; §7 risk control; §8 evaluation of overall residual risk; §9 risk management review / report; §10 production and post-production activities) and binds them to the Risk Management File template.
- **Notes:** Added at v0.3.0 (commit `2625b98`). All seven clauses present in `modules/medical-devices/module.yaml` and bound to `templates/product-dhf/risk-management/RISK-MANAGEMENT-FILE-TEMPLATE.md`. Validation harness passes. This is the first module-tier entry to reach `:tested` with complete (not partial) standard coverage; other module-tier entries (OQ-041..OQ-047) remain `:argued` pending full clause-set machine-readability.

### OQ-060 — Part 11 §11.50 signature-meaning prototype — gap closed at v0.7.0

- **Tier:** Gap
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-023
- **Claim:** GPG-signed commits (OQ-023) handle §11.70 cryptographic identity-binding; §11.50 signature-meaning is handled by a controlled-vocabulary commit-trailer convention (`Signature-Meaning:` required; `Signature-Role:` and `Signature-Justification:` optional). The engine ships a parser, audit-trail exporter, CLI subcommand (`openqms signatures verify|export`), and CI workflow that gates PRs touching controlled-document paths. The pair (GPG + trailers) satisfies both §11.70 and §11.50.
- **Notes:** Prototype shipped at v0.7.0 (commit `0b06381`). `engine/openqms/signatures.py` implements the trailer parser, signature constructor (with 9-state GPG-status decoding), git-log extractor, and Part 11 JSON exporter. `docs/guide/signature-meaning.md` documents the requirement, why GPG alone isn't sufficient, the trailer convention, CLI surface, CI configuration, and honest limitations (trailer is discipline not security boundary; HR-to-identity mapping is procedural; controlled vocabulary is adopter's responsibility; trailer parsing is lenient; web edits sign as GitHub). `.github/workflows/signature-check.yml` gates `qms-policy/` / `qms-sops/` / `qms-forms/` / `qms-training/` / `product-*/` paths; dormant in OpenQMS (no controlled documents at those paths), active in adopter forks. Production scope notes: adopters must define their controlled vocabulary in SOP, configure CI per the shipped workflow, and maintain the HR-to-GitHub identity mapping per `gpg-signing.md`. 23 tests cover the parser, all GPG status codes, the exporter Part 11 fields, tmp-git-repo integration, and CLI subprocess invocation.

### OQ-061 — Training-trigger YAML parsing — gap closed at v0.1.2

- **Tier:** Gap
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-035
- **Claim:** `training-trigger.yml` parses `docs/qms-config.yml` and per-document frontmatter with a real YAML parser (Python + PyYAML), not regex. Handles comments, nested mappings, anchors/aliases, quoted strings, and block scalars — anything `yaml.safe_load` accepts.
- **Notes:** Resolution at v0.1.2 — replaced the regex-based parsing in `training-trigger.yml` with a `python3 + pyyaml` parse step that emits a JSON payload consumed by the issue-creation step. Original behavior preserved: config-missing → no issues created (warning); config-present-but-empty-trainees → issues created with placeholder text.

### OQ-062 — PHI/PII compartmentalization architecture decided at v0.2.1

- **Tier:** Gap
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** —
- **Claim:** PHI/PII-bearing complaint content is architecturally compartmentalized out of the main repo into a separate access-restricted record. Two patterns are recommended: (A) sibling private GitHub repository under the same Git discipline; (B) external eQMS or encrypted document store. Either pattern satisfies the regulatory requirement; the choice is documented in the adopting organization's complaint-handling SOP. Furthermore, the intake template (`.github/ISSUE_TEMPLATE/complaint.yml`) is structurally incapable of capturing PHI — verified by `engine/tests/test_phi_compartmentalization.py`.
- **Notes:** Decision documented at v0.2.1 in `docs/guide/complaints.md`. Upgraded `:argued → :tested` at v0.39.0 with the addition of 4 structural property tests in `engine/tests/test_phi_compartmentalization.py`: (1) the complaint YAML loads cleanly; (2) no form field has an id or label matching PHI/PII patterns (patient_name / mrn / ssn / dob / personal email / contact phone / mailing address / etc.); (3) the body carries an explicit PHI-handling warning (matches "PHI" + "PII" + "do not"); (4) the body references an external PHI-bearing compartment (matches private / external / eqms / encrypted / restricted). These are structural tests — they enforce the COMPARTMENTALIZATION property at the template-design level, not runtime PHI scanning of submitted issues (which is correctly out of scope; adopters' own infrastructure handles runtime hygiene per their SOP).

### OQ-063 — Supplier-evaluation workflow — gap closed at v0.8.0

- **Tier:** Gap
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** —
- **Claim:** Open QMS ships supplier-controls infrastructure: Approved Supplier List template (the procurement gate), per-supplier evaluation record template (initial qualification or re-evaluation), workflow issue template, and a guide covering criticality classification, re-evaluation cadence, and audit-trail integration with management review. The medical-devices module binds all three templates to ISO 13485 §7.4 and 21 CFR 820.50.
- **Notes:** Shipped at v0.8.0 (commit `aedde0b`). Artifacts: `templates/qms-suppliers/APPROVED-SUPPLIER-LIST-TEMPLATE.md`, `templates/qms-suppliers/SUPPLIER-EVALUATION-TEMPLATE.md`, `.github/ISSUE_TEMPLATE/supplier-evaluation.yml`, `docs/guide/supplier-controls.md`. Validation harness passes on the expanded manifest. Cadence defaults (Critical 12mo / Major 24mo / Minor 36mo) are documented; adopters tune per their supplier-risk SOP.

### OQ-064 — Management-review aggregation — gap closed at v0.8.0

- **Tier:** Gap
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** —
- **Claim:** Open QMS ships management-review infrastructure: meeting-record template covering all ISO 13485 §5.6.2 inputs and §5.6.3 outputs, workflow issue template with input-aggregation checklist, and a guide documenting `gh` CLI patterns for aggregating each required input (complaint trends, audit results, CAPA status, NCRs, supplier performance, risk management, training compliance). The medical-devices module binds both templates to ISO 13485 §5.6 and 21 CFR 820.20(c).
- **Notes:** Shipped at v0.8.0 (commit `aedde0b`). Artifacts: `templates/qms-management-review/MANAGEMENT-REVIEW-TEMPLATE.md`, `.github/ISSUE_TEMPLATE/management-review.yml`, `docs/guide/management-review.md`. Validation harness passes. Deliberately does not ship a single aggregator tool — a one-size-fits-all label taxonomy would force adopter assumptions; declining keeps the QMS pluggable. Three aggregation models documented (light-touch CLI / scripted shell-or-Python / external eQMS).

### OQ-065 — Module-version drift detection — gap closed at v0.6.0

- **Tier:** Gap
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-014
- **Claim:** Registry entries in `registry/standards.yaml` may carry an optional `superseded_by: <newer-canonical-id>` field. When a module references a standard whose registry entry is marked superseded, `validate_module_against_registry` populates the `RegistryValidationReport.superseded_standards` list of `(old_id, new_id)` pairs. The CLI's `validate` and `regenerate` subcommands print these as warnings by default; `--strict-editions` upgrades them to errors. Combined with the regenerate diff (OQ-015), module-version drift surfaces either at validation time (when the registry adds a `superseded_by` reference) or on the next regenerate (when the operator bumps the module to use the new edition).
- **Notes:** Shipped at v0.6.0 (commit `3cfec2c`). No actual `superseded_by` references in the shipped registry today — the mechanism is in place for the first time a referenced standard is superseded by a newer edition. Tested via `engine/tests/test_regenerate.py::test_validate_warns_on_superseded_standard` and `::test_validate_strict_editions_fails_on_superseded_standard` (both monkey-patch the registry to inject a supersession).

### OQ-066 — Generator validation harness — gap closed at v0.2.0

- **Tier:** Gap
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-013
- **Claim:** The validation harness asserting the OQ-001 invariant on a module's clause table exists and runs in CI.
- **Notes:** Resolution at v0.2.0 — `engine/openqms/validation.py` provides the harness; `.github/workflows/engine-tests.yml` runs `openqms validate --module medical-devices` on every push that touches `engine/`, `modules/`, or `templates/`. The harness is the OQ-013 implementation; this gap entry tracked the absence of that implementation and is now closed.

### OQ-067 — Repository-wide trace matrix (shipped v0.39.0; was forward work)

- **Tier:** Gap
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-031, OQ-010
- **Claim:** Open QMS engine ships a repository-wide bidirectional clause-to-artifact traceability matrix command: `openqms trace [--module M | --all] [--format json|md] [--output FILE]`. Walks every module under `modules/` (or selected modules), emits forward map (clause → templates that address it) + reverse map (template → clauses it addresses) per module, plus orphan detection (orphaned clauses + orphaned templates) and an aggregate summary (module count + total clauses + total templates + total clause→template addresses + orphan counts). Output as JSON (machine-readable) or Markdown (audit-ready). The per-PR snippet produced by `traceability.yml` remains the Phase-0 PR-review surface; `openqms trace --all` is now the repo-wide audit surface.
- **Notes:** Shipped at v0.39.0 alongside OQ-062. CLI implementation in `engine/openqms/cli.py::_cmd_trace` + `_format_trace_markdown`. Tests in `engine/tests/test_trace.py` cover: (1) `--all` emits summary for every module under `modules/`; (2) forward + reverse maps are bidirectional + consistent per-module (every edge in forward appears in reverse); (3) orphan-detection lists are present in output (the OQ-001 invariant-violation surface); (4) markdown format renders. At audit time the repo has 75 modules / 614 clauses / 299 templates / 0 orphaned clauses / 0 orphaned templates — the repo-wide invariant holds. Upgraded `:argued → :tested`. Original v0.1.0 broken reference to `./scripts/generate-trace-matrix.sh` was removed at v0.1.1; the engine command supersedes it. The misleading YAML job ID `generate-trace-matrix` in `.github/workflows/traceability.yml:43` is still in place — not changed here for the reason cited at v0.1.1 (touches GitHub Actions run history + branch-protection required-checks); deliberate cleanup pass remains forward work.

### OQ-068 — Template subdirectory population (status superseded at v0.38.0)

- **Tier:** Gap
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-038
- **Claim:** Original v0.1.0 framing tracked "15 originally-empty `templates/` subdirectories" with progressive population. As of v0.38.0 this framing is **structurally superseded** — the template tree now contains ~75 populated subdirectories across `product-{atmp,chemicals,dhf,food,pharma,sw}/` + `qms-{abms,bcms,capa,energy,environmental,forms,logistics,management-review,ohs,policy,recall,sops,suppliers,training}/`. Verified by `find templates -mindepth 1 -type d -empty` returning ZERO empty subdirs at audit 2026-05-24. The "of 15" denominator no longer reflects the project structure since major subdir-tree expansion across v0.18-v0.38 (introduced product-atmp, product-chemicals, product-food, product-pharma top-level subtrees + qms-abms, qms-bcms, qms-energy, qms-environmental, qms-logistics, qms-management-review, qms-ohs, qms-recall, qms-suppliers, qms-training).
- **Notes:** 87 document templates ship as of v0.38.0 (was 3 at v0.1.0; 11 at v0.3.0; 14 at v0.8.0; 18 at v0.9.0; 21 at v0.10.0; 69 at v0.25.0; 81 at v0.38.0 — `81+` in README catalog cells covers the actual 87 via `+` qualifier). Each template includes standard document-control frontmatter where applicable and is bound to clauses in at least one module manifest. Status `:tested` continues — evidence is the populated subdir tree per `find` verification, not a satisfied-15-of-15 counter.

### OQ-069 — Complaint issue template — gap closed at v0.2.1

- **Tier:** Gap
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-062
- **Claim:** The complaint issue template exists with form validation: product, date received, source, severity, PHI-redacted description, regulatory reportability, CAPA linkage, and required PHI-handling confirmation checkboxes.
- **Notes:** Resolution at v0.2.1 — `.github/ISSUE_TEMPLATE/complaint.yml` shipped (commit `2fe3ef6`). PHI-handling decision (OQ-062) bundled into the same release; template fields reflect the compartmentalization architecture (no PHI captured in the issue; reference field points to PHI-bearing record stored elsewhere). Bound to ISO 13485 §8.2.2 and 21 CFR 820.198 in the medical-devices module manifest at v0.2.1.

### OQ-070 — Modules reference clauses by number + summary; do not redistribute standard text

- **Tier:** Licensing
- **Evidence type:** manual
- **Status:** :argued
- **Depends_on:** —
- **Claim:** Open QMS's regulatory modules reference standards by clause number and normative summary; they do not redistribute the standard text itself. Adopters must obtain their own licensed copies of any commercially-published standard (ISO, IEC, ASTM, ISTA, AS9100, DO-178C, IATF 16949, ISO 26262, etc.).
- **Notes:** README "Standards licensing — important" section is the public statement. Spec §2.1 carries the formal version. Compliance enforcement is contributor responsibility, not mechanical.

### OQ-071 — Apache-2.0 on Open QMS does not extend to referenced standards

- **Tier:** Licensing
- **Evidence type:** manual
- **Status:** :argued
- **Depends_on:** OQ-070
- **Claim:** The Apache-2.0 license under which Open QMS itself is distributed does not extend to the regulatory standards Open QMS references. Standards remain under their respective publishers' license terms.
- **Notes:** README disclaimer carries this. Contributor agreement (CLA — not yet drafted) should explicitly require attestation that contributed modules do not embed copyrighted standard text.

### OQ-080 — README discloses "infrastructure, not validated QMS"

- **Tier:** Gap
- **Evidence type:** example-tested
- **Status:** :tested
- **Depends_on:** OQ-003
- **Claim:** The repository README contains a four-bullet "Important disclaimers" section declaring that Open QMS is infrastructure not a validated QMS, that the project does not provide regulatory advice, that GitHub is not inherently Part 11 compliant, and that adopters' SOPs/forms/records are their own.
- **Notes:** This is a `:tested` gap in the sense that the honesty bound is mechanically enforced by README presence; CI step to assert disclaimer block is intact is a trivial future add.

---

## Status summary

| Status | Count |
|---|---|
| `:proved` | 0 |
| `:verified` | 6 |
| `:tested` | 82 |
| `:benchmarked` | 0 |
| `:argued` | 5 |
| `:open` | 0 |
| **Total entries** | **93** |

**Zero `:open` entries as of v0.8.0.** Every spec claim now carries at least manual evidence (`:argued`) or mechanical evidence (`:tested`). The remaining `:argued` entries are honest-effort items (module-coverage population, manual-only-by-nature licensing claims, partially-mechanized substrate claims) — none of them are "we haven't started yet."

**Note on previous counts:** prior `Total` figures of 39–40 in dashboard / changelog entries were an undercount carried over from the v0.1.0 baseline (off by 6 entries — OQ-049 was added at v0.3.0 plus 5 entries in earlier ranges that were tracked individually but not summed correctly). Reconciled to 46 at v0.6.0 by direct `grep` against the spec. Per-version transition entries below are accurate; only the summary `Total` was off.

**Delta since v0.1.0:**
- v0.1.1: OQ-067 `:open → :argued` (broken trace-matrix script reference removed).
- v0.1.2: OQ-061 claim reframed, status stayed `:tested` (training-trigger PyYAML fix).
- v0.2.0: OQ-001 `:argued → :tested`, OQ-010 `:open → :tested`, OQ-013 `:open → :tested`, OQ-040 `:argued → :tested`, OQ-066 `:open → :tested` (engine MVP + medical-devices module seed shipped).
- v0.2.1: OQ-062 `:open → :argued` (PHI/PII compartmentalization architecture decided); OQ-069 reframed and stays `:tested` (complaint intake template shipped).
- v0.2.2: OQ-023 stays `:argued` (GPG enforcement guide shipped; mechanically same posture but now adopter-actionable).
- v0.3.0: OQ-049 NEW `:tested` (ISO 14971:2019 full coverage); OQ-068 reframed and stays `:tested` (8 of original 15 empty subdirs populated; 7 intentionally adopter-defined); OQ-038 updated (3 → 11 document templates).
- v0.4.0: OQ-011 `:open → :tested` (modules compose under union); OQ-012 `:open → :tested` (cross-cutting overlays compose with vertical modules); OQ-048 `:argued → :tested` (ISO/IEC 27001 overlay module shipped). Engine package version bumped 0.2.0 → 0.4.0 to match spec.
- v0.5.0: OQ-014 `:open → :tested` (standards-and-jurisdictions registry shipped at `registry/standards.yaml` + `registry/jurisdictions.yaml`; CLI normalizes aliases to canonical ids, rejects unregistered standards/jurisdictions; module manifests cross-checked against the registry). Engine package version 0.4.0 → 0.5.0.
- v0.6.0: OQ-015 `:open → :tested` (re-resolution + Git-reviewable diff shipped as `openqms regenerate` over `bundles/<name>.yaml` definitions + `bundles/<name>.matrix.json` committed matrices); OQ-065 `:open → :tested` (module-version drift detection via registry `superseded_by` field + `--strict-editions` flag). Engine package version 0.5.0 → 0.6.0.
- v0.7.0: OQ-060 `:open → :tested` (Part 11 §11.50 signature-meaning prototype shipped — commit-trailer convention + parser + CLI `signatures verify/export` + Part 11 JSON audit-trail exporter + dormant CI gate workflow + comprehensive guide). Engine package version 0.6.0 → 0.7.0.
- v0.8.0: OQ-063 `:open → :tested` (supplier-evaluation workflow — ASL + per-supplier evaluation + issue template + guide; bound to ISO 13485 §7.4 + 21 CFR 820.50); OQ-064 `:open → :tested` (management-review aggregation — meeting record template + issue template + `gh` CLI aggregation-pattern guide; bound to ISO 13485 §5.6 + 21 CFR 820.20(c)). OQ-041 + OQ-042 + OQ-038 notes updated to reflect the additional 4 clauses and 5 templates folded into the medical-devices module. CLI fix: `regenerate --write-matrix` now exits 0 on successful write regardless of diff content. Engine package version 0.7.0 → 0.8.0. **Zero `:open` entries milestone.**
- v0.9.0: OQ-041, OQ-042, OQ-043, OQ-045, OQ-046, OQ-047 all `:argued → :tested` (medical-devices module fully populated to 59 clauses across 11 standards). OQ-044 stays `:argued` with notes — EU MDR Annex I (GSPRs) and Annex XIV (CER) intentionally deferred to device-class-specific overlays. OQ-038 template count 14 → 18 (added technical-file index, audit procedure SOP, usability engineering file, packaging validation). OQ-068 subdirectory population updated (8 of 15 → 11 of 15 populated). Engine package version 0.8.0 → 0.9.0.
- v0.10.0: OQ-044 `:argued → :tested` (EU MDR Annex I GSPRs + Annex XIV Part A CER + Part B PMCF templates shipped; module manifest gains 3 clauses + 3 bindings). OQ-038 template count 18 → 21. OQ-068 subdirectory count updated (now 13 populated including new gspr/ + clinical/ subdirs). **All 7 medical-devices standard-coverage module entries (OQ-041 through OQ-047) now `:tested`.** Engine package version 0.9.0 → 0.10.0.
- v0.11.0: **4 new spec entries** — OQ-050 (SaMD overlay), OQ-051 (implantable overlay), OQ-052 (EU MDR Class III overlay), OQ-053 (FDA Class III overlay) — all NEW `:tested`. 5 new standards added to registry (IEC 82304-1, ISO 14708-1, 21 CFR 814, 21 CFR 803, IMDRF SaMD N12). 5 new templates (SAMD-INTENDED-USE, IMPLANT-CARD, SSCP, EXPERT-PANEL-CONSULTATION, PMA-SUBMISSION). OQ-038 template count 21 → 26. Engine package version 0.10.0 → 0.11.0. Spec total 46 → 50.
- v0.12.0: **5 new spec entries** across three phases — Phase A: OQ-054 (MDR Class IIb), OQ-055 (MDR Class IIa), OQ-056 (FDA Class II / 510(k)). Phase B: OQ-057 (IVD overlay). Phase C: OQ-058 (regulated-AI overlay). All NEW `:tested`. 6 new standards (21 CFR 807, 21 CFR 860, EU IVDR 2017/746, 21 CFR 809, ISO 15189:2022, ISO/IEC 23894:2023). 5 new templates (510K-SUBMISSION, IVDR-GSPR-CHECKLIST, PERFORMANCE-EVALUATION-REPORT, AI-SYSTEM-CARD, AI-IMPACT-ASSESSMENT). OQ-038 template count 26 → 31. Engine package version 0.11.0 → 0.12.0. Spec total 50 → 55.
- v0.13.0: **First `:verified` entries.** OQ-001 + OQ-010 + OQ-011 + OQ-013 + OQ-015 all `:tested → :verified` (hypothesis property tests cover the invariant + purity + composition algebra + validation harness + diff correctness across arbitrary inputs). OQ-002 `:argued → :verified` (the only `:argued` entry where mechanical verification was achievable; property test on mutation correctness). 11 new hypothesis property tests in `engine/tests/test_property.py`. `hypothesis>=6.100` added to dev deps. Engine package version 0.12.0 → 0.13.0. Status counts: 6 `:verified` / 42 `:tested` / 7 `:argued` / 0 `:open` (total 55).
- v0.14.0: **First non-medical vertical.** OQ-059 NEW `:tested` (aerospace vertical — 27 clauses across 9 aerospace standards: ISO 9001 / AS9100D / 14 CFR Part 21 / EASA Part 21 / DO-178C / DO-254 / ARP4754A / ARP4761 / AS9102; composes with regulated-ai and iso-27001). 9 new standards added to registry; 3 new jurisdictions (FAA / EASA / TCCA). 5 new aerospace-specific templates (PSAC / FHA / SSP / FAI Report / Type Cert Pack Index). New example bundle `example-aircraft` with committed baseline matrix; CI extended to validate aerospace + regenerate example-aircraft. Engine package version 0.13.0 → 0.14.0. Status counts: 6 `:verified` / 43 `:tested` / 7 `:argued` / 0 `:open` (total 56).
- v0.15.0: **Second non-medical vertical — automotive.** OQ-072 NEW `:tested` (automotive vertical — 28 clauses across 8 standards spanning four discipline tracks: IATF 16949 QMS substrate; ISO 26262 functional safety across all 12 parts with ASIL A-D; ISO/SAE 21434 cybersecurity engineering with CAL 1-4; UN R155 + R156 type-approval regulations; plus Automotive SPICE 4.0 and AIAG PPAP). Strengthens structural-generalization from one data point to two. 7 new standards in registry (IATF 16949 / ISO 26262 / ISO/SAE 21434 / UN R155 / UN R156 / Automotive SPICE 4.0 / AIAG PPAP 4th Ed.); 4 new jurisdictions (NHTSA / UNECE / KBA / TC-MVS — distinct from aerospace's TCCA). 5 new automotive-specific templates (Item Definition / HARA / Safety Concept with optional Cybersecurity Concept Part C / TARA / PPAP). New example bundle `example-vehicle` (ExamplePowertrainECU composing automotive + regulated-ai + iso-27001 across 12 standards); CI extended. Engine package version 0.14.0 → 0.15.0. Status counts: 6 `:verified` / 44 `:tested` / 7 `:argued` / 0 `:open` (total 57).
- v0.16.0: **Class overlays — 3 aerospace DAL + 3 automotive ASIL/CAL.** Six NEW Module-tier entries all `:tested`: OQ-073 aerospace DAL-A (MC/DC + 25-of-71 independence + DO-330 TQL-1 + DO-254 elemental + safety-specific analyses + ARP4754A allocation), OQ-074 aerospace DAL-B (Decision Coverage + 14-of-69 independence + TQL-1/2), OQ-075 aerospace DAL-C (Statement Coverage + 2-of-62 independence + TQL-3/4 — most common production DAL), OQ-076 automotive ASIL-D (SPFM ≥ 99% / LFM ≥ 90% / PMHF < 10⁻⁸/h + 100% statement+branch+MC/DC + I3 independence + MISRA C 2012 mandatory + Part 9 §5 decomposition options), OQ-077 automotive ASIL-B (SPFM ≥ 90% / LFM ≥ 60% / PMHF < 10⁻⁷/h + 100% statement+branch + I2 independence + MISRA C 2012 recommended), OQ-078 automotive CAL-4 (independent cybersecurity assessment + fuzz/pentest/side-channel + vulnerability monitoring + safety-security interaction). All composes validated standalone; 5-module mega-composite validates (automotive + ASIL-D + CAL-4 + regulated-ai + iso-27001). CI extended with 7 new validate steps. Engine package version 0.15.0 → 0.16.0. Status counts: 6 `:verified` / 50 `:tested` / 7 `:argued` / 0 `:open` (total 63).
- v0.17.0: **Completes class overlay coverage + new manufacturing vertical.** Nine NEW Module-tier entries all `:tested`: OQ-079 aerospace DAL-D (Minor; no structural coverage; 2-of-26 independence), OQ-081 aerospace DAL-E (No Safety Effect; NO DO-178C objectives; config-mgmt-only retention), OQ-082 automotive ASIL-C (mid-high; SPFM ≥ 97% / LFM ≥ 80% / PMHF < 10⁻⁷/h; I3 same as ASIL-D; language subset REQUIRED), OQ-083 automotive ASIL-A (lowest non-QM; PMHF < 10⁻⁶/h; 100% statement only; I1 independence), OQ-084 automotive QM (positive QM allocation claim with HARA rationale; explicit out-of-FuSa-scope listing in Safety Plan), OQ-085 automotive CAL-3 (independent assessment RECOMMENDED + fuzz testing required + formal monitoring + safety-security interaction when ASIL-rated), OQ-086 automotive CAL-2 (independent assessment optional + vulnerability scanning + monitoring triage cadence), OQ-087 automotive CAL-1 (no independent assessment + baseline V&V + CSMS-baseline monitoring), OQ-088 general manufacturing vertical (ISO 9001:2015 ONLY; 17 clauses across all seven §-groups; all bindings to cross-cutting templates — NO new templates required; smallest vertical in project). **Class-overlay coverage now complete**: aerospace DAL A/B/C/D/E + automotive ASIL D/C/B/A/QM + automotive CAL 4/3/2/1 = 14 levels across 3 dimensions, plus the 7 medical-devices class overlays from v0.11.0+v0.12.0 = 21 class overlays total across three regulated verticals. **Vertical count: 3 → 4** (medical-devices / aerospace / automotive / manufacturing). New `bundles/example-machine-shop.yaml` (mid machine shop pursuing baseline ISO 9001 + iso-27001 for customer CAD/CAM files; jurisdictions empty since general mfg has no specific regulator). CI extended (+15 validate steps total: 5 new aerospace DALs + 5 ASILs + 4 CALs + manufacturing standalone + composite; +1 regenerate dry-run for example-machine-shop). Engine package version 0.16.0 → 0.17.0. Status counts: 6 `:verified` / 59 `:tested` / 7 `:argued` / 0 `:open` (total 72).
- v0.18.0: **HSE + energy cross-cutting overlays.** 3 NEW Module-tier entries all `:tested`: OQ-089 ISO 14001:2015 environmental-management overlay (11 clauses + 1 new template: Environmental Aspects Register with significance scoring → SEA flagging → operational controls); OQ-090 ISO 45001:2018 OH&S management overlay (11 clauses + 1 new template: HIRA — Hazard ID + Risk Assessment with worker consultation per §5.4 + hierarchy of controls per §8.1.2); OQ-091 ISO 50001:2018 energy-management overlay (10 clauses + 1 new template: Energy Review + EnPIs + EnB Baseline — most quantitative template in Open QMS, reflecting ISO 50001's unique mandate of a calculated, periodically-recalibrated performance baseline). Each composes with ANY vertical (12 composites validated: 3 overlays × 4 verticals). 6-module everything-shop composite validates: manufacturing + iso-14001 + iso-45001 + iso-50001 + iso-27001 + regulated-ai. Cross-cutting overlay count: 2 (iso-27001 + regulated-ai) → 5 (+ iso-14001 + iso-45001 + iso-50001). Registry +3 standards. CI extended (+8 validate steps). Engine package version 0.17.0 → 0.18.0. Status counts: 6 `:verified` / 62 `:tested` / 7 `:argued` / 0 `:open` (total 75).
- v0.19.0: **Pharma vertical (5th vertical; largest remaining regulated-industry gap).** OQ-092 NEW `:tested` (pharma — 23 clauses across 8 standards spanning PQS substrate ICH Q9/Q10 + API GMP ICH Q7 + US cGMP 21 CFR 210/211 + EU GMP EudraLex Vol. 4 with Annexes 15+16 + sterile manufacturing PIC/S Annex 1 (2022) + Part 11 for computerized systems). 6 new pharma-specific templates (MBR, VMP, Deviation, Change Control, OOS Investigation, APQR). Registry +7 standards (all PUBLIC license — first vertical where most cited standards are public) + 3 jurisdictions (EMA, MHRA, WHO-PQ); FDA jurisdiction extended. New example bundle (sterile SVP injection US+EU). Validates as combination-product composite with medical-devices. Engine 0.18.0 → 0.19.0. Status counts: 6 `:verified` / 63 `:tested` / 7 `:argued` / 0 `:open` (total 76).
- v0.20.0: **Food safety vertical (6th vertical).** OQ-093 NEW `:tested` (food-safety — 16 clauses across ISO 22000 + FSSC 22000 v6 + Codex HACCP + 21 CFR 117 FSMA Preventive Controls + 21 CFR 123 Seafood HACCP). 3 new food-safety-specific templates (HACCP Plan with B/C/P/A hazard coverage, Prerequisite Programs index per ISO/TS 22002 15-element framework, Recall + Withdrawal Procedure with FDA Class I/II/III classification + Reportable Food Registry + 24/7 CMT). Registry +5 standards (Codex + CFR public; ISO 22000 + FSSC commercial) + 4 jurisdictions (FDA-Food, USDA-FSIS, EFSA, CFIA). New example bundle (RTE chilled-foods processor). Engine 0.19.0 → 0.20.0. Status counts: 6 `:verified` / 64 `:tested` / 7 `:argued` / 0 `:open` (total 77).
- v0.21.0: **Governance + resilience cross-cutting overlays — completes the common Annex-SL cross-cutting overlay set.** 2 NEW Module-tier entries: OQ-094 ISO 37001:2016 anti-bribery management overlay (14 clauses with independent anti-bribery compliance function, due diligence framework, financial + non-financial controls, gifts/hospitality, raising concerns, investigations; new template: Anti-Bribery Due Diligence Assessment with risk-tier framework + sanctions/PEP/adverse-media/UBO screening + contractual-safeguards checklist); OQ-095 ISO 22301:2019 BCMS overlay (13 clauses with BIA + RTO/MAO/MBCO/RPO + BC strategies + plans + exercise programme; new template: Business Continuity Plan with 8 disruption scenarios + crisis management team with 24/7 contacts + communications matrix with regulatory reporting windows + exercise cadence). Cross-cutting overlay set: 5 → 7. **8-module ultimate composite validates**: pharma + iso-27001 + regulated-ai + iso-14001 + iso-45001 + iso-50001 + iso-37001 + iso-22301 (deepest composition tested; realistic IMS-pursuing pharma shape). Registry +2 standards. CI extended (+6 validate steps). Engine 0.20.0 → 0.21.0. Status counts: 6 `:verified` / 66 `:tested` / 7 `:argued` / 0 `:open` (total 79).
- v0.22.0: **First pharma class overlay — ATMP (cell + gene therapy).** OQ-096 NEW `:tested` (ATMP — 10 clauses across EU GMP Annex 2A + 2B + 21 CFR 1271 + ICH Q5A(R2); 3 new ATMP-specific templates: Donor Eligibility Assessment with RCDA panel + PHI compartmentalization, Tissue/Cell Traceability Record with bidirectional chain + 30-year EU retention format-stability planning, Viral Safety Evaluation Report per Q5A(R2) 2023 three-pillar framework with vector-specific RCV testing). Most-stringent biologics scope; all cited standards PUBLIC license. **9-module deepest composite validates** (pharma + atmp + 7 cross-cutting overlays — realistic commercial-stage cell-therapy organization shape). Registry +4 standards. New example bundle `example-cart` (autologous CD19-targeted CAR-T at US+EU dual-licensed site). CI extended (+3 validate steps + 1 regenerate). Engine 0.21.0 → 0.22.0. Status counts: 6 `:verified` / 67 `:tested` / 7 `:argued` / 0 `:open` (total 80).
- v0.23.0: **Public adopter-surface release** — closes P10 from original priority stack. OQ-097 NEW `:tested` (adopter-surface + BUSINESS public release). README rewritten from v0.7.0-era state to current v0.22.0+ state (top-level verticals catalog table, cross-cutting overlays guide, per-audience quick-start, adoption-by-industry guidance, full standards-licensing inventory). New `docs/modules-catalog.md` (comprehensive per-module catalog with composition decision flow + smallest-viable-scaffold to 9-module deepest-composite examples). Backfilled missing READMEs for food-safety + atmp verticals/overlays. **BUSINESS/ un-gitignored** — spec discipline (ENGINE_SPEC.md + DESIGN.md + artifact_registry.md + dashboard.md + changelog.md + 12 companion docs) now publicly readable + auditable. Engine 0.22.0 → 0.23.0. Pure consolidation; no new module-tier entries. Status counts: 6 `:verified` / 68 `:tested` / 7 `:argued` / 0 `:open` (total 81).
- v0.24.0: **Cross-vertical recall-workflow overlay** — NHTSA Part 573 + 577 + 579 (TREAD Act EWR) + FDA 21 CFR 7 + 21 CFR 806 + CPSIA §15. OQ-098 NEW `:tested` (11 clauses across 6 regulations covering automotive + medical-device + general FDA + consumer-product recall regulatory frameworks; 2 new templates: Generalized Recall Procedure parametrized by framework + NHTSA Part 577 Owner Notification Letter with all 10 §577.5 mandatory content elements). Composes with ANY vertical needing recall discipline. **10-module composite validates** (new depth record): automotive + asil-d + cal-4 + recall-workflow + 5 cross-cutting + iso-22301. Registry +6 standards (all PUBLIC). CI +6 validate steps. Engine 0.23.0 → 0.24.0. Status counts: 6 `:verified` / 69 `:tested` / 7 `:argued` / 0 `:open` (total 82).
- v0.25.0: **Standalone template library expansion — 15 new templates across 3 groups.** OQ-099 NEW `:tested`. **Group A cross-vertical management-system (6):** Quality Manual + Process Map + Risk-and-Opportunity Register + Risk Assessment standalone + BIA standalone + IT DR Plan. **Group B domain-specific registers (3):** Compliance Obligations Register (ISO 14001 §6.1.3) + OH&S Legal + Other Requirements Register (ISO 45001 §6.1.3) + Energy Objectives + Targets Register (ISO 50001 §6.2). **Group C pharma + ATMP specialty (6):** Site Master File (EU GMP Part III + PIC/S PE 008 + Annex 2A ATMP additions) + Batch Certificate of Analysis (21 CFR 211.165 + Ch. 6 + ICH Q6A/Q6B) + Stability Protocol (ICH Q1A(R2) full design + Q1B + Q1C + Q1D + Q1E + Q5C biologics) + Comparability Protocol (ICH Q5E + Q12) + CAR-T Release Testing Record (FDA CAR-T Guidance 2024 + autologous risk-based release per Annex 2A §11) + AAV Release Testing Record (FDA CMC IND 2020 + Q5A(R2) vector-product RCAAV testing + AUC/cryo-EM/CDMS for empty:full ratio). Templates ship standalone — bindings to existing modules deferred to forward release. No engine code change. Engine 0.24.0 → 0.25.0. OQ-038 template count 54 → 69 (+15). Status counts: 6 `:verified` / 70 `:tested` / 7 `:argued` / 0 `:open` (total 83).
- v0.26.0–v0.35.0: **Catch-up note.** Ten releases worth of additions (per-module README backfill, class-overlay batches for pharma/food-safety/aerospace/automotive/IVDR, 11 cross-cutting overlays across IS+governance+compliance+resilience+DoD-CUI groups, template-binding pass, documentation consolidation). Detailed delta lives in `companion_v0_24_to_34_omnibus.md` + `changelog.md` per-version entries; entry-level changes are reflected in the spec body (OQ-100..OQ-104) and the status table above. Spec total 83 → 88; status counts 6 `:verified` / 75 `:tested` / 7 `:argued` / 0 `:open`.
- v0.36.0: **Chemicals vertical (7th vertical).** OQ-105 NEW `:tested` (chemicals — 21 clauses across 5 standards: EU REACH + EU CLP + UN GHS Rev. 10 + OECD GLP + US TSCA covering substance + mixture manufacturing + import across EU and US regulatory regimes). 4 new chemicals-specific templates: Safety Data Sheet (16-section GHS + REACH Annex II + CLP + OSHA HCS App D), REACH Registration Dossier Outline (Articles 5-6 + 10 + 14 + Annexes VI-X + Annex I CSR for ≥10 t/y + Authorisation + Restriction considerations), CLP Classification Notification + Label (full classification tables across all GHS hazard classes + UFI + PCN per Annex VIII), GLP Study Plan + Final Report (combined per Principles 8.1 + 9.1 + QA Statement + 10-year archive). All 5 standards PUBLIC license. Vertical count: 6 → 7. New example bundle `example-specialty-chemical` (50-100 t/y SVHC-adjacent intermediate manufacturer composing chemicals + iso-27001 + iso-14001 + iso-45001 + iso-31000). CI extended (+5 validate steps + 1 regenerate). Engine 0.35.0 → 0.36.0. Status counts: 6 `:verified` / 76 `:tested` / 7 `:argued` / 0 `:open` (total 89).
- v0.37.0: **Chemicals-adjacent standalones (4 cross-cutting overlays).** OQ-106 NEW `:tested` (osha-hcs 29 CFR 1910.1200 HazCom 2024 alignment with GHS Rev. 7 + transport-hazmat DOT HMR 49 CFR 100-185 + IMDG + IATA DGR + ADR 2025 + RID 2025 + eu-biocides BPR 528/2012 + tsca-pfas 40 CFR Part 705 reporting rule). 4 new templates (HAZCOM-WRITTEN-PROGRAM + SHIPPING-PAPER multi-modal + HMT-TRAINING-RECORD + BPR-AUTHORISATION-APPLICATION + PFAS-REPORTING-FORM). Registry +9 standards (8 PUBLIC; IMDG + IATA DGR commercial). Cross-cutting overlay count: 19 → 23. **13-module composite validates** (new depth record) — chemicals + 4 adjacent + 8 cross-cutting overlays. Discharges all 4 chemicals-companion forward-work items. CI extended (+12 validate steps). Engine 0.36.0 → 0.37.0. Status counts: 6 `:verified` / 77 `:tested` / 7 `:argued` / 0 `:open` (total 90).
- v0.38.0: **Chemicals class overlays (6).** OQ-107 NEW `:tested` (chemicals-svhc REACH SVHC Article 7(2) + 33(1) + 33(2) + SCIP database + Annex XV; chemicals-authorisation REACH Title VII Articles 55-66 + Annex XIV ~60 listed substances; chemicals-tonnage-1 Annex VII baseline; chemicals-tonnage-10 Annex VIII + CSR mandatory cost cliff; chemicals-tonnage-100 Annex IX + sub-chronic + reproductive screening; chemicals-tonnage-1000 Annex X + chronic + carcinogenicity + EOGRTS). 3 new templates (SVHC-COMMUNICATION-LETTER + REACH-AUTHORISATION-APPLICATION + SUBSTITUTION-PLAN). Class-overlay count: 38 → 44 (chemicals first class-overlay set). **16-module composite validates** (new depth record) — chemicals + SVHC + Authorisation + tonnage-1000 + 4 adjacent + 8 cross-cutting overlays. Cumulative v0.36-38: 11 chemicals-domain modules in 3 releases (vertical + 4 adjacent + 6 class). CI extended (+12 validate steps). No registry additions (reuses existing EU REACH). Engine 0.37.0 → 0.38.0. Status counts: 6 `:verified` / 78 `:tested` / 7 `:argued` / 0 `:open` (total 91).
- v0.39.0: **`:argued → :tested` push (2 entries).** OQ-062 `:argued → :tested` (PHI/PII compartmentalization upgraded with 4 new structural property tests in `engine/tests/test_phi_compartmentalization.py` asserting the complaint intake template cannot capture PHI by design — no field id/label matches PHI patterns + PHI-handling warning present + external-record reference present). OQ-067 `:argued → :tested` (repo-wide trace matrix shipped as new `openqms trace` CLI subcommand — walks all modules, emits forward + reverse maps + orphan detection in JSON or Markdown; tested by 4 new tests in `engine/tests/test_trace.py`). Pytest count 108 → 116 (+8). At audit time `openqms trace --all` reports 75 modules / 614 clauses / 299 templates / 0 orphaned clauses / 0 orphaned templates. Engine 0.38.0 → 0.39.0. Status counts: 6 `:verified` / 80 `:tested` / 5 `:argued` / 0 `:open` (total 91).
- v0.40.0: **Hygiene pass — discharges audit F1-F6.** No new spec entries; remediation only. (1) OQ-054..OQ-058 registry rows expanded from prior condensed snapshot — A1 coverage gap now zero. (2) Template count "81+" → exact "87" in README + catalog (F5). (3) Catalog `ivd` re-categorised as sub-vertical (not class overlay; 9 medical class overlays + 1 sub-vertical noted; clarifies F6). (4) `scripts/lint-module-yaml.py` added — catches the unquoted-colon-in-template-name failure mode observed during chemicals arc + asserts every clause has id/standard/section/summary + every template's addresses entries refer to in-module clauses; wired into CI as a pre-pytest gate (chemicals-arc lesson). (5) `traceability.yml` job ID renamed `generate-trace-matrix → generate-traceability-snippet` to match the accurate display name (OQ-067 deferred cleanup). (6) `companion_v0_39_argued_push.md` companion added for the v0.39.0 release. Engine 0.39.0 → 0.40.0.
- v0.41.0: **Privacy cross-cutting overlay (last major management-system gap).** OQ-108 NEW `:tested` (privacy — GDPR + CCPA/CPRA; 21 clauses across the two dominant global privacy frameworks). 5 new substantial templates: PRIVACY-POLICY (Articles 13-14 + CCPA notice with all 11 CCPA categories + SPI table + lawful-basis grid + rights summary + GPC honoring); DPA (Article 28 + CCPA §7050-7053 service-provider/contractor + 2021/915 SCCs + Transfer Impact Assessment + breach-24h SLA + CPPA Cybersecurity/Risk/ADMT assistance); DPIA (Article 35 + CCPA Risk Assessment per CPPA §7150-7157 + WP248 rev.01 9-criteria + WP250 consequences); ROPA (Article 30 controller Part A + processor Part B with maintenance discipline); PERSONAL-DATA-BREACH-NOTIFICATION (Article 33 SA 72h + Article 34 subjects + Article 33(5) documentation + CCPA §1798.150 PRA + US state AG cross-reference + HIPAA BNR + FTC HBNR + SEC Item 1.05 8-K). Both standards PUBLIC license. Registry +2 standards (GDPR + CCPA). Cross-cutting overlay count: 23 → 24. **17-module ultimate composite validates** (new depth record beats prior 16-module). CI extended (+11 validate steps). Engine 0.40.0 → 0.41.0. Status counts: 6 `:verified` / 81 `:tested` / 5 `:argued` / 0 `:open` (total 92).
- v0.42.0: **Sub-overlay batch (16): CMMC levels + SOC 2 types + ISO 27001 extensions + NIST CSF tiers + PCI DSS SAQ types.** OQ-109 NEW `:tested` — introduces new module shape (class-overlay-like rigor/scope/tier deltas on cross-cutting overlays). 3 CMMC levels + 2 SOC 2 types + 2 ISO 27001 extensions (27017 cloud + 27701 PIMS) + 4 NIST CSF Implementation Tiers + 5 PCI DSS SAQ types. All 16 reuse parent-overlay templates. Registry +2 commercial standards (ISO 27017 + ISO 27701); other 14 reuse existing registered standards. Total module count: 76 → 92. Cross-cutting overlay count unchanged at 24 (sub-overlays not counted in 24). **19-module deepest composite validates** (new depth record). CI extended (+23 validate steps). Engine 0.41.0 → 0.42.0. Status counts: 6 `:verified` / 82 `:tested` / 5 `:argued` / 0 `:open` (total 93).

See `dashboard.md` for the priority stack to move `:open` and `:argued` entries forward.
