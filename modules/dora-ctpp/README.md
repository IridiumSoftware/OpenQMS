# DORA Critical Third-Party Provider (CTPP) — Open QMS sub-overlay

Sub-overlay on the `dora` cross-cutting overlay. **CTPP designation regime** per DORA Chapter V Articles 31-44.

## Scope

ICT third-party providers designated by Commission (per ESAs joint proposal) as critical to the EU financial sector. Direct ESA Lead Overseer (EBA / ESMA / EIOPA) oversight with information-request + on-site-inspection + corrective-recommendation + penalty powers.

## Composition

`dora + dora-ctpp`. Mutually exclusive with `dora-non-ctpp` (an ICT third-party provider is either CTPP-designated or not).

## When to use

- ICT third-party providers designated CTPP by Commission
- Pre-designation preparation for providers expecting designation
- Hyperscale cloud providers + SaaS vendors with material EU financial-sector footprint

## When NOT to use

- Non-designated ICT third-party providers → `dora-non-ctpp`
- Financial entities (not their ICT providers) → `dora` baseline only
