# Management review

ISO 13485 §5.6 and 21 CFR 820.20(c) require periodic top-management review of the QMS to ensure continuing suitability, adequacy, and effectiveness. The reviews must have documented inputs (§5.6.2) and documented outputs (§5.6.3) including decisions and actions.

Open QMS provides the controlled-document template, the workflow issue template, and patterns for aggregating the inputs from across the QMS. The cadence (typically quarterly or semi-annually) is adopter-defined per SOP.

## What's in this repo

- **`templates/qms-management-review/MANAGEMENT-REVIEW-TEMPLATE.md`** — the controlled meeting record covering all ISO 13485 §5.6.2 inputs and §5.6.3 outputs.
- **`.github/ISSUE_TEMPLATE/management-review.yml`** — workflow tracker including the input-aggregation checklist.
- **Module binding** — the medical-devices module binds the template to ISO 13485 §5.6 and 21 CFR 820.20(c).

## Workflow

1. **Schedule.** Open a management-review issue via the template. The issue carries the period covered, scheduled date, chairperson, attendees, and the input-aggregation checklist.

2. **Aggregate inputs.** Before the meeting, the Management Representative (or delegate) walks the §5.6.2 input list and gathers the evidence. Open QMS doesn't ship a single "run management review" automation — most inputs live in cross-cutting GitHub queries. See **Input aggregation patterns** below.

3. **Hold the meeting.** Fill in the MR-XXX record from the template as the meeting progresses. Capture decisions, action items, and the effectiveness statement.

4. **Approve the record.** Open a PR with the completed MR-XXX. CODEOWNERS review is the §11.50 approval signature (see `docs/guide/signature-meaning.md` for `Signature-Meaning: approved`).

5. **Carry forward action items.** Action items in §4.4 become tracking issues (typically with a `management-review-action` label) and feed into the next review's §2 (prior-review action-item status).

## Input aggregation patterns

The §5.6.2 inputs are spread across the QMS. Most can be assembled via `gh` CLI queries or simple Git log walks.

### Complaint trends (§3.1)

```bash
# Complaints opened in the period
gh issue list --label complaint --search 'created:2026-Q1' --limit 200

# Open complaints (still in triage / investigation)
gh issue list --label complaint-open --limit 200
```

### Internal audit results (§3.2)

Audit reports live as controlled documents (typically under `qms-audits/` if the adopter creates that directory). Findings are usually tracked as issues with an `audit-finding` label.

```bash
gh issue list --label audit-finding --search 'created:2026-Q1'
```

### CAPA status (§3.3)

```bash
# CAPAs opened / closed in the period
gh issue list --label capa --search 'created:2026-Q1'
gh issue list --label capa --search 'closed:2026-Q1' --state closed

# Overdue CAPAs (filter on capa-open label + due-date convention)
gh issue list --label capa-open
```

### Process performance / NCRs (§3.4)

```bash
gh issue list --label ncr --search 'created:2026-Q1'
gh issue list --label ncr-open
```

### Supplier performance (§3.6)

```bash
gh issue list --label supplier-evaluation --search 'created:2026-Q1'
```

Plus the ASL diff: `git log --oneline --since=YYYY-MM-DD -- qms-suppliers/APPROVED-SUPPLIER-LIST-TEMPLATE.md` shows additions / removals / re-evaluations in the period.

### Risk management updates (§3.7)

```bash
git log --since=YYYY-MM-DD -- 'product-*/risk-management/RISK-MANAGEMENT-FILE-TEMPLATE.md'
```

### Training compliance (§3.8)

```bash
# Training issues opened by training-trigger.yml in the period
gh issue list --label training --search 'created:2026-Q1'

# Outstanding training
gh issue list --label training --state open
```

### Regulatory and standards changes (§3.5)

Typically tracked outside GitHub (regulatory intelligence feeds). Some adopters keep a `qms-regulatory-watch/` directory with dated entries; others reference an external system.

## Aggregation tooling

Open QMS does not ship a single "management review aggregator" tool. The patterns above are deliberately CLI-based so adopters can compose them per their environment:

- **Light-touch.** Run the `gh issue list` queries by hand the week before the review; paste the results into the MR record.
- **Scripted.** Write a small shell or Python script that runs the queries and emits a markdown summary. Many adopters maintain `scripts/management-review-aggregator.sh` for this.
- **External eQMS.** Some adopters use a commercial eQMS or dashboard (Grafana, Metabase) that already aggregates QMS metrics. The MR record references the dashboard snapshot.

Building a single shipped aggregator would force a one-size-fits-all label taxonomy on adopters; declining to ship one keeps the QMS pluggable.

## Cadence

Typical patterns (adopters tune per SOP):

| Organization stage | Cadence |
|---|---|
| Pre-market / actively developing | Quarterly |
| In-market, low-risk device | Semi-annually |
| Mature, multi-product | Quarterly per product line + annual portfolio review |

Triggered reviews (§5.6) fire on significant events: regulatory inspection results, major nonconformance, recall, significant CAPA, leadership change, or any event affecting the overall residual risk acceptability.

## References

- ISO 13485:2016 §5.6 — Management review.
- 21 CFR 820.20(c) — Management review.
- EU MDR Annex IX §2.2 — Quality management system audit.
- `docs/guide/complaints.md` — feedback / complaint trend inputs.
- `docs/guide/supplier-controls.md` — supplier performance inputs.
- `docs/guide/signature-meaning.md` — §11.50 trailer convention for MR approvals.
