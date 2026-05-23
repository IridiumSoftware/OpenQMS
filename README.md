# Open QMS

**An open-source, GitHub-native Quality Management System.**

Open QMS provides the infrastructure to run a compliant quality management system directly on GitHub, using pull requests for approvals, CI/CD for enforcement, and Git for the audit trail. It ships as a set of repository templates, CI workflows, document templates, and scripts that organizations can fork and adapt.

## What's included

- **Generator engine** (`engine/`) — Python CLI that resolves a `(product, jurisdictions, standards)` bundle into a QMS scaffold with complete bidirectional clause-to-artifact traceability. Run `openqms resolve …` to emit a traceability matrix; run `openqms validate --module <name>` to assert the invariant that every clause is addressed by ≥1 template and no template addresses a non-existent clause.
- **Repository structure template** for QMS documentation (SOPs, forms, DHFs, training, CAPA, suppliers)
- **CI workflows** for document control enforcement, traceability checking, training triggers, release gating, and engine tests
- **Document templates** with required metadata fields for controlled documents
- **Issue templates** for CAPAs, change requests, design inputs, nonconformances, and complaints
- **MkDocs configuration** for rendering controlled documents as a browsable site (point-of-use access)
- **Setup script** for configuring branch protection, CODEOWNERS, and required checks
- **Regulatory modules** (starting with medical devices: ISO 13485, 21 CFR 820, IEC 62304; machine-readable manifest at `modules/medical-devices/module.yaml`)

## Quick start

```bash
# 1. Use this repo as a template (or fork it)
gh repo create my-org/qms --template IridiumSoftware/open-qms --private

# 2. Clone and run setup
git clone git@github.com:my-org/qms.git
cd qms
./scripts/setup.sh

# 3. Configure your organization
#    Edit CODEOWNERS, docs/qms-config.yml, and templates as needed

# 4. Enable GitHub Pages for rendered doc site
#    Settings > Pages > Source: GitHub Actions
```

## Generator engine

The engine resolves a compliance bundle — `(product, jurisdictions, standards)` — into a QMS scaffold with a bidirectional traceability map. Every in-scope clause is addressed by at least one artifact; every emitted artifact declares the clause(s) it addresses. This invariant is mechanically checked by a per-module validation harness.

### Install (from the repo root)

```bash
pip install -e './engine[dev]'
```

### Resolve a bundle

```bash
openqms resolve \
  --product ExampleDevice \
  --jurisdiction FDA \
  --standard "ISO 13485:2016" \
  --standard "21 CFR 820" \
  --module medical-devices \
  --output traceability_matrix.json
```

The matrix contains `bundle`, `module`, `in_scope_clauses`, `artifacts`, and `traceability` (with `forward` clause-to-artifact and `reverse` artifact-to-clause maps).

### Validate a module

```bash
openqms validate --module medical-devices
```

Exit 0 on pass, 1 on invariant violation. The CI workflow `.github/workflows/engine-tests.yml` runs this on every push that touches `engine/`, `modules/`, or `templates/`.

### Compose modules

`--module` is repeatable on both `resolve` and `validate`. When multiple modules are supplied, the engine composes them — unioning clauses by ID (conflicts raise) and template `addresses` by path — before doing its work. This is how cross-cutting overlays (e.g. ISO 27001 infosec) combine with vertical regulatory modules (e.g. medical-devices) without either having to embed the other:

```bash
openqms validate --module medical-devices --module iso-27001

openqms resolve \
  --product ExampleSaMD \
  --jurisdiction FDA \
  --standard "ISO 13485:2016" \
  --standard "21 CFR 820" \
  --standard "ISO 14971:2019" \
  --standard "IEC 62304:2006+A1:2015" \
  --standard "ISO/IEC 27001:2022" \
  --module medical-devices \
  --module iso-27001 \
  --output traceability_matrix.json
```

### Status (v0.4.0)

- **Today.** Single- and multi-module resolution; `compose` primitive for unioning modules; per-module validation harness; medical-devices reference module (4 standards in scope, 20 clauses, 12 templates) plus iso-27001 cross-cutting overlay (3 clauses, 3 template bindings).
- **Forward.** Standards-and-jurisdictions registry, re-resolution-on-mutation, additional regulatory modules (regulated AI, pharma, aerospace, automotive, food safety), 21 CFR Part 11 §11.50 signature-meaning prototype.

See `engine/README.md` for the full architecture.

## Architecture

