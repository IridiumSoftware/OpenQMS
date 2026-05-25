---
document_id: SOP-IDM-001
version: 0.1.0
effective_date: YYYY-MM-DD
owner: ROLE (e.g., Quality Manager)
status: draft
addresses:
  - 21-CFR-Part-11-100-unique-attribution
  - HIPAA-164-308-a-3-workforce-security
  - ISO-27001-A-9-access-control
  - GDPR-Article-32-security-of-processing
---

# SOP — HR-to-GitHub Identity Mapping

**Purpose.** Establish the controlled correspondence between (a) the legally accountable individual on HR file and (b) their GitHub identity (account + GPG key fingerprint) so that GPG-signed commits in this repository can be attributed to a specific person for regulatory recordkeeping (21 CFR §11.100 unique-attribution; HIPAA Security Rule §164.308(a)(3) workforce security; ISO 27001 Annex A.9 access control; GDPR Article 32 security of processing).

**Scope.** All individuals authorized to commit or approve changes in `<ORG>/<REPO>`. Includes employees, contractors, and any third party with `triage`/`write`/`maintain`/`admin` role on the repo or any team granted access via CODEOWNERS.

**Why this SOP is load-bearing.** Open QMS's audit-trail and e-signature claims (OQ-022 + OQ-023 + OQ-060) depend on the GitHub account corresponding to a real, legally accountable person — not the other way around. GitHub's "Verified" badge certifies *key → account*; it does NOT certify *account → person*. This SOP closes that gap with an HR-attested mapping.

---

## 1. Roles + responsibilities

| Role | Responsibility |
|---|---|
| **HR / People Ops** | Maintains canonical employee/contractor list; attests identity at account provisioning; triggers offboarding workflow |
| **Quality Manager** | Owner of this SOP; reviews mapping accuracy quarterly; signs off on access changes for regulated-process commits |
| **IT / Security** | Operates the GitHub org admin role; provisions accounts; enforces 2FA + branch protection + signed-commits requirement |
| **Individual user** | Provides GPG public key fingerprint at provisioning; updates fingerprint on key rotation; reports compromised key within 24 hours |
| **Internal Auditor** | Reviews the identity-mapping register annually as part of the internal audit programme; samples N commits and verifies attribution chain |

---

## 2. Identity-mapping register

Maintained at `<ORG-RESTRICTED-LOCATION>` (private repo, encrypted store, or commercial HRIS export — NOT the public Open QMS repo). Each row:

| Field | Type | Required | Notes |
|---|---|---|---|
| `legal_name` | string | yes | As on HR record |
| `employee_id` | string | yes | HRIS identifier |
| `email_corporate` | string | yes | Used for git commit `Author:` field |
| `github_username` | string | yes | Lowercase exact match |
| `gpg_key_fingerprint` | hex | yes | 40-char SHA-1 fingerprint; updated on rotation |
| `role` | enum | yes | Engineer / Quality Manager / Auditor / Admin / Contractor / Other |
| `provisioned_date` | date | yes | First day authorized to commit |
| `provisioned_by` | name + role | yes | Who in IT/Security did the provisioning |
| `hr_attestation_date` | date | yes | HR-attested identity verification date |
| `last_review_date` | date | yes | Most recent quarterly review |
| `revoked_date` | date | conditional | Required when status = revoked |
| `revoked_by` | name + role | conditional | Required when status = revoked |
| `status` | enum | yes | active / suspended / revoked |
| `notes` | text | no | Any caveats (contractor-end-date, conditional access, etc.) |

---

## 3. New-hire provisioning workflow

1. **HR notifies IT/Security** of new hire + start date + assigned role.
2. **IT/Security provisions GitHub org membership** at the appropriate role (`read` baseline; `triage`/`write`/`maintain`/`admin` per role assignment).
3. **New hire creates personal GPG key** per `docs/guide/gpg-signing.md`; uploads public key to GitHub via Settings → SSH and GPG keys.
4. **New hire submits GPG fingerprint** to IT/Security via a designated intake form or ticket. Fingerprint format: `gpg --fingerprint <KEY-ID>` output verbatim (40-char hex with spaces).
5. **HR attests identity** — by signed memo, HRIS export, or notarized statement — that the GitHub username + GPG fingerprint correspond to the named individual on HR file. Attestation captured + stored.
6. **IT/Security adds row** to identity-mapping register with `status: active` + `hr_attestation_date` + `provisioned_date`.
7. **IT/Security enforces 2FA** at org level + branch protection rule "Require signed commits" + "Require linear history" + "Restrict who can push to matching branches" (typically `admin` role only — adopter org policy).
8. **Quality Manager reviews + signs** the new-hire row (signature meaning: `Reviewed`) and adds the user to the appropriate CODEOWNERS team(s).

