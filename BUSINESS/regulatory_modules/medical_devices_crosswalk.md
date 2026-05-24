# Medical Devices Regulatory Module — Crosswalk

**Version:** v0.1.0 DRAFT
**Date:** 2026-05-22
**Spec entries:** OQ-040 (module) · OQ-041 (ISO 13485) · OQ-042 (21 CFR 820) · OQ-043 (21 CFR Part 11) · OQ-044 (EU MDR) · OQ-045 (IEC 62304) · OQ-046 (IEC 62366-1 + IEC 60601-1) · OQ-047 (ISTA + MDSAP) · OQ-048 (ISO 27001 overlay)

Detailed clause-by-clause crosswalk for the medical-devices regulatory module. Source material preserved from the v2.0 DRAFT spec (2026-05-22). When the generator engine (P1 in dashboard) is built, this crosswalk is the source of truth that the machine-readable `modules/medical-devices/clauses.yaml` is derived from.

**Standards licensing note (OQ-070).** This crosswalk references standards by clause number and normative summary only. It does **not** redistribute standard text. Adopters must obtain their own licensed copies of ISO 13485, IEC 62304, IEC 62366-1, IEC 60601-1, ISTA 2A/3A, MDSAP audit model documents, and ISO 27001 from their respective publishers.

---

## §4.2 — ISO 13485:2016 (Quality Management Systems for Medical Devices)

| Clause | Requirement | GitHub Mechanism | Gap / Risk |
|---|---|---|---|
| 4.1.6 | Software used in the QMS shall be validated. Validation shall be performed prior to initial use and after changes. | GitHub itself must be validated for intended use. Validation protocol required covering repository integrity, access controls, merge protections, and audit trail reliability. | GitHub is a SaaS platform — validation must address the supplier's infrastructure (SOC 2 reports, uptime SLAs) plus your configured use. Revalidation triggers on GitHub platform updates are hard to control. |
| 4.2.3 | Medical device file — a compilation of documents for each medical device type/family. | Dedicated repository or directory structure per device type. Tags/releases used to snapshot the file at key milestones. | Auditors expect a navigable, consolidated view. A repo directory listing is not self-evidently a "medical device file" without a manifest or index document. |
| 4.2.4 | Document control — approval prior to issue, review/update with re-approval, identification of changes and current revision status, availability at points of use, legibility, prevention of unintended use of obsolete documents. | Branch protection rules enforce approval via PR review. Commit diffs show changes. `main` branch = current effective version. Tags mark revisions. Obsolete docs archived via Git history. | "Approval" in Git is a merge approval, not a formal signature with role identification. Need to map PR approvers to QMS roles (e.g. QA approval vs. engineering approval). Effective date ≠ merge date without explicit metadata. "Available at point of use" requires that production/manufacturing personnel can access controlled documents without Git literacy. |
| 4.2.5 | Control of records — records shall remain legible, readily identifiable, and retrievable. Storage, protection, retrieval, retention period, and disposition shall be defined. | Git history is immutable (with caveats). GitHub retention policies, backup strategy, and export procedures must be documented. | Git allows force-push and history rewrite if not properly locked down. Retention period enforcement is not native — need policy + periodic verification. Binary files (PDFs, scans) bloat repos and degrade performance. |
| 7.3 | Design and development — planning, inputs, outputs, review, verification, validation, transfer, changes. Traceability between inputs, outputs, verification, and validation at every stage. | Issues = design inputs. PRs = design reviews. Linked issues/PRs = traceability matrix. CI checks = automated verification where applicable. Tags/releases = design transfer milestones. | Traceability depends entirely on disciplined linking. GitHub has no native "traceability matrix" view — would need a CI job or external tool to generate/enforce it. Design review records need formal minutes/sign-off beyond a PR comment thread. |
| 6.3 | Infrastructure — including information systems. | GitHub infrastructure (cloud) managed by Microsoft/GitHub. On-prem option via GitHub Enterprise Server. | Must document infrastructure qualification. Cloud dependency means you don't control availability. |
| 8.2.3 | Monitoring and measurement of processes. | GitHub Actions can generate metrics (PR cycle time, review coverage, open nonconformances). | Requires custom implementation. Not out-of-the-box. |

