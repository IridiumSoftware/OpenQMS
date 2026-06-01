# Open QMS

**Open-source GitHub-native QMS generator** — produces traceable Quality Management System scaffolds for regulated industries, with bidirectional clause-to-template traceability enforced as a mechanically-checked invariant.

Open QMS is **infrastructure, not a validated QMS.** Adopters validate the deployment for their specific regulated scope. The architecture is defensible at audit; the semantic adequacy of any specific SOP against any specific clause requires QA judgment (the OQ-080 firewall).

[**Read the compliance-architecture trust-gate document →**](compliance-architecture.md)

---

## Current scope — v0.68.0

| Dimension | Count |
|---|---|
| Verticals (regulated industries) | **8** — medical-devices · aerospace · automotive · manufacturing · pharma · food-safety · chemicals · finance (SOX/ICFR) |
| Module shapes | **6** — vertical · sub-vertical · class overlay · cross-cutting overlay · sub-overlay · cross-overlay |
| Class overlays (rigor / product-class) | **44** across 6 verticals |
| Cross-cutting overlays | **26** — ISO 27001 · regulated-AI · ISO 14001/45001/50001 · ISO 37001 · ISO 22301 · ISO 31000 · ISO 37301 · SOC 2 · PCI DSS · HITRUST · NIST CSF · DORA · privacy (GDPR+CCPA) · HIPAA · US state privacy · recall-workflow · others |
| Sub-overlays | **26** — CMMC levels · SOC 2 types · ISO 27001 extensions · NIST CSF tiers · PCI DSS SAQ types · DORA tiers · HITRUST levels · ISO 37301 sectoral profiles |
| Cross-overlays | **12** — combination-product · IMS · food-pharma-grade · connected-medical-device · cell-therapy-supply-chain · food-allergen-recall · defense-aerospace-cyber · digital-health-multi-region · automotive-supply-chain · clinical-trial-multi-region · banking-resilience · utility-cybersecurity |
| Validation family (P2) | **3** — validation-package + validation-package-fda + validation-package-eu (risk-based CSV/CSA) |
| Total modules | **120** + general |
| Registry standards | **144** (most PUBLIC license; commercial standards flagged) |
| Registry jurisdictions | **20** |
| Document templates | **119** with frontmatter schema validated in CI |
| Example bundles | **8** vertical-specific + **4** stage-specific presets |
| Spec entries (status) | **114** — 6 `:verified` / 103 `:tested` / 5 `:argued` / 0 `:open` |
| Engine CLI subcommands | **11** — `resolve` · `validate` · `regenerate` · `signatures` · `trace` · `trace-instances` · `coverage` · `crosswalk` · `jurisdictions-query` · `registry` · `verify-deployment` |
| Pytest suite | **251 tests** in CI gating every push |
| Deepest composition tested in CI | **24-module ultra composite** (medical-devices + pharma + combination-product + connected-medical-device + digital-health-multi-region + sterile + HIPAA + privacy + 11 cross-cutting + IMS + SOC 2 + HITRUST + ISO 27001 cloud/privacy + ISO 37301) |

---

## How Open QMS thinks about a QMS

| QMS activity | GitHub-native equivalent |
|---|---|
| Document approval | PR with required CODEOWNERS reviewers + GPG-signed approval commit |
| Change control | Issue → PR → review → merge (state machine enforced in CI) |
| CAPA | Issue with structured CAPA template (7-state lifecycle) |
| Complaint intake | Issue with PHI-compartmentalized triage template |
| Training record | Auto-generated issue on controlled-doc update; close = completion |
| Periodic doc review | Issue with 3-outcome flow + version-bump enforcement |
| Quarterly access review | Issue tied to HR-to-GitHub identity-mapping register |
| Annual restoration test | Issue with 13-step runbook |
| Per-module regulatory review | Issue + finding-log file + per-module attestation badge |
| Release | Signed tag (`git tag -s`) → CI verification → release-artifact ZIP |
| Audit trail | Git history (immutable under force-push-disabled) + commit-trailer signature meaning per §11.50 |
| Traceability matrix | `openqms trace --all` — zero-orphan invariant enforced in CI |
| Coverage gate | `openqms coverage --all --threshold 100` — 100% aggregate clause coverage required |
| Deployment posture verification | `openqms verify-deployment --policy deployment-policy.yaml` |

