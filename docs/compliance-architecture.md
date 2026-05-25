# Compliance architecture — Open QMS

**Audience:** Quality leaders, regulatory affairs, IT/SecOps, and internal/external auditors evaluating Open QMS for adoption or in-flight audits.

**Question this document answers:** *Is Open QMS's architecture defensible at audit?*

**Honest scope:** Open QMS is an open-source generator that produces GitHub-native QMS scaffolds. It is **infrastructure, not a validated commercial eQMS**. This document maps how the architecture addresses each common compliance topic, what is in-scope for the generator vs. the adopter's organizational responsibility, and where to find the evidence in this repo.

For the formal claim discipline (every named behavior gets a spec entry + evidence file + status), see [`BUSINESS/ENGINE_SPEC.md`](../BUSINESS/ENGINE_SPEC.md) + [`BUSINESS/artifact_registry.md`](../BUSINESS/artifact_registry.md). For the per-release record, see [`BUSINESS/changelog.md`](../BUSINESS/changelog.md).

---

## 1. 21 CFR Part 11 — Electronic records & electronic signatures (US FDA)

**What Part 11 requires:** secure, attributable, contemporaneous electronic records with linked e-signatures that capture the meaning of the signing act (§11.50); audit trails that record what changed, who, when, why (§11.10(e)); validation of computerized systems used in regulated processes (§11.10(a)).

**How Open QMS addresses it:**

| Requirement | Architecture component | Spec entry | Evidence file |
|---|---|---|---|
| §11.10(a) validation of systems | Engine itself is validated by 129-test pytest suite + bundle-baseline regression check + zero-orphan trace invariant + 100% aggregate clause-coverage gate | OQ-001, OQ-010, OQ-011, OQ-013, OQ-015 (`:verified` via hypothesis property tests) | `engine/tests/test_property.py` |
| §11.10(c) protection of records | Git history is immutable under force-push-disabled branch protection | OQ-022 `:argued` | `docs/guide/gpg-signing.md` |
| §11.10(e) audit trails | Every commit is a structured, attributable, immutable change record with author + timestamp + intent (commit message) + content diff | OQ-001 `:verified`, OQ-022 `:argued` | git itself + branch protection |
| §11.50 signature meaning | Commit-trailer convention: `Signature-Meaning:` required; `Signature-Role:` and `Signature-Justification:` optional; parser + GPG-status decoder + audit-trail JSON exporter shipped | OQ-060 `:tested` | `engine/openqms/signatures.py`, `docs/guide/signature-meaning.md`, `.github/workflows/signature-check.yml` (dormant — active in adopter forks via path filter) |
| §11.100 unique e-signature attribution | GPG key registration + HR-attested identity mapping per individual | OQ-023 `:argued` | `docs/guide/gpg-signing.md` |
| §11.200 e-signature components & controls | GPG private key + passphrase + key-on-device | OQ-023 `:argued` | `docs/guide/gpg-signing.md` |
| §11.300 controls for ID codes / passwords | GitHub authentication (2FA org-mandated) + GPG passphrase | OQ-023 `:argued` | adopter-org responsibility |

**Adopter responsibility (NOT in Open QMS scope):**
- Branch protection configuration (force-push-disabled, required reviewers, required status checks)
- Org-mandated 2FA
- GPG key registration + HR-attested identity mapping per signer
- Active enforcement of the `signature-check.yml` workflow (dormant by default; activate in adopter fork)
- Periodic access review + key rotation policy
- Decision on signature-meaning vocabulary controlled at the org level

**Honest limitations:** GitHub's "Verified" badge certifies key→account, not account→person. The signature-meaning system is a prototype — Part 11 §11.50 binding is established in the convention + parser + audit-trail exporter but the convention itself is opinionated and not certified by FDA. Adopters operating in fully Part 11–binding scope (drug-product release records, clinical trial source data) should treat this as the audit-trail layer for governance records, not a substitute for a validated CSV-treated production records system.

**See also:** `modules/pharma/module.yaml` (clauses bound to 21 CFR 211 + Part 11 for computerized systems); `modules/medical-devices/module.yaml` (clauses bound to ISO 13485 §4.2 + 21 CFR 820.40 document controls).

---

## 2. EU GMP Annex 11 — Computerised systems

**What Annex 11 requires:** risk-based validation; suppliers under formal agreement; functional + technical specifications; system-life-cycle approach; audit trails enabled for GMP-relevant data; periodic review; archive integrity; incident management; e-signatures meeting §11.50-equivalent (linked to identity, traceable to record, includes meaning).

**How Open QMS addresses it:**

