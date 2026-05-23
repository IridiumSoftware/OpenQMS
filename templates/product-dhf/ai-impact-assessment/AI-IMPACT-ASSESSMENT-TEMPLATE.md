---
document_id: AIIA-XXX
title: "[AI System Name] — AI Impact Assessment"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[RA / ML Lead, Title]"
status: draft
approved_by: "[Governance / Ethics / RA Lead, Title]"
approval_date: YYYY-MM-DD
---

# AIIA-XXX: [AI System Name] AI Impact Assessment

Per EU AI Act 2024/1689 Article 9 (risk management system for high-risk AI) + Article 27 (fundamental rights impact assessment for deployers of certain high-risk AI) and NIST AI RMF Govern + Measure + Manage functions. The AI Impact Assessment combines the risk management system documentation with the fundamental-rights / societal-impact analysis required for high-risk AI. Mandatory for high-risk AI in EU; recommended for any AI system per NIST AI RMF.

## 1. System under assessment

- **AI system name + version:** [name + version]
- **EU AI Act risk classification:** [Prohibited / High-risk per Annex III §X / Limited-risk / Minimal-risk]
- **High-risk classification rationale** (if high-risk): [Annex III subsection + justification]
- **Linked AI System Card:** AISC-XXX
- **Linked RMF (medical / sector device-level):** RMF-XXX-001 (if applicable)

## 2. Risk management process (Article 9 + NIST AI RMF Govern)

- **Risk management plan:** [scope, methodology, team, cadence]
- **Risk acceptability criteria:** [explicit thresholds per impact category]
- **Stakeholder identification:** [users, deployers, end-users / affected persons, regulators, society]
- **Roles and responsibilities:** [governance structure, accountability]
- **Third-party AI component governance:** [foundation models, pre-trained components, datasets — provider, license, vetting]

## 3. Risk identification (NIST AI RMF Map)

### 3.1 Intended use context

[Mirrors the AISC-XXX intended use; carry-forward summary.]

### 3.2 Identified risks (categorized)

| Risk ID | Category | Description | Affected stakeholder(s) | Source (data / model / deployment / human-AI interaction) |
|---|---|---|---|---|

**Risk categories** to consider (non-exhaustive; expand per system):
- **Performance** — accuracy degradation, distribution shift, edge-case failures.
- **Robustness** — adversarial attacks, input perturbation, noisy data.
- **Bias / fairness** — disparate impact across protected classes, statistical bias, representation bias.
- **Privacy** — training data leakage, membership inference, model inversion.
- **Security** — model theft, poisoning attacks, jailbreaks.
- **Transparency / explainability** — opacity preventing user interpretation.
- **Accountability** — unclear responsibility for outputs.
- **Safety** — physical or psychological harm from AI-driven decisions.
- **Societal** — labor displacement, concentration of power, erosion of human agency.
- **Environmental** — energy consumption of training and inference.

## 4. Risk measurement (NIST AI RMF Measure + EU AI Act Article 9(2)(b))

| Risk ID | Likelihood | Severity if realized | Pre-mitigation risk score | Measurement methodology |
|---|---|---|---|---|

**Measurement methodologies** to consider:
- Quantitative: test-set evaluation, red-teaming, statistical fairness audits, benchmark scores.
- Qualitative: structured interviews with affected stakeholders, scenario analysis, ethics review boards.
- Mixed: post-deployment monitoring with both metrics and user feedback.

## 5. Risk control (NIST AI RMF Manage + EU AI Act Article 9(4)-(7))

| Risk ID | Control measure | Type (technical / organizational / informational) | Implementation evidence | Verification of effectiveness | Residual risk |
|---|---|---|---|---|---|

**Risk control hierarchy** per ISO 14971 / ISO 23894 (in priority order):
1. **Elimination** through design — remove the risk source (e.g. don't use a feature that introduces unacceptable bias).
2. **Protective measures** — technical mitigations (e.g. confidence thresholds; human-in-the-loop gates; differential privacy; output filtering).
3. **Information for safety** — disclosures, warnings, training for deployers (Article 13).

## 6. Human oversight (EU AI Act Article 14)

[Article 14 requires high-risk AI to be designed so natural persons can oversee its operation. Document:]

- **Oversight model:** [Human-in-the-loop / Human-on-the-loop / Human-in-command]
- **Skills / training required of the human overseer:** [enumerated]
- **Interface affordances for oversight:**
  - Ability to fully understand system capacities and limitations: [how the UI surfaces this]
  - Awareness of automation bias: [training + UI countermeasures]
  - Ability to correctly interpret output: [explanations, confidence, calibration display]
  - Ability to decide not to use, override, or interrupt: [stop / override / disable controls]
- **Failure modes that human oversight is intended to catch:** [list]

## 7. Fundamental rights impact assessment (Article 27, where applicable)

[For deployers of high-risk AI listed in Annex III §1(a), §5(b), §5(c) — public authorities or private entities providing public services. Even where not legally required, recommended for any high-risk AI.]

- **Affected persons / groups:** [who interacts with the system; demographics]
- **Potential adverse impacts on fundamental rights:**
  - Right to non-discrimination (charter Art 21)
  - Right to private and family life (Art 7)
  - Protection of personal data (Art 8)
  - Right to effective remedy (Art 47)
  - Freedom of expression (Art 11)
  - [Other rights as applicable per sector and use]
- **Mitigation measures for each identified adverse impact:** [enumerated]
- **Residual fundamental-rights risk:** [acceptable / requires further mitigation]
- **Mechanism for affected persons to exercise rights:** [appeals, opt-out, human review]

## 8. Overall residual risk acceptability

[Statement by top management (or designee) per NIST AI RMF Govern that the overall residual risk, weighed against benefits, is acceptable for the intended use. Per ISO 14971 §8 if also a medical device.]

## 9. Post-deployment monitoring

[Per NIST AI RMF Manage + EU AI Act Article 9(2)(c) / Article 72 PMS for AI:]

- **Monitoring metrics:** [what is tracked; cadence; data sources]
- **Triggers for re-assessment:** [performance drift > threshold; new failure mode; regulatory change; complaint pattern]
- **Re-assessment cadence (in absence of trigger):** [periodicity]
- **Feedback loop to risk management:** [how monitoring data updates this AIIA]

## 10. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| ML / Engineering Lead | | | |
| Regulatory Affairs Lead | | | |
| Ethics / Governance Lead | | | |
| Top Management Designee (overall residual risk) | | | |

## 11. References

- EU AI Act 2024/1689 Article 9 — Risk management system for high-risk AI.
- EU AI Act 2024/1689 Article 14 — Human oversight.
- EU AI Act 2024/1689 Article 27 — Fundamental rights impact assessment.
- NIST AI RMF 1.0 — Govern, Measure, Manage functions.
- ISO/IEC 23894:2023 — AI risk management guidance.
- ISO/IEC 42001:2023 — AI management system.
- ISO 14971:2019 — Medical device risk management (composes for medical AI).
- Linked artifacts: AISC-XXX, RMF-XXX-001 (if medical), SRS-XXX, SAD-XXX.

## 12. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
