# Automotive ASIL-C — Open QMS class overlay

Class overlay on the **automotive** vertical. Mid-high ISO 26262 functional safety level between ASIL-D and ASIL-B. Assigned for hazardous events with high (S, E, C) combinations short of ASIL-D (e.g., S3 × E4 × C2; S3 × E3 × C3; S2 × E4 × C3) per Part 3 §6 Table 4.

## Scope

Common for high-rigor production functions that fall below ASIL-D-only items.

## Standards covered

- ISO 26262:2018

5 clauses encoding rigor delta:

| Element | ASIL-C specifics |
|---|---|
| Hardware metrics | **SPFM ≥ 97%** + **LFM ≥ 80%** + **PMHF < 10⁻⁷/h** |
| Software structural coverage | **100% statement + 100% branch** (MC/DC recommended — major delta from ASIL-D which mandates) |
| Confirmation measures | **I3 independence** (same as ASIL-D — the major confirmation-measures cost-jump from ASIL-B's I2) |
| SW methods | Language subset **REQUIRED** (MISRA C 2012 mandatory + required); defensive programming + restricted pointers + restricted dynamic memory required |

## Composition

```bash
openqms validate --module automotive --module automotive-asil-c
```

## When to use

HARA yields ASIL-C per Part 3 §6 Table 4. Note: the I3 independence requirement is often the underappreciated cost-jump between ASIL-B and ASIL-C — projects sometimes prefer to either upgrade to ASIL-C cleanly or use Part 9 §5 decomposition to keep elements at ASIL-B.

## When NOT to use

Lower (S, E, C) → ASIL-B/A/QM; higher (S3×E4×C3) → ASIL-D.

## Standards licensing

ISO 26262:2018 commercial.

## Forward work

- ASIL-C Safety Case template
- Part 9 §5 decomposition template (C = B(C) + A(C), etc.)
