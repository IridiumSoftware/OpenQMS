# Aerospace DAL-C — Open QMS class overlay

Class overlay on the **aerospace** vertical. DAL-C applies when the FHA classifies a failure condition as **Major** — significant reduction in functional capabilities, significant increase in flight-crew workload, or some discomfort to occupants.

**Most common DAL for production avionics functions** that are supervised by a higher-DAL function OR perform non-critical automation. The 2-of-62 independence requirement is substantially lighter than DAL-A/B, which is why so much production avionics targets DAL-C explicitly.

## Scope

ARP4754A §5 allocation assigns DAL-C from the FHA's Major classification. §3.5 decomposition is commonly invoked to allocate a higher DAL (B or A) into multiple DAL-C elements with independence argumentation — a frequent practical optimization.

## Standards covered

- DO-178C:2011 (software)
- DO-254:2000 (hardware) — note: DAL-C does NOT require DO-254 §6.2 elemental analysis (delta from DAL-A/B)
- ARP4754A:2010

5 clauses encoding rigor delta:

| Element | DAL-C specifics |
|---|---|
| Structural coverage | **Statement Coverage** (DO-178C Table A-7 obj 7) — major delta from DAL-B's Decision Coverage |
| Independence | **2-of-62 objectives** (Annex A) — substantial cost-of-process reduction |
| Tool qualification | TQL-3 or TQL-4 typical |
| ARP4754A allocation | Rationale traced from FHA Major OR §3.5 decomposition argumentation |

## Composition

```bash
openqms validate --module aerospace --module aerospace-dal-c
```

## When to use

Software / hardware allocated DAL-C per FHA Major OR per §3.5 decomposition from higher DAL.

## When NOT to use

If FHA Major was assigned but the function is supervised by an independent monitor allocated at higher DAL, the §3.5 decomposition may still result in DAL-C — but the supervisor must meet its own DAL.

## Standards licensing

DO-178C + DO-254 + ARP4754A commercial (RTCA / SAE International).

## Forward work

- §3.5 decomposition argumentation template
- DAL-C PSAC sub-template
