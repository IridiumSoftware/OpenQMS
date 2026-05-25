---
document_id: SOP-BCM-002
version: 0.1.0
effective_date: YYYY-MM-DD
owner: ROLE (e.g., IT/Security Lead or Quality Manager)
status: draft
addresses:
  - ISO-22301-Article-8-2-operations
  - HIPAA-164-308-a-7-contingency-plan
  - 21-CFR-Part-11-10-backup-retrieval
  - Annex-11-Article-7-1-data-integrity
---

# SOP — Open QMS Backup, Restore, and Restoration Testing

**Purpose.** Establish a verifiable backup + restore posture for the Open QMS repository so that GMP/GxP records (commit history, signed audit trails, module + template + bundle definitions) are recoverable in the event of system failure, accidental loss, ransomware, GitHub outage, or org-account compromise. Mandates an annual restoration-test cadence.

**Scope.** The `<ORG>/<REPO>` Open QMS deployment + any forks containing controlled records.

**Why this SOP is load-bearing.** Open QMS's audit-trail claim (§4 of `docs/compliance-architecture.md`) depends on git history being recoverable. Git is inherently distributed (every clone is a backup), but adopters must have an explicit backup destination + cadence + restoration-test record to defend the "recoverable" claim at audit — clone-count is not the same as tested-restoration.

---

## 1. Roles + responsibilities

| Role | Responsibility |
|---|---|
| **IT/Security Lead** | Owner of this SOP; operates backup automation; coordinates restoration tests |
| **Quality Manager** | Reviews + signs annual restoration-test record; reviews this SOP annually |
| **Backup operator** (may be same as IT/Security Lead) | Executes daily/weekly backup runs; monitors backup success; escalates failures |
| **Internal Auditor** | Reviews backup records + restoration-test record as part of annual internal audit |

---

## 2. Backup destinations + cadence

### Minimum-viable backup posture (3-2-1 rule)

- **3** copies of the data
- **2** different storage media
- **1** copy off-site / off-cloud-provider

Concrete instantiation for Open QMS:

| Copy | Storage | Cadence | Mechanism |
|---|---|---|---|
| **Primary** | GitHub-hosted upstream | Real-time | git push (every adopter commit) |
| **Mirror 1** | Org-controlled secondary git server (GitLab self-hosted, Gitea, Bitbucket Server, or second GitHub org) | Daily | `git clone --mirror` cron job |
| **Mirror 2** | Cold storage (encrypted S3 / GCS / Azure Blob / on-premise tape) | Weekly | `git bundle create` + encrypted upload |
| **Mirror 3** (off-site / off-cloud) | Geographically separate region OR different cloud provider OR removable encrypted media | Monthly | Same as Mirror 2, different destination |

### Backup automation

```bash
# Daily mirror-clone (Mirror 1) — example cron
# 0 2 * * * /usr/local/bin/openqms-backup-mirror.sh
#
# openqms-backup-mirror.sh:
#   set -euo pipefail
#   DEST=/var/backups/openqms-mirror
#   git -C "$DEST" remote update --prune || \
#     git clone --mirror git@github.com:<ORG>/<REPO>.git "$DEST"

# Weekly cold-storage bundle (Mirror 2) — example
# 0 3 * * 0 /usr/local/bin/openqms-backup-bundle.sh
#
# openqms-backup-bundle.sh:
#   set -euo pipefail
#   DATE=$(date -u +%Y%m%dT%H%M%SZ)
#   BUNDLE=/tmp/openqms-${DATE}.bundle
#   git -C /var/backups/openqms-mirror bundle create "$BUNDLE" --all
#   gpg --encrypt --recipient backup-key "$BUNDLE"
#   aws s3 cp "${BUNDLE}.gpg" s3://<ORG>-openqms-backup/cold/${DATE}.bundle.gpg
#   rm "$BUNDLE" "${BUNDLE}.gpg"
```

Adopter must:
- Use a dedicated backup service account (not a personal user account).
- Rotate backup service account credentials per org policy (typically 90 days).
- Encrypt cold-storage bundles at rest using a recipient key controlled by the backup operator, not the engineering team (separation of duties).

---

## 3. RTO / RPO / MAO declaration

Per ISO 22301:2019 §8.2.2 Business Impact Analysis. Adopter MUST fill in actual values; defaults below are illustrative.

| Metric | Definition | Suggested target | Adopter actual |
|---|---|---|---|
| **RPO** (Recovery Point Objective) | Max acceptable data loss in time terms (= longest acceptable gap between backups) | ≤ 24 hours (daily mirror cadence) | _________________ |
| **RTO** (Recovery Time Objective) | Max acceptable time to restore service after declared incident | ≤ 4 hours (mirror restore + DNS swap + access provisioning) | _________________ |
| **MAO** (Maximum Acceptable Outage) | Outer bound; outage beyond this point triggers business-continuity escalation | ≤ 48 hours | _________________ |
| **MBCO** (Minimum Business Continuity Objective) | Minimum service level acceptable during disruption | Read-only access to most recent mirror | _________________ |

Adopter declarations should reflect the most stringent applicable regulator (e.g., DORA Article 11 requires defined ICT business continuity policy; HIPAA Security Rule §164.308(a)(7) requires contingency plan with explicit RTO; NERC CIP-009 requires recovery plan for BES Cyber Systems).

