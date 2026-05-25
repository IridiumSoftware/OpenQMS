# Open QMS

**An open-source, GitHub-native Quality Management System generator.**

Open QMS resolves a `(product, jurisdictions, standards, modules)` bundle into a complete QMS scaffold with bidirectional clause-to-artifact traceability. It ships as a Python CLI + a library of regulatory modules + a library of document templates that compose into the QMS for your specific scope.

The infrastructure runs directly on GitHub: pull requests for approvals, CI/CD for enforcement, Git for the audit trail.

## Current scope (v0.50.0)

| Dimension | Count |
|---|---|
| Verticals (regulated industries) | **7** — medical-devices, aerospace, automotive, manufacturing, pharma, food-safety, chemicals |
| Class overlays (rigor-level + product-class) | **44** across 6 verticals (medical 9 / aerospace 7 / automotive 11 / pharma 6 / food-safety 5 / chemicals 6) |
| Cross-cutting overlays | **26** — iso-27001, regulated-ai, iso-14001, iso-45001, iso-50001, iso-37001, iso-22301, recall-workflow, iso-31000, iso-37301, soc-2, pci-dss, hitrust-csf, nist-csf, dora, eu-gpsr, tisax, defense-cui, cmmc, osha-hcs, transport-hazmat, eu-biocides, tsca-pfas, privacy, hipaa, us-state-privacy |
| **Sub-overlays** (class-overlay-shape deltas on cross-cutting overlays) | **26** — cmmc-level-1/2/3, soc-2-type-i/ii, iso-27001-cloud/privacy, nist-csf-tier-1/2/3/4, pci-dss-saq-a/a-ep/d-merchant/d-sp/p2pe, dora-ctpp/non-ctpp/tlpt, hitrust-e1/i1/r2, iso-37301-public-sector/financial-services/healthcare/general-business |
| **Cross-overlays** (bind ACROSS specific vertical combinations) | **12** — combination-product, integrated-management-system, food-pharma-grade, connected-medical-device, cell-therapy-supply-chain, food-allergen-recall, defense-aerospace-cyber, digital-health-multi-region, **automotive-supply-chain** (v0.50.0), **clinical-trial-multi-region** (v0.50.0), **banking-resilience** (v0.50.0), **utility-cybersecurity** (v0.50.0) |
| Registry — standards | **~135** (v0.50.0 +5 PUBLIC: ICH E6(R3) + EU CTR 536/2014 + NERC CIP + EU NIS2 + FFIEC IT Handbook) |
| Registry — jurisdictions | **20** (FDA / EMA / MHRA / WHO-PQ / Health Canada / EU MDR / PMDA / TGA / ANVISA / FAA / EASA / TCCA / NHTSA / UNECE / KBA / TC-MVS / FDA-Food / USDA-FSIS / EFSA / CFIA) |
| Document templates | **103** (v0.50.0 cross-overlays reuse parent-overlay templates; no new templates) |
| Example bundles (validated end-to-end) | **8** |
| Total modules | **116** + general |
| Spec entries (status: 6 :verified / 91 :tested / 5 :argued / 0 :open) | **102** |
| Engine CLI subcommands | **9** — `resolve`, `validate`, `regenerate`, `signatures`, `trace`, `coverage` (v0.49.0), `crosswalk` (v0.49.0), `jurisdictions-query` (v0.49.0), `registry` |
| Deepest composition tested in CI | **24-module ultra composite** (medical-devices + pharma + combination-product + connected-medical-device + digital-health-multi-region + sterile + hipaa + privacy + 11 cross-cutting + IMS + SOC 2 + HITRUST + ISO 27001 cloud/privacy + ISO 37301) |

The compose primitive validates 11-module composites: e.g., `pharma + pharma-sterile + pharma-biologics + atmp + iso-27001 + soc-2 + iso-31000 + iso-22301 + iso-14001 + iso-45001 + iso-50001` — the realistic shape for a clinical-stage biotech doing sterile ATMP manufacturing with full integrated management system + SOC 2 attestation + ISO 31000 risk framework.

**See [`docs/modules-catalog.md`](docs/modules-catalog.md) for the complete catalog with per-module standards covered + adoption guidance.**

## Quick start

### Choose your vertical + run

