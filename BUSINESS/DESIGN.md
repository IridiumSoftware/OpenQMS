# DESIGN — Open QMS

**Version:** v0.12.0 DRAFT
**Date:** 2026-05-23
**Maintainer:** Aaron Green

Authoritative architectural narrative. Defers to `ENGINE_SPEC.md` on what is *established*; this document captures *intent*. For permanent build-record per session, see `companion_*.md` files (index at `companion_index.md`).

---

## 1. Purpose

Open QMS is an open-source, GitHub-native **generator** for regulated-industry Quality Management Systems. Given a tuple of `(product, jurisdiction-set, standards-set)` plus the regulatory modules in scope, the generator emits an unvalidated MVP QMS — repository structure, SOPs, design history file scaffolding, software lifecycle artifacts, CAPA workflows, training matrices, supplier controls, technical-file structure — with complete bidirectional traceability between in-scope regulatory clauses and the generated artifacts.

The intent is dual:

- **For established organizations.** A reference QMS scaffold to compare against an existing QMS in order to surface novel efficiency ideas, missing artifacts, or simpler workflows.
- **For new teams.** A starting QMS that is rigorous about clause coverage and explicit about its own gaps, ready to be adopted, validated, and extended by the consuming organization.

Open QMS is released under Apache-2.0. It is infrastructure, not a validated quality system; validation for any intended use is the consuming organization's responsibility.

## 2. Scope

Open QMS covers the use of GitHub (cloud or enterprise) as the primary platform for:

- Document control (SOPs, work instructions, forms, templates)
- Design history file (DHF) management
- Design control traceability (inputs → outputs → verification → validation)
- Software development lifecycle documentation (per IEC 62304 and equivalent industry standards)
- Change control and CAPA record management
- Complaint and nonconformance record retention
- Packaging and shipping validation documentation
- Supplier and purchasing controls documentation
- Technical file / design dossier / submission-pack assembly for regulatory submissions

The platform model is multi-product and multi-jurisdiction. A single organizational instance of Open QMS may host many products simultaneously, each assigned to its own `(jurisdiction-set, standards-set, modules-set)` bundle. As products evolve — e.g. a research-use-only tool crossing the threshold into a regulated classification — the operator reassigns the product's regulatory buckets and the engine re-resolves the artifact set under the new scope, preserving the traceability invariant by reconstruction. Git history captures every mutation as part of the audit trail.

### 2.1 What ships today (v0.12.0)

**Engine** (`engine/openqms/`, Python 3.11+, Apache-2.0):

- Bundle resolver — pure function from `(Bundle, Module) → ResolvedQMS` (OQ-010).
- Per-module validation harness — asserts the OQ-001 invariant (OQ-013).
- Composition primitive — `compose(list[Module]) → Module` (OQ-011, OQ-012).
- Standards-and-jurisdictions registry — `registry/standards.yaml` + `registry/jurisdictions.yaml`, strict CLI validation, alias normalization, supersession field (OQ-014, OQ-065).
- Regenerate workflow — `openqms regenerate --bundle <name>` re-resolves stored bundle definitions and emits structured diff against `bundles/<name>.matrix.json` (OQ-015).
- Signature-meaning prototype — commit-trailer convention + parser + Part-11-format audit-trail exporter + dormant CI gate (OQ-060).
- CLI — `resolve`, `validate`, `regenerate`, `registry list/show`, `signatures verify/export`.

**Regulatory modules** (11 total):

- 1 vertical: `medical-devices` (62 clauses across 11 standards).
- 4 device-class/category overlays: `samd`, `implantable`, `mdr-class-iii`, `fda-class-iii`.
- 3 additional class overlays: `mdr-class-iib`, `mdr-class-iia`, `fda-class-ii`.
- 1 IVD overlay: `ivd` (IVDR + 21 CFR 809 + ISO 15189; cross-cutting, composes with medical-devices with adopters declaring MDR clauses NA per IVD scope).
- 1 regulated-AI cross-cutting overlay: `regulated-ai` (NIST AI RMF + EU AI Act + ISO 42001 + ISO 23894). Composes with any vertical.
- 1 infosec cross-cutting overlay: `iso-27001`.

**Templates** (31 document templates + 5 issue templates):

