# QMS maturity model — Open QMS

**Audience:** founders + operators + investors + boards reasoning about QMS scope across the startup lifecycle. Closes compliance-architecture forward-work P4's progression-rationale half at v0.61.0.

**Goal:** explain what *should* be IN the QMS at each startup stage, *why* each addition matters at that stage, *what* triggers graduation between stages, and *how* opinionated this model is (vs alternative models that exist).

For the actual bundle YAML files per stage, see [`presets/`](../../presets/). For the trust-gate framing, see [`docs/compliance-architecture.md`](../compliance-architecture.md).

---

## The four stages

| Stage | Module count | Headline |
|---|---|---|
| **pre-seed** | 3 | "Awareness + baseline IS" |
| **seed** | 7 | "First customer + first regulator" |
| **series-a** | 14 | "Formal certifications becoming material" |
| **series-b-plus** | 21 | "Multi-jurisdiction + named compliance function" |

Each stage *strictly contains* the prior stage's modules. The progression is monotonic — you don't drop modules as you grow.

---

## Funding-round labels vs compliance events

The stage labels use funding-round names because they're recognizable to founders + operators + investors. **But the actual trigger for graduating is a compliance event, not a funding round.** A self-funded company that signs its first big customer may need `seed` scope without ever raising a seed round; a heavily-funded company with no customers may stay at `pre-seed` scope for longer.

Per-stage compliance-event triggers:

| Graduate to | Trigger (any of) |
|---|---|
| **seed** | first paying customer signs · vertical commitment is made ("we're a medical-device company") · first non-founder hire |
| **series-a** | SOC 2 Type II becomes a customer requirement · 15+ employees · first formal certification pursuit (ISO 9001 / MDSAP / ISO 13485 / ISO 27001) · multi-customer pressure for similar attestations |
| **series-b-plus** | HITRUST i1 or r2 becomes a customer requirement · 50+ employees · first non-home-jurisdiction market · NIST CSF tier-3+ goal declared · energy / sustainability becomes a stakeholder ask |

---

## Why each addition matters at each stage

### pre-seed → seed (+4 modules: privacy + iso-37001 + iso-22301 + first-vertical)

The four additions reflect what changes when the first paying customer arrives:

1. **Customer data is now under your care** → `privacy` (GDPR + CCPA scope).
2. **You become someone's supplier** → `iso-37001` anti-bribery governance becomes visible.
3. **You owe service availability** → `iso-22301` BCMS (BIA + RTO/RPO discipline).
4. **You have a regulator to talk to** → vertical commitment (start with the placeholder `manufacturing`, swap for the actual vertical: `medical-devices`, `pharma`, `aerospace`, etc.).

The pre-seed substrate (risk-mgmt + IS + IMS) carries forward; nothing gets dropped.

### seed → series-a (+7 modules: SOC 2 + 27001 sub-overlays + ISO 14001/45001 + recall-workflow)

Series A is where formal certifications + multi-customer attestation requests become standing operating condition:

1. **SOC 2 Type II becomes a customer requirement** → `soc-2` + `soc-2-type-ii` sub-overlay (point-in-time vs observation-period).
2. **You're fully cloud-resident** → `iso-27001-cloud` (ISO 27017) sub-overlay.
3. **Privacy posture must be certifiable** → `iso-27001-privacy` (ISO 27701 PIMS) sub-overlay.
4. **Physical operations scale** → `iso-14001` (environmental) + `iso-45001` (OH&S).
5. **Consumer-facing product may need recall** → `recall-workflow` (cross-vertical recall framework spanning NHTSA / FDA / CPSIA / EU GPSR).

### series-a → series-b-plus (+7 modules: HITRUST + NIST CSF + ISO 37301 + ISO 50001)

Series B+ is where compliance becomes a named function with budget + the org operates across multiple jurisdictions:

1. **Compliance function formalizes** → `iso-37301` compliance management system + `iso-37301-general-business` sectoral profile.
2. **Healthcare-tech customers ask for HITRUST** → `hitrust-csf` + `hitrust-i1` (Intermediate scoping; ~182 controls).
3. **US-government-adjacent customers ask for NIST CSF mapping** → `nist-csf` + `nist-csf-tier-3` (Repeatable maturity).
4. **Sustainability + energy become stakeholder asks** → `iso-50001` energy MS.

Beyond series-b-plus the additions become organization-specific (EU regimes / US sector frameworks / cross-overlays); the preset stops being prescriptive and points adopters at [`docs/modules-catalog.md`](../modules-catalog.md).

---

## What the model is opinionated about

This is **one valid opinion**, not the only one. Specifically:

