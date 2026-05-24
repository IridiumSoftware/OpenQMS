---
document_id: REC-XXX
title: "[Site / Product Family Scope] — Generalized Recall Procedure"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Recall Coordinator / Regulatory Affairs Director, Title]"
status: draft
approved_by: "[Recall Coordinator + Top Management + Legal Counsel + (per industry) QA Director / Regulatory Affairs / Plant Manager]"
approval_date: YYYY-MM-DD
mock_recall_cadence: "Minimum annually + ad hoc on significant product / supply-chain / regulatory change"
regulatory_framework_in_scope: "[NHTSA 49 CFR 573/577/579 | FDA 21 CFR 7 + 21 CFR 806 (medical devices) | FDA 21 CFR 117 Subpart D (food) | CPSIA §15 (consumer products) | EU Article 19 General Product Safety Regulation | other — list]"
---

# REC-XXX: Generalized Recall Procedure

Cross-vertical recall procedure parametrized by regulatory framework. Defines the organization's process for identifying, classifying, reporting, executing, and closing a product recall, removal, correction, withdrawal, or substantial-product-hazard notification across whichever regulatory framework(s) apply to its products.

The procedure is the SAME shape across industries (decision flow, regulator notification, customer/owner notification, effectiveness checks, root-cause investigation, closure); the DIFFERENCES are in classification scheme, regulator-specific notification timing, and required notification content. This template encodes the common shape + parametrizes the framework-specific details.

**Industry-specific framework references:**

| Industry | Primary regulatory framework | Classification scheme | Regulator notification window |
|---|---|---|---|
| Automotive (NHTSA) | 49 CFR Part 573 + 49 CFR Part 577 + 49 CFR Part 579 (TREAD Early Warning) | "Safety-related defect" or "Noncompliance with FMVSS"; no I/II/III sub-classification | Within 5 working days of decision per 49 CFR 573.6 |
| Medical devices (FDA) | 21 CFR 7 + 21 CFR 806 | Class I (serious adverse health consequences or death) / Class II / Class III | 21 CFR 806 corrections + removals within 10 working days per §806.10 |
| Pharmaceuticals (FDA) | 21 CFR 7 + 21 CFR 314.81 (NDA holders) | Class I / II / III | Field Alert per §314.81(b)(1)(ii) within 3 working days |
| Food (FDA) | 21 CFR 7 + 21 CFR 117 Subpart D + 21 USC §350f Reportable Food Registry | Class I / II / III | Class I to Reportable Food Registry per §350f within 24 hours of determination |
| Food (USDA-FSIS) | 9 CFR 418 + Recall Communications Plan | Class I / II / III | Immediate notification to FSIS District Office |
| Consumer products (CPSC) | CPSIA §15 (15 USC §2064) | "Substantial product hazard" (one tier) | Within 24 hours of obtaining info reasonably supporting conclusion per §15(b) |
| EU (general products) | Regulation (EU) 2023/988 General Product Safety Regulation Art. 19 | Serious risk / non-serious | Notify Safety Gate (RAPEX successor) immediately if serious risk |

## 1. Scope

- **Products covered:** [enumerated]
- **Regulatory framework(s) applicable:** [from table above — list all that apply to this product scope]
- **Geographic distribution covered:** [markets]
- **Pre-existing complaint + adverse-event systems linked:** [reference]

## 2. Recall team (cross-vertical roster)

| Role | Primary | Backup | 24/7 contact | Authority |
|---|---|---|---|---|
| Recall Coordinator (single decision-maker) | | | | Initiates + leads recall execution |
| Regulatory Affairs Director | | | | Regulator notification per applicable framework |
| QA Director | | | | Product disposition + corrective action |
| Plant Manager | | | | Production hold + resource commitment |
| Legal Counsel | | | | Customer + consumer communications review; insurance; contractual obligations |
| Logistics / Supply Chain | | | | Recovery of product; distribution-list assembly |
| Marketing / Communications | | | | Customer + media communication; public notice content |
| HR Lead | | | | Internal communication to employees |
| Engineering / R&D Lead | | | | Technical investigation; root-cause analysis |
| Insurance contact | | | | Product-recall + product-liability insurance notification |
| IT | | | | Trace data extraction from ERP / WMS / MES / CRM |
| Industry-specific role | | | | (per framework — e.g., DER for aerospace; QP for pharma EU; PCQI for food FSMA) |

