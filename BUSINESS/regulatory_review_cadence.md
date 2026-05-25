# Regulatory review cadence — Open QMS module crosswalks

**Purpose.** Document how often each Open QMS module's clause-to-template crosswalk should be reviewed against the authoritative regulator-side text by a qualified reviewer, what counts as a qualified reviewer, how findings are tracked, and how the resulting attestation is surfaced to adopters.

**Why this exists.** Open QMS proves *structural* coverage (every declared clause maps to ≥ 1 declared template — OQ-001 `:verified`; zero-orphan trace invariant enforced in CI). It does **not** prove *semantic adequacy* — that a clause summary accurately captures the authoritative text, or that a bound template substantively satisfies the regulator's intent. That gap is the OQ-080 firewall; this cadence document is how the project narrows it over time.

**This is process governance, not code.** The deliverable is a documented cadence + per-module attestation log; the actual reviews happen in the regulator-side text + reviewer's professional judgment.

---

## 1. Review-cadence schedule

| Standard kind | Review cadence | Rationale |
|---|---|---|
| **Active major standard** (currently-published; under active regulator interpretation) | **Annual** | Regulators issue guidance, FAQs, warning letters, and consensus interpretations that drift the operative reading of clauses even when the standard text doesn't change |
| **Cited standard receives a revision** | **On-revision (immediate trigger)** | Any update to a cited standard (e.g., ISO 14971:2019 → :2020 amendment; EU AI Act delegated acts; FDA Final Guidance issuance) triggers a re-review within 90 days |
| **Frozen / superseded standard still in active use** | **Biannual** | Standards in sunset phase (e.g., HIPAA pre-2024 Reproductive Health rule; ISO 13485:2003 in markets still recognizing it) merit re-review at lower cadence |
| **Forward / draft standard** (issued but not yet binding) | **Quarterly during pre-effective window** | Effective-date approaching means clause text may shift before binding; once binding, transitions to Annual cadence |
| **Sub-overlay / class-overlay** (depends on parent) | **Inherits parent cadence** | Reviewed jointly with the parent module |
| **Cross-overlay** (binds across verticals) | **Annual + on any parent-module re-review** | Intersection layer must remain consistent with its parents |
| **Architecture / Substrate / Invariant tier spec entries** | **Per release** | Already covered by per-release CI + cross-audit (A0-A6) |

**Default for new modules:** Annual cadence from first ship date, unless module README declares otherwise.

---

## 2. Reviewer-qualification standard

A "qualified reviewer" for a given module is an individual who meets at least ONE of the following criteria for the standard(s) covered by the module:

| Criterion | Examples |
|---|---|
| **Active regulatory professional** with ≥ 5 years experience in the standard's domain | RAC-certified individual for FDA-regulated; CQE / CQA for ISO 9001 family; ASQ Six Sigma Black Belt for manufacturing-quality; CISSP / CISA for IS security; SQA-certified for GxP |
| **Sitting member of a standards-development body** for the cited standard | ISO TC 210 member for medical devices; SAE J3061 working group member for automotive; IEC TC 65 for industrial security |
| **Practicing notified-body / certification-body auditor** for the standard | BSI / DEKRA / SGS / TÜV / NSF / DNV / UL auditor with active accreditation |
| **Practicing FDA Investigator (current or recent, ≤ 5 years)** for FDA-cited modules | CDER / CDRH / CBER / CVM Investigator with active engagement |
| **Practicing clinical/quality consultant** with documented work history at named regulated organizations + ≥ 3 closed regulatory submissions in the standard's domain | Independent QA/RA consultant with NDA-permitted disclosure of recent engagements |
| **Academic with peer-reviewed publications** specifically on the standard's interpretation (≥ 3 publications in the past 5 years) | Regulatory affairs / law / quality management academic |

**Documenting reviewer qualifications.** Each completed review must cite which criterion qualifies the reviewer, by name + organization + (where applicable) certification body + certification ID + expiry date. The qualification record may be redacted for public posting but must be retained in full in the adopter / project records.

---

## 3. Review-finding tracking format

Each completed review produces a finding-log file at `BUSINESS/regulatory_reviews/<module-name>_<reviewer-org>_<YYYY-MM-DD>.md` with the following structure:

```markdown
---
module: <module-name>
module_version: <module-yaml-version>
standards_reviewed:
  - <standard-id-1>
  - <standard-id-2>
reviewer_name: <name>
reviewer_org: <organization>
reviewer_qualification: <criterion-from-§2>
reviewer_qualification_evidence: <certification-id-or-publication-cite-or-NDA-permitted-statement>
review_date: YYYY-MM-DD
review_method: <"clause-by-clause" | "sample-N-clauses" | "delta-from-prior-review">
prior_review_ref: <prior-review-file-or-"none">
overall_attestation: <"adequate" | "adequate-with-minor-findings" | "adequate-with-major-findings" | "not-adequate" | "scope-revision-required">
---

# Regulatory review — <module-name>

## Scope

Which clauses were reviewed; sampling strategy if not exhaustive; standards-versions targeted.

## Findings

| Severity | Clause | Finding | Recommendation |
|---|---|---|---|
| <minor / major / critical> | <clause-id> | <what's wrong> | <what to do> |

## Open questions

Any clauses where reviewer is uncertain or recommends external referral.

## Reviewer attestation

Signed reviewer statement attesting to the review per §2 of `regulatory_review_cadence.md`.
```

