# iso-14001 — Open QMS cross-cutting overlay

Environmental Management System (EMS) overlay covering ISO 14001:2015. Composes with ANY vertical (medical-devices, aerospace, automotive, manufacturing, pharma, food-safety) — follows Annex SL high-level structure so coexists cleanly with ISO 9001 / 13485 / AS9100D / IATF 16949 / ICH Q10 / ISO 22000 + sibling cross-cutting overlays (iso-27001, regulated-ai, iso-45001, iso-50001, iso-37001, iso-22301).

## Scope

11 clauses encoding the substantive ISO 14001:2015 additions over the Annex SL baseline:

| § | Topic | Distinguishing element |
|---|---|---|
| §4.2 | Interested parties | Environmental-relevant: regulators, communities, customers, NGOs |
| §5.2 | Environmental policy | Commits to protection of environment (prevention of pollution + sustainable resource use + climate change mitigation/adaptation + biodiversity) |
| **§6.1.2** | **Environmental aspects** | Defining EMS artifact — lifecycle-perspective identification + significance criteria → SEAs (Significant Environmental Aspects) |
| §6.1.3 | Compliance obligations | Both legal + voluntary commitments (per §3.2.9 definition) |
| §6.1.4 | Planning action | Address aspects + obligations + risks + opportunities |
| §6.2 | Environmental objectives | Measurable, monitored, communicated, updated |
| §7.4 | Communication | Internal + external (per compliance obligations) |
| §8.1 | Operational control of SEAs | Lifecycle perspective in design + procurement + outsourced processes |
| §8.2 | Emergency preparedness + response | With periodic test |
| §9.1.2 | Evaluation of compliance | Documented evaluation per obligation |
| §10.2 | Nonconformity + corrective action | Incl. mitigating adverse environmental impacts |

## Templates introduced

- **`templates/qms-environmental/ENVIRONMENTAL-ASPECTS-REGISTER-TEMPLATE.md`** — §6.1.2 register with significance scoring → SEA flagging → operational controls + emergency procedures + compliance-obligations cross-reference (lifecycle perspective explicit)
- **`templates/qms-environmental/COMPLIANCE-OBLIGATIONS-REGISTER-TEMPLATE.md`** (v0.25.0 standalone) — §6.1.3 dedicated register

Reuses cross-cutting templates: quality-policy (extended with environmental commitments per §5.2), SOP, AUDIT-PROCEDURE, MANAGEMENT-REVIEW, CAPA.

## Composition

```bash
openqms validate --module <vertical> --module iso-14001
```

Validated with all 6 verticals individually and in 5-overlay everything-shop composite (manufacturing + iso-14001 + iso-45001 + iso-50001 + iso-27001 + regulated-ai) + 9-module deepest composite (pharma + atmp + 7 cross-cutting).

## When to use

Organizations pursuing ISO 14001 certification OR required by customer/regulatory flow-down to maintain an EMS. Particularly relevant for: manufacturers with significant environmental aspects (emissions, waste, resource use); pharma + cell-therapy (solvent handling, hazardous waste); food processors (water, refrigerants, packaging).

## Standards licensing

ISO 14001:2015 commercial (ISO / national member bodies). See repo-root README "Standards licensing — important".

## Forward work

- CBAM-specific carbon-border-adjustment template (EU Regulation 2023/956)
- Lifecycle assessment (LCA) template per ISO 14040 + 14044
- Environmental Product Declaration (EPD) template per ISO 14025
