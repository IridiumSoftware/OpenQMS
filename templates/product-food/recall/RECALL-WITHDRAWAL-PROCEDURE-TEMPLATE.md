---
document_id: RECALL-XXX
title: "[Site / Organization Scope] — Recall and Withdrawal Procedure"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Recall Coordinator / QA Director, Title]"
status: draft
approved_by: "[Plant Manager + Food Safety Manager + Legal Counsel]"
approval_date: YYYY-MM-DD
mock_recall_cadence: "Minimum annually + ad hoc on significant supply-chain or product change"
---

# RECALL-XXX: Recall and Withdrawal Procedure

Per 21 CFR 117 Subpart D (FSMA Recall Plan requirement for products subject to Preventive Controls) + 21 CFR 7 (general FDA recall procedures) + 21 CFR 11 (electronic records during recall) + Codex Alimentarius CXC 1-1969 + ISO 22000:2018 §8.9 (control of NC + withdrawal/recall). Defines the organization's process for promptly + effectively recalling or withdrawing potentially unsafe food product from distribution channels.

**Recall** — removal of distributed product because of an unsafe condition or violation of regulation.
**Withdrawal** — removal of distributed product because of a quality issue not subject to regulatory action.
**Market action** — broad term covering both.

This document is the procedure. Each invocation of the procedure produces a specific Recall/Withdrawal Record (RWR-XXX) linking to this procedure version + the specific incident.

## 1. Recall classification

Per FDA / Codex classification:

| Class | Hazard | Examples |
|---|---|---|
| **Class I** | Reasonable probability of serious adverse health consequences or death | Listeria contamination of RTE food; undeclared major allergen; foreign material with sharp-injury potential; Salmonella in low-water-activity product |
| **Class II** | Temporary or medically reversible adverse health consequences with low probability of serious consequences | Undeclared minor allergen for non-life-threatening sensitivity; bacterial contamination unlikely to cause serious illness; sub-clinical undeclared substance |
| **Class III** | Not likely to cause adverse health consequences | Minor labeling violation; sub-spec quality issue with no safety implication |

Classification is FDA's call (FDA classifies after firm initiates), but the firm's initial assessment determines speed + scope. **When in doubt, treat as Class I.**

## 2. Recall team

| Role | Primary | Backup | 24/7 contact | Authority |
|---|---|---|---|---|
| Recall Coordinator (single decision-maker) | | | | Initiates + leads recall execution |
| QA Director | | | | Product disposition + corrective action |
| Plant Manager | | | | Production hold + resource commitment |
| Regulatory Affairs | | | | FDA / USDA-FSIS / state agency notification |
| Legal Counsel | | | | Customer / consumer communications review; insurance |
| Logistics / Supply Chain | | | | Recovery of product; distribution-list assembly |
| Marketing / Communications | | | | Customer + media communication |
| Food Safety Manager | | | | Root-cause investigation lead |
| Insurance contact | | | | Product-recall insurance claim notification |
| IT | | | | Trace data extraction from ERP / WMS / MES |

## 3. Recall decision (Hour 0 — initiation)

Triggers for recall consideration:
- Consumer complaint with adverse health report
- Positive finished-product test (microbiological, chemical, foreign-material)
- Positive environmental test in a high-risk zone with potential product contact
- Supplier notification of contaminated ingredient
- Regulatory inspection finding requiring market action
- Internal audit finding requiring market action

**Decision flow:**

1. Recall Coordinator notified by any team member becoming aware of a triggering event.
2. Recall Coordinator convenes Recall Team within 4 hours (or 1 hour for known Class I).
3. Team reviews evidence + applies decision criteria + classifies.
4. If recall confirmed: Recall Coordinator authorizes initiation; document time + decision rationale.

## 4. Hour 1–24 actions

- [ ] **Product hold** — all in-process + warehouse inventory of affected product placed on hold immediately
- [ ] **Distribution list assembly** — extract from ERP / WMS / customer-shipment records, batch + lot + ship-date + customer-account list. Target: <4 hours
- [ ] **Quantity calculation** — units shipped, units returned + on-hand, units estimated still in market, units estimated already consumed
- [ ] **Regulatory notification:**
  - **FDA** — voluntary recall is initiated by firm; firm notifies FDA District Office within 24 hours; complete Reportable Food Registry filing if Class I per 21 USC §350f
  - **USDA-FSIS** (meat / poultry) — immediate notification to FSIS District Office; FSIS publishes recall release
  - **State agencies** — per state requirements
  - **Importing country authorities** — per export agreements
