---
document_id: RMF-XXX-001
title: "[Product Name] — Risk Management File"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Risk Manager / RA, Title]"
status: draft
approved_by: "[Risk Manager / RA, Title]"
approval_date: YYYY-MM-DD
---

# RMF-XXX-001: [Product Name] Risk Management File (ISO 14971)

## 1. Risk management plan

- **Scope:** [Product/version covered by this RM file.]
- **Risk management team:** [Roles + names; per ISO 14971 §4.2 requires top-management appointment.]
- **Risk acceptability criteria:** [Probability × severity matrix or equivalent. Documented method for declaring residual risk acceptable.]
- **Review cadence:** [When the RM file is re-reviewed — typically each design change, each post-market trigger, and at periodic intervals defined by SOP.]
- **References to related documents:** SRS, SAD, SOUP register, verification/validation protocols, post-market surveillance plan.

## 2. Hazard identification and risk analysis (ISO 14971 §5)

| ID | Hazard | Hazardous situation | Foreseeable sequence of events | Harm | Probability | Severity | Pre-mitigation risk |
|---|---|---|---|---|---|---|---|
| H-001 | [e.g. battery overheating] | [device in use during ambulatory monitoring] | [overcurrent → thermal runaway → enclosure breach] | [thermal burn] | [Low/Med/High] | [Negligible/Minor/Serious/Critical] | [score per matrix] |

## 3. Risk control (ISO 14971 §7)

| Hazard ID | Risk control measure | Type (inherent safety / protective measure / information for safety) | Implementation evidence | Verification of effectiveness |
|---|---|---|---|---|
| H-001 | [thermal cutoff at 60°C] | Protective measure (hardware) | [SAD §3.2; PCB rev D] | [VP-XXX-007 test case TC-12 results] |

## 4. Residual risk evaluation (ISO 14971 §8)

| Hazard ID | Post-mitigation probability | Post-mitigation severity | Post-mitigation risk | Acceptable? | Justification |
|---|---|---|---|---|---|
| H-001 | [Low] | [Minor] | [Acceptable per matrix] | Yes | [reference to acceptability criteria] |

## 5. Overall residual risk acceptability (ISO 14971 §8)

[Statement that all individual residual risks are acceptable AND that the overall residual risk is acceptable in light of the benefits. Per ISO 14971:2019 this is a separate, explicit determination by top management.]

## 6. Risk-benefit analysis (ISO 14971 §8)

[For each residual risk evaluated as marginal or unacceptable on its own: documented analysis showing intended use benefit outweighs residual risk. Required for medical devices where some non-zero risk is inherent to the clinical benefit.]

## 7. Risk management report (ISO 14971 §9)

[Final report summarizing: RM plan was implemented; overall residual risk is acceptable; methods for collecting post-production information are in place. Signed by the risk-management team and reviewed by top management.]

## 8. Production and post-production information (ISO 14971 §10)

- **Information collection methods:** complaints (see `docs/guide/complaints.md`), service records, regulatory reports, post-market surveillance plan, PMCF if applicable.
- **Trigger for RM file update:** [criteria — e.g. any newly identified hazard, any complaint indicating a previously-uncharacterized harm, any change in probability/severity estimates].
- **Loop back to §2:** Updates to the hazard analysis and risk evaluation per the post-market evidence.

## 9. References

- ISO 14971:2019 — Application of risk management to medical devices.
- ISO 24971 (informative) — Guidance on the application of ISO 14971.
- Linked artifacts: SRS-XXX-001, SAD-XXX-001, SOUP-XXX-001, VP-XXX-001, VAL-XXX-001.

## 10. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