## §4.3 — 21 CFR Part 820 (FDA Quality System Regulation)

| Section | Requirement | GitHub Mechanism | Gap / Risk |
|---|---|---|---|
| 820.20 | Management responsibility — management representative, quality policy, quality planning. | Repo-level README with quality policy. CODEOWNERS file maps responsibility. | Policy documents need controlled distribution evidence. CODEOWNERS is a technical file, not a quality record. |
| 820.22 | Quality audit — procedures for planned quality audits. | Audit checklists and findings stored as issues or in dedicated audit directory. | Internal audit records must be access-restricted. GitHub repo-level permissions are coarse (read/write/admin), not document-level. |
| 820.30 | Design controls — plans, inputs, outputs, reviews, verification, validation, transfer, changes. | Same as ISO 13485 §7.3 mapping above. | Same gaps. FDA expects objective evidence of formal design reviews — PR approval alone may not suffice without supplementary meeting minutes / sign-off records. |
| 820.40 | Document controls — approval and distribution, changes. | Branch protection + PR merge = approval. `main` = distributed/effective. Change history in Git log. | Same as ISO 13485 §4.2.4. FDA specifically looks for "designated individual(s)" approving — need to demonstrate that PR approvers have the authority and competence. |
| 820.70 | Production and process controls — including environmental and contamination controls. | Production SOPs stored in repo. | Work instructions at point of use (manufacturing floor) need a rendering/distribution layer. Operators won't use GitHub. |
| 820.90 | Nonconforming product — procedures for control. | Issues with labels (NCR, CAPA, deviation). Templates enforce required fields. | Disposition decisions and rework/concession approvals need e-signature-grade sign-off, not just a GitHub comment. |
| 820.100 | Corrective and preventive action — CAPA. | Issues with CAPA template, labels, milestone tracking. | Effectiveness checks and formal closure approvals need structured workflow enforcement. |
| 820.180–820.198 | Records — DHR, DMR, QSR, complaint files. Retention, confidentiality, backup. | Repos organized by record type. Access controls via teams. Backup via GitHub's infrastructure + independent backup job. | Record retention enforcement is manual. Complaint files may contain PHI/PII requiring additional controls beyond standard GitHub access. |

## §4.4 — 21 CFR Part 11 (Electronic Records; Electronic Signatures)

This regulation is the single largest constraint on using GitHub as a QMS. The §11.50 gap (signature meaning) is tracked formally as ENGINE_SPEC OQ-060.

| Requirement | GitHub Mechanism | Gap / Risk |
|---|---|---|
| 11.10(a) Validation of systems. | Must validate GitHub for intended use. | Validation must cover your specific configuration. |
| 11.10(b) Generate accurate copies of records. | `git clone`, `git archive`, GitHub export tools. | Binary file handling and LFS complicate complete record reproduction. |
| 11.10(c) Protection of records — access limited to authorized individuals. | GitHub Teams, branch protection, repository permissions. | No document-level access control. |
| 11.10(d) Audit trail — computer-generated, timestamped, independent of operators. | Git log + GitHub audit log (Enterprise). | Git timestamps client-side and spoofable unless enforced server-side. Free/Team audit logs limited. |
| 11.10(e) Operational system checks — enforce sequencing. | GitHub Actions, required status checks, branch protection. | Custom implementation required. |
| **11.50 Signature manifestations** — signed records shall display name, date/time, and **meaning** of signature. | **Not natively supported.** Git commits have author + timestamp but not meaning. | **Critical gap (OQ-060).** PR approvals show who approved and when, not the regulatory meaning. Needs structured commit metadata + CI verification, or external e-signature integration. |
| 11.70 Signature/record linking — signatures bound to records. | GPG/SSH commit signatures bind author identity to content. | Addresses this well if enforced org-wide. |
| 11.100 General e-signature requirements — unique, verified identity. | GitHub accounts individual. SSO/MFA at org level. | GitHub account ≠ verified identity without documented proofing. |
| 11.200 Two-factor identification. | GitHub SSO + MFA. | Document MFA enforcement and non-bypassability. |
| 11.300 Password controls. | GitHub/SSO password policies. | Reference IdP password policy in validation. |

