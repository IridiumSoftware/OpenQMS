# iso-31000 — Open QMS cross-cutting overlay

ISO 31000:2018 risk management framework overlay. **The meta-framework** — composes with any vertical and unifies the many domain-specific risk frameworks already in Open QMS (ICH Q9 pharma, HARA auto FuSa, TARA auto cyber, FHA aero, HACCP food, ISO 27001 §6.1 IS risk, ISO 14001 §6.1 environmental risk).

## Scope

Risk management as a CROSS-CUTTING organizational discipline. Distinct from but complementary to domain-specific risk standards.

## Standards covered

Commercial license (ISO):

- ISO 31000:2018 (Risk management — Guidelines)

4 clauses across the framework's 3-part structure (Principles + Framework + Process):

| Element | ISO 31000 §§ | Topic |
|---|---|---|
| 8 Principles | §4 | Integrated + structured + customized + inclusive + dynamic + best-information + human factors + continual improvement |
| Framework | §5 | Leadership + commitment + integration into governance + design + implementation + evaluation + improvement OF THE FRAMEWORK |
| Process | §6 | Communication + scope/context/criteria + risk assessment (ID + analysis + evaluation) + treatment + monitoring/review + recording/reporting — the OPERATIONAL execution |
| Integration | §5.2 | Risk management integrated into ALL organizational activities; not a separate function |

## Composition

```bash
openqms validate --module <vertical> --module iso-31000
```

The v0.25.0 RISK-ASSESSMENT-TEMPLATE + RISK-AND-OPPORTUNITY-REGISTER-TEMPLATE both reference ISO 31000 + ISO 31010 — this overlay formalizes their binding.

## When to use

Organizations seeking a unified risk-management framework spanning all risk dimensions. Particularly relevant where multiple domain-specific risk standards apply (a pharma + ATMP organization may have ICH Q9 + Q5A viral safety + cybersecurity TARA + HIRA OH&S + ISO 27001 risk + ISO 22301 BCMS risk + ISO 14001 environmental risk; ISO 31000 unifies the meta-process).

## When NOT to use

Organizations with a single dominant risk framework that's sufficient on its own.

## Standards licensing

ISO 31000 commercial. ISO 31010 (Risk Assessment Techniques, complementary) commercial.

## Forward work

- ISO 31010 risk-assessment-technique catalog overlay (FMEA / FTA / HAZOP / What-If / bow-tie / fault tree / Monte Carlo / etc.)
- ISO Guide 73 risk terminology cross-reference
- Enterprise Risk Management (COSO ERM) sibling overlay