- Organizational: quality-policy, SOP, audit-procedure, approved-supplier-list, supplier-evaluation, management-review.
- Product DHF: design-input, design-outputs (placeholder), risk-management-file, verification-protocol, validation-protocol, technical-file-index, usability-engineering-file, packaging-validation, gspr-conformity-checklist, clinical-evaluation, pmcf-plan, samd-intended-use, implant-card, sscp, expert-panel-consultation, pma-submission, 510k-submission, ivdr-gspr-checklist, performance-evaluation-report, ai-system-card, ai-impact-assessment.
- Product software: software-requirements, software-architecture, soup-register, software-test-protocol, software-release.
- Issue templates: CAPA, change-request, design-input, nonconformance, complaint, supplier-evaluation, management-review.

**CI workflows** (`.github/workflows/`):

- `doc-control.yml` — required-frontmatter validation on controlled-document PRs.
- `traceability.yml` — issue-PR linkage check; per-PR snippet.
- `release-gate.yml` — release-tag completeness gating.
- `training-trigger.yml` — controlled-doc revision triggers training assignment issues (PyYAML-parsed).
- `deploy-docs.yml` — MkDocs publish to GitHub Pages.
- `engine-tests.yml` — pytest + module validation + example-bundle regression check on every push touching engine / modules / templates / registry / bundles.
- `signature-check.yml` — dormant in OpenQMS; active in adopter forks; gates PRs on controlled paths.

**Standards registry** — 26 standards across medical-devices, IVD, AI, infosec, packaging domains.

**Bundles** — `bundles/example-samd.yaml` + committed `bundles/example-samd.matrix.json` baseline. CI runs `regenerate --bundle example-samd` (dry-run) on every push as a regression-detection mechanism.

### 2.2 Roadmap (forward work)

- **Non-medical verticals** — financial-services, aerospace, automotive, food-safety, education, employment-decision systems. Each new vertical extends the platform's verticality and lets the `regulated-ai` overlay compose across regulated industries.
- **IVDR class overlays** — `ivdr-class-c`, `ivdr-class-d` analogous to the existing MDR class overlays.
- **`medical-devices-ivd` standalone vertical** — for IVD adopters who don't want the MDR-clauses-NA composition pattern. Re-declares shared QMS clauses; excludes MDR specifically.
- **Drag-and-drop GUI** — web interface for the bundle resolver. CLI is the load-bearing build; GUI is the UX layer.
- **`qms-signatures.yml` schema** — optional controlled-vocabulary enforcement for `Signature-Meaning` trailer values per adopter SOP.
- **Property-tested invariants** — hypothesis-style property tests for OQ-002 (mutation preserves invariant by reconstruction) to upgrade from `:argued` to `:verified`.
- **Open Honest Foundation engagement** — possible upstream home for OpenQMS standards (TBD per Konscience venture trajectory).

**Out of scope:** ERP, inventory/lot tracking, production record automation, post-market surveillance databases. These require dedicated systems regardless of QMS platform.

### 2.3 Standards Licensing

Open QMS's regulatory modules reference standards by clause number and normative summary; they **do not redistribute the standard text itself**. Many referenced standards (ISO, IEC, ASTM, ISTA, AS9100, DO-178C, IATF 16949, ISO 26262, etc.) are commercially published copyrighted works sold under per-user or per-organization license terms. Adopters must obtain their own licensed copies. The Apache-2.0 license on Open QMS does not extend to the standards it references. See README "Standards licensing — important" and ENGINE_SPEC OQ-070 / OQ-071.

---

## 3. Vision and Generator Model

### 3.1 The generator as a decision-table engine

Open QMS treats compliance as a decision-table problem. The rows of the table are the in-scope regulatory clauses (drawn from the active `jurisdiction-set ∪ standards-set` filtered by the active modules); the columns are artifact templates (SOPs, design history records, software lifecycle documents, etc.); the cells are clause-to-artifact bindings declared by the active regulatory modules. The generator resolves a compliance bundle into an artifact set by composing the relevant modules and emitting the artifacts that satisfy the union of in-scope clauses.

### 3.2 The load-bearing invariant

> Given `(product, jurisdiction-set, standards-set)`, the generator emits an unvalidated MVP QMS such that there is a complete bidirectional traceability map between the in-scope regulatory clauses and the generated artifacts: every clause in scope is addressed by at least one artifact, and every artifact declares the clause(s) it addresses. Mutations of the input tuple preserve the invariant by reconstruction. Immutable Git history captures every diff.

