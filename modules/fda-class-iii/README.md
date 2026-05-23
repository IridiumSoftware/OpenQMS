# FDA Class III overlay (PMA path)

Cross-cutting overlay adding FDA Class III-specific requirements. Class III is the most stringent FDA classification — requires Premarket Approval (PMA), not just 510(k) clearance.

Use via:

```bash
openqms resolve --module medical-devices --module fda-class-iii ...
```

## What this overlay adds

- **PMA application** (21 CFR 814 Subpart B) — the technical-data + clinical-investigation submission for Class III approval.
- **PMA supplements** (§814.39) — changes to an approved Class III device require PMA supplement or 30-day notice; manufacturing site changes require Manufacturing Site Change Supplement.
- **Annual report** (§814.84) — for each PMA-approved device.
- **Medical Device Reporting** (21 CFR 803) — adverse event reporting to FDA (30-day standard; 5-day for events requiring remedial action). Bound to the existing complaint workflow with reportability assessment.

## Naming clarification

FDA's "MDR" (Medical Device Reporting per 21 CFR 803) is **not** the EU MDR (Medical Devices Regulation 2017/745). The acronym collision is a recurring source of confusion. In this overlay, "MDR" means the FDA adverse-event reporting regulation.

## Composition patterns

```bash
# US-only Class III submission
openqms resolve --module medical-devices --module fda-class-iii ...

# US + EU dual submission for an implantable Class III device
openqms resolve \
  --module medical-devices \
  --module implantable \
  --module mdr-class-iii \
  --module fda-class-iii \
  ...
```