```bash
# 1. Use this repo as a template (or fork it)
gh repo create my-org/qms --template IridiumSoftware/open-qms --private

# 2. Clone + install the engine
git clone git@github.com:my-org/qms.git
cd qms
pip install -e './engine[dev]'

# 3. Validate the vertical + overlays you'll use
openqms validate --module medical-devices --module iso-27001
# → module: medical-devices+iso-27001-overlay
#   invariant_holds: True

# 4. Resolve your bundle into a traceability matrix
openqms resolve \
  --product MyDevice \
  --jurisdiction FDA --jurisdiction "EU MDR" \
  --standard "ISO 13485:2016" --standard "21 CFR 820" \
  --module medical-devices \
  --output traceability_matrix.json

# 5. Or use a stored bundle definition + the regenerate workflow
openqms regenerate --bundle example-samd --write-matrix
git add bundles/example-samd.matrix.json
git commit -m "Refresh example-samd matrix"
```

### Verticals at a glance

| Vertical | Module ID | Primary standards | Class overlays |
|---|---|---|---|
| **Medical devices** | `medical-devices` | ISO 13485 / 21 CFR 820 / 21 CFR Part 11 / EU MDR / ISO 14971 / IEC 62304 / IEC 62366-1 / IEC 60601-1 / ISTA / MDSAP | 7 (samd, implantable, mdr-class-iii/iib/iia, fda-class-iii/ii) |
| **Aerospace** | `aerospace` | ISO 9001 / AS9100D / 14 CFR Part 21 / EASA Part 21 / DO-178C / DO-254 / ARP4754A / ARP4761 / AS9102 | 5 (DAL-A through DAL-E) |
| **Automotive** | `automotive` | ISO 9001 / IATF 16949 / ISO 26262 / ISO/SAE 21434 / UN R155 / UN R156 / Automotive SPICE 4.0 / AIAG PPAP | 9 (ASIL D/C/B/A/QM + CAL 4/3/2/1) |
| **Manufacturing** (general) | `manufacturing` | ISO 9001 only | (none — ISO 9001 has no rigor tiers) |
| **Pharma** | `pharma` | ICH Q7/Q9/Q10 + 21 CFR 210/211 + EudraLex Vol. 4 + PIC/S Annex 1 + 21 CFR Part 11 (all public license) | 1 (atmp — cell + gene therapy) |
| **Food safety** | `food-safety` | ISO 22000 + FSSC 22000 v6 + Codex HACCP + 21 CFR 117 (FSMA) + 21 CFR 123 (Seafood HACCP) | (none yet — forward) |
| **Chemicals** | `chemicals` | EU REACH + EU CLP + UN GHS Rev. 10 + OECD GLP + US TSCA (all public license) | (none yet — OSHA HCS + DOT HazMat + biocides + cosmetics + pesticides forward) |

### Cross-cutting overlays

Each composes with any vertical (and with each other — the 7-overlay set follows Annex SL):

| Overlay | Standard(s) | When to use |
|---|---|---|
| `iso-27001` | ISO/IEC 27001:2022 | Information security; common for any organization handling customer/proprietary data |
| `regulated-ai` | NIST AI RMF + EU AI Act + ISO/IEC 42001 + ISO/IEC 23894 | Products that use ML in safety / risk / decision contexts |
| `iso-14001` | ISO 14001:2015 | Environmental management |
| `iso-45001` | ISO 45001:2018 | Occupational health + safety; worker consultation per §5.4 |
| `iso-50001` | ISO 50001:2018 | Energy management with calculated EnB baseline |
| `iso-37001` | ISO 37001:2016 | Anti-bribery; due diligence + independent compliance function |
| `iso-22301` | ISO 22301:2019 | Business continuity (BIA + RTO/RPO + exercise programme) |

## Generator engine

The engine resolves a compliance bundle — `(product, jurisdictions, standards, modules)` — into a QMS scaffold with a bidirectional traceability map. Every in-scope clause is addressed by ≥1 artifact; every emitted artifact declares the clause(s) it addresses. This invariant (OQ-001) is mechanically checked by a per-module validation harness (OQ-013) and property-tested across arbitrary inputs (OQ-001 at status `:verified`).

### CLI surface

```bash
openqms validate --module <name>             # assert OQ-001 invariant
openqms validate --module A --module B       # compose then assert
openqms resolve --product ... --module ...   # emit traceability matrix
openqms regenerate --bundle <name>           # re-resolve + diff vs. committed matrix
openqms regenerate --bundle <name> --write-matrix  # accept the change
openqms regenerate --bundle <name> --strict-editions  # upgrade supersession warnings to errors
openqms registry list                        # list standards + jurisdictions
openqms registry show --id "<id>"            # show registry entry
openqms signatures verify --commit <sha>     # 21 CFR Part 11 §11.50 signature meaning
openqms signatures export --since <ref>      # Part 11-format JSON audit trail
```