Formalized in ENGINE_SPEC as OQ-001 + OQ-002.

What the generator does **not** claim: that the output is validated; that the generated artifacts are sufficient for any conformity assessment; that the generator substitutes for human judgment of regulatory affairs professionals, auditors, or notified bodies.

What the generator **does** guarantee: coverage of every in-scope clause by at least one named artifact; forward traceability; reverse traceability; reproducibility; auditable evolution via Git diffs.

### 3.3 The CLI today; drag-and-drop later

The intended end-user experience is that a quality lead, regulatory affairs manager, or founder configuring a new project's QMS scope can:

1. **Declare a product.** Name, intended use, classification, risk profile.
2. **Select jurisdictions.** From the registry of supported regulators.
3. **Add applicable standards.** From the registry of supported standards.
4. **Compose modules.** Pick the vertical (medical-devices, future fintech, etc.) + relevant class overlays + relevant category overlays + applicable cross-cutting overlays (iso-27001, regulated-ai).
5. **Generate.** The engine resolves the bundle and emits the QMS scaffold.

The CLI handles steps 1-5 today (`openqms resolve --product … --jurisdiction … --standard … --module …`). Stored bundle definitions in `bundles/<name>.yaml` persist a configuration; `openqms regenerate --bundle <name>` re-resolves on demand. The drag-and-drop GUI is forward work.

### 3.4 Multi-product, multi-jurisdiction, evolving scope

An Open QMS instance holds an organization-level state of `(product → (jurisdiction-set, standards-set, modules-set))` assignments. Operations: add product, add/remove standard from a product, add/remove module, reassign product to new buckets, accommodate a standard supersession. Every mutation triggers re-resolution (`openqms regenerate --bundle <name>`); the invariant holds by reconstruction; the Git diff on `bundles/<name>.matrix.json` is the regulatory audit trail of how the scope and artifacts co-evolved.

### 3.5 The regulatory module pattern

A regulatory module is a self-contained package at `modules/<name>/module.yaml` containing a clause table, artifact templates, and a clause-to-template binding manifest. Modules compose via the `compose(list[Module]) → Module` primitive: clauses union by ID (identical content silently dedups; conflicting content raises); template addresses union by path (merged); standards dedup.

Two module kinds, distinguished by intent rather than mechanism:

- **Vertical modules** carry the substantive clause set for a regulated industry: `medical-devices` ships; future `financial-services`, `aerospace`, `automotive`, `food-safety` would follow the same pattern.
- **Overlay modules** add cross-cutting or class-specific requirements that compose with verticals: `iso-27001` (infosec), `regulated-ai` (NIST AI RMF + EU AI Act + ISO 42001), `samd` / `implantable` / `ivd` (device categories), `mdr-class-iia/iib/iii` + `fda-class-ii/iii` (risk classes).

The dedup-by-content-equality semantics let multiple overlays declare the same clause (e.g. `MDR-Art54` in both `mdr-class-iib` and `mdr-class-iii`; `MDR-Art32` in both `implantable` and `mdr-class-iii`); compose silently absorbs the duplicates so adopters can layer overlays freely.

### 3.6 Composition patterns

End-to-end examples:

```bash
# Class IIa SaMD with AI/ML, US + EU dual market
openqms resolve \
  --product DiagnosticAI \
  --jurisdiction FDA --jurisdiction "EU MDR" \
  --standard "ISO 13485:2016" --standard "21 CFR 820" \
  --standard "21 CFR Part 11" --standard "EU MDR 2017/745" \
  --standard "ISO 14971:2019" --standard "IEC 62304:2006+A1:2015" \
  --standard "IEC 82304-1:2016" --standard "NIST AI RMF 1.0" \
  --standard "EU AI Act" --standard "ISO/IEC 42001:2023" \
  --module medical-devices --module samd --module mdr-class-iia \
  --module regulated-ai --module iso-27001 \
  --output traceability_matrix.json

# Class III implantable, US PMA + EU MDR, with AI driving therapy
openqms resolve \
  --product NeuroImplant \
  --jurisdiction FDA --jurisdiction "EU MDR" \
  ...full standards list... \
  --module medical-devices --module implantable \
  --module mdr-class-iii --module fda-class-iii --module regulated-ai \
  ...

# IVD with AI for diagnostic prediction
openqms resolve \
  --product BloodPanelAI \
  --jurisdiction FDA --jurisdiction "EU MDR" \
  ...IVDR + IVD-specific standards... \
  --module medical-devices --module ivd --module regulated-ai \
  ...
```