| Requirement | Architecture component | Where covered |
|---|---|---|
| Risk-based validation | Engine validation discipline (pytest + baselines + invariants); per-module validation harness | OQ-013 `:verified`; `modules/pharma/module.yaml` clauses |
| Supplier agreement | Open QMS is Apache-2.0 open source; the "supplier" is the project + the adopter's own DevOps team | License + adopter org |
| Specifications | `BUSINESS/ENGINE_SPEC.md` (102 entries); `DESIGN.md`; per-module `module.yaml` is the functional spec | Repo root |
| System-life-cycle | Git history is the SDLC trail; releases tagged; changelog versioned | `BUSINESS/changelog.md` |
| Audit trails for GMP-relevant data | git commit log + signature-meaning trailers (§11.50 binding) | `engine/openqms/signatures.py` |
| Periodic review | Cross-audit protocol (A0-A6) run per major release | `BUSINESS/audit_*.md` |
| Archive integrity | Git's content-addressed object store + GitHub durability + adopter export | adopter responsibility |
| Incident management | Issue templates + ChangeManagement workflow + complaint template with PHI-compartmentalization | `.github/ISSUE_TEMPLATE/`, `docs/guide/complaints.md` |
| E-signatures Annex 11 §14 | GPG-signed commits + signature-meaning trailers (same as §11.50) | OQ-060 |

**Pharma module standards covered:** ICH Q9 quality risk management + ICH Q10 PQS + ICH Q7 API GMP + 21 CFR 210/211 cGMP + EudraLex Vol. 4 with Annexes 15 (Qualification & Validation) + 16 (QP Certification) + PIC/S Annex 1 (2022) sterile manufacturing + Part 11 for computerized systems.

**Adopter responsibility:** Annex 11 §1 risk management documented at org level; Annex 11 §3 supplier audit (adopter audits Open QMS — `BUSINESS/` is public for this purpose); Annex 11 §4 validation lifecycle (URS + IQ/OQ/PQ — see §7 below).

---

## 3. ISO 13485:2016 — Medical devices QMS

**What ISO 13485 requires:** documented quality management system covering management responsibility (§5), resource management (§6), product realization (§7 — design controls, purchasing, production, validation, identification & traceability, customer property, preservation), and measurement/analysis/improvement (§8 — feedback, complaint handling, internal audit, CAPA).

**How Open QMS addresses it:**

- **`modules/medical-devices/module.yaml`** ships 62 clauses spanning all 8 §-groups across 11 standards (ISO 13485, ISO 14971, IEC 62304, IEC 62366-1, IEC 60601 family, ISO 11607 packaging, 21 CFR 820, EU MDR Annex I + Annex XIV, Article 117 cross-reg, FDA QSR transition). Bound to 30+ templates including Quality Manual, Design History File, Risk Management File, Design Verification/Validation Protocols, Software Requirements/Architecture/Test Protocols, SOUP Register, Audit Procedure, Management Review Record, Supplier Evaluation, CAPA workflow.
- **9 class overlays** for risk-class + product-class deltas: mdr-class-iii / mdr-class-iib / mdr-class-iia + fda-class-iii / fda-class-ii + samd + implantable + ivd (sub-vertical).
- **Cross-cutting overlays** add risk management (iso-31000), IS (iso-27001), AI/ML (regulated-ai), BCMS (iso-22301), anti-bribery (iso-37001), privacy (privacy + hipaa + us-state-privacy).
- **Cross-overlays** for intersection-specific requirements: combination-product (medical-devices + pharma), connected-medical-device (med-dev + AI + privacy + IS + HIPAA — FDA §524B + EU MDR Annex I §17.2 + SBOM + Cures Act), digital-health-multi-region (per-jurisdiction scope + data residency + multi-region consent + MDSAP harmonisation).

**Spec entries:** OQ-040 (medical-devices module) through OQ-058 (regulated-AI overlay); OQ-072 onwards for verticals + class overlays added since v0.14.0.

**At-audit demonstration:** `openqms trace --module medical-devices --format md` produces the bidirectional traceability matrix mapping every clause → bound template. `openqms coverage --module medical-devices` reports % clause-coverage (100% at v0.51.0). `openqms validate --module medical-devices` enforces the per-module validation harness.

**Adopter responsibility:** organizational quality manual sign-off, training records, supplier audit cadence, internal audit programme, management review cadence, post-market surveillance + vigilance reporting actually filed with the regulator.

---

## 4. Audit trails

**What auditors look for:** who changed what, when, why; ability to reconstruct prior states; immutability of the trail itself; signature linkage to the change.

**How Open QMS addresses it:**

- **Git history is the audit trail.** Every change is a commit with author + email + timestamp + diff + message. Git's content-addressed object store provides cryptographic integrity (any tampering invalidates the SHA chain).
- **Immutability is enforced by branch protection** (force-push-disabled on the protected branch). Without this enforcement, history is mutable — adopter MUST configure branch protection to claim audit-trail immutability.
- **Signature linkage** via GPG-signed commits binds identity to content (OQ-023). Combined with the §11.50 signature-meaning trailers (OQ-060), each change can carry not just "who signed" but "for what reason" (Approved / Reviewed / Witnessed / Authored / etc.).
- **Bidirectional traceability** from spec entry → registry row → evidence file is maintained via `openqms trace` (OQ-067) + zero-orphan invariant enforced in CI on every push.
- **Per-release evidence snapshot:** the `bundles/*.matrix.json` files committed alongside each `bundles/*.yaml` are the reproducible-output baseline; CI re-runs `openqms regenerate` in dry-run mode and fails if any matrix has drifted (OQ-015 `:verified`).
- **Audit export** via `openqms signatures export --output audit.json` produces a Part 11–style JSON of every commit with parsed signature-meaning trailers + GPG verification status.