### Composition

`--module` is repeatable. The engine composes via union (clauses joined by ID; conflicts raise; template addresses merged):

```bash
# 9-module composite — commercial-stage cell-therapy organization with fully-integrated MS
openqms validate \
  --module pharma --module atmp \
  --module iso-27001 --module regulated-ai \
  --module iso-14001 --module iso-45001 --module iso-50001 \
  --module iso-37001 --module iso-22301
# → invariant_holds: True
```

Cross-cutting overlays (iso-27001, regulated-ai, iso-14001, iso-45001, iso-50001, iso-37001, iso-22301) all follow Annex SL so they compose with each other and with every vertical without naming collisions.

### Bundles + regenerate

A stored bundle definition at `bundles/<name>.yaml` pins the input tuple. `openqms regenerate --bundle <name>` re-resolves and prints a structured diff against the prior matrix at `bundles/<name>.matrix.json`. The committed matrix file is the regulatory audit trail; CI runs the dry-run on every push, turning the matrix into a regression-detection mechanism.

11 shipped example bundles cover every vertical + several cross-vertical compositions:

| Bundle | Demonstrates |
|---|---|
| `example-samd` | Medical-devices SaMD with iso-27001 |
| `example-aircraft` | Aerospace avionics composing regulated-ai + iso-27001 |
| `example-vehicle` | Automotive ECU composing regulated-ai + iso-27001 (UN R155 type-approval scope) |
| `example-machine-shop` | General-manufacturing ISO 9001 + iso-27001 (no jurisdiction-specific regulator) |
| `example-drug-product` | Sterile drug-product (small-volume parenteral) at US+EU dual-licensed site composing pharma + 4 cross-cutting overlays |
| `example-cart` | Autologous CD19-targeted CAR-T composing pharma + atmp + 4 cross-cutting overlays |
| `example-food-processor` | Mid-size RTE chilled-foods processor composing food-safety + 3 cross-cutting overlays |

### Signatures — 21 CFR Part 11 §11.50 prototype

GPG-signed commits satisfy §11.70 (cryptographic identity binding) but §11.50 separately requires the signature to display its *meaning* (approved / reviewed / authorized / etc.). The engine bridges the gap with a commit-trailer convention (`Signature-Meaning:`, optional `Signature-Role:` / `Signature-Justification:`) plus parser, audit-trail exporter, and CI gate. `openqms signatures verify --commit <sha>` checks a single commit; `openqms signatures export --since <ref>` emits Part 11-format JSON records. Full guide: `docs/guide/signature-meaning.md`.

### Registry

`registry/standards.yaml` and `registry/jurisdictions.yaml` catalog every standard + jurisdiction the engine knows about. `--standard` and `--jurisdiction` CLI arguments are validated against the registry; unknown values raise rather than silently filtering to empty. Aliases (`"ISO 13485"`) normalize to canonical ids (`"ISO 13485:2016"`). Inspect with `openqms registry list` or `openqms registry show --id <id>`. Module manifests are cross-checked against the registry on every validation run.

The registry also supports `superseded_by` on standards — when a referenced standard is superseded by a newer edition, `validate` and `regenerate` print warnings (or, with `--strict-editions`, errors).

## Architecture

