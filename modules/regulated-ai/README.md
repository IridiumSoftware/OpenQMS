# Regulated-AI cross-cutting overlay

Adds AI/ML-system requirements to any vertical regulatory module. AI regulation is cross-cutting because it composes with sector-specific regulation — medical-devices use ISO 13485 + IVDR/MDR + this overlay; financial AI would use SEC/FINRA + this overlay; employment-decision AI would use EEOC + this overlay.

Use via:

```bash
# Medical-AI SaMD with full AI governance
openqms resolve \
  --module medical-devices \
  --module samd \
  --module regulated-ai \
  --standard "NIST AI RMF 1.0" \
  --standard "EU AI Act" \
  --standard "ISO/IEC 42001:2023" \
  ...

# Medical-AI IVD (e.g. AI/ML diagnostic algorithm)
openqms resolve \
  --module medical-devices \
  --module ivd \
  --module regulated-ai \
  ...
```

## What this overlay adds

### NIST AI Risk Management Framework (1.0)
Four functions covered as separate clauses:
- **Govern** — culture, policies, roles, accountability, diversity, third-party AI governance.
- **Map** — context-setting; categorize the AI system, identify stakeholders, characterize impacts.
- **Measure** — quantitative/qualitative/mixed-method assessment of trustworthy characteristics (validity, reliability, safety, security, accountability, transparency, explainability, privacy, fairness).
- **Manage** — prioritize and respond to risks based on Measure outputs.

### EU AI Act 2024/1689 (Chapter III §2 high-risk AI requirements)
Articles 9-15 as separate clauses:
- **Art 9** — Risk management system for high-risk AI (lifecycle-iterative).
- **Art 10** — Data and data governance (datasets relevant, representative, error-free, bias-examined).
- **Art 11** — Technical documentation (per Annex IV).
- **Art 12** — Record-keeping / automatic logging.
- **Art 13** — Transparency and provision of information to deployers.
- **Art 14** — Human oversight.
- **Art 15** — Accuracy, robustness, cybersecurity.

### ISO/IEC 42001:2023 — AI Management System
Consolidated AIMS clause covering the management-system clauses §4-§10 (parallel structure to ISO 9001 / 13485). Composes with existing sector QMS as the AI-management overlay.

### ISO/IEC 23894:2023 — AI Risk Management Guidance
Extends ISO 31000 with AI-specific risk considerations. For medical-AI, composes with ISO 14971 — the RMF binding in this overlay folds AI risks into the existing risk-management file.

## New templates (2)

- **AI System Card / Model Card** (`templates/product-dhf/ai-system-card/`) — transparency documentation per EU AI Act Article 11 + Article 13 + NIST AI RMF Map. The model card is the public-facing summary of model capabilities, intended use, training data, evaluation results, and limitations.
- **AI Impact Assessment** (`templates/product-dhf/ai-impact-assessment/`) — EU AI Act Article 9 risk management process + NIST AI RMF Govern/Measure/Manage. Mandatory for high-risk AI per EU AI Act.

## Existing template bindings extended

- **Risk Management File** (RMF) — gains ISO 23894 AI risk management binding. AI-specific risks (data quality, model robustness, fairness, explainability) compose with the existing ISO 14971 risk management.
- **Quality Policy** — gains ISO/IEC 42001 AI management system binding (the AIMS sits on top of the existing QMS).
- **Software Architecture** — gains EU AI Act Article 15 (accuracy / robustness / cybersecurity) binding.
- **Software Test Protocol** — gains EU AI Act Article 10 (data governance — training/validation/test datasets) binding.
- **Technical File Index** — gains EU AI Act Article 12 (automatic logging) binding.

## EU AI Act risk categories

The EU AI Act categorizes AI systems by risk:
- **Prohibited** (Article 5) — practices contrary to EU values (e.g. social scoring by public authorities).
- **High-risk** (Article 6 + Annex III) — most safety-relevant AI; this overlay's clauses primarily target high-risk AI requirements.
- **Limited-risk** (Articles 50-52) — transparency obligations (e.g. AI-generated content disclosure).
- **Minimal-risk** — most other AI; no specific obligations beyond general law.

This overlay's clauses assume high-risk AI scope. Adopters of limited-risk or minimal-risk AI scope a subset; the overlay's clauses then declare NA where not applicable.

## Sector composition notes

- **Medical AI** — compose with medical-devices + (samd or ivd as applicable) + (class overlay). Medical-AI is typically high-risk under the EU AI Act per Annex III §5 (safety-relevant medical devices) plus already-high under MDR/IVDR; the requirements stack.
- **Future fintech AI** — would compose with a future `financial-services` vertical module (not yet shipped). EU AI Act covers credit scoring as high-risk per Annex III §5(b).
- **Future employment AI** — would compose with a future `employment-decisions` module. EU AI Act Annex III §4 covers AI for recruitment, promotion, termination.
