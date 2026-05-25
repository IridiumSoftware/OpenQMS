# US State Privacy Umbrella — Open QMS cross-cutting overlay

26th Open QMS cross-cutting overlay. **US state comprehensive privacy laws** using the VCDPA template family — single overlay covering 14+ states with state-divergence handling.

## Scope

As of 2026-05-25, comprehensive state privacy laws in effect or enacted in:
- **California** — covered by `privacy` overlay (CCPA/CPRA)
- **Virginia VCDPA** (effective 2023-01-01) — template state
- **Colorado CPA** (2023-07-01)
- **Connecticut CTDPA** (2023-07-01)
- **Utah UCPA** (2023-12-31)
- **Texas TDPSA** (2024-07-01)
- **Oregon OCPA** (2024-07-01)
- **Montana MCDPA** (2024-10-01)
- **Iowa ICDPA** (2025-01-01)
- **Delaware DPDPA** (2025-01-01)
- **New Hampshire NHPA** (2025-01-01)
- **New Jersey NJDPA** (2025-01-15)
- **Tennessee TIPA** (2025-07-01)
- **Minnesota MCDPA** (2025-07-31)
- **Maryland MODPA** (2025-10-01) — **STRICTER variant**
- **Indiana INCDPA** (2026-01-01)
- **Florida FDBR** (2024-07-01) — **NARROW scope** (only ≥$1B online ad revenue entities)

## Standards covered

10 clauses across the common VCDPA template + state-divergence handling. Single registry standard: "US State Privacy Laws" covering all named state codes.

## Composition

Most natural: `privacy + us-state-privacy` — privacy covers GDPR + CCPA (California); us-state-privacy covers the other ~14 states. Most US digital operators need both.

Often also composes with: `hipaa` (if PHI also processed), `iso-27001 + iso-27001-privacy` (ISMS + PIMS certification), `hitrust-csf + hitrust-r2` (validated multi-framework attestation including state privacy mapping).

## Templates introduced

2 new templates + 2 extensions to existing privacy templates:

1. **`US-STATE-PRIVACY-MATRIX-TEMPLATE.md`** — state-by-state divergence tracker. Per-state: applicability thresholds (revenue + consumer count + % from sale), cure periods (30-day-sunset vs persistent), UOOM recognition (GPC mandatory vs optional), sensitive data scope, Maryland MODPA stricter posture, Florida FDBR narrow scope, response deadlines, penalty caps.
2. **`DATA-PROTECTION-ASSESSMENT-TEMPLATE.md`** — state-level DPA (parallel to GDPR DPIA). Heightened-risk processing identification (targeted advertising / sale of personal data / sensitive data / profiling / children's data) + safeguard assessment + risk-benefit balance.
3. **PRIVACY-POLICY** extension — state-by-state addendum with per-state controller-contact + consumer-rights summary + UOOM honoring statement + appeal procedure.
4. **DPA** extension — controller-processor contractual requirements per VCDPA-template states.

## Critical divergences from VCDPA template

- **Maryland MODPA (effective 2025-10-01)** — DATA MINIMIZATION strict-necessity standard for sensitive data; banned sale of sensitive data; banned targeted advertising to <18; narrower GLBA exception; up to $10k/$25k penalties.
- **Florida FDBR** — narrow scope; effectively only big-tech entities (Google + Meta + Amazon + Apple).
- **Texas TDPSA** — cure period does NOT sunset (most states' cure periods sunset after 2-4 years).
- **UOOM divergence** — mandatory in 8 states (Colorado + Connecticut + Texas + Oregon + Montana + Delaware + New Jersey + Minnesota); optional in 6 (Virginia + Utah + Iowa + Tennessee + Indiana + New Hampshire).

## When to use

- Any US digital operator with consumer base outside California
- Multi-state SaaS / e-commerce / consumer-tech
- Maryland-customer operators (MODPA strictness requires specific posture)
- Pre-compliance scoping for new state law effective dates

## When NOT to use

- California-only operators → `privacy` (CCPA/CPRA) alone sufficient
- Non-US operators with no US consumer base → `privacy` (GDPR scope) alone

## Forward work

- Per-state appeal procedure templates
- Universal Opt-Out Signal handling SOP (GPC + IAB GPP + DAA AppChoices)
- Maryland MODPA-specific data minimization assessment
- Florida FDBR threshold determination workflow
- State-AG complaint response template
- Washington My Health My Data Act (MHMDA) — distinct from comprehensive privacy; consumer health data only; standalone overlay forward work
