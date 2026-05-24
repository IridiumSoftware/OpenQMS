# iso-45001 — Open QMS cross-cutting overlay

Occupational Health + Safety Management System (OHSMS) overlay covering ISO 45001:2018. Composes with ANY vertical. Follows Annex SL.

## Scope

11 clauses. The distinguishing OHSMS-vs-other-Annex-SL element is **§5.4 consultation + participation of workers** — non-managerial workers + their representatives consulted + participating in development + planning + implementation + evaluation + improvement of the OHSMS. Mechanisms + time + training + barrier removal required. This requirement has no analog in ISO 9001 / 14001 / 27001 / 42001 / 50001.

| § | Topic | Distinguishing element |
|---|---|---|
| §4.2 | Interested parties | Workers + their representatives, contractors, communities, families of workers |
| §5.2 | OH&S policy | Commits to safe + healthy working conditions; elimination of hazards + reduction of OH&S risks; worker consultation + participation |
| **§5.4** | **Worker consultation + participation** | THE foundational OHSMS requirement |
| **§6.1.2** | **Hazard ID + risk assessment + opportunities** | Ongoing + proactive; routine + non-routine; **psychosocial factors explicitly required** |
| §6.1.3 | Legal + other requirements | Per industry + jurisdiction |
| §6.1.4 | Planning action | |
| §7.3 | Awareness | Incl. **right to remove self from imminent danger** + protection from undue consequences |
| **§8.1.2** | **Hierarchy of controls** | Elimination > substitution > engineering > administrative > PPE. PPE is the **last resort**, not the default |
| §8.1.3 | Management of change | |
| §8.1.4 | Procurement | Incl. contractor coordination |
| §8.2 | Emergency preparedness + response | |
| §10.2 | Incident + NC + CAPA | With worker participation in evaluation + root-cause analysis |

## Templates introduced

- **`templates/qms-ohs/HAZARD-IDENTIFICATION-RISK-ASSESSMENT-TEMPLATE.md`** (HIRA) — §6.1.2 with worker consultation per §5.4 as **precondition** (frontmatter includes required `worker_consultation:` field surfacing the standard's unique requirement at the document boundary). Hazard register with S × L matrix + hierarchy-of-controls action per §8.1.2 + cross-references to §6.1.3 legal + §8.1.3 MoC + §8.1.4 procurement + §8.2 emergency
- **`templates/qms-ohs/OHS-LEGAL-REQUIREMENTS-REGISTER-TEMPLATE.md`** (v0.25.0 standalone) — §6.1.3 dedicated register with OSHA federal + state OSH plans (Cal/OSHA Heat Illness / IIPP / ATD) + EU OSH Framework Directive

Reuses cross-cutting templates: quality-policy (extended for OH&S per §5.2), SOP, CAPA.

## Composition

```bash
openqms validate --module <vertical> --module iso-45001
```

## When to use

Any organization with workforce safety obligations (essentially all manufacturers). Particularly load-bearing for: pharma sterile + cell-therapy manufacturing (biological + chemical + shift-work psychosocial hazards); aerospace + automotive production lines; food processing (cold-room + chemical sanitizer + machinery + slip/fall + lifting).

## Standards licensing

ISO 45001:2018 commercial.

## Forward work

- Incident investigation template (ISO 45001 §10.2)
- Worker consultation evidence template (§5.4 dedicated)
