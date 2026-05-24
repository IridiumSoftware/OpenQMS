# Companion — v0.39.0 `:argued → :tested` push (OQ-062 + OQ-067)

**Session date:** 2026-05-24
**Engine version transition:** 0.38.0 → 0.39.0
**Theme:** First evidence-floor advance since v0.13.0 (which introduced the 6 `:verified` entries). Two of seven `:argued` entries upgraded to `:tested` via new tests + a new CLI command — discharges the 2 tractable items from the 2026-05-24 audit `:argued` survey.

## §1 Computational basis

Single release at commit `5318fdd` on `main` (pushed). Files shipped:

```
engine/openqms/cli.py                         (+138 lines: _cmd_trace + _format_trace_markdown)
engine/tests/test_phi_compartmentalization.py (+118 lines, 4 tests)
engine/tests/test_trace.py                    (+82 lines, 4 tests)
.github/workflows/engine-tests.yml            (+7 lines: trace + zero-orphan CI step)
engine/openqms/__init__.py                    (version bump)
engine/pyproject.toml                         (version bump)
BUSINESS/ENGINE_SPEC.md                       (OQ-062 + OQ-067 rewrites + status counts + delta line)
BUSINESS/artifact_registry.md                 (2 row updates + counts)
BUSINESS/dashboard.md                         (tier breakdown + delta line)
BUSINESS/changelog.md                         (v0.39.0 entry)
```

Build commands (replayable from clean checkout):

```bash
source .venv-engine/bin/activate

# OQ-067 smoke
openqms trace --all                                        # JSON output
openqms trace --module chemicals --format md               # markdown sample
openqms trace --all --output /tmp/repo-wide-trace.json     # to file

# OQ-062 + OQ-067 tests
pytest engine/tests/test_phi_compartmentalization.py -v
pytest engine/tests/test_trace.py -v

# Full suite + bundle baseline checks
pytest engine/tests -q                                     # 116/116
```

## §2 Results

### OQ-062 PHI/PII compartmentalization — `:argued → :tested`

The v0.2.1 architectural decision committed Open QMS to never capturing PHI in repo issues. The decision was honest-effort `:argued` for a year — the prior note explicitly said *"upgrading to `:tested` would require a runtime check that no PHI patterns appear in issue bodies, which is out of scope."* That framing was incorrectly conservative — what we actually committed to is that the **template DESIGN** cannot capture PHI. That IS testable mechanically.

4 new structural property tests in `engine/tests/test_phi_compartmentalization.py`:

| Test | What it asserts |
|---|---|
| `test_complaint_template_loads_as_valid_yaml` | YAML well-formedness |
| `test_complaint_template_has_no_phi_fields` | No form field id/label matches PHI patterns (patient_name / mrn / ssn / dob / personal email / contact phone / mailing address) |
| `test_complaint_template_carries_phi_handling_warning` | Body markdown contains "PHI" + "PII" + "do not" warning trio |
| `test_complaint_template_references_external_phi_record` | Body or field text references external compartment (private / external / ephi / encrypted / restricted / eqms) |

These don't test runtime issue bodies (still out of scope; adopter infrastructure handles runtime hygiene per their SOP). They test the artifact-as-shipped — which is what OQ-062 was always claiming.

### OQ-067 repo-wide trace matrix — `:argued → :tested`

Original v0.1.0 spec text referenced a non-existent `./scripts/generate-trace-matrix.sh`. v0.1.1 removed the broken reference and re-cast as "forward work, ships with the engine." The forward work shipped at v0.39.0.

New CLI subcommand:

```
openqms trace [--module M | --all] [--format json|md] [--output FILE]
```

For each module in scope, emits forward map (clause → templates) + reverse map (template → clauses) + orphan detection (orphaned_clauses + orphaned_templates). Aggregate summary across all modules in scope: module count + total clauses + total templates + total clause→template addresses + total orphan counts.

JSON output for tooling; Markdown for audit-ready reports.

CI extended with a `Repo-wide trace matrix (smoke check + zero-orphan invariant)` step that runs `openqms trace --all` and asserts `orphaned_clauses_total == 0` and `orphaned_templates_total == 0`. This is the OQ-001 bidirectional traceability invariant **at scale** — every push verifies that no module ever leaves a clause without a template or a template without a clause-binding.

