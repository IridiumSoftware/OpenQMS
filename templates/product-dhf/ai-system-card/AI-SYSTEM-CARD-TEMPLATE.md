---
document_id: AISC-XXX
title: "[AI System Name] — AI System Card / Model Card"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[ML Lead / RA, Title]"
status: draft
approved_by: "[ML / Clinical / RA Lead, Title]"
approval_date: YYYY-MM-DD
---

# AISC-XXX: [AI System Name] AI System Card / Model Card

Per EU AI Act 2024/1689 Article 11 (technical documentation) + Article 13 (transparency to deployers) and NIST AI RMF Map function. The AI System Card is the public-facing summary of the AI system's intended use, capabilities, training data characteristics, performance, and limitations. Functions as both regulatory documentation (input to Annex IV technical file) and transparency artifact for deployers / end-users.

Conventions adopted: structure mirrors the original "Model Cards for Model Reporting" (Mitchell et al., 2019) extended with EU AI Act + IMDRF SaMD considerations.

## 1. AI system details

- **System name + version:** [name + semver]
- **Type:** [classification / regression / generation / detection / etc.]
- **Architecture family:** [e.g. transformer; CNN; gradient-boosted trees]
- **Date of creation / last update:** YYYY-MM-DD
- **Developer / organization:** [legal entity]
- **License + redistribution terms:** [if applicable]
- **Contact for further information:** [email / form]
- **EU AI Act risk category:** [Prohibited / High-risk (Annex III §X) / Limited-risk / Minimal-risk]
- **IMDRF SaMD category (if medical):** [I / II / III / IV per SIU-XXX]

## 2. Intended use

### 2.1 Primary intended use cases

[Plain-language description of the situations and tasks the AI system is intended for. Each use case explicit.]

### 2.2 Intended users / deployers

[Who is intended to operate the system: HCP role + training; consumer/patient; financial analyst; etc.]

### 2.3 Out-of-scope uses

[Use cases the system is NOT intended for and should NOT be deployed against. Critical for limiting liability and informing deployers per EU AI Act Art 13(3)(b).]

## 3. Factors

### 3.1 Relevant factors

[Demographic / phenotypic / instrumentation / environmental factors that may affect performance. Documented even if not yet evaluated.]

### 3.2 Evaluation factors

[Subset of §3.1 actually disaggregated in the evaluation results (§5). For each factor not evaluated, state the rationale and the gap.]

## 4. Training data

- **Training dataset(s):** [name(s), source(s), date range]
- **Number of training samples:** [n]
- **Demographic composition of training data:** [breakdowns per relevant factors]
- **Data governance per EU AI Act Article 10:**
  - Data quality controls applied: [imputation, deduplication, error detection]
  - Bias examination: [methodology + findings]
  - Bias mitigation measures: [reweighting, augmentation, adversarial debiasing, etc.]
  - Statistical representativeness: [coverage analysis vs intended user / patient population]
- **Provenance:** [data acquisition consent, licensing, IP basis]

## 5. Evaluation data

- **Evaluation dataset(s):** [name(s), source(s); critically: distinct from training data]
- **Number of evaluation samples:** [n]
- **Reason for choosing this dataset:** [external validity rationale]
- **Demographic composition of evaluation data:** [breakdowns]

## 6. Quantitative performance

| Metric | Overall | Subgroup 1 | Subgroup 2 | ... | Acceptance criterion | Pass / Fail |
|---|---|---|---|---|---|---|
| Accuracy | | | | | | |
| Sensitivity / Recall | | | | | | |
| Specificity | | | | | | |
| Precision / PPV | | | | | | |
| F1 | | | | | | |
| AUROC | | | | | | |
| Calibration (Brier / ECE) | | | | | | |
| Fairness (disparate impact / equalized odds / etc.) | | | | | | |

[Disaggregate by evaluation factors per §3.2. Confidence intervals where applicable.]

## 7. Ethical considerations

[Privacy concerns; consent; potential for harm if the system fails; potential for harm if the system succeeds; conditions under which the system should not be used; bias and fairness considerations.]

## 8. Caveats and recommendations

[Known limitations of the system. Recommendations for deployers — when to defer to human judgment, when to retrain, monitoring requirements post-deployment.]

## 9. EU AI Act Article 13 transparency requirements

The instructions for use accompanying the system shall include the following items (concise, complete, correct, clear, relevant, accessible per Article 13(2)):

- [ ] Identity and contact details of the provider
- [ ] Characteristics, capabilities, and limitations of performance of the high-risk AI system
- [ ] Performance metrics specifically for groups of persons (where applicable)
- [ ] Specifications for input data
- [ ] Information enabling deployers to interpret output
- [ ] Predetermined changes to the system that have been disclosed at conformity assessment
- [ ] Human oversight measures the deployer must implement
- [ ] Computational and hardware resources needed; expected lifetime; maintenance and care measures

## 10. Logging (EU AI Act Article 12)

[Description of the automatic-logging implementation: what events are logged, log retention period, log access controls, log-based monitoring procedures. Cross-reference to the logging architecture in `SAD-XXX`.]

## 11. References

- EU AI Act 2024/1689 Article 11 — Technical documentation.
- EU AI Act 2024/1689 Article 13 — Transparency and provision of information to deployers.
- EU AI Act 2024/1689 Annex IV — Technical documentation referred to in Article 11(1).
- NIST AI RMF 1.0 — Map function.
- Mitchell et al. (2019) — Model Cards for Model Reporting. FAT* 2019.
- IMDRF/SaMD WG/N12FINAL:2014 — SaMD risk categorization (if medical).
- Linked artifacts: SIU-XXX (if medical SaMD), AIIA-XXX (AI Impact Assessment), RMF-XXX-001, SRS-XXX, SAD-XXX.

## 12. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
