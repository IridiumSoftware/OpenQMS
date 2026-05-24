# SOC 2 Type I — Open QMS sub-overlay

Sub-overlay on the `soc-2` cross-cutting overlay. **SOC 2 Type I** — point-in-time design assessment per AICPA AT-C 105 + 205.

## Scope

Independent CPA firm attests to **suitability of design** of controls AS OF A SPECIFIED DATE. NO testing of operating effectiveness.

## Standards covered

4 clauses across Type I framework + readiness pathway + customer-acceptance reality.

## Composition

`soc-2 + soc-2-type-i`. Mutually exclusive with `soc-2-type-ii` for any single attestation period (a SOC 2 examination is EITHER Type I OR Type II per AT-C 205, not both simultaneously).

## When to use

- First-year SOC 2 attestation following readiness assessment + gap remediation
- Lighter-weight customer requirement (some procurement teams accept Type I)
- SaaS startup needing rapid time-to-first-attestation
- Pre-Type-II evidence to defer customer requirement temporarily

## When NOT to use

- Enterprise customer procurement gating on Type II (most common reality)
- Renewal / continuous attestation cycle (Type II is the steady-state)
- Regulatory requirements specifying operating-effectiveness evidence (rare in pure SOC 2 context)

## Customer-acceptance reality

Many enterprise customers + procurement teams REJECT Type I as insufficient evidence of security maturity. Verify customer acceptance criteria before committing to Type-I-only attestation.