7-module composites have been tested and validate cleanly. The composition primitive scales as new vertical modules are added.

---

## 4. Architecture

### 4.1 Engine architecture

```
engine/openqms/
├── types.py           # Frozen dataclasses: Clause, ArtifactTemplate, Module, Bundle, ResolvedQMS, ValidationReport
├── module.py          # YAML manifest loader + compose primitive
├── resolver.py        # Pure function (Bundle, Module) → ResolvedQMS
├── validation.py      # Per-module OQ-001 invariant harness
├── registry.py        # Standards-and-jurisdictions registry + module cross-check
├── bundle.py          # Stored bundle definition loader
├── diff.py            # MatrixDiff + diff_matrices + format_diff
├── signatures.py      # Part 11 §11.50 commit-trailer parser + audit-trail exporter
└── cli.py             # argparse CLI: resolve, validate, regenerate, registry, signatures
```

Five subcommands: `resolve` (one-shot resolution), `validate` (module invariant check), `regenerate` (re-resolve stored bundle + diff), `registry` (inspect standards/jurisdictions), `signatures` (verify/export Part 11 trailers).

Frozen dataclasses throughout — inputs are immutable; resolver is a pure function; deterministic same-input-same-output behavior is verifiable via property tests (OQ-002 work pending).

### 4.2 Module + template architecture

```
modules/
├── medical-devices/           # vertical
│   ├── module.yaml            # 62 clauses across 11 standards
│   └── README.md
├── samd/                      # category overlay
├── implantable/               # category overlay
├── ivd/                       # category overlay (IVDR + 21 CFR 809 + ISO 15189)
├── mdr-class-iia/             # risk-class overlay
├── mdr-class-iib/             # risk-class overlay
├── mdr-class-iii/             # risk-class overlay
├── fda-class-ii/              # risk-class overlay
├── fda-class-iii/             # risk-class overlay
├── regulated-ai/              # cross-cutting overlay
├── iso-27001/                 # cross-cutting overlay
└── general/                   # placeholder (industry-agnostic)

templates/
├── qms-policy/                # quality policy
├── qms-sops/                  # SOP + audit procedure
├── qms-suppliers/             # ASL + supplier evaluation
├── qms-management-review/     # meeting record
├── qms-{capa,forms,training}/ # placeholder (org-defined)
├── product-dhf/
│   ├── design-inputs/
│   ├── design-outputs/        # placeholder (product-defined)
│   ├── risk-management/       # ISO 14971 RM file
│   ├── verification/
│   ├── validation/
│   ├── technical-file/        # MDR Annex II + ISO 13485 §4.2.3
│   ├── usability/             # IEC 62366-1
│   ├── packaging/             # ISTA 2A/3A
│   ├── gspr/                  # EU MDR Annex I checklist
│   ├── clinical/              # MDR CER + PMCF + Article 54 expert panel
│   ├── samd-intended-use/     # IMDRF SaMD framework
│   ├── implant/               # MDR Annex I §23.4 + Article 32 SSCP
│   ├── pma/                   # FDA 21 CFR 814 PMA
│   ├── 510k/                  # FDA 21 CFR 807 510(k)
│   ├── ivdr-gspr/             # IVDR Annex I checklist
│   ├── performance-evaluation/ # IVDR Annex XIII PER
│   ├── ai-system-card/        # Model Card + EU AI Act Art 11/13
│   └── ai-impact-assessment/  # EU AI Act Art 9/14/27 + NIST AI RMF
└── product-sw/                # software lifecycle per IEC 62304
    ├── requirements/
    ├── architecture/
    ├── soup-register/
    ├── test/
    └── release/
```

The module manifest's clause-to-template bindings can reference any artifact path: document templates (`templates/...`), issue templates (`.github/ISSUE_TEMPLATE/...`), CI workflows (`.github/workflows/...`), or documentation guides (`docs/guide/...`). Guides-as-artifacts is honest about cases like Part 11 §11.50 / §11.70 where the satisfying mechanism is documented procedurally rather than embodied in a template file.

### 4.3 Bundle persistence + audit trail

```
bundles/
├── README.md
├── example-samd.yaml          # stored bundle definition
└── example-samd.matrix.json   # committed baseline; Git diff = audit trail
```

