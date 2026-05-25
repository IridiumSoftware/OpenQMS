# Template frontmatter — schema + conventions

**Audience:** anyone authoring or modifying a `templates/**/*.md` file. Closes compliance-architecture forward-work P9 at v0.58.0.

**What this guide covers:** the YAML frontmatter schema enforced by `scripts/lint-template-frontmatter.py` (CI gate added at v0.58.0). Every template carries frontmatter; the schema is hard-fail.

For module.yaml schema, see `scripts/lint-module-yaml.py`. For document-control workflow that consumes the frontmatter fields, see [`docs/guide/doc-control.md`](doc-control.md).

---

## Why frontmatter is required

Frontmatter makes the template machine-readable. The CI pipeline (`engine-tests.yml` workflow at v0.58.0) parses the YAML block + validates against schema before `pytest` runs. This means:

- Authors can't ship a template with a typo'd or missing required field — CI catches it
- The doc-control workflow consumes the same fields without re-parsing
- Schema gives adopters confidence that every template they fork has the same baseline metadata

---

## The schema

### Required fields

| Field | Type | Pattern | Notes |
|---|---|---|---|
| `document_id` | string | `^[A-Za-z0-9][A-Za-z0-9_\-\[\]]*$` | Stable identifier; e.g., `SOP-IDM-001`. Leading digit OK (`510K-XXX`). Adopter fill-in brackets OK (`DI-[PRODUCT]-001`). Use `-XXX` as the adopter-fill-in suffix. |
| `version` | string | `^\d+\.\d+(\.\d+)?$` | Semver-ish: `1.0`, `0.1.0`, `2.3.4` all accepted. Two-part or three-part. |
| `owner` | string | non-empty | Role or named individual. Use `[Role]` placeholder for adopter fill-in. |
| `status` | string | one of recognized states | See state lists below. |
| **one of:** `effective_date` · `issued_date` · `issue_date` · `opened_date` · `assessment_date` · `notification_date` · `approval_date` | string | `YYYY-MM-DD` or literal `YYYY-MM-DD` placeholder | At least one date field is required. Use the field most appropriate for the record kind. |

### Recognized status values

Two lifecycle families coexist:

| Family | States | Use for |
|---|---|---|
| **Document lifecycle** | `draft` · `review` · `approved` · `effective` · `superseded` | SOPs, policies, manuals, controlled procedures, templates-as-documents |
| **Record lifecycle** | `open` · `closed` · `cancelled` | Deviations, OOS investigations, CAPA records, change-controls, traceability records |

Status may include a parenthetical qualifier (e.g., `draft (pending NHTSA acceptance)`); the schema checks the head token only.

### Optional fields

Anything you need. Templates frequently carry domain-specific frontmatter like:

- `title:` — display title
- `approved_by:` + `approval_date:` — approval evidence
- `review_cadence:` — when the document is due for next review
- `next_review:` — explicit date for next review
- `addresses:` — list of clause IDs this template binds to
- `linked_*:` — references to related artifacts
- `phi_classification:` — for HIPAA-touching templates
- `regulatory_framework_in_scope:` — for cross-jurisdiction templates
- `worker_consultation:` — for ISO 45001 templates
- `qa_approval:` — for GLP templates
- `archive_location:` — for retention-bearing templates

The schema is **permissive on extras** — domain-specific fields are encouraged.

---

## Minimal frontmatter for a new template

Copy + adapt:

```yaml
---
document_id: PREFIX-XXX
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Role / Team]"
status: draft
---
```

Then add optional fields as appropriate for the document kind.

---

## How to know what `PREFIX` to use

Existing prefixes by template group:

| Group | Prefix |
|---|---|
| `templates/qms-policy/` | `POL`, `SOP`, `IDM` (identity-mapping SOP) |
| `templates/qms-bcms/` | `BCP`, `BCM` |
| `templates/qms-capa/` | `CAPA` |
| `templates/qms-management-review/` | `MR`, `MGMT-RVW` |
| `templates/qms-recall/` | `REC`, `NHTSA-OWN`, `DIR` |
| `templates/qms-privacy/` | `PRIV-*` |
| `templates/qms-hipaa/` | `HIPAA-*` |
| `templates/qms-logistics/` | `LOG-*` |
| `templates/qms-ohs/` | `OHS-*` |
| `templates/qms-environmental/` | `ENV` |
| `templates/qms-energy/` | `EN`, `ENP` |
| `templates/qms-abms/` | `ABM` |
| `templates/qms-sops/` | `SOP-*` |
| `templates/product-dhf/` | `DI` (design input), `DO` (design output), `510K`, `RMF` |
| `templates/product-pharma/` | `MBR`, `VMP`, `APQR`, `BCOA`, `STAB`, `COMP`, etc. |
| `templates/product-atmp/` | `DON-ELIG`, `TRACE` |
| `templates/product-chemicals/` | `CHEM-*` |
| `templates/product-food/` | `HACCP`, `PRP` |
| `templates/product-sw/` | `SWR` (software requirements), `SWA` (architecture), `SWTEST`, `SOUP`, etc. |

Add to this list when introducing new prefixes.

---

## Running the linter locally

```bash
# Lint all templates
python3 scripts/lint-template-frontmatter.py

# Lint a specific subdirectory
python3 scripts/lint-template-frontmatter.py templates/qms-hipaa
```

Exit code 0 = clean; exit code 1 = at least one error.

---

## What the schema does NOT validate (yet)

These are intentional gaps that map to other forward-work items in [`docs/compliance-architecture.md`](../compliance-architecture.md):

- **State-machine enforcement of status transitions** — forward-work P5 will add `draft → review → approved → effective → superseded` transition rules + hard-fail when an out-of-order transition appears
- **`addresses:` cross-check against in-module clause IDs** — currently done by `scripts/lint-module-yaml.py` from the module side; not by the template schema lint
- **`next_review` date drift** — no per-template warning when the date has passed (could be added; tracked as future improvement)
- **Reviewer-qualification linkage to `BUSINESS/regulatory_review_cadence.md`** — for regulatory-review-bearing templates only; intentionally manual today

---

## Linkage to other Open QMS controls

- **OQ-013** per-module validation harness — module YAML linting (in place since v0.40.0)
- **OQ-122** template frontmatter schema validation — this guide's subject (in place since v0.58.0)
- **`docs/guide/doc-control.md`** — consumes the schema-validated fields in the doc-control workflow
- **`scripts/lint-template-frontmatter.py`** — the linter itself; runs in CI as a pre-pytest gate
- **`engine/openqms/template_schema.py`** — schema definition; pure Python module with no external dependencies beyond PyYAML
