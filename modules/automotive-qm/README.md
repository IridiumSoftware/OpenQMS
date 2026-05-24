# Automotive QM — Open QMS class overlay

Class overlay on the **automotive** vertical. Encodes the **Quality Management** classification per ISO 26262 — applies when HARA's (S, E, C) combination yields QM (e.g., S1 × E4 × C1, S0 × any × any, S2 × E1 × any) per Part 3 §6 Table 4.

## Why this exists as a separate overlay

The QM allocation is a **positive safety claim** that the function does NOT require ISO 26262 process discipline beyond baseline IATF 16949 quality management — it is NOT an absence of analysis. Adopters need a place to document the QM rationale that traces from HARA through to the absence-of-FuSa-rigor decision. Auditability requires that QM-classified items be explicitly listed (not silently omitted).

## Standards covered

- ISO 26262:2018

4 clauses:

| Element | QM specifics |
|---|---|
| QM applicability gate | From HARA per Part 3 §6 Table 4 — explicit (S, E, C) reference |
| NO ISO 26262-specific rigor | Per Part 2 §5.4.1 — baseline IATF 16949 + ISO 9001 process discipline applies (already in automotive vertical) |
| HARA rationale is load-bearing | Mis-classification as QM when true classification is ASIL-A+ omits required FuSa rigor — confirmation reviewer / FuSa auditor must be able to verify HARA accuracy |
| Safety Plan listing | QM items explicitly listed as out-of-FuSa-scope with HARA cross-reference enabling reviewer / auditor verification (not silent omission) |

## Composition

```bash
openqms validate --module automotive --module automotive-qm
```

## When to use

When HARA classifies an item as QM AND you want auditability of the positive claim. Failure to use this overlay means QM items don't appear in the FuSa scope documentation, which an auditor will flag as a gap.

## When NOT to use

If any item warrants ASIL-A or higher, use the corresponding ASIL overlay instead. QM only.

## Standards licensing

ISO 26262:2018 commercial.

## Forward work

- QM Safety Plan listing template with HARA cross-reference structure