## 3. Recall trigger + decision (Hour 0)

Triggers for recall consideration:

- Consumer complaint with adverse health report
- Internal quality test failure on shipped product
- Field failure pattern observed via complaint trending
- Supplier notification of contaminated/defective component
- Regulatory inspection finding requiring market action
- Adverse-event database signal (FAERS / MAUDE / FOIs / NHTSA VOQ / CPSC SaferProducts / EU Safety Gate)
- Class-action lawsuit alleging defect
- Internal audit / root-cause analysis identifying systemic risk
- TREAD Early Warning Reporting threshold breach (automotive)

**Decision flow:**

1. Recall Coordinator notified by any team member becoming aware of a triggering event.
2. Recall Coordinator convenes Recall Team within 4 hours (or 1 hour for known Class I / serious-risk).
3. Team reviews evidence + applies industry-specific classification criteria.
4. **If recall confirmed:** Recall Coordinator authorizes initiation; document time + decision rationale.

Per CPSIA §15: the threshold for substantial-product-hazard reporting is *"information which reasonably supports the conclusion"* of a substantial hazard. This is a LOW threshold; ambiguity should resolve toward reporting.

Per 49 CFR 573: NHTSA notification within 5 working days of determining the existence of a safety-related defect or noncompliance with an FMVSS.

Per 21 CFR 806: medical-device manufacturer reports a correction or removal within 10 working days of initiating it.

## 4. Hour 0–24 actions

- [ ] **Product hold** — all in-process + warehouse inventory of affected product placed on hold immediately
- [ ] **Distribution list assembly** — extract from ERP / WMS / customer-shipment records, by lot/serial/batch + ship-date + customer-account list. Target: <4 hours
- [ ] **Quantity calculation** — units shipped, units returned + on-hand, units estimated still in market, units estimated already used/consumed/installed
- [ ] **Industry-specific regulator notification (per applicable framework):**
  - **NHTSA (automotive):** Defect Information Report (DIR) submitted via NHTSA's Manufacturer Portal per 49 CFR 573.6 within 5 working days of decision; campaign number assigned by NHTSA
  - **FDA medical devices:** Report of Correction or Removal per 21 CFR 806.10 within 10 working days; consider voluntary classification request to FDA
  - **FDA pharmaceuticals:** Field Alert Report per 21 CFR 314.81(b)(1)(ii) within 3 working days for distributed product
  - **FDA food:** Reportable Food Registry filing per 21 USC §350f within 24 hours of determination of reasonable probability of serious adverse health consequence
  - **USDA-FSIS:** Immediate notification to FSIS District Office; FSIS issues recall release
  - **CPSC consumer products:** Section 15(b) report within 24 hours of obtaining information reasonably supporting conclusion of substantial product hazard
  - **State/provincial authorities:** per applicable jurisdiction
  - **Importing-country authorities:** per export agreements
- [ ] **Customer notification** — direct customers (distributors / retailers / dealers / foodservice / clinical sites) notified within 24 hours
- [ ] **Owner/consumer notification (where applicable):** triggered by regulator approval of customer-facing notification language; see industry-specific templates (e.g., NHTSA-OWNER-NOTIFICATION-TEMPLATE for automotive per 49 CFR 577)
- [ ] **Press release / public notice** — coordinated with regulator's communications office
- [ ] **Crisis-line activation** — consumer-facing 800 number for inquiries
- [ ] **Internal communication** — employees, sales force, customer-service teams informed with consistent talking points

## 5. Industry-specific notification content requirements

### Automotive — 49 CFR 577

Owner notification letters per 49 CFR 577 shall include (use NHTSA-OWNER-NOTIFICATION-TEMPLATE):

