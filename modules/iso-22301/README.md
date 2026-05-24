# iso-22301 — Open QMS cross-cutting overlay

Business Continuity Management System (BCMS) overlay covering ISO 22301:2019. Composes with ANY vertical. Follows Annex SL.

## Scope

13 clauses:

| § | Topic | Distinguishing element |
|---|---|---|
| §5.2 | BC policy | |
| §6.1 | BCMS risks + opportunities | |
| §6.2 | BC objectives | Derived from BIA |
| **§8.2.2** | **Business Impact Analysis (BIA)** | Identifies prioritized activities + RTO/MAO/MBCO/RPO |
| **§8.2.3** | **Risk assessment** | Of disruption to prioritized activities |
| **§8.4** | **BC strategies + solutions** | People + ICT + infrastructure + supplies + partners + financial resources; stabilization + continuity + recovery + return |
| §8.5 | BC plans + procedures | |
| §8.6 | Exercise programme | Tabletop, comms cascade, technical, full-scale; varied scenarios; post-exercise review |
| §8.7 | Evaluation of BC documentation + capabilities | |
| §9.1 / §9.2 / §9.3 | Monitoring + measurement / internal audit / management review | |
| §10.2 | NC + corrective action | |

## Templates introduced

- **`templates/qms-bcms/BCMS-PLAN-TEMPLATE.md`** — §8.4 + §8.5 + §8.6 + §8.7. Recovery objectives summary table; 8 disruption scenarios (site loss / supplier loss / cyber attack / key-personnel loss / utility outage / public-health event / natural disaster / transportation disruption); crisis management team with 24/7 contacts; internal + external communications matrix with regulatory reporting windows; exercise programme cadence
- **`templates/qms-bcms/BIA-TEMPLATE.md`** (v0.25.0 standalone) — §8.2.2 dedicated with activity inventory + criticality + impact-over-time + MAO/RTO/RPO/MBCO determination + resource dependencies + recovery schedule aggregation
- **`templates/qms-bcms/IT-DR-PLAN-TEMPLATE.md`** (v0.25.0 standalone) — IT-specific subset of BCMS-PLAN per ISO/IEC 27031 + NIST SP 800-34 + ISO 27001 Annex A.5.29+A.5.30. System inventory with RTO/RPO + DR architecture + backup strategy (3-2-1 + air-gap + ransomware-recovery-tested) + per-system recovery procedures + 5 disruption scenarios + exercise programme

## Composition

```bash
openqms validate --module <vertical> --module iso-22301
```

## When to use

Particularly applicable for: organizations with **significant disruption exposure** (single-site dependencies, complex supply chains); regulated services with **continuity obligations** (financial services under DORA; healthcare; critical infrastructure; utilities; telecoms).

## Standards licensing

ISO 22301:2019 commercial. ISO/TS 22317 (BIA guidelines) + 22318 (supply chain) + 22330 (people aspects) + 22331 (strategy) are complementary guidance (also commercial).

## Forward work

- Exercise after-action review template (§8.6)
- Single-site-dependency assessment template
- DORA mapping overlay for EU financial services (composes ISO 22301 + ISO 27001 + sector-specific requirements)
