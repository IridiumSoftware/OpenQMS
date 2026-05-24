# Automotive ASIL-D — Open QMS class overlay

Class overlay on the **automotive** vertical. ASIL-D is the highest ISO 26262 functional safety level, assigned when HARA classifies a hazardous event at the most stringent combination (S3 × E4 × C3) per Part 3 §6 Table 4.

## Scope

Examples of ASIL-D functions: brake-by-wire torque control, steering-by-wire angle control, airbag deployment, BMS battery-fault response.

## Standards covered

- ISO 26262:2018 (all relevant parts)

6 clauses encoding the highest-rigor deltas:

| Element | ASIL-D specifics |
|---|---|
| Hardware metrics (Part 5 §8-9 + Annex F) | **SPFM ≥ 99%** + **LFM ≥ 90%** + **PMHF < 10⁻⁸/h** |
| Software structural coverage (Part 6 Tables 12-15) | **100% statement + 100% branch + 100% MC/DC** unit-test; 100% function + 100% function-call at integration |
| Confirmation measures (Part 2 §6 Table 1) | **I3 independence** (different organizational unit minimum) for confirmation review + FuSa audit + FuSa assessment |
| SW methods (Part 6 Tables 1-3) | Formal notations + strongly-typed languages strongly recommended; **MISRA C 2012 mandatory rules required**; defensive programming + restricted pointers + restricted recursion + restricted dynamic memory |
| ASIL decomposition (Part 9 §5; optional) | D = C(D)+A(D), B(D)+B(D), D+QM(D) with dependent-failure-analysis support |

## Composition

```bash
openqms validate --module automotive --module automotive-asil-d
# Realistic top-rigor: + automotive-cal-4 + regulated-ai + iso-27001
```

## When to use

HARA at S3×E4×C3 yields ASIL-D allocation per Part 3 §6 Table 4. Mandatory for items whose failure could cause life-threatening or fatal injuries with high exposure and uncontrollability.

## When NOT to use

Lower (S, E, C) combinations yield ASIL-C/B/A/QM — use the corresponding overlay. ASIL decomposition per Part 9 §5 may reduce on individual elements.

## Standards licensing

ISO 26262:2018 commercial (ISO / national member bodies).

## Forward work

- ASIL-D-specific Safety Case template integrating Part 2 confirmation review evidence
- HW-metrics calculation template (SPFM/LFM/PMHF per FMEDA)
- MC/DC coverage reporting harness