## §4.5 — EU MDR 2017/745

| Article / Annex | Requirement | GitHub Mechanism | Gap / Risk |
|---|---|---|---|
| Article 10(9) | QMS shall address all parts of Annex IX and cover risk management, clinical evaluation, PMS, vigilance. | Repository structure covers these domains. | Comprehensive coverage depends on organizational discipline, not platform capability. |
| Annex I | General Safety and Performance Requirements (GSPRs) — must be documented and traceable. | GSPR checklist stored as a controlled document. Links to supporting evidence via issue/PR references. | Traceability to evidence is manual unless CI-enforced. |
| Annex II | Technical documentation — device description, design and manufacturing information, GSPR compliance, benefit-risk, product verification/validation. | Dedicated repo or directory for technical documentation per device. Releases snapshot the tech file at submission milestones. | Notified bodies expect a structured, navigable technical file — not a raw Git directory. Need a rendering/export layer to produce reviewer-friendly output. |
| Annex IX | Conformity assessment based on QMS and technical documentation assessment. | QMS procedures in controlled repos. Audit evidence of QMS operation via Git history and issue/PR records. | Notified body auditors will need training or a guided interface to review GitHub-based evidence. |
| Annex XIV | Clinical evaluation, PMS, PMCF. | Clinical evaluation reports, literature searches, PMCF plans stored as controlled documents. | Clinical documents often involve large PDFs, literature databases, and collaborative review workflows that strain Git-based approaches. |

## §4.6 — IEC 62304 (Medical Device Software Lifecycle Processes)

| Clause | Requirement | GitHub Mechanism | Gap / Risk |
|---|---|---|---|
| 5.1 | Software development planning. | Development plan as a controlled document. GitHub Projects for task management. Milestones for phase gates. | GitHub Projects is project management, not a validated planning tool. Needs validation if used as objective evidence. |
| 5.2–5.4 | Requirements analysis, architectural design, detailed design. | Requirements as issues or markdown documents. Architecture docs in repo. Design docs reviewed via PRs. | Traceability requirements → architecture → detailed design → implementation → test must be enforceable. |
| 5.5 | Unit implementation and verification. | Source code in repo. Unit tests in CI. Code review via PR. | **GitHub's strongest area.** Native Git/CI workflow. Gap is documenting verification against specific requirements (linking test results to requirement IDs). |
| 5.6–5.7 | Integration and integration testing. System testing. | CI/CD pipelines. Test results stored as artifacts. | Test result artifacts must be retained as quality records with traceability to software versions (Git tags). |
| 5.8 | Software release. | Git tags and GitHub Releases. Release notes as controlled documents. | Release process must enforce that all required activities are complete before release. GitHub Actions can gate this (`release-gate.yml` does this today). |
| 6 | Software maintenance. | Issue tracking for bugs/enhancements. PRs for changes. SOUP management via dependency tracking. | SOUP (software of unknown provenance) tracking requires a maintained register. Dependabot helps but is not a validated SOUP register. |
| 7 | Risk management of software. | Risk analysis documents in repo. Software hazard analysis linked to requirements and mitigations. | Risk management traceability (hazard → cause → mitigation → verification) requires disciplined cross-referencing. |
| 8 | Software configuration management. | Git is configuration management. Branch strategy, tagging, and release management are native. | **GitHub's strongest area.** Git was literally designed for this. Ensure the branching strategy is documented and enforced. |
| 9 | Software problem resolution. | Issues and PRs with bug/problem labels. Templates for problem reports. | Problem resolution records must link to impact assessment, risk analysis, and verification of fix. |

## §4.7 — IEC 62366-1 (Usability Engineering for Medical Devices)

| Clause | Requirement | GitHub Mechanism | Gap / Risk |
|---|---|---|---|
| 5.1–5.9 | Use specification, user interface specification, formative evaluation, summative evaluation, usability engineering file. | Usability engineering file as a directory in the DHF repo. Use specifications and evaluation reports as controlled documents. | Usability testing records often include images, videos, and observational data that are impractical to store in Git. Need LFS or external storage with references. |

