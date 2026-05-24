# Manufacturing — Open QMS vertical module

Vertical regulatory module for **general (non-regulated) manufacturing** — machine shops, tooling, contract manufacturing, custom fab, job shops, fabrication houses, prototyping shops, light industrial manufacturing.

This is the baseline ISO 9001 QMS for organizations whose products do NOT fall under a domain-specific regulatory framework (medical devices, aerospace, automotive, food, pharma, defense) but who still need a credible QMS for customer credibility, competitive positioning, or contractual flow-down from regulated customers.

## Scope

This module covers **ISO 9001:2015 only** — the only standard required for general-manufacturing scope. 17 clauses across the seven clause groups:

- **§4 Context of the organization** — context analysis (§4.1) + process approach (§4.4).
- **§5 Leadership** — leadership commitment (§5.1) + quality policy (§5.2).
- **§6 Planning** — risk-and-opportunity actions (§6.1) — the "risk-based thinking" core of ISO 9001:2015.
- **§7 Support** — resources (§7.1), measurement traceability (§7.1.5.2), communication (§7.4), documented information (§7.5).
- **§8 Operation** — operational planning + control (§8.1), supplier controls (§8.4), production + service provision (§8.5), post-delivery activities (§8.5.5), control of nonconforming outputs (§8.7).
- **§9 Performance evaluation** — monitoring + measurement + analysis (§9.1), internal audit (§9.2), management review (§9.3).
- **§10 Improvement** — nonconformity + corrective action (§10.2).

## Why this vertical exists

Until v0.17.0, Open QMS shipped vertical modules only for regulated industries (medical-devices, aerospace, automotive). Organizations doing general manufacturing — the machine shop down the street, the tooling supplier, the contract manufacturer that builds parts for any customer who walks in the door — had no entry point. They didn't need the full machinery of MDR / DO-178C / IATF 16949, but they did want a credible ISO 9001 scaffold.

This vertical fills that gap. It's deliberately the smallest vertical in the project: ISO 9001 only, no domain-specific extensions, all bindings to cross-cutting templates that already ship.

## Composition with overlays

Composes cleanly with cross-cutting overlays where the organization needs additional discipline:

- **`iso-27001`** — for organizations also pursuing information-security certification (e.g., custom manufacturers handling customer proprietary designs).
- **`regulated-ai`** — if any production process uses ML (predictive maintenance, computer-vision quality inspection, ML-driven CNC parameter optimization).

The manufacturing module does NOT define class overlays of its own — ISO 9001 has no equivalent of DAL / ASIL / CAL rigor tiers. Organizations needing higher rigor typically migrate up to a regulated vertical (aerospace → AS9100D; automotive → IATF 16949; medical-devices → ISO 13485) rather than overlaying a class on top of the base ISO 9001.

## What is intentionally NOT in scope

- **Industry-specific QMS standards** — AS9100D (aerospace), IATF 16949 (automotive), ISO 13485 (medical devices). Each is its own vertical because it adds substantively to the ISO 9001 baseline.
- **Food safety** — ISO 22000, FSSC 22000, HACCP. Forward vertical.
- **Pharma GMP** — ICH Q7 (API), 21 CFR 210/211 (US), EudraLex Vol. 4 (EU), PIC/S Annex 1 (sterile). Forward vertical.
- **Environmental management** — ISO 14001. Forward overlay (likely cross-cutting since it composes with any vertical).
- **Occupational health + safety** — ISO 45001. Forward overlay (cross-cutting).
- **Energy management** — ISO 50001. Forward overlay.
- **Anti-bribery** — ISO 37001. Forward overlay.

## Adoption guidance

If your organization:

- Manufactures parts for **any-and-all customers** including regulated industries (aerospace primes, OEMs, medical OEMs) → **use this module to start**, then consider migrating to or composing the domain-specific vertical when a regulated customer requires it. Many job shops live indefinitely on ISO 9001 alone, accepting customer-flowed-down requirements (PPAP submissions for automotive parts; AS9102 FAI for aerospace parts) without needing the full IATF / AS9100D registration.
- Has a **single regulated customer base** → use the corresponding vertical directly (`modules/automotive/`, `modules/aerospace/`, `modules/medical-devices/`). The vertical includes ISO 9001 as its substrate.
- Is a **contract software developer** → ISO 9001 is appropriate; consider composing `iso-27001` for IS posture and `regulated-ai` if developing ML products.

## Standards licensing

Open QMS references ISO 9001:2015 by clause number and normative summary only. ISO 9001:2015 is a commercially-published copyrighted work sold by ISO / national member bodies (US: ANSI; UK: BSI; etc.). Adopters obtain their own licensed copies. See repo-root `README.md` "Standards licensing — important" for the broader licensing posture.

## Forward work

- **Quality manual template** — many ISO 9001 adopters maintain a top-level quality manual that pulls together the §4.1 context, §4.4 process map, §5.2 policy, and pointers to all other documented information. Currently the existing `quality-policy.md` template covers §5.2 only; a `QUALITY-MANUAL-TEMPLATE.md` consolidating §4 + §5 + §6 references would streamline adoption.
- **Process map template** — §4.4 requires the organization to determine + document the sequence + interaction of QMS processes. A `PROCESS-MAP-TEMPLATE.md` (matrix or flow diagram) would help.
- **Risk-and-opportunity register template** — §6.1 needs documented information on what risks + opportunities were identified, what actions were planned, and how effectiveness was evaluated. Currently bound to SOP-TEMPLATE.md as a placeholder; a dedicated template would improve adoption.
- **Forward verticals** — food safety (ISO 22000), pharma GMP (ICH Q7 + 21 CFR 210/211), industrial machinery + functional safety (IEC 61508 / ISO 13849 for non-automotive non-aerospace safety-of-machinery), construction QMS.