At v0.39.0 audit time `openqms trace --all` reports:

| Field | Value |
|---|---|
| modules_in_scope | 75 |
| total_clauses | 614 |
| total_templates | 299 |
| total_clause_addresses | 683 |
| orphaned_clauses_total | 0 |
| orphaned_templates_total | 0 |

Repo-wide OQ-001 invariant holds.

## §3 Verification

| OQ-NNN | Evidence type (was → is) | Test/artifact reference |
|---|---|---|
| OQ-062 | manual → example-tested | `engine/tests/test_phi_compartmentalization.py` (4 tests) + `.github/ISSUE_TEMPLATE/complaint.yml` |
| OQ-067 | manual → example-tested | `engine/tests/test_trace.py` (4 tests) + `engine/openqms/cli.py::_cmd_trace` + CI zero-orphan gate |

Both upgrades pass A4 status honesty per CLAUDE.md table — `example-tested` evidence supports `:tested` status (NOT `:verified` which requires property-tested or higher).

Could either move higher? Probably not without disproportionate effort. OQ-062 could in principle become `:verified` via a Hypothesis property test that generates random YAML form-spec mutations and asserts no PHI fields appear post-mutation — but the value-add over the 4 explicit tests is low and the generator is contrived. OQ-067 could become `:verified` via a property test that walks arbitrary module graphs and asserts the forward/reverse map bidirectionality property holds — borderline tractable but redundant with the existing OQ-001 property test which already proves the same property on the resolver output.

Honest stop point: `:tested` is the right ceiling here.

## §4 Spec impact

0 NEW entries; 2 status upgrades. Spec total unchanged at 91.

| Entry | Was | Now |
|---|---|---|
| OQ-062 | `:argued` (Gap, manual evidence) | `:tested` (Gap, example-tested evidence) |
| OQ-067 | `:argued` (Gap, manual evidence) | `:tested` (Gap, example-tested evidence) |

Status counts:
- v0.38.0: 6 `:verified` / 78 `:tested` / 7 `:argued` / 0 `:open`
- v0.39.0: 6 `:verified` / 80 `:tested` / **5 `:argued`** / 0 `:open`

Remaining 5 `:argued` are honest-effort-by-nature:
- **OQ-003** — invariant disclaimer ("generator emits unvalidated MVP"); meta-claim about what we do NOT validate; unfalsifiable by design
- **OQ-022** — Git history immutability under force-push-disabled config; adopter-org-gated (we can't test that an adopter's `main` has force-push disabled)
- **OQ-023** — GPG signing binds identity to content; adopter-org-gated (we can't test that an adopter's contributors have GPG keys)
- **OQ-070** — Modules cite clauses by number + summary; no redistribution; manual interpretation of where summary ends and redistribution begins
- **OQ-071** — Apache-2.0 doesn't extend to referenced standards; legal interpretation, not mechanical

None of these can move without leaving spec scope or making dishonest claims about what Open QMS controls.

## §5 Tests

Suite count: 108 → 116 (+8). 100% pass.

```
engine/tests/test_phi_compartmentalization.py (4 tests)
engine/tests/test_trace.py                    (4 tests)
```

All 8 bundle baselines clean post-release.

## §6 What changed in `openqms` CLI surface

New subcommand `trace`. Help text:

```
openqms trace --help
usage: openqms trace [-h] [--module MODULE] [--all] [--format {json,md}]
                     [--output OUTPUT]

options:
  --module MODULE     Module name or path to module.yaml. Repeatable.
                      If omitted (or --all), every module under
                      ./modules/ is included.
  --all               Include every module under ./modules/.
  --format {json,md}  Output format: json (default) or md.
  --output OUTPUT     Output path. Default: stdout.
```

Existing subcommands unchanged: `resolve`, `validate`, `regenerate`, `signatures`, `registry`.

## §7 Acceptance + close-out

v0.39.0 shipped (commit `5318fdd`, pushed `885142e..5318fdd  main -> main`). CI green expected on next push (zero-orphan invariant new gate). `:argued` count at the honest floor — 2 tractable items closed, 5 by-nature items remain.

Per user direction "do OQ-062 and OQ-067" — both shipped.

---

*Companion doc per TCE evidence-discipline; small-session shape (single release, narrow scope). Update `companion_index.md` to add this row.*