## §4.8 — IEC 60601-1 (and Collaterals) (Medical Electrical Equipment Safety)

| Relevance | GitHub Mechanism | Gap / Risk |
|---|---|---|
| Test reports, risk management files, essential performance documentation. | Controlled documents in repo. Test reports linked to product configurations via tags. | Large test reports (EMC, electrical safety) are typically PDFs from external labs. Storage and retrieval of large binaries in Git is suboptimal. |

## §4.9 — ISTA Standards (Packaging and Distribution Testing)

| Standard | Requirement | GitHub Mechanism | Gap / Risk |
|---|---|---|---|
| ISTA 2A / 3A | Packaging validation — test protocols, results, shipping configuration documentation. | Packaging validation protocols and reports stored as controlled documents. Linked to specific product/packaging configurations via tags or directory structure. | Packaging validation is typically a one-time or periodic activity with large PDF reports and photographic evidence. Git handles the document control aspect fine but binary file management is a recurring concern. |
| ISTA 3B / 6-FEDEX / 6-AMAZON | Channel-specific testing for retail or e-commerce distribution. | Same as above — controlled documents per channel/configuration. | Same binary file concern. |

## §4.10 — MDSAP (Medical Device Single Audit Program)

| Element | Requirement | GitHub Mechanism | Gap / Risk |
|---|---|---|---|
| Single audit covering multiple regulators (US, Canada, Brazil, Japan, Australia) against a unified ISO 13485-based program. | Module composition: MDSAP activates ISO 13485 clause coverage plus jurisdiction-specific additions for each participating regulator. Audit evidence assembled from the same artifact set rather than duplicated. | The generator can produce a unified evidence base; the audit-readiness layer (assembling the audit dossier in MDSAP-auditor-expected format) is custom tooling on top of the generator. |

## §4.11 — ISO/IEC 27001 (Information Security — Cross-Cutting Overlay)

| Clause | Requirement | GitHub Mechanism | Gap / Risk |
|---|---|---|---|
| Annex A controls relevant to medical-device organizations handling PHI, design files, source code, manufacturing data. | Overlay module: ISO 27001 clauses compose with the vertical (medical-devices) module rather than replacing it. Access controls, audit logging, incident management map onto GitHub Enterprise capabilities + supplementary tooling. | Overlap with Slop Audit's infosec dimensions is meaningful and is a candidate dock point with the Open Honest standards portfolio. Documenting the overlap is a v0.2+ spec target. |

---

## Cross-cutting constraints (medical devices module)

These constraints recur across multiple clauses above and warrant standalone tracking.

**Training control** — ISO 13485 §6.2, 21 CFR 820.25, EU MDR Annex IX §2.2 require personnel be trained on applicable procedures and that training records be maintained. GitHub gap: when a document is revised, training assignment / completion / linkage is not native. Open QMS's `training-trigger.yml` is a partial address (ENGINE_SPEC OQ-035); robustness gap tracked at OQ-061.

**Supplier controls** — ISO 13485 §7.4, 21 CFR 820.50, EU MDR Article 10(9)(c) require documented supplier evaluation/selection/monitoring/re-evaluation. Tracked at OQ-063.

**CAPA and nonconformance** — ISO 13485 §8.5, 21 CFR 820.90 / 820.198. Issue templates capture; effectiveness check and formal closure workflow gap tracked at OQ-033 notes.

**Management review** — ISO 13485 §5.6, 21 CFR 820.20. Aggregation tooling gap tracked at OQ-064.

---

## Engine-readable format (forward)

When the generator engine (dashboard P1) lands, this crosswalk becomes the source for:

- `modules/medical-devices/clauses.yaml` — clause identifiers, normative summaries (no standard text), gap annotations.
- `modules/medical-devices/templates/` — artifact templates with frontmatter declaring the clause(s) each template addresses.
- `modules/medical-devices/manifest.yaml` — the clause-to-template binding manifest, asserting that every clause in `clauses.yaml` is bound to ≥1 template and every template in `templates/` declares ≥1 clause from `clauses.yaml`.

The per-module validation harness (OQ-013) is the mechanical check on those three files; passing it upgrades OQ-040..OQ-048 from `:argued` to `:tested`.
