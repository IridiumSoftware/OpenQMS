# Open QMS engine

Python implementation of the Open QMS bundle resolver and per-module validation harness.

## Install

From the repo root:

```bash
pip install -e './engine[dev]'
```

This installs the `openqms` package and the `openqms` CLI entry point in editable mode, plus pytest for the test suite.

## CLI

### Resolve a bundle

```bash
openqms resolve \
  --product ExampleDevice \
  --jurisdiction FDA \
  --standard "ISO 13485:2016" \
  --standard "21 CFR 820" \
  --module medical-devices \
  --output traceability_matrix.json
```

Emits a JSON traceability matrix to the named file (or stdout if `--output -`). The matrix has five sections: `bundle`, `module`, `in_scope_clauses`, `artifacts`, and `traceability` (with `forward` and `reverse` maps).

`--jurisdiction`, `--standard`, and `--module` are all repeatable. When `--module` is given more than once, the engine **composes** the modules before resolution (see *Composition* below).

### Validate a module (or a composite)

```bash
openqms validate --module medical-devices
openqms validate --module medical-devices --module iso-27001
```

Loads each module from `modules/<name>/module.yaml`. With one `--module`, validates that single module. With multiple, composes them first and validates the composite. Checks that every clause is addressed by at least one template and no template addresses a non-existent clause. Exit code 0 on pass, 1 on invariant violation.

Equivalent via `python -m`:

```bash
python -m openqms validate --module medical-devices
```

### Standards-and-jurisdictions registry

Both `--standard` and `--jurisdiction` arguments are validated against the registry at `<repo>/registry/` (`standards.yaml` + `jurisdictions.yaml`). Unknown standards and jurisdictions raise rather than silently filtering to empty resolution. Aliases like `"ISO 13485"` are normalized to canonical ids like `"ISO 13485:2016"` before being passed to the resolver.

Inspect the registry:

```bash
openqms registry list
openqms registry show --id "ISO 13485"
openqms registry show --id FDA
```

`validate` also cross-checks the module's `standards:` list and per-clause `standard:` field against the registry. A module that references an unregistered standard fails validation with a specific error.

Escape hatch (skip standards validation; jurisdictions remain strictly validated):

```bash
openqms resolve --allow-unregistered-standards ...
openqms validate --allow-unregistered-standards ...
```

### Composition

`--module` is repeatable on both `resolve` and `validate`. The engine composes the modules via `openqms.module.compose` before doing its work. Composition rules:

- **Clauses** union by `id`. Duplicate IDs are silently absorbed if their content matches; conflicts (same ID, different content) raise.
- **Templates** union by `path`; their `addresses` lists are merged (deduped, first-seen order preserved). The template `name` from the first module wins.
- **Standards** are concatenated and deduped (first-seen order).
- The composite is **not** automatically validated; call `validate` if you want to check it.

Example end-to-end with the shipped medical-devices vertical and the iso-27001 cross-cutting overlay:

```bash
openqms resolve \
  --product ExampleSaMD \
  --jurisdiction FDA \
  --standard "ISO 13485:2016" \
  --standard "21 CFR 820" \
  --standard "ISO 14971:2019" \
  --standard "IEC 62304:2006+A1:2015" \
  --standard "ISO/IEC 27001:2022" \
  --module medical-devices \
  --module iso-27001 \
  --output traceability_matrix.json
```

The resulting matrix shows the quality-policy template addressing four clauses — two from medical-devices and two from the ISO 27001 overlay — because both modules bound that path.

## Tests

```bash
pytest engine/tests -v
```

The CI workflow at `.github/workflows/engine-tests.yml` runs the same suite on every push that touches `engine/`, `modules/`, or `templates/`.

## Architecture

The engine is intentionally small. Core types in `openqms/types.py` are frozen dataclasses:

- `Bundle` — input tuple `(product, jurisdictions, standards)`.
- `Module` — clause table + artifact templates + bindings, loaded from `module.yaml`.
- `ResolvedQMS` — output of the resolver: in-scope clauses, emitted artifacts, bidirectional traceability map.
- `ValidationReport` — output of the per-module validation harness.

The resolver in `openqms/resolver.py` is a pure function. Given `(bundle, module)` it filters the module's clause table to the standards in scope, selects every template that addresses at least one in-scope clause, and emits the traceability map. Same inputs → same outputs; no I/O; no mutation of inputs.

The validation harness in `openqms/validation.py` implements the OQ-001 invariant on a module:

- every clause in the module is addressed by at least one template (no orphaned clauses)
- every template's `addresses` entries resolve to clauses in the module (no orphaned artifacts)

The composition primitive `openqms.module.compose(list[Module]) -> Module` unions multiple modules into one. Clauses union by ID (conflicts raise); templates union by path with merged `addresses`; standards are deduped. The composite's invariant is checked by passing it to `validate` (composition itself does not validate).

The CLI in `openqms/cli.py` is a thin argparse wrapper over the three primitives.

## License

Apache-2.0. See `../LICENSE`.