---

## Quick paths

**New to the project?**

1. [`Compliance architecture`](compliance-architecture.md) — 11-section trust-gate document mapping 10 highest-frequency adopter-evaluator topics (21 CFR Part 11 · EU GMP Annex 11 · ISO 13485 · audit trails · e-signatures · permissions · validation · backup/recovery · record retention · cybersecurity · system administration controls) to architecture components + spec entries + evidence files + adopter responsibilities.
2. [`Modules catalog`](modules-catalog.md) — full module inventory with adoption guidance.
3. [`Quick start`](guide/quickstart.md) — install + first commands.

**Just hired into an Open QMS adopter org?**

- [`Onboarding (first 30 days)`](guide/onboarding.md) — day-1 / day-2-7 / week-2 / week-3-4 / month-1 checklist with completion criteria.
- Plus the role guide matching your hat: [Quality Manager](guide/role-quality-manager.md) · [Engineer](guide/role-engineer.md) · [Auditor](guide/auditor-walkthrough.md).

**Picking a starting scope for your startup?**

- [`Maturity model + startup-stage presets`](guide/maturity-model.md) — 4 industry-agnostic presets (`pre-seed` → `seed` → `series-a` → `series-b-plus`) with per-stage IN/OUT rationale + compliance-event graduation triggers.
- Each preset ships as a bundle YAML at [`presets/`](https://github.com/IridiumSoftware/open-qms/tree/main/presets) on GitHub.

**Setting up your fork?**

- [`GPG signing`](guide/gpg-signing.md) + [`Signature meaning (§11.50)`](guide/signature-meaning.md) — the audit-trail attribution chain.
- [`Document routing (CODEOWNERS)`](guide/document-routing.md) — how PR review chains route to functional teams.
- [`Verify deployment`](guide/verify-deployment.md) — automated verification that your fork's branch-protection + signed-commits + CODEOWNERS coverage matches declared policy.

**At audit?**

- [`Auditor walkthrough`](guide/auditor-walkthrough.md) — traditional-QMS-concept → GitHub-equivalent mapping.
- [`Document control`](guide/doc-control.md) + [`Traceability`](guide/traceability.md) + [`CAPA lifecycle`](guide/capa-lifecycle.md) — the operating workflows.
- [`Release management`](guide/release.md) — `git tag -s` discipline + release-artifact archival.

---

## Honest disclaimers

- **Not a validated commercial eQMS.** Open QMS is the substrate; adopters validate their own deployment for their own scope (per OQ-080).
- **Not a substitute for QA judgment.** The modules encode regulatory requirements; the adopter's quality professionals interpret them for their product, risk, and jurisdiction.
- **Not a regulator-certified Part 11 implementation.** The §11.50 signature-meaning prototype is an opinionated convention; production drug-release records typically warrant validated commercial systems for the batch-records-themselves layer.
- **Apache-2.0 on Open QMS code does NOT extend to referenced standards.** ISO / IEC / IATF / AIAG / USP / IMDG / IATA DGR / ISO 27017 / ISO 27701 and similar are commercial standards that adopters must license separately (per OQ-070 + OQ-071).
- **Per-module regulatory review status is published.** Per [`BUSINESS/regulatory_review_cadence.md`](https://github.com/IridiumSoftware/open-qms/blob/main/BUSINESS/regulatory_review_cadence.md), the honest starting baseline is **0 / 119 modules** independently reviewed by a §2-qualified reviewer. Modules pass the engine's structural coverage invariant + clause-template binding; semantic adequacy against authoritative regulator text is process-governance work tracked separately.

---

## Project repository

[github.com/IridiumSoftware/open-qms](https://github.com/IridiumSoftware/open-qms)

Forward-work priorities + status: see [`Compliance architecture`](compliance-architecture.md) §Forward work. Per-release record: [`BUSINESS/changelog.md`](https://github.com/IridiumSoftware/open-qms/blob/main/BUSINESS/changelog.md). Formal spec discipline: [`BUSINESS/ENGINE_SPEC.md`](https://github.com/IridiumSoftware/open-qms/blob/main/BUSINESS/ENGINE_SPEC.md).