**Spec entries:** OQ-022, OQ-023, OQ-060, OQ-067, OQ-015.

**At-audit demonstration:** show the auditor `git log --show-signature --pretty=fuller` for a representative time window; demonstrate `openqms signatures export`; show the branch protection settings screenshot; demonstrate `openqms trace --all` zero-orphan output.

**Adopter responsibility:** branch protection configuration; org-mandated GPG signing; deletion/archival policy (when the time comes to actually purge old branches per retention schedule — see §9).

---

## 5. E-signatures

**What regulators require:** signature is unique to one individual; not re-usable; secure (private credential); linked to the record being signed; captures the meaning of the signing act (approval, review, witness, authorship — Part 11 §11.50).

**How Open QMS addresses it:**

- **GPG-signed commits.** Per-individual GPG key registered with GitHub. Org policy requires the registered key match HR-on-file identity. `gpg --sign` cryptographically binds the signer's private key to the commit object's SHA. (OQ-023 `:argued`.)
- **Signature meaning via commit trailer** (Part 11 §11.50 binding). The convention is:
  ```
  Signature-Meaning: Approved | Reviewed | Witnessed | Authored | Acknowledged
  Signature-Role: Quality Manager | Engineer | Auditor | ...           (optional)
  Signature-Justification: short free-text reason                       (optional)
  ```
  Parsed by `engine/openqms/signatures.py`; exported to Part 11–style audit trail JSON.
- **Verification:** the dormant `.github/workflows/signature-check.yml` activates in adopter forks via path filter and rejects PRs missing the trailer.
- **Multi-signer pattern:** GitHub PR "required reviewers" plus per-review GPG-signed approval commits captures the multi-signer workflow (engineer signs the change, quality manager signs the review, witness if separate).

**Honest limitations:** the signature-meaning system is a prototype convention, not a regulator-certified mechanism. Adopters in fully Part 11–binding scope should treat this as the records-governance layer; production drug-release records typically warrant a validated CSV-treated commercial eQMS for batch records themselves.

**Guides:** `docs/guide/gpg-signing.md`, `docs/guide/signature-meaning.md`.

---

## 6. Permissions / access controls

**What regulators require:** access limited to authorized individuals; role-based assignments; periodic access review; segregation of duties (the person who authors a record cannot solely approve it).

**How Open QMS addresses it:**

- **GitHub org permissions** provide the access layer: read / triage / write / maintain / admin per individual or team.
- **Branch protection rules** enforce: required PR review (with required-reviewer-count ≥ 1 and "require approvals from CODEOWNERS"), required status checks (engine-tests CI must pass), require signed commits, dismiss stale reviews on new commits, restrict who can push to protected branches.
- **CODEOWNERS file** maps repo subdirectories to role-named teams (e.g., `/modules/medical-devices/ @org/quality-medical-devices`); a PR touching that path requires a review from a member of that team. This is the segregation-of-duties primitive.
- **PR + required reviewers** is the role-based approval mechanism (OQ-020 `:tested`).
- **Branch protection prevents merge without CI + approvals** (OQ-021 `:tested`).
- **Force-push-disabled** preserves history immutability (OQ-022 `:argued`).

**Adopter responsibility:** team structure that reflects the org's role taxonomy; CODEOWNERS file per the adopter's role assignment; access review cadence (quarterly is typical; see `docs/guide/auditor-walkthrough.md`); offboarding process to revoke access when individuals depart.

---

## 7. Validation (engine validation + module validation)

**What regulators require:** documented evidence that a system performs as intended in its operational environment; per ICH Q9 + ISO 14971, validation scope is proportionate to risk.

**How Open QMS addresses it:**

**Engine validation (Open QMS itself):**
- 129/129 pytest tests passing in CI on every push
- Bundle-baseline regression check (any drift in `bundles/*.matrix.json` fails CI)
- YAML linter (catches malformed module YAML before runtime, e.g., the unquoted-colon failure mode observed during chemicals arc)
- Zero-orphan trace invariant enforced on every push (`openqms trace --all`)
- 100% aggregate clause-coverage gate enforced on every push (`openqms coverage --all --threshold 100`)
- 6 invariant + architecture spec entries `:verified` via hypothesis property tests (OQ-001 + OQ-002 + OQ-010 + OQ-011 + OQ-013 + OQ-015)
- Per-release semver discipline; engine version surfaced via `openqms --version`

