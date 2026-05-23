# Open QMS — stored bundle definitions

A **bundle definition** pins the input tuple to the resolver: product identity, the jurisdictions and standards in scope, and the modules to compose. Storing the tuple as a versioned YAML file is what enables the `regenerate` workflow.

## Files

- `<name>.yaml` — the bundle definition. Required keys: `name`, `product`, `modules`. Optional: `jurisdictions`, `standards`.
- `<name>.matrix.json` — the resolved traceability matrix, written by `openqms regenerate --bundle <name> --write-matrix`. Committed; its Git diff is the regulatory audit trail.

## Workflow

```bash
# Dry-run: re-resolve and show what would change. Exit 1 if anything would change.
openqms regenerate --bundle example-samd

# Accept the change: write the new matrix and commit it.
openqms regenerate --bundle example-samd --write-matrix
git add bundles/example-samd.matrix.json
git commit -m "regenerate example-samd: ISO 14971:2026 supersedes 2019"
```

The dry-run gating in CI is what turns the matrix file into a regression-detection mechanism. If any module manifest, registry entry, or template binding change unexpectedly affects an in-flight bundle's resolution, the CI fails. The operator either reverts the module change or runs `--write-matrix` to accept the drift, and the commit is the audit-trail record of the decision.

## Edition supersession

The standards registry supports a `superseded_by` field on each entry. When a module references a standard whose registry entry carries `superseded_by`, the engine warns by default and errors under `--strict-editions`. Combined with the regenerate diff, this is how module-version drift gets surfaced (OQ-065 in the spec).
