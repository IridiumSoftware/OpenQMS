# DORA TLPT (Threat-Led Penetration Testing) — Open QMS sub-overlay

Sub-overlay on the `dora` cross-cutting overlay. **Threat-Led Penetration Testing regime** per DORA Chapter IV Articles 26-27 operationalised via TIBER-EU framework.

## Scope

Significant financial entities meeting materiality thresholds (G-SIIs, O-SIIs, central securities depositories, central counterparties, large credit institutions, major payment + e-money institutions, key investment firms, large insurance undertakings).

## Composition

`dora + dora-tlpt` (financial entity perspective). May also compose `dora + dora-ctpp + dora-tlpt` for CTPPs whose services are in scope of multiple financial entities' TLPT exercises (pooled testing per Article 26(4)).

## When to use

- Significant financial entity meeting Article 26 materiality threshold
- Pre-TLPT preparation for entities approaching threshold
- ICT third-party providers serving in-scope financial entities (procurement preparation)

## TIBER-EU phases

Preparation (Generic Threat Landscape) → Testing (Targeted Threat Intelligence + Red Team Test) → Closure (Replay + Purple Team + Test Summary Report) → Remediation (Plan + follow-up). Test Manager internal; TI Provider + Red Team Provider external + accredited per ESAs RTS.