**Module validation (each `modules/<name>/module.yaml`):**
- Per-module `openqms validate --module <name>` runs the validation harness asserting: every clause is bound to ≥ 1 template; every template's `addresses` entries refer to in-module clauses; declared standards exist in the registry; YAML schema is well-formed
- Composition validation: `openqms validate --module <m1> --module <m2> [...]` composes modules under union and re-runs the harness on the composite
- Repo-wide coverage report: `openqms coverage --all` returns aggregate + per-module metrics

**What's NOT shipped (forward work — flagged in feedback received 2026-05-25 as P2):**
- URS (User Requirements Specification) template
- IQ (Installation Qualification) template
- OQ (Operational Qualification) template
- PQ (Performance Qualification) template
- Change Assessment template
- Computer System Validation (CSV) protocol covering the adopter's deployment of Open QMS itself
- Validation Master Plan (VMP) for the Open QMS deployment

These are planned for a dedicated `validation-package` cross-cutting overlay in a future release.

**Existing validation templates** (in scope today):
- `VERIFICATION-PROTOCOL-TEMPLATE.md`
- `VALIDATION-PROTOCOL-TEMPLATE.md`
- `SOFTWARE-TEST-PROTOCOL-TEMPLATE.md` (IEC 62304 §5.5-5.7)
- `RISK-MANAGEMENT-FILE-TEMPLATE.md` (ISO 14971)
- Per-vertical validation: pharma module covers Annex 15 qualification & validation; medical-devices covers ISO 13485 §7.5.6 + 21 CFR 820.75 process validation.

**Adopter responsibility:** authoring the URS for their specific deployment scope; running IQ/OQ/PQ in their environment; signing off the Validation Summary Report; periodic re-validation per change-control trigger.

---

## 8. Backup / recovery

**What regulators require:** GMP/GxP records are recoverable in the event of system failure; backup is tested via periodic restoration exercises; RTO + RPO defined per criticality.

**How Open QMS addresses it:**

- **Git is inherently distributed.** Every clone is a full backup of history + objects. Adopters cloning to multiple workstations + CI runners already have N-way replication.
- **GitHub's underlying durability** provides primary storage redundancy (GitHub's own backup posture is documented in their SOC 2 Type II report; adopters can request).
- **Adopter-driven export:** `git clone --mirror` to an org-controlled backup destination on the adopter's schedule. Scriptable; cron-able.
- **`bundles/*.matrix.json` files** are the reproducible-output snapshots; regenerable from the YAML inputs via `openqms regenerate`.
- **Bundle-baseline regression check** in CI ensures the regeneration is deterministic — if the matrix changes unexpectedly, CI fails and the change must be approved (this IS the audit trail).
- **ISO 22301 BCMS cross-cutting overlay** (`modules/iso-22301/`) provides the BCMS substrate for adopters needing formal RTO/MAO/MBCO/RPO discipline; **`templates/qms-bcms/BCP.md`** is the Business Continuity Plan template.

**Adopter responsibility:** organizational backup strategy (frequency + destination + retention); restoration testing cadence (typically annual minimum); DR runbook; RTO/RPO definition per record type; compliance with org IT policy.

---

## 9. Record retention

**What regulators require:** records retained for the period specified by the applicable regulation (highly variable: ISO 13485 §4.2.5 lifetime + N years; HIPAA §164.316 6 years; ATMP EU 30 years; 21 CFR 211.180 1 year after expiry date or 3 years after distribution).

**How Open QMS addresses it:**

- **Git history retention** is effectively indefinite within the repository (no automatic expiry); when the adopter decides to archive or purge, the action is a deliberate, audited operation.
- **Per-module clauses encode the retention requirement** for each regulated record class. Example: ATMP module clauses cite the 30-year EU traceability retention. HIPAA module cites §164.316 6-year retention. Pharma cites 21 CFR 211.180 retention windows. The retention requirement is captured at the clause level so the adopter sees it in the trace matrix.
- **`tissue-cell-traceability-record.md` template** (ATMP) explicitly addresses 30-year format-stability planning — a forward-thinking concern because file formats today may not be readable in 30 years.
- **The adopter's retention policy** is encoded in the `docs/guide/doc-control.md` guide (template; adopter customizes) + the org's records retention schedule.

**Adopter responsibility:** records retention schedule per regulated jurisdiction; periodic archival or purge process; archive integrity verification (does the archived data still parse? this is the format-stability question); legal hold process for records under litigation hold.

---

## 10. Cybersecurity

**What regulators require:** technology supporting GMP/GxP operations is protected from cyber threats; access controls, monitoring, incident response, vulnerability management, supply-chain risk; per-domain heightening (medical-device cyber per FDA §524B + EU MDR §17.2; banking per DORA + FFIEC; utility per NERC CIP + EU NIS2; defense per CMMC + DFARS).

**How Open QMS addresses it:**

**Cross-cutting overlays** (apply to any vertical):
- **`iso-27001`** — ISMS substrate (Annex A controls)
  - **`iso-27001-cloud`** sub-overlay — ISO 27017 cloud-services additions
  - **`iso-27001-privacy`** sub-overlay — ISO 27701 PIMS extension
