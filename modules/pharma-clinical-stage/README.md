# pharma-clinical-stage — Open QMS class overlay

Class overlay on the **pharma** vertical. Encodes the staged-expectations framework distinct from full commercial manufacturing. Clinical-stage organizations operate under FDA + EMA + MHRA frameworks where full commercial cGMP is applied progressively as the program advances Phase 1 → Phase 2 → Phase 3 → BLA/NDA.

## Scope

Pre-commercial pharma organizations — investigational programs in clinical development. Often composed with pharma-imp overlay for IMP-specific manufacturing scope.

## Standards covered

PUBLIC license:

- 21 CFR 312 (informed by FDA Guidance for Industry "CGMP for Phase 1 Investigational Drugs" July 2008)
- EU GMP Annex 13
- ICH Q10

5 clauses:

| Element | Specifics |
|---|---|
| Phase 1 cGMP flexibility | FDA enforcement discretion per 2008 Guidance; written procedures + adequate facilities + qualified personnel + raw material controls + finished product testing required, but full 21 CFR 210/211 rigor relaxed |
| Phase 2/3 ramp-up | Phase-appropriate expansion toward full cGMP; process validation Stage 1 typically in Phase 2; Stage 2 typically Phase 3 → BLA/NDA |
| Evolving specifications | Analytical methods + process knowledge mature across phases; change-control accommodates evolution while maintaining safety + regulatory integrity |
| Clinical supply forecasting | Small-batch manufacturing + JIT logistics + cold chain + study-site distribution; stock-out mid-study is serious operational risk |
| Pre-commercial readiness | Site Master File + VMP + commercial-scale validation + commercial Quality Manual ready for PAI (Pre-Approval Inspection) at NDA/BLA |

## Composition

```bash
# Typical: clinical-stage + IMP overlay
openqms validate --module pharma --module pharma-clinical-stage --module pharma-imp

# For biologics in clinical development
openqms validate --module pharma --module pharma-clinical-stage --module pharma-imp --module pharma-biologics

# For ATMP in clinical development (CAR-T, AAV)
openqms validate --module pharma --module pharma-clinical-stage --module pharma-imp --module atmp
```

## When to use

Pre-commercial pharma — any program in clinical development (Phase 1-3) where full commercial cGMP is not yet appropriate. Particularly load-bearing for startup + clinical-stage biotech organizations transitioning toward commercial readiness.

## When NOT to use

Commercial manufacturing (use pharma without this overlay). Marketed drug products + biologics post-approval.

## Standards licensing

PUBLIC license.

## Forward work

- Phase-specific sub-overlays (Phase 1 / Phase 2 / Phase 3 with specific cGMP expectations per phase)
- Pre-Approval Inspection (PAI) readiness checklist template
- BLA / NDA filing preparation workflow template