**Severity calibration:**

| Severity | Meaning | Required response |
|---|---|---|
| **minor** | Clause summary phrasing could be sharper; binding satisfies regulator intent | Address in next module release; no urgency |
| **major** | Clause summary materially misrepresents regulator text OR binding does not substantively address the clause | Address within 90 days; module status flag added to README until closed |
| **critical** | Clause summary is wrong in a way that could mislead an adopter into non-compliance | Address within 30 days; module deprecation notice considered; adopters notified |

---

## 4. Per-module attestation badge

Each module's `README.md` carries a "Last reviewed" badge in the header:

```markdown
**Last regulatory review:** YYYY-MM-DD by <reviewer-org> · attestation: <overall_attestation>
· next review due: YYYY-MM-DD · log: [`BUSINESS/regulatory_reviews/<file>`](...)
```

For modules that have **not yet been reviewed** by a qualified reviewer per §2:

```markdown
**Last regulatory review:** not yet reviewed by an independent qualified reviewer
· structural coverage verified by Open QMS engine (OQ-001 zero-orphan + 100% coverage)
· semantic adequacy attestation pending · see `BUSINESS/regulatory_review_cadence.md`
```

Honest framing is the rule — "not yet reviewed" is a true statement and informative to adopters; soft-pedalling it would undermine the OQ-080 firewall.

---

## 5. How adopters use this

| Adopter situation | What to do |
|---|---|
| Evaluating a module for first-time adoption | Check the README badge; if "not yet reviewed" decide whether to (a) commission your own review, (b) accept structural-coverage-only with documented risk, or (c) skip until reviewed |
| Module passes annual review; no findings | No action required |
| Module passes annual review; minor findings | Read the finding log; assess if your specific use case is affected |
| Module passes annual review; major or critical findings | Pause use of that module in regulated processes until findings are closed |
| Module overdue for annual review | Engage with the project to schedule; consider commissioning a review independently and contributing the log |

---

## 6. How the project executes this

Open QMS itself is maintained by a small team. The project's role is:

- **Documenting the cadence** (this file).
- **Receiving + integrating reviewer-contributed logs** from any qualified reviewer who reviews + submits a finding log.
- **Surfacing the badge state** on every module README.
- **Sponsoring or commissioning reviews** when adopters fund them (or when grant funding is available).
- **Tracking review-debt** as a public list in this file (see §7 below) so the gap is visible.

**The project does not gatekeep** — any reviewer meeting §2 may submit a review log via PR. The PR review focuses on (a) reviewer-qualification evidence is documented, (b) log file follows §3 format, (c) badge update is correct.

---

## 7. Review debt (initial baseline as of v0.55.0)

| Module count | Reviewed | Pending | Overdue |
|---|---|---|---|
| 116 modules + general | 0 | 116 | 0 (none have reached the annual cadence trigger yet, since this cadence was just established) |

**The initial state: no module has yet been reviewed by an independent qualified reviewer per §2.** This is the honest baseline. The cadence is now declared; the work begins.

**First-tier review targets** (highest-adoption-likelihood modules — should be reviewed first if review capacity becomes available):

1. `modules/medical-devices/` — ISO 13485 + 21 CFR 820 + ISO 14971 + IEC 62304 + EU MDR
2. `modules/pharma/` — ICH Q9 + Q10 + Q7 + 21 CFR 211 + EudraLex Vol. 4 + PIC/S Annex 1
3. `modules/iso-27001/` — ISO 27001 + Annex A
4. `modules/hipaa/` — 45 CFR 160 + 164 + HITECH
5. `modules/privacy/` — GDPR + CCPA/CPRA
6. `modules/regulated-ai/` — NIST AI RMF + EU AI Act + ISO 42001 + ISO 23894
7. `modules/aerospace/` — AS9100D + DO-178C + DO-254
8. `modules/automotive/` — IATF 16949 + ISO 26262 + ISO/SAE 21434

---

## 8. Linkage to project discipline

| This document supports | How |
|---|---|
| OQ-080 README-disclosure-as-honesty-bound | Operationalizes the disclosure: "coverage is not compliance" becomes a tracked process, not a closing statement |
| OQ-119 compliance architecture trust-gate | Closes forward-work P14 (originally identified by independent reviewer 2026-05-25) |
| `docs/compliance-architecture.md` §"Open-but-permanent: coverage is not compliance" | Provides the operational mechanism the conceptual statement promises |
| Future per-module review badges | Concrete adopter-facing signal of which modules carry independent attestation vs structural-coverage-only |
