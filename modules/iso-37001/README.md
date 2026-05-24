# iso-37001 — Open QMS cross-cutting overlay

Anti-Bribery Management System (ABMS) overlay covering ISO 37001:2016. Composes with ANY vertical. Follows Annex SL.

## Scope

14 clauses encoding the substantive ISO 37001:2016 additions:

| § | Topic | Distinguishing element |
|---|---|---|
| §5.1.2 | Governing body + senior mgmt responsibility | |
| §5.2 | Anti-bribery policy | |
| **§5.3.2** | **Independent compliance function** | Appropriate competence + status + authority + independence + resources; reports directly to governing body / senior management |
| §6.1 | ABMS risks + opportunities | |
| §7.2.2.2 | Due diligence on personnel | For positions exposed to more than low bribery risk |
| §7.3 | Awareness + training | |
| **§8.2** | **Due diligence on transactions/projects/business associates** | Risk-proportionate with periodic re-assessment |
| §8.3 | Financial controls | Segregation + authorization + cash + expenses + gifts/hospitality/donations |
| §8.4 | Non-financial controls | Procurement + commercial + operational + HR |
| §8.5 | Controls cascaded to controlled orgs + business associates | Medium + High risk |
| §8.7 | Gifts + hospitality + donations | Pre-approval thresholds + register |
| §8.9 | Raising concerns | Whistleblowing + non-retaliation |
| §8.10 | Investigating bribery | |
| §9.4 | Compliance-function review | |

## Templates introduced

- **`templates/qms-abms/DUE-DILIGENCE-ASSESSMENT-TEMPLATE.md`** — §8.2 + §8.5. Risk-tier framework (Low / Medium / High / Prohibited) with scaled depth + approval authority + re-assessment cadence; sanctions + PEP + adverse-media + UBO screening; contractual-safeguards checklist with FCPA + UK Bribery Act + OECD Convention references

Reuses cross-cutting: quality-policy (extended for anti-bribery), SOP, MANAGEMENT-REVIEW.

## Composition

```bash
openqms validate --module <vertical> --module iso-37001
```

## When to use

Particularly applicable for: **public-sector vendors**, **extractive industries**, **defense contractors**, **healthcare suppliers**, **infrastructure contractors**, **intermediary-heavy sales channels** (agents, distributors, lobbyists), **high-CPI jurisdiction operations** (per Transparency International Corruption Perceptions Index). Customer flow-down requirements increasingly require ISO 37001 certification.

## Standards licensing

ISO 37001:2016 commercial.

## Forward work

- Compliance function organizational-independence template (§5.3.2 dedicated)
- Whistleblowing channel SOP template (§8.9)
- 8D-style bribery investigation template (§8.10)
