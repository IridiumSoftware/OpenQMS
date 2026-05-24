# iso-50001 — Open QMS cross-cutting overlay

Energy Management System (EnMS) overlay covering ISO 50001:2018. Composes with ANY vertical. Follows Annex SL.

## Scope

10 clauses. **ISO 50001 is unique among the management-system standards in mandating a quantitative, calculated, periodically-recalibrated performance baseline (EnB).** Adopters must produce real numbers (energy intensity in MWh-equiv/tonne, chiller efficiency in kW/ton, etc.) — not just process discipline.

| § | Topic | Distinguishing element |
|---|---|---|
| §5.2 | Energy policy | Commits to procurement of energy-efficient products + design for energy performance + continual improvement of energy performance + the EnMS |
| **§6.3** | **Energy review** | Analyze use + consumption; identify Significant Energy Uses (SEUs); determine current performance; identify + prioritize improvement opportunities. **Analytical foundation of the EnMS** |
| **§6.4** | **Energy Performance Indicators (EnPIs)** | Methodology + values + reviews + comparison to baselines documented |
| **§6.5** | **Energy Baseline (EnB)** | Calculated from energy review; revised on EnPI-no-longer-reflects, static-factor change, operations change |
| §6.6 | Planning for data collection | Key characteristics, relevant variables, operational criteria, static factors |
| §8.1 | Operational control of SEUs | Criteria for effective operation + maintenance |
| §8.2 | Design | Energy performance improvement opportunities in design |
| §8.3 | Procurement | Energy-using products + equipment + services + energy itself |
| §9.1.1 | Monitoring + measurement + analysis | Incl. investigation + response to significant deviations |
| §10.2 | Nonconformity + corrective action | |

## Templates introduced

- **`templates/qms-energy/ENERGY-REVIEW-AND-ENPI-BASELINE-TEMPLATE.md`** — combined §6.3 + §6.4 + §6.5 + §6.6. **Most quantitative template in Open QMS** — per-SEU performance basis + improvement opportunity with payback; per-EnPI formula + numerator + denominator + normalization model; per-EnB calculation method + recalibration triggers; data collection plan; operational + procurement implications
- **`templates/qms-energy/ENERGY-OBJECTIVES-TARGETS-REGISTER-TEMPLATE.md`** (v0.25.0 standalone) — §6.2 register with org-level + SEU-specific + operational/behavioral objectives linked to EnPIs

Reuses cross-cutting: quality-policy (extended for energy), SOP, CAPA.

## Composition

```bash
openqms validate --module <vertical> --module iso-50001
```

## When to use

Energy-intensive operations: sterile pharma (HVAC + cleanroom intensive); cold-chain food (refrigeration); large-scale manufacturing; data centers. CBAM / SBTi / RE100 commitments increase the relevance for any manufacturer.

## Standards licensing

ISO 50001:2018 commercial.

## Forward work

- Sub-metering plan template (per §6.6)
- ISO 50006 EnPI / EnB methodology cross-reference
