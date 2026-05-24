# Aerospace DAL-E — Open QMS class overlay

Class overlay on the **aerospace** vertical. DAL-E applies when the FHA classifies a failure condition as **No Safety Effect** — a failure that does NOT affect aircraft operational capability or increase flight-crew workload.

## Scope

DAL-E is rare in practice because most software touched by the aircraft's certified configuration tends to be at least DAL-D. Typical DAL-E examples: cabin-management entertainment systems isolated from flight-critical busses; ground-only software.

## Standards covered

- DO-178C:2011 (software) — note: NO objectives apply at DAL-E
- ARP4754A:2010

4 clauses encoding the substantiation discipline:

| Element | DAL-E specifics |
|---|---|
| DO-178C process | **NO DO-178C objectives apply** at DAL-E (§2.2.4 + Tables A-1..A-10) — the software is not subject to DO-178C process discipline at all |
| Configuration management | Still required so cert authority can verify the deployed software matches what was DAL-E-classified |
| ARP4754A allocation | The No-Safety-Effect substantiation is the **load-bearing claim** — isolation from safety-critical busses + functions; failure-impact analysis showing no contribution to any safety goal |

## Composition

```bash
openqms validate --module aerospace --module aerospace-dal-e
```

## When to use

FHA classifies failure condition as No Safety Effect AND the substantiation (isolation + failure-impact analysis) is documented.

## When NOT to use

If there's any reasonable failure path that could contribute to a safety goal, even indirectly (e.g., shared resource contention; common-mode failure with adjacent system), DAL-D or higher applies. DAL-E substantiation is heavily scrutinized by certification authorities.

## Standards licensing

DO-178C + ARP4754A commercial.

## Forward work

- DAL-E No-Safety-Effect substantiation template (isolation argumentation + failure-impact analysis)
