---
document_id: ER-XXX
title: "[Organization / Site / Boundary Scope] — Energy Review, EnPIs, and EnB Baseline"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Energy Manager / Energy Team Lead, Title]"
status: draft
approved_by: "[Top Management + Energy Team]"
approval_date: YYYY-MM-DD
review_cadence: "Annually + on significant change in facilities/equipment/systems/processes/staffing/operating patterns affecting energy performance"
---

# ER-XXX: Energy Review, Energy Performance Indicators, and Energy Baseline

Per ISO 50001:2018 §6.3 (Energy Review), §6.4 (Energy Performance Indicators), §6.5 (Energy Baseline). Together these three sections form the analytical foundation of the EnMS: the energy review determines what we use, where, by how much, and where the improvement opportunities are; the EnPIs are the metrics we'll track; the EnB is the historical-state reference against which we measure performance change. ISO 50001 is unique among the management-system standards in mandating a quantitative, calculated, periodically-recalibrated performance baseline.

## 1. Scope + boundaries

- **EnMS boundaries:** [physical sites + facilities + activities covered]
- **Energy types in scope:** [electricity, natural gas, fuel oil, propane, gasoline, diesel, district steam, district chilled water, renewable on-site generation, etc.]
- **Reporting period covered by this review:** [start YYYY-MM-DD to end YYYY-MM-DD; typically 12 consecutive months]
- **Relevant variables identified:** [production output, heating/cooling degree-days, occupancy, operating hours, raw-material throughput — variables that materially affect energy consumption and must be normalized away in EnPI calculation]
- **Static factors:** [facility footprint, equipment population, building envelope — held constant for the baseline]

## 2. Energy review (§6.3)

### 2.1 Past + present energy use + consumption

| Energy type | Source | Annual consumption | Unit | Cost | CO2-e | Method (metered / sub-metered / estimated) | Reference |
|---|---|---|---|---|---|---|---|

### 2.2 Identification of areas of significant energy use (SEUs)

A Significant Energy Use (SEU) is an energy use accounting for substantial consumption + having considerable potential for energy performance improvement. Per ISO 50001 §6.3 b), criteria for significance are defined here.

**Significance criteria:** [e.g., "any single energy-consuming equipment, system, process, or facility that exceeds 5% of total energy consumption OR is a top-5 consumer by absolute energy use OR is identified by the energy team as having ≥ 20% improvement potential"]

| SEU # | SEU description (equipment / system / process / facility) | Annual consumption | % of total | Relevant variables | Static factors | Personnel affecting performance | Performance basis (current performance metric + value) |
|---|---|---|---|---|---|---|---|
| SEU-1 | [e.g., chiller plant CHL-001 + CHL-002] | | % | Cooling load (ton-hours), CDD | Building floor area | Maintenance technician + facility operator | kW / ton |

### 2.3 Improvement opportunities for SEUs

Per §6.3 c) — opportunities for improving energy performance shall be identified, prioritized, and recorded.

| Opportunity # | SEU # | Description | Estimated annual savings | Investment | Payback (years) | Priority | Status | Linked objective # |
|---|---|---|---|---|---|---|---|---|
| OPP-1 | SEU-1 | Variable frequency drive retrofit on CHL-001 condenser pump | 240 MWh/yr | $35k | 1.8 | High | Approved | OBJ-001 |

## 3. Energy Performance Indicators (§6.4)

EnPIs are quantitative values or measures of energy performance, defined by the organization. They must enable comparison of energy performance over time. For each SEU + at the organization-level, an EnPI is defined.

| EnPI # | EnPI name | Definition (formula) | Numerator | Denominator (relevant variable) | Unit | SEU # | Applicable to | Frequency | Acceptance threshold |
|---|---|---|---|---|---|---|---|---|---|
| EnPI-1 | Chilled-water plant efficiency | Average kW input / average ton refrigeration output | kWh | Ton-hours | kW/ton | SEU-1 | CHL plant | Monthly | < 0.62 kW/ton (peak) |
| EnPI-organization | Site-level energy intensity | Total energy / production output | MWh + therms (converted to common units) | Production tonnes | MWh-equiv / tonne | All SEUs | Site total | Monthly | ≤ EnB-organization × 0.97 (3% YoY improvement target) |