---

## 4. Quarterly access review cadence

- **Cadence:** every 90 days.
- **Trigger:** calendar-driven, no event-based skip.
- **Reviewer:** Quality Manager + IT/Security.
- **Scope:** every row in the identity-mapping register with `status: active`.
- **Per-row checks:**
  1. Individual is still employed/contracted per HR (cross-check against current HR list).
  2. GitHub role assignment matches current job function.
  3. GPG fingerprint on file matches `gpg --fingerprint <KEY-ID>` output (key has not been rotated without notification).
  4. Recent commits attributed to this user verify cleanly (`git log --show-signature` sample of N commits).
  5. CODEOWNERS team memberships are appropriate.
- **Output:** signed review record (GitHub Issue with `Signature-Meaning: Reviewed` commit trailer on closure); deviations recorded as findings + tracked to closure.
- **Last-review-date updated** on every reviewed row.

---

## 5. Key rotation handling

- **User responsibility:** notify IT/Security ≥ 5 business days before key rotation (planned) or within 24 hours (compromised key — emergency rotation).
- **For planned rotation:**
  1. User generates new GPG key per `docs/guide/gpg-signing.md`.
  2. User uploads new public key to GitHub.
  3. User submits new fingerprint to IT/Security per §3.4.
  4. IT/Security updates the register row's `gpg_key_fingerprint` field + appends a rotation entry to the row's `notes` field with old + new fingerprint + rotation date.
  5. Old key retained for verification of historical commits (do not delete).
- **For emergency rotation (compromised key):**
  1. User notifies IT/Security + Quality Manager immediately.
  2. IT/Security marks compromised key as such on GitHub (Settings → SSH and GPG keys → Delete only after archival).
  3. IT/Security flags affected commit range in register notes for incident-investigation review.
  4. New key issued per §3.3-3.6 (same workflow as new-hire, abbreviated).
  5. Incident captured in CAPA-equivalent workflow per `docs/guide/complaints.md` or adopter's incident-response SOP.

---

## 6. Offboarding workflow

1. **HR notifies IT/Security** of separation + effective date.
2. **Pre-separation:**
   - User commits any in-flight changes + signs off any outstanding PR reviews.
   - User's CODEOWNERS team memberships are reviewed; succession assigned.
3. **At separation (or as soon as practical):**
   - IT/Security revokes GitHub org membership.
   - IT/Security removes user from all CODEOWNERS teams.
   - IT/Security updates register row to `status: revoked` + `revoked_date` + `revoked_by`.
   - User's GPG key remains on GitHub (do not delete) for historical commit verification — record in register notes that key is retained for verification only, not for new attribution.
4. **Quality Manager signs** the offboarding row (signature meaning: `Reviewed`).
5. **Internal Auditor confirms** at next quarterly review that no commits have been attributed to the offboarded user after `revoked_date`.

---

## 7. Audit-log retention

- **GitHub org audit log** retained per the adopter's records retention schedule (minimum: as required by the most-stringent applicable regulation; ATMP 30 years, HIPAA 6 years, ISO 13485 lifetime + N, etc. — see `docs/compliance-architecture.md` §9).
- **Identity-mapping register** retained for the same period.
- **HR attestation records** retained per HR records retention policy + the longer of the regulatory retention requirement.
- **Periodic export** of the GitHub audit log to org-controlled long-term storage (recommended: monthly, automated).

---

## 8. Linkage to other Open QMS controls

| This SOP supports | How |
|---|---|
| OQ-022 force-push-disabled immutability | Identity-mapping makes the commit author attribution legally enforceable |
| OQ-023 GPG-signed commits | Identity-mapping provides the HR-to-key binding GitHub does not |
| OQ-060 §11.50 signature meaning | Identity-mapping provides the §11.100 unique-attribution layer underneath §11.50 meaning |
| OQ-020 PR + required reviewers role-based approval | CODEOWNERS team membership + role assignment driven by identity-mapping |
| OQ-119 compliance architecture trust-gate | Concretizes §1 (Part 11), §5 (e-signatures), §6 (permissions), §11 (system administration controls) |

---

## 9. Document control

| Field | Value |
|---|---|
| Document ID | SOP-IDM-001 |
| Version | (per frontmatter) |
| Effective date | (per frontmatter) |
| Next review | (effective date + 12 months) |
| Owner | (per frontmatter) |
| Approver | Quality Manager |
| Distribution | All authorized GitHub users + HR + IT/Security |
| Supersedes | (prior version ID + date if applicable) |
