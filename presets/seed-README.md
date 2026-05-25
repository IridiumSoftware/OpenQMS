# seed preset

**Stage assumptions:** 5-15 people, first paying customers, regulator on horizon, vertical commitment made (placeholder: `manufacturing`).

**Module count:** 7 — `pre-seed (3)` + `privacy` + `iso-37001` + `iso-22301` + `manufacturing`.

---

## What's added over `pre-seed`

| Module | Why now |
|---|---|
| `privacy` | First paying customer = customer data under your care. GDPR + CCPA scope kicks in based on customer location + your processing scope. Privacy notices + DPA + ROPA + breach-notification process are no longer optional. |
| `iso-37001` | Anti-bribery governance becomes visible to investors + customers as you formalize. Even small startups with no procurement budget need due-diligence-of-vendors + gifts-and-hospitality policy + raising-concerns mechanism. |
| `iso-22301` | First customer SLA = service-availability commitment. ISO 22301 BCMS substrate gives you BIA + RTO/RPO discipline before your first outage forces you to learn it under pressure. |
| `manufacturing` | First vertical, as placeholder. **Adopters must swap this for their actual vertical** — medical-devices / pharma / aerospace / automotive / food-safety / chemicals. Manufacturing is the lowest-regulator-pressure default (ISO 9001 only, no vertical-specific regulator). |

---

## What's still NOT IN

| Not yet | Why deferred |
|---|---|
| SOC 2 (Type I or II) | Auditor engagement is the cost gate. SOC 2 makes sense when a customer requires it for contract signing. Seed-stage startups usually have ≤ 1 customer asking; defer to series-a when multiple customers ask. |
| Sub-overlays (CMMC levels / NIST CSF tiers / SOC 2 types / SAQ types / DORA tiers / HITRUST levels / ISO 37301 sectoral profiles) | Sub-overlays split rigor levels within a cross-cutting overlay. At seed the parent overlay at baseline rigor is enough. |
| Cross-overlays (combination-product / connected-medical-device / digital-health-multi-region / banking-resilience / clinical-trial-multi-region / etc.) | These encode intersection-specific regulatory requirements. At seed you likely don't yet have the cross-vertical scope to need them. |
| Sector-specific frameworks (HIPAA / FFIEC / NERC CIP / CMMC / etc.) | Add when your specific sector + customer base requires. Healthcare-tech: HIPAA at seed if processing PHI; otherwise series-a. |
| HITRUST / NIST CSF | Industry-specific certification frameworks. HITRUST is healthcare-tech; NIST CSF is US-government-adjacent. Add when the customer base requires. |
| `iso-37301` compliance MS substrate | Compliance-management overlay. At seed the compliance function is usually 0.5-1 FTE on the QM's plate; ISO 37301 substrate becomes useful at series-a+. |

---

## Graduate to `series-a` when

Any of:

- **SOC 2 Type II becomes a customer requirement.** A signed contract that names SOC 2 Type II as a precondition is the trigger.
- **15+ employees.** HR processes scale + formal access reviews + segregation-of-duties is now load-bearing.
- **First formal certification pursuit.** ISO 9001 audit / MDSAP audit / ISO 13485 audit / ISO 27001 cert pursuit = series-a-tier rigor is now operating-condition.
- **Multi-customer pressure.** When you have 3+ customers asking for similar attestations (SOC 2, ISO 27001, GDPR-mapping-to-our-controls), it's no longer per-customer custom; it's a standing operation.

---

## Compose with your actual vertical

**The `manufacturing` module is a placeholder.** Swap it out before shipping:

```yaml
# Pharma seed
modules:
  - iso-31000
  - iso-27001
  - integrated-management-system
  - privacy
  - iso-37001
  - iso-22301
  - pharma                  # ← swap manufacturing for pharma
  # consider adding the relevant pharma class overlay:
  # - pharma-clinical-stage
  # - pharma-biologics
  # - atmp
```

```yaml
# Medical-device seed
modules:
  - iso-31000
  - iso-27001
  - integrated-management-system
  - privacy
  - iso-37001
  - iso-22301
  - medical-devices         # ← swap manufacturing for medical-devices
  # consider adding the relevant device class overlay:
  # - mdr-class-iib (or mdr-class-iia / mdr-class-iii / fda-class-ii / etc.)
  # - samd (if SaMD)
  # - hipaa (if processing PHI)
```

```yaml
# Aerospace seed
modules:
  - iso-31000
  - iso-27001
  - integrated-management-system
  - privacy
  - iso-37001
  - iso-22301
  - aerospace               # ← swap manufacturing for aerospace
  # consider adding the relevant DAL overlay:
  # - aerospace-dal-c (or dal-a / dal-b / dal-d / dal-e)
```

---

## Linkage

- [`presets/README.md`](README.md) — preset family index
- [`docs/guide/maturity-model.md`](../docs/guide/maturity-model.md) — cross-stage progression
- [`presets/seed.yaml`](seed.yaml) + [`presets/seed.matrix.json`](seed.matrix.json)
- [`presets/pre-seed-README.md`](pre-seed-README.md) — prior stage
- [`presets/series-a-README.md`](series-a-README.md) — next stage
