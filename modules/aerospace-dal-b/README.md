# Aerospace DAL-B — Open QMS class overlay

Class overlay on the **aerospace** vertical. DAL-B applies when the FHA classifies a failure condition as **Hazardous** — a large reduction in functional capabilities or safety margins, severe injuries to occupants, or excessive flight-crew workload such that they cannot be relied upon to perform tasks accurately.

## Scope

ARP4754A §5 allocation assigns DAL-B from the FHA's Hazardous classification.

## Standards covered

- DO-178C:2011 (software)
- DO-254:2000 (hardware)
- ARP4754A:2010

6 clauses encoding rigor delta:

| Element | DAL-B specifics |
|---|---|
| Structural coverage | **Decision Coverage (DC)** (DO-178C Table A-7 obj 6) — major delta from DAL-A's MC/DC |
| Independence | **14-of-69 objectives** (Annex A) |
| Tool qualification | TQL-1 or TQL-2 typical |
| Hardware verification | DO-254 §6.2 **elemental analysis** still required (DAL-B + DAL-A both) |
| ARP4754A allocation | Rationale traced from FHA Hazardous classification |

## Composition

```bash
openqms validate --module aerospace --module aerospace-dal-b
```

## When to use

Software / hardware allocated DAL-B per ARP4754A §5 from FHA Hazardous classification.

## When NOT to use

Lower-severity classifications (Major → DAL-C; Minor → DAL-D; No Safety Effect → DAL-E). Higher-severity (Catastrophic) requires DAL-A with MC/DC + 25-objective independence.

## Standards licensing

DO-178C + DO-254 + ARP4754A are commercially-published (RTCA / SAE International).

## Forward work

- DAL-B PSAC sub-template with decision-coverage reporting structure
- 14-objective independence matrix pre-populated
