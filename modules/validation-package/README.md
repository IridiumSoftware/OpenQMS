# Open QMS — validation-package baseline overlay module

Risk-based **computerized-system validation** for production / quality-management-system software. This is the **market-neutral baseline** of the P2 validation family; two market overlays refine it:

- `validation-package-fda` — FDA **Computer Software Assurance (CSA)** framework + 21 CFR Part 11 + Part 820/QMSR *(P2.2)*
- `validation-package-eu` — EU GMP **Annex 11** + **Annex 15** + ISO 13485 *(P2.3)*

## The model

It is **not "CSV vs CSA."** CSA (and GAMP 5 2nd ed.) define one **risk-based spectrum**; classic **CSV — robust scripted IQ/OQ/PQ — is the highest assurance tier**, applied to high-risk functions. The rigor is a **per-function determination output**, recorded in the Assurance Determination — not a choice of module.

| Dial | What | Where |
|---|---|---|
| **Rigor** | assurance tier per feature/function (scripted-robust / -limited / unscripted-scenario / -exploratory) | the Assurance Determination (data) |
| **Market** | which predicate rules apply (FDA CSA vs EU Annex 11) | which overlay you compose |

## Clauses (v0.1.0)

11 baseline clauses across GAMP 5 (2nd ed.), ISO 13485:2016 (§4.1.6 / §7.5.6 / §7.6 / §4.2.5), and IEC/IEEE/ISO 29119-1:2022 — covering inventory, intended-use classification, GAMP categorization, risk determination, assurance activities, URS, VMP, the assurance record, change/revalidation, and periodic review.

## Templates

`templates/qms-validation/` — System Inventory, **Assurance Determination** (the per-function risk decision; FDA's 5-column format, authored as a P15 Tier-2 trace table), tier-aware **Assurance Record** (§V.A.6 field set), URS, Validation Master Plan, Change Assessment.

## Honesty bound (OQ-080)

The module ships the *framework + determination + tier-aware record + traceability*. It records the risk decision and proves the artifact set matches the declared tier; it does **not** decide whether a function is high-risk, nor prove a validated system is fit for use — those remain adopter QA judgment.

See `BUSINESS/companion_p2_validation_package.md` for the full design.
