# pre-seed preset

**Stage assumptions:** 1-5 people, MVP product, no paying customers yet, no specific regulator yet.

**Module count:** 3 — `iso-31000` + `iso-27001` + `integrated-management-system`.

---

## What's IN

| Module | Why at pre-seed |
|---|---|
| `iso-31000` | Risk-management awareness substrate. Even without a single paying customer, the team must be able to identify + assess + communicate risks (technical, regulatory, market). ISO 31000 is the framework-agnostic risk vocabulary that travels with the team as the org grows. |
| `iso-27001` | Information security baseline. From day 1, the team has source code + customer leads + financial data. ISO 27001 Annex A controls are the universally-recognized baseline; even a 2-person team can implement controls proportionate to scope. |
| `integrated-management-system` | IMS substrate. As you add management systems later (privacy / quality / BCMS / etc.), the integrated-management-system overlay ensures they share policy + scope + audit-programme + management-review — avoiding the parallel-MS sprawl that swallows mid-stage QA teams. |

---

## What's NOT IN (intentionally)

| Not yet | Why deferred |
|---|---|
| Privacy regime | No customer data yet → no GDPR / CCPA scope. Add at `seed` when first customer signs. |
| Specific vertical (medical-devices / pharma / etc.) | Vertical-specific clauses encode regulator-imposed obligations that don't apply yet. Add at `seed` once vertical is committed. |
| Anti-bribery (ISO 37001) | No transactional surface large enough to materially trigger anti-bribery exposure. Add at `seed` when governance becomes visible to investors / customers. |
| BCMS (ISO 22301) | No service-availability commitments to customers yet. Add at `seed` when first customer SLA exists. |
| Cross-overlays (combination-product / connected-medical-device / etc.) | These encode intersection-specific regulatory requirements that only apply when the relevant verticals + cross-cuttings are all in scope. Premature. |
| Sub-overlays (SOC 2 types / CMMC levels / NIST CSF tiers) | These split rigor levels within a cross-cutting overlay; at pre-seed the parent overlay (ISO 27001) at baseline rigor is enough. |
| SOC 2 / HITRUST / formal certifications | Auditor engagement is expensive; certification before the first paying customer is sunk cost. Add when a customer explicitly asks. |

---

## Graduate to `seed` when

Any of:

- **First paying customer signs.** Their data is now under your care — privacy regime + BCMS scope start to apply.
- **Vertical commitment is made.** "We're a medical-device company" / "We're a pharma company" — the vertical's regulator obligations now apply.
- **First non-founder employee hired.** HR / training / supplier (you become someone's supplier) / governance considerations now apply.

---

## Compose with your vertical

The pre-seed preset is industry-agnostic. Adopters who know their vertical can layer it now:

```bash
# Pre-seed + medical-devices
openqms validate --module iso-31000 --module iso-27001 \
                 --module integrated-management-system \
                 --module medical-devices
```

But don't feel obligated. Adding the vertical at pre-seed buys regulatory clauses you won't yet need; deferring to seed is the lower-effort path most of the time.

---

## Adopter responsibility

A preset is a starting point, not a substitute for QA judgment. Specifically:

- The 3 modules are the *minimum* — adopter org may need to add (e.g., HIPAA if processing any PHI even pre-customer; ITAR / EAR if export-controlled tech).
- The preset assumes Apache-2.0-compatible licensing posture (referenced standards must be licensed by adopter per OQ-070 + OQ-071).
- The matrix baseline reflects the modules' state at v0.61.0 ship; drift over time is expected as modules evolve.

---

## Linkage

- [`presets/README.md`](README.md) — preset family index
- [`docs/guide/maturity-model.md`](../docs/guide/maturity-model.md) — cross-stage progression
- [`docs/compliance-architecture.md`](../docs/compliance-architecture.md) — trust-gate framing
- [`presets/pre-seed.yaml`](pre-seed.yaml) — the bundle YAML
- [`presets/pre-seed.matrix.json`](pre-seed.matrix.json) — committed resolved-matrix baseline
