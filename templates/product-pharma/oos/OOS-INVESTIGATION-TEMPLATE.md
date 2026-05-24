---
document_id: OOS-XXX
title: "[Test + Sample Identifier] — Out-of-Specification Investigation"
version: "1.0"
opened_date: YYYY-MM-DD
opened_by: "[Analyst reporting the OOS]"
owner: "[Investigation Lead — typically QC Lab Supervisor or QA Investigator]"
status: open
qa_approver: "[QA Director]"
closure_date: YYYY-MM-DD
---

# OOS-XXX: Out-of-Specification Investigation

Per FDA Guidance for Industry "Investigating Out-of-Specification (OOS) Test Results for Pharmaceutical Production" (October 2006) + 21 CFR 211.192 + EudraLex Vol. 4 Part I Chapter 6 §6.34 + USP <1010>. An OOS result is any test result that falls outside the specifications or acceptance criteria established in product applications, official compendia, or established release criteria.

The OOS process has two phases, each with distinct gates:

- **Phase 1 — Laboratory Investigation.** Conducted by the analyst + supervisor immediately upon OOS identification. Focused on identifying assignable lab cause WITHOUT retesting. If an obvious lab error is identified (calculation, instrument malfunction, sample preparation, glassware contamination), the result may be invalidated with documented rationale. Phase 1 ends within 24-48 hours typically.
- **Phase 2 — Full-Scale Investigation.** Triggered when Phase 1 does not identify assignable lab cause. Cross-functional (QC + Production + Engineering + QA) investigation extending into manufacturing process, raw materials, environmental conditions, equipment, and previous batches. Retesting may be considered only with a documented protocol per the FDA guidance. Phase 2 typically completes within 30 days.

**Releasing a batch with an invalidated OOS result without proper Phase 1/2 investigation is a major regulatory observation in every jurisdiction.**

## 1. OOS identification

