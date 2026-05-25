# series-b-plus preset

**Stage assumptions:** 50-200+ people, multi-jurisdiction operations, regulator-engaged, formal compliance function exists as a named org unit, multiple formal certifications maintained in parallel.

**Module count:** 21 — `series-a (14)` + `hitrust-csf` + `hitrust-i1` + `nist-csf` + `nist-csf-tier-3` + `iso-37301` + `iso-37301-general-business` + `iso-50001`.

---

## What's added over `series-a`

| Module | Why now |
|---|---|
| `hitrust-csf` | HITRUST Common Security Framework. Healthcare-tech buyers (hospitals + payers + EHRs) often require HITRUST. Even non-healthcare orgs that have healthcare-tech as a customer segment benefit from the framework's multi-framework crosswalk (ISO + NIST + COBIT + PCI + etc.) feeding cross-cert efficiency. |
| `hitrust-i1` | HITRUST Intermediate scoping (~182 controls). Most series-b-plus orgs targeting HITRUST start at i1 rather than the full r2 (~200-2000 controls). r2 sub-overlay available when pursuing the full assessment. |
| `nist-csf` | NIST CSF 2.0 6-Function backbone (Govern + Identify + Protect + Detect + Respond + Recover). US-government-adjacent + critical-infrastructure-adjacent customers commonly ask for NIST CSF mapping. Becomes the universal cyber-control taxonomy for multi-regime cross-reference. |
| `nist-csf-tier-3` | Tier-3 (Repeatable) sub-overlay. Repeatable maturity = formal processes + organization-wide consistency + risk-informed practices. Common goal at series-b-plus. (Tier-4 Adaptive sub-overlay available when the customer / board asks for it; tier-3 is the practical target.) |
| `iso-37301` | Compliance management system substrate. By series-b-plus the compliance function is a named team with budget; ISO 37301 (Annex SL HLS-aligned) is the substrate framework for documented compliance MS. |
| `iso-37301-general-business` | Sectoral profile sub-overlay. General-business is the default; swap for `iso-37301-financial-services` / `iso-37301-healthcare` / `iso-37301-public-sector` if applicable. |
| `iso-50001` | Energy management. At series-b-plus, energy consumption becomes a material business cost + sustainability + investor + customer concern; ISO 50001 substrate provides the calculated EnB baseline + EnPIs (energy performance indicators) discipline. |

---

## What's still NOT IN (because vertical-specific or jurisdiction-specific)

Beyond series-b-plus the composition becomes too organization-specific to predict in a baseline preset. Adopters use this preset as the foundation and layer the following based on actual business scope:

### EU-specific frameworks

| Module | When to add |
|---|---|
| `dora` + `dora-ctpp`/`-non-ctpp`/`-tlpt` | EU financial-services entity; DORA Articles 2 + 17 (incident reporting) + 26 (TLPT) |
| `banking-resilience` (cross-overlay) | Multi-jurisdiction bank with EU + US presence (DORA + FFIEC alignment) |
| EU MDR / IVDR overlays | EU medical-device + IVD market entry |
| EU AI Act elements | High-risk AI system per EU AI Act |
| `eu-biocides` | Biocide-product placement in EU |

### US sector-specific

| Module | When to add |
|---|---|
| `hipaa` (cross-cutting) | Healthcare-tech processing PHI |
| `connected-medical-device` (cross-overlay) | Connected medical device with cyber + EHR integration |
| `defense-cui` + `cmmc` + `cmmc-level-1`/`-2`/`-3` | DoD supply chain |
| `defense-aerospace-cyber` (cross-overlay) | DoD aerospace prime |
| `utility-cybersecurity` (cross-overlay) | Electric / pipeline / water / transportation utility operator |
| `nerc-cip` (via utility-cybersecurity) | BES Cyber System operator |
| `tsca-pfas` + `osha-hcs` + `transport-hazmat` | Chemical / industrial manufacturer |

### Multi-region

| Module | When to add |
|---|---|
| `digital-health-multi-region` (cross-overlay) | Digital-health platform across US + EU + UK + Canada + Switzerland |
| `clinical-trial-multi-region` (cross-overlay) | Multi-region pharma clinical trial |
| `automotive-supply-chain` (cross-overlay) | Tier-1 supplier serving multiple OEMs |
| `us-state-privacy` (cross-cutting) | Multi-US-state operations (16+ state privacy laws) |

### ATMP / cell therapy

| Module | When to add |
|---|---|
| `atmp` | Cell + gene therapy + CAR-T |
| `cell-therapy-supply-chain` (cross-overlay) | Commercial ATMP with vein-to-vein logistics |

---

## Graduate from `series-b-plus` to ... what?

There is no `series-c-plus` preset — beyond series-b-plus the composition is genuinely organization-specific. The framing inverts: instead of "what's the next baseline," the question becomes "what does my specific multi-jurisdiction + multi-vertical + multi-certification organization need?"

Typical post-series-b-plus pattern:

1. **Periodic maturity assessment** (annual; using NIST CSF tiers as the common yardstick) to identify which modules to add or which sub-overlay levels to escalate.
2. **Per-customer-ask scope additions** — when a new customer brings a regulatory requirement not in scope, add the module + revalidate.
3. **Per-regulator-action scope additions** — when a regulator publishes new guidance or new framework, add the module + update affected templates.
4. **M&A-driven scope additions** — when acquiring or being acquired, scope may need to harmonize with the partner's QMS.

The preset's role at series-b-plus is to be the most-complete baseline; further additions are explicit operational decisions, not preset-driven.

---

## Compose with your vertical + cross-overlays

Series-b-plus startups typically have a primary vertical + 1-3 cross-overlays. Example for a healthcare-tech series-b-plus serving US + EU markets:

```yaml
modules:
  # series-b-plus baseline (21)
  - iso-31000
  - iso-27001
  - integrated-management-system
  - privacy
  - iso-37001
  - iso-22301
  - medical-devices              # ← swap manufacturing
  - soc-2
  - soc-2-type-ii
  - iso-27001-cloud
  - iso-27001-privacy
  - iso-14001
  - iso-45001
  - recall-workflow
  - hitrust-csf
  - hitrust-i1
  - nist-csf
  - nist-csf-tier-3
  - iso-37301
  - iso-37301-general-business
  - iso-50001
  # vertical class overlay
  - samd                          # ← if SaMD
  # additional cross-cuttings
  - hipaa                         # ← PHI processing
  - us-state-privacy              # ← multi-US-state
  # cross-overlays
  - connected-medical-device      # ← if connected
  - digital-health-multi-region   # ← if multi-region
```

That's ~26 modules — large but coherent. The preset gets you to 21; the last 5 are scope-specific.

---

## Linkage

- [`presets/README.md`](README.md) — preset family index
- [`docs/guide/maturity-model.md`](../docs/guide/maturity-model.md) — cross-stage progression
- [`presets/series-b-plus.yaml`](series-b-plus.yaml) + [`presets/series-b-plus.matrix.json`](series-b-plus.matrix.json)
- [`presets/series-a-README.md`](series-a-README.md) — prior stage
- [`docs/modules-catalog.md`](../docs/modules-catalog.md) — full module catalog for layering