- **`nist-csf`** — NIST CSF 2.0 6-Function backbone
  - **`nist-csf-tier-1`** through **`-tier-4`** sub-overlays — Implementation Tiers
- **`soc-2`** — SOC 2 Trust Services Criteria
  - **`soc-2-type-i`** — point-in-time
  - **`soc-2-type-ii`** — observation-period
- **`hitrust-csf`** — HITRUST CSF
  - **`hitrust-e1`** (Essentials, 44 controls) + **`-i1`** (Intermediate, 182) + **`-r2`** (Risk-based 2-year, 200-2000+)
- **`pci-dss`** — PCI DSS v4
  - 5 SAQ sub-overlays (saq-a / saq-a-ep / saq-d-merchant / saq-d-sp / saq-p2pe)
- **`dora`** — EU Digital Operational Resilience Act
  - **`dora-ctpp`** + **`-non-ctpp`** + **`-tlpt`** sub-overlays
- **`cmmc`** — Cybersecurity Maturity Model Certification
  - **`cmmc-level-1`** + **`-2`** + **`-3`** sub-overlays
- **`defense-cui`** — DoD Controlled Unclassified Information

**Cross-overlays** (intersection-specific cybersecurity):
- **`connected-medical-device`** — FDA §524B cyber-device + EU MDR Annex I §17.2 + SBOM + Cures Act + AI/ML PCCP
- **`defense-aerospace-cyber`** — DFARS 7012/7019/7020/7021 + DO-326A/DO-356A airworthiness cyber + ITAR + DoDI 5000.90
- **`banking-resilience`** — DORA + FFIEC IT Handbook + NIST CSF + multi-stream incident reporting + TLPT
- **`utility-cybersecurity`** — NERC CIP-002 through CIP-014 + TSA Pipeline SD + CISA 16-sector + EU NIS2 + IEC 62443 + CIRCIA
- **`digital-health-multi-region`** — per-jurisdiction cyber framework (FDA + EU MDR + UK + Canada + Switzerland) + multi-stream breach notification

**HIPAA Security Rule** (in `modules/hipaa/`) provides healthcare-specific cyber: administrative + physical + technical safeguards per §164.308 + §164.310 + §164.312; risk analysis per §164.308(a)(1)(ii)(A) template.

**Spec entries:** OQ-048 (iso-27001), OQ-058 (regulated-ai), OQ-104 (cross-cutting overlay batch IS+governance+compliance+resilience+DoD-CUI), OQ-108 (privacy), OQ-109 + OQ-110 (sub-overlay batches), OQ-112 (HIPAA), OQ-113 (cross-overlay batch including connected-medical-device + defense-aerospace-cyber), OQ-118 (banking-resilience + utility-cybersecurity).

**Adopter responsibility:** organizational SOC + incident response capability; threat model documented; vulnerability management programme; penetration testing cadence (DORA TLPT mandatory for significant entities); supply-chain risk monitoring; cyber-insurance posture; per-regulator incident reporting actually filed within mandated windows.

---

## 11. System administration controls

**What regulators require:** the people administering the system are themselves identified, trained, and access-limited; admin actions are logged + auditable; change-management governs system modifications.

**How Open QMS addresses it:**

- **GitHub org admin role** is the administrative layer. Org owners + repo admins are the privileged identities.
- **Admin actions logged in GitHub audit log** (org-level — adopter must enable + retain per their retention schedule).
- **Branch protection rules ARE the change-management primitive** for repo content. Modifications to protected branches require PR + review + status checks + signatures.
- **Repository settings changes** (branch protection rule edits, GPG key requirements, CODEOWNERS changes) are themselves admin actions, logged in the org audit log.
- **Document control via PR workflow** is documented in `docs/guide/doc-control.md`.
- **Change-control issue template** + design-control traceability per OQ-031 / OQ-032 / OQ-033.
- **Auditor walkthrough guide** at `docs/guide/auditor-walkthrough.md` describes the at-audit demonstration sequence.

**Adopter responsibility:** admin role assignment + periodic review; admin training records; change-window policy if applicable; org audit-log retention; CODEOWNERS curation; offboarding process for departing admins.

---

## What Open QMS is NOT — disclaimers

Per OQ-080 (`:tested` — README discloses "infrastructure, not validated QMS"):

- **Not a validated commercial eQMS.** Open QMS is the substrate; adopters validate their own deployment for their own scope.
- **Not a substitute for QA judgment.** The modules encode regulatory requirements; the adopter's quality professionals interpret them for their product, risk, and jurisdiction.
- **Not a substitute for organizational training.** The training-trigger workflow surfaces who needs training when; the actual training content and delivery is adopter-driven.
- **Not a regulator-certified Part 11 implementation.** The §11.50 signature-meaning prototype is an opinionated convention; production drug-release records typically warrant validated commercial systems for the batch-records-themselves layer.
- **Apache-2.0 license on Open QMS code does NOT extend to referenced standards.** ISO, IEC, IATF, AIAG, USP, IMDG, IATA DGR, ISO 27017, ISO 27701, and similar are commercial standards that adopters must license separately. (See OQ-070 + OQ-071.)