A `BundleDef` pins `(product, jurisdictions, standards, modules)`. `openqms regenerate --bundle <name>` re-resolves, prints structured diff against the prior `<name>.matrix.json`, and (with `--write-matrix`) overwrites the file. The resulting Git commit IS the regulatory audit-trail unit. CI runs the dry-run on every push as a regression-detection mechanism.

### 4.4 Required supplementary tooling (for adopters)

| Capability | Tool options |
|---|---|
| E-signature meaning (Part 11 §11.50) | `signatures verify/export` subcommand + commit-trailer convention (shipped at v0.7.0; OQ-060) |
| E-signature identity (Part 11 §11.70) | GPG/SSH-signed commits + `docs/guide/gpg-signing.md` runnable checklist (OQ-023) |
| Training management | LMS integration, or extend `training-trigger.yml` |
| Document rendering (point-of-use access) | GitHub Pages + MkDocs (shipped) |
| Traceability matrix generation | `openqms regenerate` produces it from bundle (shipped at v0.6.0; OQ-015) |
| Audit trail export | Git history + `openqms signatures export` for §11.50-format records + GitHub Enterprise audit log API for system-level events |
| Complaint / PII-protected records | Sibling private repo (Pattern A) or external eQMS (Pattern B); see `docs/guide/complaints.md` (OQ-062) |
| QMS metrics dashboard | `gh issue list` patterns documented in `docs/guide/management-review.md`; or external dashboard (Grafana, Metabase, commercial eQMS) |
| Binary file management | Git LFS, or external storage with references |

---

## 5. Validation Requirements

The generator emits an **unvalidated MVP QMS**. Validation for any intended use is the consuming organization's responsibility, performed against that organization's own validation protocols and quality system. Open QMS does not provide validated QMS documentation; it provides a starting scaffold with declared coverage and traceability.

For organizations adopting an Open QMS-generated scaffold and operating it on GitHub, validation per ISO 13485 §4.1.6 and 21 CFR Part 11 must cover: Installation Qualification (org configuration, SSO/MFA, branch protection, CODEOWNERS, required checks, permissions, backup); Operational Qualification (approval workflows, CI gating, audit trails, signature verification, obsolete-doc prevention); Performance Qualification (end-to-end design change, CAPA lifecycle, document revision with training trigger, audit-trail export, regenerate-on-mutation diff workflow); Ongoing validation (revalidation triggers on platform updates, configuration changes, module-version bumps, input-tuple changes, registry standard supersessions).

---

## 6. Risk Assessment Summary

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Auditor unfamiliarity with GitHub leads to findings | High | Medium | `docs/guide/auditor-walkthrough.md`; render key records as PDF on release. |
| Force-push or history rewrite destroys audit trail | Low (if configured) | Critical | `setup.sh` disables force-push; org-level monitoring required (OQ-022). |
| Part 11 e-signature meaning gap leads to FDA observation | Medium → Low (post-v0.7.0) | High | OQ-060 prototype shipped: commit-trailer convention + parser + dormant CI gate. Adopters wire to their controlled-vocabulary SOP. |
| Binary file bloat degrades repo performance | High | Medium | Enforce Git LFS for files > 1 MB. |
| SaaS outage prevents QMS access | Low | High | Local clones as backup. |
| Personnel without Git skills cannot use QMS | High | Medium | MkDocs rendered site (OQ-024); limit Git operations to trained personnel. |
| Cross-repo / cross-module traceability breaks down | Medium → Low (post-v0.6.0) | High | `openqms regenerate` + committed `<bundle>.matrix.json` baseline + CI dry-run regression check (OQ-015). |
| Module versions drift relative to standards | Medium → Low (post-v0.6.0) | High | Registry `superseded_by` field + `--strict-editions` CLI flag (OQ-014, OQ-065). |
| Generator emits "complete" artifact set that misses a clause | Medium → Low | High | OQ-013 validation harness + CI runs on every push touching engine / modules / templates / registry / bundles. |
| Composition produces unexpected results | Low | Medium | Multi-module composite is tested at 7-module scale; dedup-by-content-equality semantics catch divergent clause definitions. |
| Adopter doesn't customize device-class GSPR applicability | Medium | Medium | GSPR / IVDR-GSPR templates ship with explicit per-class applicability columns + NA-justification sections; documented in `modules/<class-overlay>/README.md`. |