---

## 4. Restoration-test cadence (annual minimum)

**Annual cadence is the regulatory minimum.** Adopters under DORA-equivalent regimes typically test quarterly. Test calendar reminder owner: IT/Security Lead.

### Restoration-test runbook

The annual test simulates total loss of the primary GitHub repository + restoration from Mirror 1 (or Mirror 2 if Mirror 1 also lost).

| Step | Action | Pass criteria |
|---|---|---|
| 1 | Declare test in progress; notify Quality Manager + Internal Auditor; designate test repository name (`<ORG>/<REPO>-restoration-test-<DATE>`) | Notification sent + acknowledged |
| 2 | Pull most recent Mirror 1 to a fresh workstation OR pull most recent Mirror 2 bundle to a fresh workstation | Mirror pull completes without error |
| 3 | `git fsck --full --strict` on the restored copy | Zero corruption errors |
| 4 | `git log --oneline | wc -l` matches expected commit count (within ±RPO window) | Count matches within tolerance |
| 5 | Verify HEAD commit is signed: `git log --show-signature -1` | Signature verifies (or expected-unsigned for the bundle commit itself) |
| 6 | Push restored copy to test-repository GitHub URL | Push completes |
| 7 | Clone test repository to second workstation; run engine validation: `cd engine && uv sync --frozen && uv pip install -e '.[dev]'; pytest tests -q` | 100% pytest pass (current target: 129/129) |
| 8 | Run repo-wide invariants: `openqms trace --all`; `openqms coverage --all --threshold 100`; `openqms signatures export` | All invariants hold |
| 9 | Verify bundle baseline regression on the restored copy: `openqms regenerate --bundle example-samd` (and one other) | Zero diff |
| 10 | Measure actual elapsed time from step 1 to step 9 | Within declared RTO |
| 11 | Document findings in `BUSINESS/restoration_test_YYYY-MM-DD.md` with: test date, restoration source, elapsed time, deviations from runbook, pass/fail per criterion, recommendations | Document committed + GPG-signed |
| 12 | Quality Manager signs the restoration-test record (`Signature-Meaning: Reviewed`) | Signature on file |
| 13 | Delete test repository to avoid drift; archive restoration-test record in BUSINESS/ | Test repo deleted; record retained |

**Test-fail handling:** if any step fails, raise an incident per `docs/guide/complaints.md` or adopter's incident-response SOP; treat as CAPA; do not close until root cause identified + corrective action verified.

---

## 5. Archive integrity + format-stability planning

Long-retention regulated records (ATMP 30 years EU; HIPAA 6 years; ISO 13485 lifetime + N) require periodic verification that archived data still parses + renders. Format-stability is the often-overlooked failure mode: in 30 years, today's Markdown / YAML / JSON formats may be readable but rendering tools may have evolved.

### Format-stability checklist

- **Annually:** verify Mirror 2 bundles unpack cleanly; pick 3 random bundles from prior years, restore to scratch workstation, run engine validation. Document in same restoration-test record.
- **On major dependency upgrade** (Python, pyyaml, uv, GitHub Actions): test that historical bundles still validate against the new toolchain.
- **Every 5 years:** sample render each kind of artifact (module.yaml, template.md, bundles/*.matrix.json) using a contemporary toolchain to confirm continued readability. Capture screenshots / outputs in archive metadata.
- **For ATMP / 30-year retention:** consider migration to an archival format every 10 years (e.g., printed + PDF/A snapshots of critical records — this is an open question across regulated industries; document the adopter's chosen approach).

---

## 6. Backup-failure escalation

| Trigger | Escalation |
|---|---|
| Daily mirror job fails ≥ 2 consecutive days | Backup operator → IT/Security Lead within 4 hours |
| Weekly bundle upload fails ≥ 1 week | IT/Security Lead → Quality Manager within 1 business day |
| Monthly off-site copy fails | Quality Manager + IT/Security Lead joint review within 1 week |
| Mirror corruption detected during restoration test | CAPA-equivalent process; backup posture re-evaluated end-to-end |

---

## 7. Linkage to other Open QMS controls

| This SOP supports | How |
|---|---|
| §4 audit trails (`docs/compliance-architecture.md`) | Backup makes the immutable git history actually recoverable |
| §8 backup/recovery (`docs/compliance-architecture.md`) | Concretizes the adopter responsibility surface |
| §9 record retention | Provides the format-stability verification discipline |
| `modules/iso-22301/` BCMS overlay | This SOP is one operational artifact of the BCMS substrate |
| `modules/hipaa/` Security Rule §164.308(a)(7) contingency plan | Per-record-type backup discipline maps here |
| `modules/atmp/` 30-year EU retention | Format-stability checklist (§5) operationalizes this |

---

## 8. Document control

| Field | Value |
|---|---|
| Document ID | SOP-BCM-002 |
| Version | (per frontmatter) |
| Effective date | (per frontmatter) |
| Next review | (effective date + 12 months) |
| Owner | (per frontmatter) |
| Approver | Quality Manager |
| Distribution | IT/Security team + Quality team + adopter's Business Continuity Manager (if separate) |
| Supersedes | (prior version ID + date if applicable) |