```
open-qms/
├── .github/
│   ├── workflows/                 # CI: doc control, traceability, training, release, engine-tests, signature-check
│   └── ISSUE_TEMPLATE/            # CAPA, change request, design input, NCR, complaint, supplier-evaluation, management-review
├── engine/                        # Generator engine (Python)
│   ├── openqms/                   # Types, module loader, resolver, validation, registry, regenerate, signatures, CLI
│   └── tests/                     # pytest + hypothesis property tests (108 tests)
├── BUSINESS/                      # Spec + design + companion docs (public as of v0.23.0)
│   ├── ENGINE_SPEC.md             # 80 spec entries with logic tiers + evidence types + status
│   ├── DESIGN.md                  # Architectural narrative
│   ├── artifact_registry.md       # S-ID → evidence file mapping
│   ├── dashboard.md               # Status summary + priority stack
│   ├── changelog.md               # Versioned release log
│   └── companion_*.md             # Per-session computational basis + verification records
├── docs/                          # MkDocs source + adopter guides
│   ├── modules-catalog.md         # Comprehensive module catalog ← START HERE for module choice
│   ├── guide/                     # Per-topic guides (signature-meaning, gpg-signing, complaints, etc.)
│   └── regulatory/                # Regulatory crosswalks
├── modules/                       # Regulatory modules (machine-readable manifests + per-module READMEs)
│   ├── medical-devices/ + 7 class overlays (samd, implantable, mdr-class-iii/iib/iia, fda-class-iii/ii) + ivd
│   ├── aerospace/ + 5 DAL overlays (A through E)
│   ├── automotive/ + 9 class overlays (ASIL D/C/B/A/QM + CAL 4/3/2/1)
│   ├── manufacturing/             # ISO 9001 only
│   ├── pharma/ + atmp class overlay
│   ├── food-safety/
│   ├── general/                   # Industry-agnostic substrate
│   └── 7 cross-cutting overlays: iso-27001, regulated-ai, iso-14001, iso-45001, iso-50001, iso-37001, iso-22301
├── registry/                      # Standards + jurisdictions registry
│   ├── standards.yaml             # 63 standards with aliases + edition + license_kind + superseded_by
│   └── jurisdictions.yaml         # 20 jurisdictions with applicable_standards
├── bundles/                       # Stored bundle definitions + committed matrices (11 examples)
├── scripts/                       # Setup, validation, audit helpers
└── templates/                     # 57 document templates organized by QMS area
    ├── qms-policy/, qms-sops/, qms-forms/, qms-training/, qms-capa/
    ├── qms-suppliers/, qms-management-review/
    ├── qms-environmental/, qms-ohs/, qms-energy/, qms-abms/, qms-bcms/
    ├── product-dhf/               # Design history file (medical + aero + auto)
    ├── product-sw/                # Software lifecycle (IEC 62304 + DO-178C + ASPICE)
    ├── product-pharma/            # MBR, VMP, deviation, change control, OOS, APQR
    └── product-atmp/              # Donor eligibility, traceability, viral safety
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
| 21 CFR Part 11 §11.50 signature meaning | `Signature-Meaning:` commit trailer | `signature-check.yml` gates controlled-doc paths |
| Bundle regression detection | Committed `bundles/<name>.matrix.json` | `engine-tests.yml` runs `openqms regenerate` dry-run |

## Adoption guidance

**If your organization makes medical devices** → start with `medical-devices`; add an appropriate class overlay for your risk class (samd, implantable, or mdr-class-iii/iib/iia + fda-class-iii/ii); compose with iso-27001 (always); compose with regulated-ai if any ML-driven function.

**If your organization makes aviation products** → start with `aerospace`; add a DAL overlay per FHA classification (DAL-A through DAL-E); compose with regulated-ai if avionics include ML; compose with iso-27001.

**If your organization makes road vehicles** → start with `automotive`; add an ASIL overlay per HARA classification (ASIL-D / -C / -B / -A / QM); add a CAL overlay per TARA classification (CAL-4 through CAL-1); compose with regulated-ai for ADAS/AD scope; iso-27001 for organizational IS.

**If your organization is a job shop / machine shop / contract manufacturer (non-regulated)** → start with `manufacturing` (ISO 9001 only); compose with iso-27001 if you handle customer proprietary CAD/CAM.

**If your organization makes pharmaceuticals** → start with `pharma` (covers ICH + cGMP + EU GMP + PIC/S Annex 1; all standards are public-license); add `atmp` if cell/gene therapy; compose all 7 cross-cutting overlays for fully-integrated management system (PQS + IS + AI + EMS + OHSMS + EnMS + ABMS + BCMS).

**If your organization makes food + beverage** → start with `food-safety` (ISO 22000 + FSSC 22000 + Codex HACCP + FSMA + Seafood HACCP); compose with iso-14001 + iso-45001 + iso-50001 (typical for processors with refrigeration intensity).

**If your organization makes combination products (drug + device)** → compose `medical-devices + pharma` (21 CFR Part 4 combination-product cGMP spans both).

For full adoption pathways and module-by-module guidance, see [`docs/modules-catalog.md`](docs/modules-catalog.md).

## Status (v0.22.0)

**80 spec entries** with rigorous status discipline (every entry carries evidence; zero `:open`):

- **6 `:verified`** — invariant + architecture entries with hypothesis property tests (OQ-001 + OQ-002 + OQ-010 + OQ-011 + OQ-013 + OQ-015)
- **67 `:tested`** — example-tested entries covering all modules + workflows + cross-cutting bindings
- **7 `:argued`** — manual-by-nature licensing claims + adopter-org-gated substrate enforcement + SOP-bound architecture decisions

See `BUSINESS/ENGINE_SPEC.md` for the full spec, `BUSINESS/changelog.md` for release history, and `BUSINESS/dashboard.md` for the priority stack.

**Test suite:** 108 pytest + hypothesis tests passing. CI runs validation on every overlay + composite + every example bundle's regenerate dry-run on every push touching `engine/`, `modules/`, `registry/`, `templates/`, or `bundles/`.

## Standards licensing — important

Open QMS's regulatory modules reference standards by clause number and normative summary, but **do not redistribute the standard text itself**. Many of the standards referenced are commercially published copyrighted works sold by their publishers under per-user or per-organization license terms.

**Adopters must obtain their own licensed copies of any standard they intend to implement against.** The crosswalks in this repository are useful as a map and as a coverage check; they are not a substitute for the standards themselves.

**Public-license (representative, freely available):**

- US federal regulations: 21 CFR Parts 11, 117, 123, 210, 211, 803, 807, 809, 814, 820, 860, 1271 (via FDA / GovInfo / ecfr.gov)
- 14 CFR Part 21 (FAA); EU Directives + Regulations (via EUR-Lex)
- EU GMP EudraLex Vol. 4 + Annexes (via European Commission)
- NIST publications (AI RMF 1.0; SP 800-53)
- EU AI Act 2024/1689
- ICH guidances (Q5A, Q5D, Q5E, Q6B, Q7, Q9, Q10, Q11, Q12, etc.) via ich.org
- PIC/S Annex 1
- Codex Alimentarius (CXC 1-1969 General Principles of Food Hygiene)
- UN R155 / R156 (UNECE WP.29)

**Commercially licensed (representative, not exhaustive):**

- ISO standards (9001, 13485, 14001, 22000, 22301, 26262, 27001, 37001, 42001, 45001, 50001, 14971, 15189) — purchased per copy from ISO or national member bodies (ANSI, BSI, etc.)
- IEC standards (60601-1, 62304, 62366-1, 82304-1) — from IEC or national bodies
- ISO/IEC joint standards (23894) — from ISO/IEC
- ISO/SAE joint standards (21434) — from ISO + SAE
- SAE International standards (AS9100D, AS9102, ARP4754A, ARP4761, J3061)
- RTCA standards (DO-178C, DO-254, DO-330, DO-326A)
- IATF 16949 (from IATF national bodies)
- VDA QMC (Automotive SPICE 4.0)
- AIAG (PPAP, APQP, MSA, SPC, PFMEA)
- ISTA standards (2A, 3A, etc.) via ISTA membership
- FSSC 22000 v6 (from Foundation FSSC)
- IMDRF guidances (SaMD N12, Essential Principles)
- IATF 16949
- ISO 14708-1 (active implantables)

Pharma is notable as the first Open QMS vertical where **most cited standards are public license** (ICH guidances + CFR Parts + EudraLex + PIC/S). Cell therapy / ATMP is similar (all PUBLIC). Manufacturing requires only ISO 9001 commercial license.

Open QMS contributors and adopters are responsible for complying with the license terms of any standard they reference, implement against, or distribute alongside their own QMS. **The Apache-2.0 license on Open QMS itself does not extend to the standards it references.** Budget for licensed standards as part of the cost of operating in a regulated industry — this is true regardless of QMS platform.

## Important disclaimers

- **This is infrastructure, not a validated QMS.** You must validate the system for your intended use per your applicable regulations.
- **Open QMS does not provide legal or regulatory advice.** The regulatory mappings are reference material. Consult qualified regulatory professionals for your specific situation.
- **GitHub's platform is not inherently Part 11 compliant.** The gap analysis in `docs/regulatory/` describes what supplementary controls are needed (organizational GPG enforcement; PHI compartmentalization; controlled-document signing discipline; record retention).
- **Your organization's SOPs, forms, and quality records are yours.** Open QMS provides templates. You fill them in. Open QMS does not adjudicate semantic correctness of your clause-to-artifact mapping (that's your V&V responsibility evidenced by your certification audit).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New regulatory modules + class overlays + templates contributions welcome — the platform composition pattern (OQ-011 compose primitive, OQ-013 validation harness, OQ-014 registry, OQ-015 regenerate) has been demonstrated stable across 18 releases without engine code change.

## License

Apache 2.0. See [LICENSE](LICENSE).