---

## 7. Decision Criteria

Adopting an Open QMS-generated scaffold is viable if the organization commits to building and validating the supplementary tooling above, accepts the ongoing validation burden, has sufficient Git literacy or builds a rendering layer, addresses the Part 11 e-signature gap with a documented validated approach (the v0.7.0 prototype is the documented path), implements CI-enforced traceability and regression detection via `regenerate` rather than relying on procedural discipline alone, and treats the generator's output as a starting scaffold rather than a validated quality system.

A hybrid approach — Open QMS for software lifecycle, DHF management, engineering documentation, and the workflows that have shipped templates — paired with a lightweight commercial eQMS for any workflow not yet templated (typically: training-management automation beyond `training-trigger.yml`; complaint PHI-bearing record storage; advanced supplier-evaluation analytics) — reduces risk while capturing the version-control advantages where they matter most. This is the most likely adoption pattern for established organizations.

---

## 8. Digital Signatures (shipped at v0.7.0)

21 CFR Part 11 §11.50 — *signature manifestations shall display the printed name, date/time, and meaning of the signature* — was the single largest gap between Git-as-substrate and a Part-11-compliant electronic-signature regime. GPG-signed commits (OQ-023) bind identity to content; they do not natively bind the *meaning* of the signature.

**Prototype shipped at v0.7.0** (OQ-060):

- **Commit-trailer convention** — `Signature-Meaning: approved` required; `Signature-Role: QA-Lead` and `Signature-Justification: <free text>` optional. Adopters define the controlled vocabulary in their signature-handling SOP.
- **Engine parser + extractor** — `openqms.signatures` module parses commit messages, decodes GPG verification status, emits Part 11 §11.50-format JSON audit records.
- **CLI** — `openqms signatures verify --commit <sha>` (with `--require-gpg` flag); `openqms signatures export --since <ref>` (full audit-trail emission).
- **CI gate** — `.github/workflows/signature-check.yml` ships dormant in OpenQMS (no controlled documents at the gated paths); activates in adopter forks that populate `qms-policy/`, `qms-sops/`, etc.
- **Guide** — `docs/guide/signature-meaning.md` covers the requirement, the trailer convention, CLI surface, CI configuration, and honest limitations (trailer is discipline not security boundary; HR-to-identity mapping is procedural; web edits sign as GitHub).

The pair (GPG + trailers) satisfies §11.70 and §11.50. The §11.50 implementation is honest about being a prototype — production deployment requires adopter SOP for controlled vocabulary, adopter CI configuration, and adopter HR-to-GitHub identity mapping per `gpg-signing.md` §2.

ENGINE_SPEC reference: OQ-060 (`:tested`).

---

## 9. Provenance

This document is the architectural-narrative counterpart of `ENGINE_SPEC.md`. Earlier drafts of the spec lived at `~/Desktop/Research Papers/Relational_Emergence/Closure v5/BUSINESS/GitHub_QMS_Spec_Medical_Devices.md` (v1.0 by NeuraSignal Operations 2026-04-02; v2.0 DRAFT by Aaron Green 2026-05-22). The closure-v5 location is historical; this DESIGN.md + ENGINE_SPEC.md pair is the authoritative replacement.

**Companion docs index** at `companion_index.md` lists permanent build-records per substantive session (engine MVP, Phase 0 round-out, Phase 1 engine completion, signature meaning, org workflows, medical-devices population, overlay modules). Companions follow the TCE §1-§4 standard (computational basis / results / verification / spec impact) and are the recommended starting point for any future session picking up context.

**Crosswalk material** in `regulatory_modules/medical_devices_crosswalk.md` preserves the detailed clause-by-clause crosswalk content from the v2.0 DRAFT spec; the machine-readable manifest at `modules/medical-devices/module.yaml` is the operational source of truth.

Open QMS is part of Aaron Green's broader spec-discipline practice — the Triadic Coordination Engine (`~/Desktop/triadic-coordination-engine/`) is the methodology lineage. Konscience (with Ilya Krakovich) is the most likely commercial implementer of Open QMS as the regulated-AI organizational and decision twin substrate. The Open Honest Foundation engagement (initial reconnaissance call 2026-05-22) remains an open option for upstream standards-body governance — to be revisited once OpenQMS has either further matured or attracted external adopters.