```
open-qms/
├── .github/
│   ├── workflows/          # CI: doc control, traceability, training, release, engine-tests
│   └── ISSUE_TEMPLATE/     # CAPA, change request, design input, NCR, complaint
├── engine/                 # Generator engine (Python: bundle resolver + validation harness)
│   ├── openqms/            # Source: types, module loader, resolver, validation, CLI
│   └── tests/              # pytest suite
├── docs/                   # MkDocs source for rendered QMS site
├── modules/                # Regulatory modules (machine-readable manifests)
│   ├── medical-devices/    # ISO 13485, 21 CFR 820, ISO 14971, IEC 62304 (vertical)
│   ├── iso-27001/          # ISO/IEC 27001:2022 (cross-cutting overlay)
│   └── general/            # Industry-agnostic QMS processes
├── scripts/                # Setup, validation, audit helpers
└── templates/              # QMS directory structure template
    ├── qms-policy/
    ├── qms-sops/
    ├── qms-forms/
    ├── qms-training/
    ├── qms-capa/
    ├── qms-suppliers/
    ├── qms-management-review/
    ├── product-dhf/        # Design history file (per product)
    └── product-sw/         # Software lifecycle (IEC 62304)
```

## How it works

| QMS activity | GitHub mechanism | CI enforcement |
|---|---|---|
| Document approval | PR with required reviewers (CODEOWNERS) | `doc-control.yml` checks metadata, approvers |
| Change control | Issue (change request) → PR → review → merge | `traceability.yml` verifies issue linkage |
| CAPA | Issue with template → investigation → corrective PR | Labels + milestone tracking |
| Training | Doc merge triggers training assignment issue | `training-trigger.yml` creates issues per trainee |
| Release | Git tag → CI verifies completeness → GitHub Release | `release-gate.yml` blocks incomplete releases |
| Audit trail | Git log + GitHub audit log (Enterprise) | Immutable by design (force-push disabled) |
| Point-of-use access | MkDocs renders docs as static site | `deploy-docs.yml` publishes on merge |
| Module clause coverage | `modules/*/module.yaml` clause-to-template bindings | `engine-tests.yml` runs `openqms validate` |

## Regulatory scope

Open QMS is designed to be extended with regulatory modules. The first module covers **medical devices**:

- ISO 13485:2016
- 21 CFR Part 820 (FDA QSR)
- 21 CFR Part 11 (Electronic Records / Signatures)
- EU MDR 2017/745
- IEC 62304 (Software Lifecycle)
- IEC 62366-1 (Usability Engineering)

Modules for other regulated industries (pharma, aerospace, automotive, food safety) can be contributed by the community.

## Standards licensing — important

Open QMS's regulatory modules reference standards by clause number and normative summary, but **do not redistribute the standard text itself**. Many of the standards referenced are commercially published copyrighted works sold by their publishers under per-user or per-organization license terms.

**Adopters must obtain their own licensed copies of any standard they intend to implement against.** The crosswalks in this repository are useful as a map and as a coverage check; they are not a substitute for the standards themselves.

Public-domain or freely accessible (representative):

- US federal regulations (21 CFR Part 820, 21 CFR Part 11) — public, via FDA / GovInfo
- EU regulations (MDR 2017/745, AI Act 2024/1689) — public, via EUR-Lex
- NIST publications (AI RMF, SP 800-53) — public, via NIST

Commercially licensed (representative, not exhaustive):

- ISO standards (13485, 27001, 42001, 22000, 9001) — purchased per copy from ISO or national member bodies (ANSI, BSI, etc.) under ISO's terms
- IEC standards (62304, 62366-1, 60601-1) — purchased per copy from IEC or national member bodies under IEC's terms
- ASTM standards — purchased from ASTM International
- ISTA standards (2A, 3A, etc.) — accessed via ISTA membership or per-document purchase
- Industry-specific standards (AS9100 from SAE; DO-178C from RTCA; IATF 16949 from IATF; ISO 26262; etc.) — each under its own publisher's terms

Open QMS contributors and adopters are responsible for complying with the license terms of any standard they reference, implement against, or distribute alongside their own QMS. **The Apache-2.0 license on Open QMS itself does not extend to the standards it references.** If you are evaluating Open QMS for a regulated program, budget for the licensed standards your applicable jurisdictions and product class require — this is part of the cost of operating in a regulated industry regardless of QMS platform.

## Important disclaimers

- **This is infrastructure, not a validated QMS.** You must validate the system for your intended use per your applicable regulations.
- **Open QMS does not provide legal or regulatory advice.** The regulatory mappings are reference material. Consult qualified regulatory professionals for your specific situation.
- **GitHub's platform is not inherently Part 11 compliant.** The gap analysis in `docs/regulatory/` describes what supplementary controls are needed.
- **Your organization's SOPs, forms, and quality records are yours.** Open QMS provides templates. You fill them in.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Apache 2.0. See [LICENSE](LICENSE).