- Manufacturer name, address, vehicle/equipment description, model years affected (§577.5(a))
- Defect/noncompliance description (§577.5(b))
- Risk to motor vehicle safety described in vehicle-owner-comprehensible terms (§577.5(c))
- Warning against continued use if applicable, with available means to prevent loss / injury (§577.5(d))
- Description of remedy + reasonable time for remedy availability (§577.5(e))
- Statement that remedy is no-charge (§577.5(f))
- Instructions on obtaining remedy + complaint procedure with NHTSA (§577.5(g))
- NHTSA recall campaign number (§577.5)
- Timing per §577.7 (no later than 60 days after submission of 573 report to NHTSA, unless extended)
- Second notification per §577.8 if remedy completion rate is < 70% at 6 months

### Medical devices — 21 CFR 806

Reports of Corrections and Removals shall include (§806.10):

- Date of correction/removal initiation
- Description of action
- Reason
- Total units distributed (incl. dates)
- Identity of affected product (model, version, lot/serial)
- Identity of consignees + their locations
- Risk associated with correction/removal
- Reference to MDR adverse-event reports if related (per §803)
- Copies of communications to consignees

### Food — 21 CFR 117 Subpart D + 21 CFR 7

Per FDA recall classification (Class I / II / III) — see template's REC-XXX §1 classification table. Public notice via FDA Press Release coordination for Class I + Class II.

### Consumer products — CPSIA §15 + 16 CFR 1115

Section 15(b) Report shall include description of product + nature of risk + number of units distributed + corrective action proposed. CPSC reviews + may publish Recall Notice + Joint Press Release with manufacturer.

## 6. Hour 24–168 actions (recovery + verification)

- [ ] **Effectiveness checks** per applicable framework — direct contact with consignees to verify they received the notification + acted on it
  - **FDA Class I:** Level A (100%); Class II: Level B (sample-based); Class III: Level C (~10%)
  - **NHTSA:** Quarterly status reports per 49 CFR 573.7 until completion rate stabilizes
  - **CPSC:** Quarterly Progress Report per agreed schedule until termination
- [ ] **Recovery tracking** — units recovered vs. units shipped; ongoing recovery rate trending
- [ ] **Disposition** — recovered product destroyed (with witness verification + Certificate of Destruction) OR reworked/reconditioned (only with regulator agreement)
- [ ] **Daily status report** to applicable regulator(s)
- [ ] **Owner second notification** — automotive: per §577.8 if completion < 70% at 6 months; equivalents in other frameworks

## 7. Hour 168+ — closure + root cause

- [ ] **Root-cause investigation** — using applicable HACCP/Food Safety Plan/HARA/TARA/Design FMEA/etc. as starting reference. Linked to deviation/NC/OOS records.
- [ ] **CAPA** — corrective + preventive actions implemented; effectiveness check scheduled
- [ ] **Hazard analysis re-assessment** — has the underlying hazard control been confirmed adequate? Update if gap identified.
- [ ] **Supplier action** (if supply-chain root cause) — supplier-status review; ASL impact; corrective-action verification
- [ ] **Insurance claim** — product-recall insurance + product-liability insurance notification + claim assembly
- [ ] **Class-action / litigation hold** — preservation of evidence; legal counsel coordination
- [ ] **Recall termination request** to applicable regulator(s) once recovery + corrective actions complete; regulator issues termination letter
- [ ] **Trend analysis** — does this recall fit a pattern? Should annual product quality review reflect systemic concern?

## 8. TREAD Early Warning Reporting (automotive only) — 49 CFR 579

Distinct from defect-determination reporting per 49 CFR 573. Automotive manufacturers above thresholds must submit quarterly EWR reports per 49 CFR 579:

- Production data (§579.21)
- Death / injury / property damage claims (§579.21(c))
- Field reports (§579.21(d))
- Consumer complaints (§579.21(e))
- Warranty claims (§579.21(f))
- Foreign defect notifications + recalls (§579.21(g))

A pattern in EWR data may trigger a recall determination under 49 CFR 573 — the two frameworks are linked.