**EnPI normalization:** when relevant variables change (e.g., production volume varies), EnPIs are normalized using a regression model or engineering analysis. The normalization method is documented per EnPI.

## 4. Energy Baseline (§6.5)

The Energy Baseline (EnB) is a quantitative reference providing the basis for comparison of energy performance. For each EnPI, an EnB is calculated for the reporting period chosen.

| EnPI # | EnB period | EnB value | Method (regression / engineering / aggregate) | Normalization model | EnB conditions (static factors held constant) |
|---|---|---|---|---|---|
| EnPI-1 | [YYYY] | 0.68 kW/ton | Aggregate weighted average | None (steady-state operation) | CHL-001 + CHL-002 in service throughout period |
| EnPI-organization | [YYYY] | 1.45 MWh-equiv / tonne | Regression: Energy = a × Production + b × CDD + c | Production + CDD | Building footprint, equipment population, product mix as of baseline-period end |

**EnB recalibration triggers (§6.5):**

- Major modifications to facilities, equipment, systems, or processes affecting energy performance.
- Significant change to static factors.
- Change in the data + measurement methods supporting the EnPI.
- Discovery that the EnPI no longer reflects energy use + consumption appropriately.

When an EnB is recalibrated, the rationale is documented + the new baseline is approved before subsequent performance reporting against it.

## 5. Action plans + objectives (cross-reference to §6.6)

Energy objectives + targets derived from this review are documented in the Energy Objectives + Targets register (OBJ-XXX). This review's improvement opportunities (per §2.3) feed that register.

## 6. Operational control + procurement implications

Per ISO 50001 §8.1 and §8.3 — criteria for effective operation + maintenance of SEUs (operational controls) and energy-considered procurement criteria (energy-using equipment, energy services, energy purchases) are derived from this review.

| SEU # | Operational control criterion | SOP / engineering reference |
|---|---|---|
| SEU-1 | Chiller staging logic + setpoint band per loading condition | SOP-XXX chiller operating procedure |

## 7. Data collection + measurement plan (§6.6)

The energy data collection + measurement plan describes what is measured, how, where, when, by whom, and how the data feeds the EnPIs.

| EnPI # | Data point | Source (meter / sub-meter / utility bill / estimation) | Measurement frequency | Data owner | Storage location |
|---|---|---|---|---|---|

## 8. Review + update cadence

Triggers for re-review (in addition to scheduled annual review):

- Significant change in facilities, equipment, systems, processes, staffing, operating patterns
- New SEU emerging from energy review or improvement project
- EnB recalibration trigger met (per §4)
- Management review action

Last review date: [YYYY-MM-DD] · Next scheduled review: [YYYY-MM-DD]

## 9. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Energy Manager / Energy Team Lead | | | |
| Energy Team representative | | | |
| Operations / Facilities Lead | | | |
| Top Management representative | | | |

## 10. References

- ISO 50001:2018 §6.3 — Energy review.
- ISO 50001:2018 §6.4 — Energy performance indicators.
- ISO 50001:2018 §6.5 — Energy baseline.
- ISO 50001:2018 §6.6 — Planning for collection of energy data.
- ISO 50001:2018 §8.1 — Operational planning and control.
- ISO 50001:2018 §8.3 — Procurement of energy services, products, equipment, and energy.
- ISO 50001:2018 §9.1 — Monitoring + measurement + analysis + evaluation of energy performance + the EnMS.
- ISO 50001:2018 Annex A.6.5 — Energy baseline normalization guidance.
- Linked: OBJ-XXX (Energy Objectives + Targets), SOP-XXX (SEU operational SOPs), procurement specifications referencing energy criteria.

## 11. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
