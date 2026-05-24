# dora — Open QMS cross-cutting overlay

EU Digital Operational Resilience Act (Regulation (EU) 2022/2554) overlay. Effective January 17, 2025. Composes with any vertical.

## Scope

EU financial entities + their ICT third-party service providers (CTPPs). Financial entities = credit institutions + investment firms + insurance + crypto-asset service providers + market infrastructures + central counterparties + etc.

## Standards covered

PUBLIC license:

- EU DORA — Regulation (EU) 2022/2554

6 clauses across DORA's 6 chapters:

| Chapter | Topic | Specifics |
|---|---|---|
| II (Art. 5-16) | ICT risk management framework | Governance + ICT asset criticality + protection + detection + response + recovery |
| III (Art. 17-23) | Incident reporting | Classification by common criteria; **major incident reporting: 4h initial / 72h intermediate / 1mo final** to competent authorities |
| IV (Art. 24-27) | Resilience testing | Regular testing per risk profile; **TLPT every 3 years for significant ICT providers** (TIBER-EU framework) |
| V (Art. 28-44) | Third-party risk | Register; due diligence; CTPP designation; concentration risk; **Article 30 contractual** mandatory clauses |
| VI (Art. 45) | Information sharing | Trusted communities; IOC/TTP/alert/configuration sharing |
| Art. 30 | Contractual provisions | Service description + locations + data processing + security + access + termination + audit + sub-outsourcing |

## Composition

```bash
openqms validate --module <vertical> --module dora
# Typical financial-services composition:
openqms validate --module manufacturing --module dora --module iso-27001 --module iso-22301
# (manufacturing as "general organization" baseline; DORA + IS + BCMS)
```

## When to use

EU financial entities in DORA scope; ICT third-party providers serving EU financial customers; designated Critical Third-Party Providers (CTPPs).

## When NOT to use

Non-EU + non-financial organizations (though some adopters use DORA as a maturity reference even outside formal scope).

## Standards licensing

PUBLIC (EUR-Lex).

## Forward work

- TIBER-EU TLPT framework standalone overlay
- Article 30 contractual addendum template
- CTPP designation readiness checklist
- ESAs Joint Implementing + Regulatory Technical Standards (ITS/RTS) cross-references
