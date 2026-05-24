# Automotive CAL-2 — Open QMS class overlay

Class overlay on the **automotive** vertical. Mid-low ISO/SAE 21434 Cybersecurity Assurance Level.

## Scope

TARA per Annex E yields CAL-2 for damage scenarios with moderate-impact / low-feasibility or low-impact / moderate-feasibility combinations.

## Standards covered

- ISO/SAE 21434:2021

4 clauses:

| Element | CAL-2 specifics |
|---|---|
| Independent cybersecurity assessment | **OPTIONAL** (adopter CSMS decides when to invoke) |
| V&V (§10 + §13) | Baseline security functional testing + **vulnerability scanning** of dependencies + exposed interfaces (fuzz + pentest recommended but not required) |
| Continuous monitoring (§11) | Vulnerability monitoring with **documented triage cadence** (e.g., "all new CVEs affecting BoM triaged within N business days") — no formal response-time commitments for fix deployment |

## Composition

```bash
openqms validate --module automotive --module automotive-cal-2
```

## When to use

TARA yields CAL-2.

## When NOT to use

Higher/lower TARA outcomes.

## Standards licensing

ISO/SAE 21434:2021 commercial.

## Forward work

- CAL-2 Cybersecurity Case template
