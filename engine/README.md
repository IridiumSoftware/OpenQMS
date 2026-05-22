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

`--jurisdiction` and `--standard` are repeatable. `--module` accepts either a module name (looked up under `./modules/<name>/module.yaml`) or a path to a manifest file.

### Validate a module

```bash
openqms validate --module medical-devices
```

Loads the module manifest at `modules/<name>/module.yaml`, checks that every clause is addressed by at least one template and no template addresses a non-existent clause. Exit code 0 on pass, 1 on invariant violation.

Equivalent via `python -m`:

```bash
python -m openqms validate --module medical-devices
```

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

The CLI in `openqms/cli.py` is a thin argparse wrapper over the two.

## License

Apache-2.0. See `../LICENSE`.
