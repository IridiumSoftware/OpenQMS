# SOC 2 Type II — Open QMS sub-overlay

Sub-overlay on the `soc-2` cross-cutting overlay. **SOC 2 Type II** — observation-period operating-effectiveness assessment per AICPA AT-C 105 + 205.

## Scope

Independent CPA firm attests to BOTH design suitability AND operating effectiveness of controls **over an observation period** (typically 6 months first-time, 12 months annual renewal).

## Standards covered

5 clauses across Type II framework + observation period + renewal cadence + enterprise customer default + control-failure handling.

## Composition

`soc-2 + soc-2-type-ii`. Mutually exclusive with `soc-2-type-i` for any single attestation period.

## When to use

- Enterprise customer procurement requirement (default expectation)
- Steady-state annual SOC 2 renewal
- Second-year+ following Type I → Type II progression
- B2B SaaS with material customer base requiring vendor security attestation

## When NOT to use

- Pre-readiness state (do gap assessment + Type I first)
- Very-small SaaS with no enterprise customer pressure (Type I may suffice)
- Adopters cannot commit to a continuous 6+ month observation window

## Operational notes

- **Observation window:** minimum 3 months; 6 months typical first; 12 months typical annual renewal
- **Renewal cadence:** annual; common windows 11/1-10/31 or 10/1-9/30 (fiscal year)
- **Bridge letter:** auditor optionally issues "gap letter" covering observation-period-end → next-report-availability period (no-material-change-occurred attestation)
- **Modified opinions:** qualified / adverse / disclaimer outcomes possible; target unqualified
