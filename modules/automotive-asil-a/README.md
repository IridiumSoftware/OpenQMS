# Automotive ASIL-A — Open QMS class overlay

Class overlay on the **automotive** vertical. Lowest non-QM ASIL tier. Common for non-life-critical but safety-relevant functions.

## Scope

HARA at S1 × E4 × C3, S2 × E2 × C3, S2 × E3 × C2 (or other combinations yielding ASIL-A per Part 3 §6 Table 4). Note: S1 × E4 × C1 → QM, not ASIL-A — both significant exposure AND significant uncontrollability are required for ASIL-A allocation.

## Standards covered

- ISO 26262:2018

5 clauses encoding the lightest-rigor non-QM tier:

| Element | ASIL-A specifics |
|---|---|
| Hardware metrics | **PMHF < 10⁻⁶/h** — NO quantitative SPFM/LFM targets required |
| Software structural coverage | **100% statement only** (branch + MC/DC recommended; major delta from ASIL-B which mandates branch) |
| Confirmation measures | **I1 independence** (different person within the same team — lightest tier short of QM) |
| SW methods | Language subset (MISRA C 2012 mandatory) + defensive programming + restricted pointers — all RECOMMENDED (not required) |

## Composition

```bash
openqms validate --module automotive --module automotive-asil-a
```

## When to use

HARA yields ASIL-A.

## When NOT to use

If the (S, E, C) combination yields QM, no FuSa rigor required (use `automotive-qm` to document the positive QM allocation). Higher (S, E, C) → ASIL-B/C/D.

## Standards licensing

ISO 26262:2018 commercial.

## Forward work

- ASIL-A Safety Case template
