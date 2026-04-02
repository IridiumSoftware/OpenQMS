# Open QMS

**An open-source, GitHub-native Quality Management System.**

Open QMS provides the infrastructure to run a compliant quality management system directly on GitHub, using pull requests for approvals, CI/CD for enforcement, and Git for the audit trail. It ships as a set of repository templates, CI workflows, document templates, and scripts that organizations can fork and adapt.

## What's included

- **Repository structure template** for QMS documentation (SOPs, forms, DHFs, training, CAPA, suppliers)
- **CI workflows** for document control enforcement, traceability checking, training triggers, and release gating
- **Document templates** with required metadata fields for controlled documents
- **Issue templates** for CAPAs, change requests, design inputs, nonconformances, and complaints
- **MkDocs configuration** for rendering controlled documents as a browsable site (point-of-use access)
- **Setup script** for configuring branch protection, CODEOWNERS, and required checks
- **Regulatory reference modules** (starting with medical devices: ISO 13485, 21 CFR 820, EU MDR, IEC 62304)

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

## Architecture

```
open-qms/
├── .github/
│   ├── workflows/          # CI: doc control, traceability, training, release
│   └── ISSUE_TEMPLATE/     # CAPA, change request, design input, NCR, complaint
├── docs/                   # MkDocs source for rendered QMS site
├── modules/                # Regulatory-specific extensions
│   ├── medical-devices/    # ISO 13485, 21 CFR 820, IEC 62304
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

## Regulatory scope

Open QMS is designed to be extended with regulatory modules. The first module covers **medical devices**:

- ISO 13485:2016
- 21 CFR Part 820 (FDA QSR)
- 21 CFR Part 11 (Electronic Records / Signatures)
- EU MDR 2017/745
- IEC 62304 (Software Lifecycle)
- IEC 62366-1 (Usability Engineering)

Modules for other regulated industries (pharma, aerospace, automotive, food safety) can be contributed by the community.

## Important disclaimers

- **This is infrastructure, not a validated QMS.** You must validate the system for your intended use per your applicable regulations.
- **Open QMS does not provide legal or regulatory advice.** The regulatory mappings are reference material. Consult qualified regulatory professionals for your specific situation.
- **GitHub's platform is not inherently Part 11 compliant.** The gap analysis in `docs/regulatory/` describes what supplementary controls are needed.
- **Your organization's SOPs, forms, and quality records are yours.** Open QMS provides templates. You fill them in.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Apache 2.0. See [LICENSE](LICENSE).
