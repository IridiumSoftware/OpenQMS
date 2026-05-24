# recall-workflow — Open QMS cross-vertical overlay

Cross-vertical product-recall workflow covering four regulatory frameworks: **NHTSA** (automotive) + **FDA** (medical devices + pharma + food) + **CPSC** (consumer products). Composes with ANY vertical needing recall discipline.

## Scope

11 clauses across 6 standards (all PUBLIC license):

| Framework | Standards | Notification window |
|---|---|---|
| **NHTSA automotive** | 49 CFR 573 + 577 + 579 (TREAD EWR) | DIR within 5 working days |
| **FDA general** | 21 CFR 7 | Class I/II/III + effectiveness checks A/B/C |
| **FDA medical devices** | 21 CFR 806 (Reports of Corrections + Removals) | Within 10 working days |
| **FDA pharmaceuticals** | 21 CFR 314.81(b)(1)(ii) Field Alert | Within 3 working days |
| **FDA food** | 21 CFR 117 Subpart D + 21 USC §350f Reportable Food Registry | 24 hours for Class I |
| **CPSC consumer products** | CPSIA §15 / 15 USC §2064(b) | 24 hours of obtaining info reasonably supporting conclusion |

## Architectural decision

Shipped as one cross-cutting overlay rather than 4 per-vertical class overlays because the recall procedure SHAPE is essentially identical across frameworks (decision flow + classification + regulator notification + customer notification + effectiveness checks + recovery + root cause + closure) — only the classification scheme + notification windows + notification content differ, which are parametrized in the Generalized Recall Procedure template.

## Templates introduced

- **`templates/qms-recall/GENERALIZED-RECALL-PROCEDURE-TEMPLATE.md`** — cross-vertical with framework-specific notification table; 11-role 24/7 Recall Team; hour-0 trigger + decision flow; hour-1-24 actions (product hold + distribution-list extraction + framework-specific regulator notification + customer notification + press release + crisis-line); hour-24-168 (effectiveness + recovery + daily status); hour-168+ (root cause + CAPA + closure); TREAD §579 EWR section for automotive; mock-recall annual cadence
- **`templates/qms-recall/NHTSA-OWNER-NOTIFICATION-TEMPLATE.md`** — automotive-specific 49 CFR 577 owner notification letter with all 10 §577.5 mandatory elements + §577.7 60-day timing + §577.8 second notification at <70% completion at 6 months + §577.9 reimbursement

## Composition

```bash
openqms validate --module automotive --module recall-workflow
openqms validate --module medical-devices --module recall-workflow
openqms validate --module manufacturing --module recall-workflow   # consumer products under CPSIA
openqms validate --module food-safety --module recall-workflow
```

10-module deepest composite validates: `automotive + automotive-asil-d + automotive-cal-4 + recall-workflow + regulated-ai + iso-27001 + iso-14001 + iso-45001 + iso-50001 + iso-22301`.

## When to use

Any vertical with recall obligations under the four frameworks. Food-safety vertical already has its own internal recall template; composing with recall-workflow adds the cross-vertical generalized procedure + (where relevant) NHTSA / FDA medical-device / CPSIA specific clauses beyond food.

## Standards licensing

All cited regulations are PUBLIC license (US federal regulations via ecfr.gov; statutes via USC).

## Forward work

- EU Article 19 General Product Safety Regulation 2023/988 standalone overlay
- FDA pharma Field Alert Report 21 CFR 314.81 dedicated workflow template
- Product-liability insurance claim coordination workflow
- Class-action litigation hold integration template
