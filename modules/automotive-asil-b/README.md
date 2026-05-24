# Automotive ASIL-B — Open QMS class overlay

Class overlay on the **automotive** vertical. Mid-tier ISO 26262 functional safety level. Common for production ECUs implementing non-life-critical but safety-relevant functions.

## Scope

HARA at (S2 × E4 × C2; S3 × E3 × C1; S2 × E3 × C3) per Part 3 §6 Table 4 typically yields ASIL-B.

## Standards covered

- ISO 26262:2018

5 clauses encoding rigor delta:

| Element | ASIL-B specifics |
|---|---|
| Hardware metrics | **SPFM ≥ 90%** + **LFM ≥ 60%** + **PMHF < 10⁻⁷/h** |
| Software structural coverage | **100% statement + 100% branch** (MC/DC recommended but NOT required — major delta from ASIL-D) |
| Confirmation measures | **I2 independence** (different team within the same organizational unit — less stringent than ASIL-C's I3 minimum) |
| SW methods | MISRA C 2012 recommended (not mandatory — delta from ASIL-C) |

## Composition

```bash
openqms validate --module automotive --module automotive-asil-b
```

## When to use

HARA yields ASIL-B per Part 3 §6 Table 4. Often the practical sweet-spot for production ECUs — sufficient FuSa rigor without ASIL-C's I3 independence cost.

## When NOT to use

Higher (S, E, C) → ASIL-C/D; lower → ASIL-A or QM.

## Standards licensing

ISO 26262:2018 commercial.

## Forward work

- ASIL-B Safety Case template
