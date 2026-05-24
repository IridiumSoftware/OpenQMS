# pharma-imp — Open QMS class overlay

Class overlay on the **pharma** vertical. Adds Investigational Medicinal Product (IMP) requirements for drugs in clinical trials (Phase 1-3, pre-marketing-authorisation).

## Scope

IMP GMP is distinct from commercial GMP:
- Process is less mature; specifications evolve with development
- Smaller batches (clinical-supply scale, not commercial scale)
- Blinding + randomization required for placebo-controlled studies
- Sponsor responsibility model (not commercial MA-holder)
- Reduced regulatory submission burden vs. commercial NDA/MAA

## Standards covered

PUBLIC license:

- EU GMP Annex 13 (Manufacture of Investigational Medicinal Products)
- 21 CFR 312 (Investigational New Drug Application)

5 clauses:

| Element | Specifics |
|---|---|
| Annex 13 QA | Sponsor responsibility + IMPMA + evolving specs + blinding handling + returns/destruction |
| Annex 13 blinding | Packaging + labelling supports blinding; randomization codes + emergency unblinding |
| Annex 13 QP certification | IMP-specific (different from commercial); per IMPD + GMP + trial arrangements |
| 21 CFR 312 Phase 1 cGMP | FDA enforcement discretion per "CGMP for Phase 1 Investigational Drugs" Guidance (2008); phase-appropriate ramp-up Phase 2/3 |
| 21 CFR 312.30 | Protocol amendments + IND safety reports + annual reports; manufacturing changes affecting safety require IND amendment |

## Composition

```bash
openqms validate --module pharma --module pharma-imp
# Often combined with clinical-stage flexibility:
openqms validate --module pharma --module pharma-imp --module pharma-clinical-stage
# For ATMP IMPs:
openqms validate --module pharma --module pharma-imp --module atmp
```

## When to use

Manufacturing investigational drugs for clinical trials (Phase 1-3) — pre-commercial. Sponsor + IND holder + IMPMA holder organizations.

## When NOT to use

Commercial manufacturing (use pharma alone). Non-clinical research-grade material (not GMP scope).

## Standards licensing

PUBLIC license.

## Forward work

- Phase-specific class overlays (Phase 1 vs. Phase 2 vs. Phase 3 — different rigor expectations per FDA staged approach)
- Clinical-supply forecasting + just-in-time manufacturing workflow
- IMP-specific stability protocol (often shorter shelf-life + study-duration scope)
