# Supplier controls

ISO 13485 §7.4, 21 CFR 820.50, and EU MDR Article 10(9)(c) require documented supplier evaluation, selection, monitoring, and re-evaluation. Open QMS provides the controlled-document templates, issue-template workflow, and clause bindings; the cadence and criticality criteria are adopter-defined per SOP.

## What's in this repo

- **`templates/qms-suppliers/APPROVED-SUPPLIER-LIST-TEMPLATE.md`** — the controlled record of every supplier qualified to provide product or service in scope. The procurement gate.
- **`templates/qms-suppliers/SUPPLIER-EVALUATION-TEMPLATE.md`** — per-supplier evaluation record (initial qualification or re-evaluation).
- **`.github/ISSUE_TEMPLATE/supplier-evaluation.yml`** — workflow tracker for evaluation cycles.
- **Module binding** — the medical-devices module binds both templates to ISO 13485 §7.4 and 21 CFR 820.50.

## Workflow

1. **Trigger.** An evaluation cycle starts via one of three paths:
   - **Initial qualification** — a new supplier is identified (procurement or engineering raises the need).
   - **Periodic re-evaluation** — the scheduled cadence is due (track via the ASL's `Re-evaluation due` column).
   - **Triggered re-evaluation** — an NCR, complaint, supplier change notification, or performance metric breach demands an off-cycle review.

2. **Open the workflow issue.** Use `supplier-evaluation.yml`. The issue is the tracker; the evaluation record itself is the controlled document.

3. **Conduct the evaluation.** Fill in `SUPPLIER-EVALUATION-TEMPLATE.md` (SE-XXX). Cover the assessments appropriate to the criticality:
   - **Critical:** quality-system assessment (audit or comprehensive questionnaire + certificate evidence) + capability assessment + sample/lot qualification.
   - **Major:** quality-system assessment (questionnaire + certificate) + capability assessment.
   - **Minor:** quality-system assessment (certificate evidence or postal questionnaire) only.

4. **Decision.** Approve / Approve with conditions / Reject. Record in §6 of the SE record.

5. **Update the ASL.** Open a PR updating `ASL-001`:
   - Add or update the supplier row.
   - Set the next re-evaluation date per criticality cadence.
   - Reference the SE-XXX record id.
   - The PR's CODEOWNERS review is the §11.50 approval signature (see `docs/guide/signature-meaning.md` for `Signature-Meaning: approved` trailer convention).

6. **Close the issue.** When the PR merges, link both ways and close the supplier-evaluation issue.

## Re-evaluation cadence (defaults; adopters tune per SOP)

| Criticality | Re-evaluation interval | Trigger sensitivity |
|---|---|---|
| Critical | 12 months | Any NCR or complaint linked to supplier → triggered re-eval |
| Major | 24 months | Aggregate threshold of NCRs/complaints → triggered re-eval |
| Minor | 36 months | Significant supplier change only |

## Procurement gate

The ASL is the canonical list. Purchase orders for products in ASL scope must reference an approved SUP-xxx id. POs to suppliers not on the ASL are nonconformances. Adopters typically enforce this via:

- **Procedural** — the procurement SOP requires the buyer to check the ASL before raising a PO.
- **Automated** — the procurement system queries the ASL (parsed from the markdown table or a derived structured form) and rejects POs to unlisted suppliers.

Open QMS does not ship procurement-system automation. Adopters integrate per their environment.

## Audit trail

Every supplier-related decision is captured as either:

- A controlled-document PR (initial qualification, re-evaluation, ASL update) — Git history is the audit trail.
- An issue (the workflow tracker) — labels (`supplier-evaluation`, `supplier-evaluation-open`) drive aggregation in management review.

The management-review template (`templates/qms-management-review/MANAGEMENT-REVIEW-TEMPLATE.md`) explicitly enumerates supplier performance as a required input (§3.6). The management-review issue template's input-aggregation checklist references this guide.

## References

- ISO 13485:2016 §7.4 — Purchasing.
- 21 CFR 820.50 — Purchasing controls.
- EU MDR Article 10(9)(c) — Resources and supplier responsibility.
- `docs/guide/management-review.md` — supplier performance as a management-review input.
- `docs/guide/signature-meaning.md` — §11.50 signature-meaning trailers for ASL approvals.
