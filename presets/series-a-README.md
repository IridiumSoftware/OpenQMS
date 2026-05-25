# series-a preset

**Stage assumptions:** 15-50 people, scaling rapidly, certifications becoming materially required by customers + regulators.

**Module count:** 14 — `seed (7)` + `soc-2` + `soc-2-type-ii` + `iso-27001-cloud` + `iso-27001-privacy` + `iso-14001` + `iso-45001` + `recall-workflow`.

---

## What's added over `seed`

| Module | Why now |
|---|---|
| `soc-2` | SOC 2 Trust Services Criteria. By series-a multiple customers ask for SOC 2 attestation. The TSC framework (Security + Availability + Processing Integrity + Confidentiality + Privacy) is now standing operating condition. |
| `soc-2-type-ii` | Observation-period sub-overlay. Type II adds the 3-12 month observation window that customers actually want (Type I is point-in-time and weaker signal). Sub-overlay encodes the observation-period discipline. |
| `iso-27001-cloud` | ISO 27017 cloud-services additions. Series-a startups are usually fully cloud-resident; cloud-services controls are no longer satisfied by the baseline 27001 Annex A controls alone. |
| `iso-27001-privacy` | ISO 27701 PIMS extension. The privacy module (GDPR + CCPA) covers the regulatory layer; ISO 27701 PIMS extension covers the ISO-framework integration with ISO 27001 controls — making the privacy posture certifiable rather than just policy-stated. |
| `iso-14001` | Environmental management. Applicable when physical operations (manufacturing facility / lab / warehouse) become non-trivial. Even pure-software startups often have an office + travel + procurement footprint worth ISO 14001 substrate. |
| `iso-45001` | Occupational H&S management. Worker consultation per §5.4 + hierarchy of controls per §8.1.2 becomes meaningful at 15+ employees with any physical workforce. |
| `recall-workflow` | Cross-vertical recall discipline. If you have any consumer-facing product (medical device / drug / food / vehicle / consumer good), recall-workflow framework (NHTSA 49 CFR 573/577/579 + FDA 21 CFR 7 + 21 CFR 806 + CPSIA §15 + EU GPSR) becomes operationally relevant. |

---

## What's still NOT IN

| Not yet | Why deferred |
|---|---|
| HITRUST | Healthcare-tech-specific; defer to series-b-plus unless your customer base is dominated by healthcare. |
| NIST CSF | US-government-adjacent + critical-infrastructure-adjacent; defer to series-b-plus unless you sell into those segments. |
| `iso-37301` compliance MS substrate | At series-a the compliance function is usually 1-2 FTE; ISO 37301 substrate becomes useful when the function formalizes at series-b-plus. |
| EU-specific regimes (DORA / NIS2 / EU MDR / EU AI Act) | Add when EU operations are material — often series-b-plus. |
| US-sector-specific (HIPAA Security Rule deep / FFIEC / NERC CIP / CMMC) | Add when your specific sector + customer base requires. |
| Cross-overlays (combination-product / connected-medical-device / banking-resilience / etc.) | Cross-overlays bind across specific vertical combinations. Layer explicitly when applicable; not in the baseline preset. |
| `iso-50001` energy MS | Energy-management overlay. Applicable when energy consumption is a material business cost or sustainability target — series-b-plus typically. |

---

## Graduate to `series-b-plus` when

Any of:

- **HITRUST i1 or r2 attestation becomes a customer requirement.** Most common in healthcare-tech buyers (hospitals + payers + EHRs).
- **50+ employees.** Compliance function formalizes as a named team rather than a shared role; ISO 37301 compliance MS substrate now load-bearing.
- **First non-home-jurisdiction regulatory market.** EU entry (GDPR-specific + EU MDR if device + DORA if financial) or APAC entry (PDPL / PIPL / similar) triggers multi-jurisdiction coordination.
- **NIST CSF tier-3 (Repeatable) goal declared.** Often customer-driven; sometimes board-driven as a maturity signal.
- **Energy / sustainability becomes a stakeholder ask.** Investor / customer / regulator pressure on Scope 1+2+3 emissions; ISO 50001 substrate becomes useful.

---

## Compose with your vertical

The series-a preset still uses `manufacturing` as the vertical placeholder. Swap for your actual vertical the same way as in `seed`:

```yaml
# Example: medical-device series-a pursuing SOC 2 Type II + HIPAA
modules:
  - iso-31000
  - iso-27001
  - integrated-management-system
  - privacy
  - iso-37001
  - iso-22301
  - medical-devices         # ← swap manufacturing
  - mdr-class-iib           # ← class overlay
  - hipaa                   # ← HIPAA-specific cross-cutting overlay
  - soc-2
  - soc-2-type-ii
  - iso-27001-cloud
  - iso-27001-privacy
  - iso-14001
  - iso-45001
  - recall-workflow
  - connected-medical-device  # ← cross-overlay if connected SaMD
```

---

## Linkage

- [`presets/README.md`](README.md) — preset family index
- [`docs/guide/maturity-model.md`](../docs/guide/maturity-model.md) — cross-stage progression
- [`presets/series-a.yaml`](series-a.yaml) + [`presets/series-a.matrix.json`](series-a.matrix.json)
- [`presets/seed-README.md`](seed-README.md) — prior stage
- [`presets/series-b-plus-README.md`](series-b-plus-README.md) — next stage