- **Privacy is at seed, not pre-seed.** Some argue privacy should be at pre-seed because data-protection by-design is a posture, not a customer-driven event. The counter is: with no customers, no employees, and no third-party data flows, privacy is a posture without a substrate. We choose to add privacy when the substrate exists.
- **SOC 2 is at series-a, not seed.** Some early-stage healthcare-tech startups pursue SOC 2 Type I at seed to break through customer-procurement. We treat SOC 2 as series-a because Type II is what customers actually want, and the observation period is meaningful only when operations are stable enough to attest.
- **HITRUST is at series-b-plus, not series-a.** HITRUST i1 is feasible at series-a for a healthcare-tech startup. We treat it as series-b-plus because of the formal-compliance-function dependency — without a named compliance team, HITRUST attestation tends to be one-shot rather than ongoing.
- **No vertical is in any preset by default.** This is deliberate — vertical commitments belong in adopter hands. The `manufacturing` placeholder in `seed` / `series-a` / `series-b-plus` is a swap-out target, not a recommendation. Adopters who skip the swap are signaling "we operate as a general manufacturer without a specific regulator," which is fine but should be a conscious choice.
- **No HIPAA in any preset.** HIPAA is healthcare-specific; layering it on top of any preset is the documented pattern. Some opinions hold HIPAA should be at series-a baseline for healthcare-tech. We treat it as adopter-layered to keep the preset industry-agnostic.

If your org disagrees with these defaults, fork the preset YAML and adjust. The preset's role is to ground the decision in an opinionated baseline, not to constrain it.

---

## Anti-patterns

### "We're pre-seed but we adopted series-b-plus from day 1 — we'll be ready when we scale"

**Why this is wrong:** controls without operations become theater. A 3-person team running 21 modules' worth of policies + SOPs + reviews spends their time on the system, not on the product. Auditors recognize the pattern; customers in regulatory diligence call it out.

**The fix:** match scope to stage. Add modules when the compliance event arrives, not before.

### "We're series-b-plus but still running seed-stage scope — we don't need all that"

**Why this is wrong:** at series-b-plus you have customers expecting certifications + regulators expecting documented processes + investors expecting compliance posture as a defensibility moat. Running seed-stage scope at series-b-plus is unauditable — and one major customer churn (or board concern) away from being a fire drill.

**The fix:** schedule the graduation. Each stage's added modules typically take 3-12 months to onboard substantively (policies + training + first audit cycle + first effectiveness check). Plan ahead.

### "We're a healthcare-tech startup, so we need HIPAA + HITRUST + SOC 2 + ISO 27001 + EU MDR all at seed"

**Why this is wrong:** without the operating substrate the certifications attest to *what*? An empty system passes certification once; an empty system fails the first surveillance audit.

**The fix:** the preset progression is a sequencing tool. Hit each compliance event as it arrives. Healthcare-tech adopters often do `seed + hipaa` rather than `seed` alone; that's a one-module addition, not a stage-skip.

### "We started at pre-seed in 2020 and never updated"

**Why this is wrong:** modules evolve. Per `BUSINESS/regulatory_review_cadence.md`, modules carry a "last reviewed by X on Y" badge; adopters who haven't refreshed the matrix in 2+ years are running stale scope.

**The fix:** `openqms regenerate --bundle presets/<your-stage>.yaml` in dry-run mode at least quarterly; if anything drifts, decide deliberately whether to accept or revert. The matrix file IS the audit trail.

---

## Vertical layering across all stages

The presets are industry-agnostic. Per-vertical layering looks similar across stages:

| Vertical | At seed swap | At series-a/b-plus add |
|---|---|---|
| Medical devices | `medical-devices` | + class overlay (`mdr-class-iib` etc.) + `hipaa` if PHI + `connected-medical-device` cross-overlay if connected + `digital-health-multi-region` cross-overlay if multi-region |
| Pharma | `pharma` | + class overlay (`pharma-clinical-stage`, `pharma-biologics`, `atmp`) + `clinical-trial-multi-region` cross-overlay if multi-region trials + `cell-therapy-supply-chain` cross-overlay if ATMP |
| Aerospace | `aerospace` | + DAL overlay (`aerospace-dal-c` etc.) + `aerospace-defense` if DoD + `defense-aerospace-cyber` cross-overlay if DoD aerospace |
| Automotive | `automotive` | + ASIL/CAL overlay (`automotive-asil-d`, `automotive-cal-4`) + `automotive-supply-chain` cross-overlay if tier-1 supplier |
| Food safety | `food-safety` | + FSMA / Codex class overlay + `food-allergen-recall` cross-overlay if multi-channel |
| Chemicals | `chemicals` | + REACH overlays + `osha-hcs` + `transport-hazmat` + `tsca-pfas` |
| Financial services | (n/a — `iso-37301-financial-services` sub-overlay swap) | + `dora` + `banking-resilience` cross-overlay |
| Utility | (n/a — start at `manufacturing` baseline + cross-overlay) | + `utility-cybersecurity` cross-overlay |

For the full module catalog see [`docs/modules-catalog.md`](../modules-catalog.md).

---

## Linkage

- [`presets/`](../../presets/) — the 4 preset bundles
- [`presets/README.md`](../../presets/README.md) — preset family index
- Per-preset READMEs:
  - [`presets/pre-seed-README.md`](../../presets/pre-seed-README.md)
  - [`presets/seed-README.md`](../../presets/seed-README.md)
  - [`presets/series-a-README.md`](../../presets/series-a-README.md)
  - [`presets/series-b-plus-README.md`](../../presets/series-b-plus-README.md)
- [`docs/compliance-architecture.md`](../compliance-architecture.md) — trust-gate framing
- [`docs/modules-catalog.md`](../modules-catalog.md) — full module catalog
- [`BUSINESS/regulatory_review_cadence.md`](../../BUSINESS/regulatory_review_cadence.md) — per-module independent review cadence
