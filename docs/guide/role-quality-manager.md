# Role guide — Quality Manager

**Audience:** Quality Manager / Quality Lead / Head of Quality / RA-QA owner of an Open QMS deployment. This guide assumes you have completed [`docs/guide/onboarding.md`](onboarding.md) and have admin or maintain role on the repo.

**What this guide covers:** the day-to-day, week-to-week, month-to-month, and annual workflows that the Quality Manager owns in an Open QMS deployment.

---

## Your responsibilities at a glance

| Cadence | Activity | Driven by |
|---|---|---|
| **Daily** | Triage new CAPAs / NCRs / Complaints (label, assign, prioritize) | Issue inbox |
| **Daily** | Sign off on PRs touching controlled documents (`Signature-Meaning: Approved`) | PR review queue |
| **Weekly** | Review open CAPA backlog; verify aging cases have status updates | [`docs/guide/capa-lifecycle.md`](capa-lifecycle.md) |
| **Monthly** | Review training-completion backlog; chase outstanding completions | Training Completion issues |
| **Quarterly** | Co-lead Access Review with IT/Security | [Access Review issue form](../../.github/ISSUE_TEMPLATE/access-review.yml) |
| **Quarterly** | Internal audit cycle (rotating module scope) | Your internal audit programme |
| **Annual** | Management Review meeting + record | [Management Review issue form](../../.github/ISSUE_TEMPLATE/management-review.yml) |
| **Annual** | Restoration Test sign-off | [Restoration Test issue form](../../.github/ISSUE_TEMPLATE/restoration-test.yml) |
| **Annual** | Document review for each controlled document past its `next_review` date | [Document Review issue form](../../.github/ISSUE_TEMPLATE/document-review.yml) |
| **On-trigger** | Standard revision response (cited standard updates → module review + finding-log) | Cited-standard publishers |
| **On-trigger** | Regulatory review log review (when an independent reviewer submits one) | [Regulatory Review issue form](../../.github/ISSUE_TEMPLATE/regulatory-review.yml) + [`BUSINESS/regulatory_review_cadence.md`](../../BUSINESS/regulatory_review_cadence.md) |

---

## Daily — PR sign-off workflow

When a PR touches a controlled document (anything under `templates/`, `modules/`, or `BUSINESS/`), you (or your delegate per CODEOWNERS) are typically the approver of record.

**What "approver of record" means in §11.50 terms:** your approval commit carries the `Signature-Meaning: Approved` trailer. That commit + your GPG signature + the identity-mapping register row attributing the GPG fingerprint to you is the chain that makes the approval a Part 11 / Annex 11–defensible electronic signature.

### Approval workflow

1. Review the PR diff for substance — does the change satisfy its stated purpose?
2. Verify CI is green (YAML lint + pytest + bundle baselines + zero-orphan trace + 100% coverage).
3. If the PR modifies a controlled document, verify the `version:` field in frontmatter is incremented appropriately (minor for content change; major for breaking schema change). The doc-control workflow warns on non-increment but is currently soft-fail (see compliance-architecture P5 forward work).
4. Approve via GitHub PR review.
5. Optionally add a follow-up commit (or the merge commit) carrying:
   ```
   Signature-Meaning: Approved
   Signature-Role: Quality Manager
   Signature-Justification: <one-line reason if non-obvious>
   ```
6. Merge.

### When to reject

- Frontmatter required fields missing or malformed
- Substantive change without corresponding evidence in the PR description (e.g., a SOP change with no rationale or no link to the driving CAPA)
- Cited standard misrepresented (you noticed; raise as comment, do not approve)
- CODEOWNERS not satisfied (more than one reviewer team should have signed off)

---

## Weekly — CAPA aging review

Open CAPAs left to age silently is the most common process-failure pattern. Weekly cadence catches this before audit.

Workflow:

1. Open the CAPA issue list (label `capa-open`).
2. Filter by `updated > 7 days ago`.
3. For each aging CAPA:
   - If it has a named owner + a clear next step: comment to nudge.
   - If it does not: reassign or close with `Signature-Meaning: Reviewed` + `Justification: closed due to <reason>` (e.g., duplicate, scope-revision, no-action-required).
4. If aging CAPAs exceed a threshold you set (e.g., > 10), this is a process-load signal; raise at next management review.

See [`docs/guide/capa-lifecycle.md`](capa-lifecycle.md) for the full state machine.

---

## Monthly — training-completion follow-up

Training-trigger automation creates Training Completion issues per [`docs/guide/training.md`](training.md). Quality Manager owns the chase loop:

1. Filter open issues by label `training-pending`.
2. Filter by `created > 30 days ago`.
3. For each:
   - Ping the trainee in a comment with a deadline (e.g., "complete by EOD Friday or escalate").
   - If repeated non-response: escalate to the trainee's manager.
   - If non-completion persists past escalation: open a CAPA for the underlying training-compliance gap.
