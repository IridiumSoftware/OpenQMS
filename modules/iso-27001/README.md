# Open QMS — ISO/IEC 27001 cross-cutting overlay module

First overlay module shipped with Open QMS. Demonstrates the engine's multi-module composition primitive (`openqms.module.compose`) by adding information-security clauses that compose with any vertical regulatory module.

## Status (v0.1.0)

`module.yaml` is a **minimal seed** demonstrating composition. It declares three Annex A controls in-scope and binds them to existing OpenQMS templates already used by the medical-devices module:

| Clause | Title | Bound templates |
|---|---|---|
| `ISO27001-A.5.1` | Policies for information security | Quality policy |
| `ISO27001-A.5.31` | Legal / regulatory / contractual requirements | Quality policy, SOP template |
| `ISO27001-A.8.31` | Separation of dev / test / production environments | Software release record |

Each bound template *also* appears in the medical-devices module manifest with its own clause bindings. When the two modules are composed, the templates' `addresses` lists are unioned — for example, the quality-policy template ends up addressing four clauses: `ISO13485-4.2.4`, `CFR820-820.40` (from medical-devices) plus `ISO27001-A.5.1`, `ISO27001-A.5.31` (from this overlay).

## Use it via composition

The CLI's `--module` argument is repeatable. Compose medical-devices + iso-27001 to resolve a SaMD bundle that also takes infosec posture into account:

```bash
openqms resolve \
  --product ExampleDevice \
  --jurisdiction FDA \
  --standard "ISO 13485:2016" \
  --standard "21 CFR 820" \
  --standard "ISO/IEC 27001:2022" \
  --module medical-devices \
  --module iso-27001 \
  --output traceability_matrix.json
```

The validation harness similarly accepts multiple `--module` arguments and runs against the composite:

```bash
openqms validate --module medical-devices --module iso-27001
```

## Coverage roadmap

The shipped seed covers 3 of ISO/IEC 27001:2022's ~93 Annex A controls. The full Annex A surface (organizational / people / physical / technological controls) requires either:

- Adding more clause-to-template bindings as new OpenQMS templates land (e.g. an access-control SOP template would bind to A.5.15, A.5.16, A.8.2, A.8.3).
- Composing with adopter-maintained extension manifests that add overlay-specific templates.

## Standards licensing

Clauses are referenced by number and normative paraphrase only. ISO/IEC 27001:2022 itself is not redistributed here. Adopters implementing against ISO 27001 must obtain a licensed copy from ISO or a national member body. See the repo-root `README.md` "Standards licensing — important" section.
