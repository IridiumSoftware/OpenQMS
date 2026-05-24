# Automotive CAL-1 — Open QMS class overlay

Class overlay on the **automotive** vertical. **Lowest** ISO/SAE 21434 Cybersecurity Assurance Level.

## Scope

TARA per Annex E yields CAL-1 for damage scenarios with **low impact AND low feasibility**.

## Standards covered

- ISO/SAE 21434:2021

4 clauses:

| Element | CAL-1 specifics |
|---|---|
| Independent cybersecurity assessment | **NOT required** — cybersecurity case + final assessment may be performed by the development team |
| V&V (§10 + §13) | Baseline security functional testing only — NO fuzz / pentest / side-channel |
| Continuous monitoring (§11) | CSMS-baseline vulnerability monitoring — no response-time commitments specific to CAL-1 |
| Safety-security interaction | Not formally required at CAL-1 (the item is unlikely to be ASIL-rated if cyber-rated CAL-1) |

## Composition

```bash
openqms validate --module automotive --module automotive-cal-1
```

## When to use

TARA yields CAL-1 (low impact AND low feasibility).

## When NOT to use

Higher TARA outcomes → CAL-2/3/4.

## Standards licensing

ISO/SAE 21434:2021 commercial.

## Forward work

- CAL-1 minimal Cybersecurity Case template