## 9. Mock recall

Mock recall exercise minimum annually per applicable framework. Tests:

- Distribution-list extraction speed + accuracy
- Lot/serial/batch traceability (1-up-1-down + within-facility for food; per-VIN for automotive; per-UDI for medical devices)
- Team activation + communication
- Documentation completeness

**Acceptance:** 100% traceability of selected lot/VIN/UDI in ≤ N hours (NHTSA expects manufacturer-defined target; FDA food guidance suggests ≤4 hours; medical-device UDI traceability expected near-immediate).

Mock-recall outcome documented in MOCK-REC-XXX records.

## 10. Linked records

- This procedure version invoked
- REC-XXX specific recall record (per invocation)
- Distribution list (raw extraction)
- Defect Information Report (NHTSA) / Report of Correction or Removal (FDA medical device) / Field Alert Report (pharma) / RFR filing (food) / Section 15(b) Report (CPSC) per framework
- Owner/customer notification(s) sent
- Press release(s)
- Effectiveness check results
- Recovery + destruction records
- Root-cause investigation report
- CAPA records
- Regulator termination letter

Retention per applicable framework minimums (NHTSA: minimum 5 years per 49 CFR 573.13; FDA medical devices: 2 years; FDA food: 2 years; CPSC: 5 years; longer for complex/long-shelf-life products).

## 11. Sign-off (procedure approval)

| Role | Name | Date | Signature |
|---|---|---|---|
| Recall Coordinator | | | |
| Regulatory Affairs Director | | | |
| QA Director | | | |
| Plant Manager | | | |
| Legal Counsel | | | |
| Insurance contact | | | |
| Top Management representative | | | |

## 12. References

**Automotive (NHTSA):**
- 49 CFR Part 573 — Defect and Noncompliance Responsibility and Reports.
- 49 CFR Part 577 — Defect and Noncompliance Notification.
- 49 CFR Part 579 — Reporting of Information and Communications about Potential Defects (TREAD Act EWR).
- 49 USC §30118 — Notification of defects and noncompliance.
- NHTSA's Office of Defects Investigation (ODI) procedures.

**Medical devices (FDA):**
- 21 CFR Part 7 — Enforcement Policy (general FDA recall classification + effectiveness checks).
- 21 CFR Part 806 — Medical Devices; Reports of Corrections and Removals.
- 21 CFR Part 803 — Medical Device Reporting (adverse-event reporting, distinct from corrections + removals).
- 21 CFR §820.198 — Complaint files (Quality System Regulation).

**Pharmaceuticals (FDA):**
- 21 CFR Part 7 (same general recall policy).
- 21 CFR §314.81(b)(1)(ii) — Field Alert Reports.
- 21 USC §360bbb-3 (EUA-related recall provisions where applicable).

**Food (FDA):**
- 21 CFR Part 7 (same general recall policy).
- 21 CFR Part 117 Subpart D — FSMA Recall Plan.
- 21 USC §350f — Reportable Food Registry.

**Food (USDA):**
- 9 CFR Part 418 — Recall coordination.
- FSIS Directive 8080.1 — Recall of Meat and Poultry Products.

**Consumer products (CPSC):**
- CPSIA §15 (15 USC §2064) — Substantial product hazards.
- 16 CFR Part 1115 — Substantial product hazard reports.
- 16 CFR Part 1117 — Reporting of choking incidents.

**EU:**
- Regulation (EU) 2023/988 — General Product Safety Regulation (replaced GPSD).
- Article 19 — Information obligations + Safety Gate notification.

**International:**
- Codex Alimentarius CXC 1-1969 §5.7 — Recall procedures (food).

Linked: GENERALIZED-RECALL-PROCEDURE (this), NHTSA-OWNER-NOTIFICATION-TEMPLATE (49 CFR 577 letter); HACCP / FSP / HARA / TARA / Design FMEA (root-cause starting references); deviation / NC / OOS / CAPA / complaint records; supplier-evaluation records; mock-recall records (MOCK-REC-XXX).

## 13. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
