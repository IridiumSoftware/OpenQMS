# Aerospace DAL-D — Open QMS class overlay

Class overlay on the **aerospace** vertical. DAL-D applies when the FHA classifies a failure condition as **Minor** — slight reduction in functional capabilities or safety margins, slight increase in flight-crew workload, or physical discomfort to occupants.

## Scope

Typical for advisory / supervised / non-critical automation functions where consequences of failure are limited.

## Standards covered

- DO-178C:2011 (software)
- DO-254:2000 (hardware)
- ARP4754A:2010

5 clauses encoding the light-process rigor:

| Element | DAL-D specifics |
|---|---|
| Structural coverage | **None required** at any level (no statement / decision / MC/DC) |
| Independence | **2-of-26 objectives** — typically QA + SCM independence from the development activity |
| Tool qualification | TQL-4 or TQL-5 (lowest assurance tiers; many DAL-D projects use no qualified tools at all) |
| Hardware | Standard test + review activities; no DO-254 §6.2 elemental analysis |

Software testing focuses on requirements-based test cases per DO-178C §6.4.3 (Normal-Range + Robustness).

## Composition

```bash
openqms validate --module aerospace --module aerospace-dal-d
```

## When to use

FHA Minor classification → DAL-D allocation per ARP4754A §5.

## When NOT to use

If failure could cause more than Minor consequences, DAL-C or higher applies.

## Standards licensing

DO-178C + DO-254 + ARP4754A commercial.

## Forward work

- DAL-D PSAC sub-template (minimal content reflecting light-process scope)