- [ ] **Customer notification** — direct customers (distributors / retailers / foodservice) notified within 24 hours with: product ID, lot/batch codes, ship dates, reason, action required (segregate + hold for return / destruction)
- [ ] **Press release** — Class I + Class II typically; coordinate with FDA Office of Affairs + USDA Office of Public Affairs
- [ ] **Crisis-line activation** — consumer-facing 800 number for inquiries

## 5. Hour 24–168 (recovery + verification)

- [ ] **Effectiveness checks** per FDA guidance — direct contact with consignees to verify they received the notification + acted on it. Three levels (A = 100% / B = sample / C = ~10%) per Class.
- [ ] **Recovery tracking** — units recovered vs. units shipped; ongoing recovery rate
- [ ] **Disposition** — recovered product destroyed (with witness verification + certificate of destruction) OR reconditioned (rare; only with FDA agreement)
- [ ] **Daily status report** to FDA / FSIS

## 6. Hour 168 onward — closure + root cause

- [ ] **Root-cause investigation** — completed using HACCP plan + Food Safety Plan + supplier records + environmental data. Linked to deviation / NC / OOS records as applicable.
- [ ] **CAPA** — corrective + preventive actions implemented; effectiveness check scheduled
- [ ] **HACCP / FSP reassessment** — has the underlying hazard control been confirmed adequate? Update if gap identified.
- [ ] **Supplier action** (if supply-chain root cause) — supplier-status review, possible removal from ASL, corrective-action verification
- [ ] **Insurance claim** — product-recall insurance notification + claim assembly
- [ ] **Recall termination** — request to FDA / FSIS once recovery + corrective actions complete; FDA issues termination letter

## 7. Mock recall

Mock recall exercise minimum annually. Tests:
- Distribution-list extraction speed + accuracy
- Lot-code traceability (1-up-1-down + within-facility)
- Team activation + communication
- Documentation completeness

Mock recall outcome documented in RWR-MOCK-XXX records.

**Acceptance:** 100% traceability of selected lot in ≤ N hours (typical target ≤ 4 hours; FDA expects substantially less than 24 hours).

## 8. Documentation requirements

For each recall, retain:

- This procedure version invoked
- RWR-XXX specific record
- Distribution list (raw extraction)
- Recall notification(s) sent to customers + FDA/FSIS
- Press release(s)
- Effectiveness check results
- Recovery + destruction records
- Root-cause investigation report
- CAPA records
- FDA / FSIS termination letter

Retention per FDA / FSIS minimums (typically minimum 2 years; longer for shelf-stable products).

## 9. Sign-off (procedure approval)

| Role | Name | Date | Signature |
|---|---|---|---|
| Recall Coordinator | | | |
| QA Director | | | |
| Plant Manager | | | |
| Food Safety Manager | | | |
| Regulatory Affairs | | | |
| Legal Counsel | | | |
| Insurance contact | | | |

## 10. References

- 21 CFR 117 Subpart D — Modified Requirements (FSMA Recall Plan).
- 21 CFR 7 — Enforcement Policy (FDA recall procedures + classification).
- 21 USC §350f — Reportable Food Registry.
- 9 CFR 418 — Recall coordination (USDA-FSIS).
- ISO 22000:2018 §8.9 — Control of product and process nonconformities + withdrawal/recall.
- Codex Alimentarius CXC 1-1969 §5.7 — Recall procedures.
- FSSC 22000 v6 — incorporates ISO 22000 recall requirements.
- FDA Industry Guidance — Product Recalls, Including Removals and Corrections.
- Linked: HACCP-XXX (HACCP plan), PRP-XXX (Prerequisite Programs incl. §15 recall PRP), FSP-XXX (Food Safety Plan), supplier-evaluation records, CAPA records, individual RWR-XXX records.

## 11. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