- **Date + time of result:** [YYYY-MM-DD HH:MM]
- **Sample identification:** [batch # + sample # + sampling point]
- **Test method (analytical procedure):** [reference]
- **Specification + acceptance criterion:** [value + units]
- **Observed result:** [value + units]
- **Magnitude of deviation:** [absolute + relative]
- **Analyst:** [name]
- **Equipment used:** [instrument ID + last calibration / qualification]
- **Reference standard used:** [reference + lot + expiry]
- **Linked Master Batch Record:** MBR-XXX
- **Linked batch number(s):** [enumerated]
- **Other tests on this batch already complete or in progress:** [enumerated — important for context]

## 2. Immediate actions

- [ ] Sample preserved (segregated, identified)
- [ ] Original raw data preserved (chromatograms, instrument logs, calculation worksheets)
- [ ] Batch placed on hold per QA notification
- [ ] Notification to Production, QA, Validation per site SOP
- [ ] Other immediate actions: [enumerated]

## 3. Phase 1 — Laboratory Investigation

Conducted by analyst + lab supervisor IMMEDIATELY. Focused on identifying assignable lab cause WITHOUT generating new analytical data on the original sample (no retesting yet).

### 3.1 Analyst interview + work review

| Element | Reviewed? | Findings |
|---|---|---|
| Calculation accuracy | | |
| Instrument operating parameters at time of test | | |
| Instrument calibration + qualification status | | |
| System suitability per analytical method | | |
| Reference standard preparation + expiry | | |
| Mobile phase / reagent preparation + expiry | | |
| Sample preparation (weighing, dilution, extraction) | | |
| Glassware cleanliness | | |
| Environmental conditions (temperature, humidity) | | |
| Analyst training currency | | |

### 3.2 Conclusion of Phase 1

| Outcome | Action |
|---|---|
| [ ] **Assignable lab cause identified** | Document cause, invalidate OOS result, retest per documented protocol; close OOS as lab error |
| [ ] **No assignable lab cause identified** | Proceed to Phase 2 full-scale investigation |
| [ ] **Inconclusive** | Proceed to Phase 2 (treat as no lab cause until proven otherwise) |

**Phase 1 conclusion:** [outcome + rationale]
**Phase 1 closed by + date:** [name + YYYY-MM-DD]

## 4. Phase 2 — Full-Scale Investigation

Required when Phase 1 does not identify assignable lab cause. Multi-functional team approach.

### 4.1 Hypothesis generation

| Hypothesis category | Specific hypothesis | Investigator | Evidence required |
|---|---|---|---|
| Manufacturing process | | Production + Engineering | |
| Raw material | | QC + Supplier QA | |
| Sampling | | QC + Production | |
| Environmental | | Facilities + QC | |
| Equipment | | Engineering + Validation | |
| Documentation / procedural | | QA | |
| Previous trend / drift | | QC + Validation (CPV) | |

### 4.2 Retesting (only with documented protocol)

Per FDA OOS Guidance (2006) §IV.A: retesting is appropriate ONLY when there is justified reason to suspect the original result is invalid OR when retesting is part of the investigation plan to test a hypothesis. The retesting plan must be approved BEFORE retesting commences.

| Retest # | Rationale | Sample source (original / fresh aliquot / re-sampled) | Method | Result | Comparison to original | Interpretation |
|---|---|---|---|---|---|---|

**Re-sampling justification (if performed):** [explicit; re-sampling is heavily scrutinized by regulators]

### 4.3 Statistical analysis

For repeated OOS or marginal-OOS situations, statistical analysis per USP <1010> + the analytical method's validation data (precision, intermediate precision, reproducibility):

- **Outlier test:** [Grubbs / Dixon's / pre-specified per method validation]
- **Trend analysis vs. historical data:** [reference]
- **Process capability of related parameters:** [reference]

### 4.4 Root cause determination

| Hypothesis | Outcome (confirmed / refuted / inconclusive) | Evidence |
|---|---|---|

**Root cause(s):**
- **Primary:** [statement]
- **Contributing factors:** [enumerated]
- **If no root cause identified:** [the FDA OOS guidance addresses this — investigation may close without root cause identified but the disposition must reflect that uncertainty]

## 5. Batch disposition

| Disposition | Authority | Required documentation |
|---|---|---|
| [ ] **Release** — invalidated OOS with documented assignable cause OR confirmed retest within spec with sound investigation; root cause addressed | QA + QP (EU) | Complete OOS report + retest data + root-cause analysis + corrective actions |
| [ ] **Release with concession / restriction** — batch acceptable but with documented limitation (e.g., for specific market only) | QA Director + QP | As above plus concession justification + market restriction documentation |
| [ ] **Rework** — only if validated rework procedure exists OR change-controlled rework is approved | QA + Production | Rework instruction + post-rework testing + final release decision |
| [ ] **Reject** — destroyed or returned | QA | Destruction record OR return-to-supplier authorization |

**Disposition:** [Release / Release with concession / Rework / Reject]
**Decided by + date:** [QA name + YYYY-MM-DD]
**Rationale:** [explicit]

## 6. Impact on other batches

- **Concurrent batches potentially affected:** [enumerated; if so, expand investigation scope]
- **Previously released batches potentially affected:** [enumerated; if so, trigger Field Alert (21 CFR 314.81) + Recall assessment]
- **Stability programs potentially affected:** [enumerated]

## 7. Regulatory reporting

- **Field Alert Report (FDA, 21 CFR 314.81(b)(1)(ii)) required?** Yes / No
- **EMA / national CA notification required?** Yes / No
- **MHRA notification required?** Yes / No
- **Reporting timeline:** [3 working days for FDA Field Alert]
- **Linked report:** [reference]

## 8. CAPA

| CAPA # | Type | Description | Owner | Due date | Effectiveness check method |
|---|---|---|---|---|---|

## 9. Closure + sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Analyst (originator) | | | |
| QC Lab Supervisor | | | |
| Investigation Lead | | | |
| Production Lead (Phase 2 involvement) | | | |
| Engineering Lead (Phase 2 involvement) | | | |
| Validation Lead (Phase 2 involvement) | | | |
| QA Investigator | | | |
| QA Director (mandatory closure approval) | | | |
| QP (EU jurisdictions) | | | |

## 10. References

- FDA Guidance for Industry — Investigating Out-of-Specification (OOS) Test Results for Pharmaceutical Production (October 2006).
- 21 CFR 211.192 — Production record review.
- 21 CFR 211.165 — Testing and release for distribution.
- 21 CFR 314.81(b)(1)(ii) — Field Alert Reports.
- EudraLex Vol. 4 Part I Ch. 6 §6.34 — Quality Control (Out-of-specification results).
- ICH Q9(R1) — Quality Risk Management.
- USP <1010> — Analytical Data — Interpretation and Treatment.
- USP <1224>, <1225>, <1226> — Validation and verification of compendial procedures (informs Phase 1 hypothesis around method performance).
- Linked: MBR-XXX, analytical method SOP, CAPA-XXX, DEV-XXX (if OOS triggered by deviation), APQR-XXX, Field Alert filings.

## 11. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial OOS entry. |