---

## How to use this document at audit

1. **Auditor asks a question** ("show me your e-signature process," "demonstrate your audit trail," "what is your validation evidence?").
2. **Map question → topic above** (e-signature → §5; audit trail → §4; validation → §7; etc.).
3. **Open the spec entries cited in that topic** in `BUSINESS/ENGINE_SPEC.md`.
4. **Open the evidence files cited in `BUSINESS/artifact_registry.md`** for those spec entries.
5. **Demonstrate the runtime behavior** via the CLI examples: `openqms trace --module X --format md`, `openqms coverage --module X`, `openqms signatures export --output audit.json`, `openqms validate --module X --module Y`.
6. **Show organizational controls** outside the repo: branch protection settings screenshot, CODEOWNERS file, GPG key registration policy, access review records, training records.

Keep `BUSINESS/dashboard.md` open as the at-a-glance status snapshot. Keep `BUSINESS/audit_*.md` files available as evidence of self-audit discipline (the cross-audit findings from the most recent release — A0–A6 against the project's own discipline).

---

## Forward work (acknowledged gaps)

This section consolidates two feedback inputs:

1. **Adopter-experience feedback received 2026-05-25** (four priorities, P1 closed at v0.52.0 by this document).
2. **Independent reviewer technical assessment received 2026-05-25** (reviewed a slightly older state at the v0.38–v0.39 era; reviewer's tactical concerns assessed against current state below).

The reviewer's headline framing — *"worth pursuing, but treat it as a generator for QMS infrastructure, not as 'the QMS'"* — matches the project's own honesty bound (OQ-080). This section names the work remaining to harden that infrastructure-layer claim.

**Effort calibration** (qualitative; informs sequencing, not commitment):

- **light** — single file or small set; mostly documentation or contained script; ≤ ½ day of focused work.
- **medium** — multiple deliverables: new templates + workflow changes + tests + composites; ½ to 2 days; bounded scope.
- **hard** — substantial new feature surface: new module + multiple templates + standards crosswalks + tests + composites + docs + per-jurisdiction handling; 2+ days; multi-session.

**Current effort distribution across remaining 6 open priorities** (post-v0.58.0): 2 hard (P2 + P15) · 4 medium (P4 + P5 + P10 + P11) · 0 light. Closed since v0.51: P1 (v0.52.0) · P6 + P7 + P8 + P12 + P13 + P14 (light batch at v0.55.0) · P3 (non-technical UX batch at v0.57.0) · P9 (template schema validation at v0.58.0).

### Adopter-experience priorities

| Priority | Effort | Gap | Plan |
|---|---|---|---|
| ✓ **P1** | — | Compliance architecture trust-gate documentation | Closed at v0.52.0 by this document |
| **P2** (next) | **hard** | Validation package templates (URS + IQ/OQ/PQ + Change Assessment + Computer System Validation protocol + Validation Master Plan) | Future release — `validation-package` cross-cutting overlay bound to 21 CFR Part 11 + EU GMP Annex 11 + ISO 13485 §7.5.6. New overlay module + 7 templates + clause crosswalks across 3 standards + composites + tests + documentation. Largest single deliverable in the queue. |
| ✓ **P3** | medium | Better non-technical UX (CAPA usability, document routing, role-specific onboarding) | **Closed at v0.57.0** (OQ-121) — 5 new issue forms (training-completion / document-review / access-review / restoration-test / regulatory-review) align 1:1 with v0.55.0 SOPs + 5 new role/process guides (`onboarding.md` + `role-quality-manager.md` + `role-engineer.md` + `document-routing.md` + `capa-lifecycle.md`). `docs/guide/` 12 → 17. |
| **P4** | medium | Opinionated startup-stage presets (pre-seed / seed / Series A / Series B+) | Future release — `presets/` family extending `bundles/`; compounds on P2. 4 preset bundles (YAML + matrix.json each) + maturity-model guide doc + per-stage progression rationale + CI integration. |

### Engine-hardening priorities (reviewer-flagged)

The reviewer identified a cluster of concerns about treating the engine itself as production-grade compliance tooling, not just a scaffold generator. Each of these is a concrete tactical fix.

| Priority | Effort | Gap | Plan |
|---|---|---|---|
| **P5** | medium | `.github/workflows/doc-control.yml` parses YAML frontmatter via `head -20 | grep ^field:` (shell over the first 20 lines); version non-increment emits a warning not a hard failure | Future release — replace with PyYAML schema-validated frontmatter parser; hard-fail version drift on controlled documents; enforce document state-transition rules (`draft → review → approved → effective → superseded`); emit a signed audit artifact per PR (commit SHA + frontmatter delta + signature trailers + CI green status, exported via `openqms signatures export` and persisted to a PR comment or artifact upload). Multi-piece: workflow rewrite + state-machine + signed-artifact emission + tests. |
| ✓ **P6** | light | Dependency pins were floor-versions only (`pyyaml>=6.0`, `pytest>=8.0`); no lockfile with hashed pins | **Closed at v0.55.0** — `engine/uv.lock` (10 packages, hashed) + `uv sync --frozen` in CI; lockfile-presence is a hard CI gate. |
| ✓ **P7** | light | Release tags were not signed | **Closed at v0.55.0** — `docs/guide/release.md` mandates `git tag -s` discipline + adopter-side verification instructions; verification step embedded in P8 workflow. |
| ✓ **P8** | light | CI logs were GitHub-default-retention; no archival pattern for the reproducible-CI-evidence claim | **Closed at v0.55.0** — `.github/workflows/release-artifact.yml` captures trace + coverage + signatures + pytest + lint + module-count + tag-signature per `v*` / `release-*` tag push; attached to GitHub Release; 90-day retention default + adopter-mirroring pattern documented. |
| ✓ **P9** | medium | Template files had no schema validation; only `module.yaml` was linted by `scripts/lint-module-yaml.py` | **Closed at v0.58.0** (OQ-122) — `engine/openqms/template_schema.py` + `scripts/lint-template-frontmatter.py` CI gate parallel to `lint-module-yaml.py`. Required fields: document_id + version + owner + status + 1 of 7 date-field aliases. 8 recognized statuses across document + record lifecycle families. Permissive on extras. 24 templates migrated same release to add frontmatter; 105/105 pass schema. 23 new pytest tests. Companion guide `docs/guide/template-frontmatter.md`. |
| **P10** | medium | No explicit negative-path test suite for bad modules (the validation harness rejects invalid YAML at runtime, but there is no curated set of intentionally-broken modules paired with assertions about the specific error messages produced) | Future release — `engine/tests/test_negative_modules.py` with ~20 broken-by-construction module fixtures (missing required field, clause-id collision, template path doesn't exist, addresses references non-existent clause, malformed YAML, duplicate name, etc.) + assertion that each produces a specific error type + message. Bounded but ~20 curated fixtures is substantial. |

### Adopter-deployment governance priorities (reviewer-flagged)

The reviewer's deepest substantive point: *"the 'immutability' and approval model are not intrinsic properties of the repo. They are deployment controls."* Branch protection, GPG enforcement, role/identity mapping, backup posture — all live in the adopter's GitHub org configuration, not the Open QMS source tree. Open QMS can ship the tools that help adopters verify their own deployment is configured correctly.

| Priority | Effort | Gap | Plan |
|---|---|---|---|
| **P11** | medium | No automated verification that an adopter fork has the required branch-protection + GPG-signing + required-reviewers + required-status-checks configuration | Future release — `scripts/verify-deployment.sh` (or `openqms verify-deployment` subcommand) that queries the GitHub API for branch protection settings, CODEOWNERS coverage, signed-commits requirement, and required-status-checks list, then compares against a `deployment-policy.yaml` declared by the adopter; failures exit nonzero. New subcommand + GitHub API integration + policy-schema design + tests + docs. |
| ✓ **P12** | light | No SOP template for HR-to-GitHub identity mapping (§11.100 unique-attribution depends on it) | **Closed at v0.55.0** — `templates/qms-policy/IDENTITY-MAPPING-SOP-TEMPLATE.md` (9 sections covering register schema + new-hire provisioning + quarterly review + key rotation + offboarding + audit-log retention; bound to §11.100 + HIPAA §164.308(a)(3) + ISO 27001 A.9 + GDPR Art. 32). |
| ✓ **P13** | light | No backup/restore SOP template + restoration-test discipline | **Closed at v0.55.0** — `templates/qms-bcms/BACKUP-RESTORE-SOP-TEMPLATE.md` (8 sections covering 3-2-1 backup posture + cron automation + RTO/RPO/MAO/MBCO declaration framework + 13-step annual restoration-test runbook + format-stability planning + failure-escalation matrix). |
| ✓ **P14** | light | Process gap — no documented cadence for third-party regulatory review of module crosswalk semantics | **Closed at v0.55.0** — `BUSINESS/regulatory_review_cadence.md` (8 sections covering cadence schedule per standard kind + 6-criterion reviewer-qualification + finding-log format with 3-tier severity + per-module attestation badge + honest 0/116 review-debt baseline + 8-module first-tier review-target list). |

### Integration-architecture priorities (reviewer-flagged)

A separate reviewer comment received 2026-05-25: *"Risk management should not be a separate artifact. The future is integrated: requirements ↔ hazards ↔ mitigations ↔ testing ↔ CAPA ↔ complaints ↔ post-market surveillance. That connectedness is where modern systems win."*

The point lands. Open QMS today enforces *clause-level* trace (OQ-001 invariant: every in-scope clause has ≥ 1 bound template; OQ-067 `openqms trace` walks forward + reverse maps; zero-orphan invariant in CI on every push). What's missing is *instance-level* trace across living records — the cross-record graph the reviewer names.

| Priority | Effort | Gap | Plan |
|---|---|---|---|
| **P15** | **hard** | No enforced instance-level trace network across the living-record kinds in the regulatory lifecycle (requirement ↔ hazard ↔ mitigation ↔ test ↔ CAPA ↔ complaint ↔ post-market surveillance finding). Existing precedent is partial: `templates/product-dhf/risk-management/RISK-MANAGEMENT-FILE-TEMPLATE.md` is a single-artifact unified view per ISO 14971; `.github/ISSUE_TEMPLATE/complaint.yml` + `nonconformance.yml` have free-text `capa_link` / "linked CAPA issue" fields with no engine validation. The clause-level trace (OQ-001 + OQ-067) operates one layer up at module YAML, not at instance level. | Future release — (1) define frontmatter schema for trace-link IDs across the ~7 record kinds (e.g., `req_id: REQ-NNN`, `linked_hazards: [HAZ-NNN]`, `linked_tests: [TST-NNN]`, `linked_capas: [CAPA-NNN]`); (2) convert free-text link fields in issue templates to structured IDs; (3) new engine subcommand `openqms trace-instances` walking the cross-record link graph across issues + markdown records; (4) instance-level zero-orphan invariant parallel to the clause-level one (e.g., every hazard has ≥ 1 mitigation; every test cites ≥ 1 requirement; every CAPA cites ≥ 1 trigger); (5) per-template frontmatter migration across ~20-40 record-producing templates; (6) CI gate; (7) documentation. Multi-session; comparable to P2 in scope. **Strategic note:** this is the differentiator the reviewer named ("connectedness is where modern systems win"); the existing OQ-001 + OQ-067 + module composition primitives are the natural substrate to build on. |

### What the reviewer flagged that is already addressed

For transparency:

| Reviewer concern | Status today |
|---|---|
| README scope says v0.38.0 but Actions shows v0.39.0 (documentation/versioning drift) | **Fixed.** v0.51.0 polishing pass synchronized scope-version across `README.md` + `docs/modules-catalog.md` + `BUSINESS/changelog.md` + `BUSINESS/ENGINE_SPEC.md` + `engine/pyproject.toml` + `engine/openqms/__init__.py`. Audit `audit_2026-05-25_v0_50.md` includes A5 (stale counts) as a per-release gate. |
| Immutable audit export | **Shipped at v0.7.0 (OQ-060).** `openqms signatures export --output audit.json` emits a Part 11–style JSON of every commit with parsed signature-meaning trailers + GPG verification status. |
| Schema validation for module YAML | **Shipped at v0.40.0.** `scripts/lint-module-yaml.py` runs as a pre-pytest CI gate; rejects malformed YAML + asserts required clause fields + asserts template `addresses` entries refer to in-module clauses. (Template-side schema validation is the P9 gap above.) |
| Bidirectional traceability invariant | **`:verified`** at OQ-001 via hypothesis property tests in `engine/tests/test_property.py`; enforced repo-wide by the zero-orphan trace invariant in CI on every push. |
| Standards-licensing posture | **Addressed at OQ-070 + OQ-071** with `:argued` status (manual-by-nature licensing claim); README "Standards licensing — important" section discloses what Apache-2.0 does and does not cover. |

### Open-but-permanent: coverage is not compliance

The reviewer's foundational point — *"the tool can prove 'each declared clause has at least one declared document,' but it cannot prove 'this SOP actually satisfies ISO 13485, Part 11, EU MDR, IEC 62304, AS9100D, IATF 16949, or cGMP in a certifiable way'"* — is permanent and architectural, not a gap to close. This is the OQ-080 firewall. Open QMS produces traceable scaffolds; semantic adequacy of any specific SOP against any specific clause requires QA judgment and (where the regulator requires) third-party assessment. The forward work above (P11 + P14 in particular) is about making the *substrate* harder to lose / fake / drift — not about claiming Open QMS will replace regulatory expertise.

---

## Cross-references

- [`README.md`](../README.md) — adopter quick-start + scope summary
- [`docs/modules-catalog.md`](modules-catalog.md) — full module inventory
- [`docs/guide/`](guide/) — 12 adopter guides covering quickstart + configuration + doc control + GPG signing + signature meaning + training + supplier controls + complaints + management review + traceability + release + auditor walkthrough
- [`BUSINESS/ENGINE_SPEC.md`](../BUSINESS/ENGINE_SPEC.md) — 102 formal spec entries with status, evidence type, depends-on
- [`BUSINESS/artifact_registry.md`](../BUSINESS/artifact_registry.md) — per-entry evidence file mapping
- [`BUSINESS/dashboard.md`](../BUSINESS/dashboard.md) — current status + priority stack
- [`BUSINESS/changelog.md`](../BUSINESS/changelog.md) — per-release record
- [`BUSINESS/audit_2026-05-25_v0_50.md`](../BUSINESS/audit_2026-05-25_v0_50.md) — most recent A0–A6 cross-audit
