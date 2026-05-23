# Open QMS standards-and-jurisdictions registry

Versioned, repo-tracked catalog of every standard and jurisdiction the engine knows about. Two files:

- `standards.yaml` — every standard, regulation, program, or guidance document. Carries publisher, edition, license kind, and accepted aliases.
- `jurisdictions.yaml` — every supported jurisdiction with the standards typically in scope there.

Implements **OQ-014** (standards-and-jurisdictions registry is versioned and immutable). Git history is the version; immutability comes from the engine treating the loaded registry as read-only.

## Why a registry

Without it, `openqms resolve --standard "ISO 13485:2017"` (typo or wrong edition) silently produces an empty traceability matrix — the resolver filters clauses by string match and no clause matches. With it, the same command raises immediately and lists the registered standards.

The registry also normalizes aliases. Users can type `--standard "ISO 13485"`; the CLI resolves to the canonical `"ISO 13485:2016"` before passing to the resolver.

## CLI integration

By default, both `--standard` and `--jurisdiction` arguments are validated against the registry. Pass `--allow-unregistered-standards` to skip standards validation (jurisdictions remain strictly validated).

```bash
openqms registry list                  # list everything registered
openqms registry show "ISO 13485"      # show details for one standard or jurisdiction
```

## Adding entries

Open a PR adding the new entry to `standards.yaml` or `jurisdictions.yaml`. Every standard entry must carry: `id`, `name`, `publisher`, `edition`, `kind` (`standard` / `regulation` / `program` / `guidance`), `license_kind` (`commercial` / `public`), and an `aliases` list (may be empty). Every jurisdiction entry must carry: `id`, `name`, `region`, and `applicable_standards` (each entry must already be in `standards.yaml`).

The CI workflow `engine-tests.yml` exercises the registry on every push that touches `engine/`, `modules/`, `templates/`, or `registry/` — module manifests are cross-checked against the registry, and the registry's own jurisdiction → standard references are verified.

## Standards licensing

This registry contains canonical identifiers and normative metadata only. Standard texts themselves are not redistributed here. Adopters implementing against any commercially-published standard must obtain their own licensed copies per the publisher's license terms. See the repo-root `README.md` "Standards licensing — important" section.