4. Once the trainee or their supervisor closes the issue with the attestation checkboxes + signature trailer, that's the training record.

---

## Quarterly — Access Review

Joint with IT/Security per [`templates/qms-policy/IDENTITY-MAPPING-SOP-TEMPLATE.md`](../../templates/qms-policy/IDENTITY-MAPPING-SOP-TEMPLATE.md) §4.

1. Open an [Access Review issue](../../.github/ISSUE_TEMPLATE/access-review.yml) at the start of the quarter.
2. Allocate ~2 hours for the review meeting with IT/Security.
3. Walk every active row in the identity-mapping register.
4. Document findings in the issue.
5. Close with `Signature-Meaning: Reviewed` trailer from both QM and IT/Security.

If findings are non-trivial, open follow-up CAPAs or NCRs to track remediation.

---

## Annual — Management Review

The cornerstone record per ISO 13485 §5.6 / 21 CFR §820.20(c). Open Management Review issue form well in advance:

1. ~30 days before review meeting: open [Management Review issue](../../.github/ISSUE_TEMPLATE/management-review.yml). Issue body becomes the agenda.
2. ~14 days before meeting: aggregate inputs:
   - CAPA status snapshot (`gh issue list -l capa-open`)
   - Complaint trends (`gh issue list -l complaint`)
   - Audit findings (internal + external)
   - Training-completion rate
   - Supplier performance
   - Customer feedback
   - Regulatory change impact
   - Resource adequacy
   - Quality-policy and -objectives review
   The aggregation pattern is documented in [`docs/guide/management-review.md`](management-review.md).
3. Hold meeting. Document decisions + actions in issue comments during meeting.
4. Within 7 days: close issue with `Signature-Meaning: Approved` from CEO/responsible-management + `Signature-Meaning: Authored` from QM.

The closed issue is the management review record.

---

## Annual — Restoration Test sign-off

You do not run the restoration test — IT/Security Lead owns the execution. Your role is sign-off on the findings document per [`templates/qms-bcms/BACKUP-RESTORE-SOP-TEMPLATE.md`](../../templates/qms-bcms/BACKUP-RESTORE-SOP-TEMPLATE.md) §4 step 12.

1. IT/Security raises a [Restoration Test issue](../../.github/ISSUE_TEMPLATE/restoration-test.yml) when the test runs.
2. They commit the findings doc at `BUSINESS/restoration_test_YYYY-MM-DD.md`.
3. You review the findings doc.
4. You add a follow-up commit to the findings doc with `Signature-Meaning: Reviewed` + your `Signature-Role: Quality Manager`.
5. You comment on the issue confirming sign-off.

If the test outcome is `Fail`, do not sign-off until the linked CAPA is closed.

---

## Annual — document review queue

Every controlled document carries a `next_review` field in frontmatter (typically `effective_date + 12 months`).

Workflow:

1. Once a quarter, generate the queue: documents where `next_review < TODAY + 90`.
   - Future tooling (compliance-architecture P5) will surface this automatically; for now, manual `grep` works: `grep -lE "^next_review:" templates/ -r | xargs grep -lE "^next_review: 202[6789]-"`.
2. For each document in the queue, open a [Document Review issue](../../.github/ISSUE_TEMPLATE/document-review.yml).
3. Assign the review to the document owner.
4. Follow the 3-outcome flow (no changes / minor change / major revision).
5. Once closed, the document's `last_review_date` should be bumped via a follow-up PR.

---

## Linkage to other Open QMS controls

- **OQ-080** README disclosure — you are the org-side judgment layer the disclosure points to; your professional judgment fills the OQ-080 firewall
- **OQ-064** management-review aggregation — operationalized by the Management Review issue form + this guide's Annual workflow
- **OQ-119** compliance architecture trust-gate — when an auditor asks "show me your quality system," your daily/weekly/monthly/annual cadences are the evidence that the system is *operating*, not just documented
- **`BUSINESS/regulatory_review_cadence.md`** — you decide when modules go for independent regulatory review per the cadence schedule

---

## Anti-patterns to avoid

- **Approving PRs without reading the diff substantively.** Rubber-stamping is what regulators look for and the easiest finding to identify at audit. If you don't have time, delegate to someone with bandwidth — that's why CODEOWNERS supports teams.
- **Closing CAPAs without an effectiveness check.** "Action taken" is not "action effective." See [`docs/guide/capa-lifecycle.md`](capa-lifecycle.md) for the effectiveness-check state.
- **Treating the Management Review as a one-meeting event.** The aggregation is the work; the meeting is the consensus point.
- **Skipping the Access Review when no obvious findings are expected.** The cadence is the control; an empty-finding review is the most common outcome AND the most defensible at audit.
- **Letting the `not yet reviewed` badge sit on critical modules indefinitely.** Per `BUSINESS/regulatory_review_cadence.md` the first-tier targets are 8 modules; budget for at least one independent review per year if possible.
