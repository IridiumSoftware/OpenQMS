# Automotive CAL-3 — Open QMS class overlay

Class overlay on the **automotive** vertical. Mid-high ISO/SAE 21434 Cybersecurity Assurance Level. Assigned when TARA identifies mid-high impact-and-feasibility combinations.

## Scope

TARA per Annex E yields CAL-3 for damage scenarios with moderate-to-high impact + moderate-to-high feasibility (between CAL-2's lower tier and CAL-4's highest tier).

## Standards covered

- ISO/SAE 21434:2021

5 clauses:

| Element | CAL-3 specifics |
|---|---|
| Independent cybersecurity assessment | **RECOMMENDED** (vs. required at CAL-4, optional at CAL-2) |
| V&V (§10 + §13) | Baseline functional + vulnerability scanning + **fuzz testing required** (pentest recommended; side-channel NOT required vs. required-where-applicable at CAL-4) |
| Continuous monitoring (§11) | Formal vulnerability monitoring with **response-time commitments** documented in CSMS + defined incident-response playbooks (rehearsal recommended; CAL-4 requires rehearsal) |
| Safety-security interaction | When item is also ASIL-rated (typically ASIL-B or ASIL-C at CAL-3 level) |

## Composition

```bash
openqms validate --module automotive --module automotive-cal-3
```

## When to use

TARA yields CAL-3.

## When NOT to use

Higher/lower TARA outcomes → CAL-4 or CAL-2/1.

## Standards licensing

ISO/SAE 21434:2021 commercial.

## Forward work

- CAL-3 Cybersecurity Case template
