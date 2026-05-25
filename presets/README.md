# Open QMS — startup-stage presets

**Audience:** founders + operators choosing a starting QMS scope. Closes compliance-architecture forward-work P4 at v0.61.0.

**Goal:** opinionated answer to *"what should be IN my QMS at my stage?"* — without forcing a one-size-fits-all answer that either over- or under-shoots.

For the cross-stage progression rationale, see [`docs/guide/maturity-model.md`](../docs/guide/maturity-model.md). For the trust-gate framing, see [`docs/compliance-architecture.md`](../docs/compliance-architecture.md).

---

## Four stages

| Stage | Module count | Bundle YAML | Typical posture |
|---|---|---|---|
| **pre-seed** | 3 | [`pre-seed.yaml`](pre-seed.yaml) | 1-5 people, MVP product, no paying customers yet, no specific regulator |
| **seed** | 7 | [`seed.yaml`](seed.yaml) | 5-15 people, first paying customers, regulator on horizon, vertical chosen |
| **series-a** | 14 | [`series-a.yaml`](series-a.yaml) | 15-50 people, scaling, certifications becoming materially required by customers + regulators |
| **series-b-plus** | 21 | [`series-b-plus.yaml`](series-b-plus.yaml) | 50-200+ people, multi-jurisdiction, formal compliance function exists |

Each stage strictly contains the modules of the prior stage. Adopters can run a preset directly OR fork to customize. The point is to ground the decision in an opinionated baseline rather than start from zero.

---

## Why startup-stage labels (not company-size labels)

Funding rounds are recognizable to founders + operators + boards. But the *actual trigger* for graduating to the next stage is a compliance event, not a funding round. Each preset README spells out the events.

Stages are also industry-agnostic — no preset bakes in `medical-devices` or `pharma` or any specific vertical. Adopters compose the preset with their actual vertical (and class overlay, if any). See [`docs/modules-catalog.md`](../docs/modules-catalog.md) for verticals + class overlays.

---

## How to use a preset

### Run a preset directly

```bash
openqms regenerate --bundle presets/pre-seed.yaml
```

Dry-run mode prints the diff against the committed `presets/pre-seed.matrix.json` baseline. Exits 1 if any module / template / clause has drifted since the baseline was written.

### Fork + customize

```bash
cp presets/seed.yaml my-qms-seed.yaml
# edit my-qms-seed.yaml to add your vertical + remove modules you don't need
openqms regenerate --bundle my-qms-seed.yaml --write-matrix
```

### Compose preset + vertical

The presets are industry-agnostic. To add your vertical (medical-devices / pharma / aerospace / automotive / food-safety / chemicals / manufacturing — *already in pre-seed and up via the `manufacturing` placeholder*), edit the `modules:` list to include the vertical you actually operate.

For example, a Series A medical-device startup pursuing SOC 2 Type II:

```yaml
modules:
  - iso-31000
  - iso-27001
  - integrated-management-system
  - privacy
  - iso-37001
  - iso-22301
  - medical-devices         # ← swap manufacturing for medical-devices
  - mdr-class-iib           # ← add the class overlay
  - hipaa                   # ← add if processing PHI
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

## Per-preset details

| Preset | What's IN (added) | What's NOT IN (intentionally) | Graduate when |
|---|---|---|---|
| **pre-seed** | risk-management awareness + IS baseline + IMS substrate | privacy / vertical / anti-bribery / BCMS / certs / sub-overlays | first paying customer · specific regulator decision · first non-founder hire |
| **seed** | + privacy + anti-bribery + BCMS + first vertical placeholder | SOC 2 / sub-overlays / cross-overlays / sector frameworks | SOC 2 Type II asked · 15+ employees · first formal cert pursuit |
| **series-a** | + SOC 2 (Type II) + ISO 27001 cloud/privacy + environmental + OH&S + recall-workflow | HITRUST / NIST CSF / ISO 37301 / multi-jurisdiction frameworks | HITRUST asked · 50+ employees · non-home-jurisdiction market · NIST CSF tier-3+ goal |
| **series-b-plus** | + HITRUST CSF/i1 + NIST CSF + ISO 37301 + energy MS | EU-specific regimes (DORA/NIS2/EU MDR) · US-sector-specific (HIPAA/FFIEC/NERC/CMMC) · cross-overlays | beyond this point, scope is too organization-specific to predict — layer your vertical + cross-overlays explicitly |

---

## CI integration

Each preset is regression-checked in CI alongside the existing `bundles/example-*` baselines. If a module or template change subtly affects a preset's resolution, CI fails — the operator either reverts or accepts the drift via `--write-matrix` commit.

See `.github/workflows/engine-tests.yml` for the regenerate dry-run gating block.

---

## Linkage to other Open QMS controls

- **OQ-015** `:verified` re-resolution + Git-reviewable diff — preset matrix files participate in this gate
- **OQ-125** this preset family — Gap-tier, batched
- **`docs/guide/maturity-model.md`** — cross-stage progression rationale + per-stage compliance-event triggers
- **`bundles/`** — vertical-specific example bundles (different framing: scope-by-product vs scope-by-maturity-stage)
- **`docs/modules-catalog.md`** — full module catalog for layering
