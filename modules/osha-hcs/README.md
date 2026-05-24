# OSHA HazCom (HCS) — Open QMS cross-cutting overlay

20th Open QMS cross-cutting overlay. **US workplace hazard-communication discipline** per 29 CFR 1910.1200 (Hazard Communication Standard, HCS 2024 final rule).

## Scope

US workplaces where employees may be exposed to hazardous chemicals — broad scope including but not limited to:

- Chemicals (primary)
- Pharma + ATMP — solvents, reagents, cleaning agents, intermediates
- Food-safety + food-processing — sanitisers, lubricants, refrigerants
- Manufacturing + machine shops — coolants, cutting fluids, paints, adhesives, plating chemistries
- Automotive — battery electrolytes, paints, brake fluids, ECU rework chemistries
- Aerospace — composites resins, hydraulic fluids, sealants, primers, anodising
- Medical devices — cleaning + sterilisation chemistries, manufacturing solvents

If your US workforce handles any hazardous chemical (almost every site), HCS applies.

## Standards covered

**1 PUBLIC standard:**

- **29 CFR 1910.1200** — OSHA Hazard Communication Standard. HCS 2024 final rule (May 2024 amendments) aligns US HazCom with UN GHS Rev. 7. Mandatory compliance dates: substance manufacturer/importer **2026-01-19**; mixture manufacturer/importer **2027-07-19**.

9 clauses across the regulation:

- §(e) Written Hazard Communication Program
- §(f) Labels + other forms of warning (incl. workplace labels + portable container exemption + pipe marking)
- §(g) Safety Data Sheets access + maintenance
- §(h) Employee information + training
- §(i) Trade secrets
- Appendix A Health hazard criteria (10 classes)
- Appendix B Physical hazard criteria (17 classes)
- Appendix C Allocation of label elements (H/P codes + pictograms)
- Appendix D SDS 16-section content

## Templates introduced

1 new template:

- **`templates/qms-ohs/HAZCOM-WRITTEN-PROGRAM-TEMPLATE.md`** — required §(e) artifact. Site-specific written program covering chemical inventory + non-routine task hazard communication + multi-employer + contractor information + program evaluation cadence. Forms-not-content.

Plus 1 cross-cutting template binding:

- **`templates/product-chemicals/sds/SAFETY-DATA-SHEET-TEMPLATE.md`** — shared with chemicals vertical. 16-section format already satisfies HCS Appendix D + UN GHS Annex 4 + REACH Annex II + EU CLP, so the same template covers both sender (chemicals) and receiver (osha-hcs) sides.

## Composition with verticals + overlays

Composes cleanly with all 7 verticals + most cross-cutting overlays. Particularly natural compositions:

- **`chemicals + osha-hcs`** — receiver-and-sender complete picture: chemicals encodes REACH/CLP/GHS SDS authoring obligations; osha-hcs encodes US workplace receiver obligations (written program + access + training).
- **`pharma + osha-hcs`** — pharma manufacturing sites have material workplace chemical exposure (solvents, reagents, cleaning chemistries).
- **`manufacturing + osha-hcs`** — general manufacturing operations universally trigger HazCom.
- **`automotive + osha-hcs`** — assembly + battery operations + paint + ECU rework.
- **`food-safety + osha-hcs`** — sanitisers + lubricants + ammonia refrigerant scope.
- **`iso-45001 + osha-hcs`** — ISO 45001 organisational OH&S management system + HazCom as a specific chemical-hazard control program. Natural pairing.

## Relationship to chemicals vertical

The chemicals vertical and osha-hcs overlay are **complementary, not duplicative**:

- **Chemicals** encodes the *sender* side: REACH Article 31 + UN GHS Annex 4 + CLP — what an authoring manufacturer must produce.
- **OSHA HCS** encodes the *receiver* side: written program + workplace label + SDS access during each shift + employee training before assignment.

A US chemical manufacturer should adopt BOTH (chemicals for outbound product compliance; osha-hcs for workforce protection at the manufacturing site).

A non-chemical-manufacturing US site (e.g., a machine shop using purchased coolants + cutting fluids) needs ONLY osha-hcs (not chemicals — the site is not placing chemicals on the market, only consuming them as inputs).

## When to use + when NOT to use

**Use when:**
- Any US workplace location where employees handle hazardous chemicals (almost every site)
- Pursuing OSHA HCS compliance per HCS 2024 alignment with UN GHS Rev. 7
- Want a baseline written program template + training discipline + SDS-access workflow

**Do not use when:**
- Non-US operations exclusively (use chemicals vertical + jurisdiction-appropriate workplace overlay; e.g., COSHH for UK / GefStoffV for Germany — both forward work)
- Site has zero chemical exposure (rare but possible for pure-software offices that outsource all cleaning to a contractor and have no chemical-using equipment)

## Forward work

- UK COSHH (Control of Substances Hazardous to Health Regulations 2002) overlay
- Germany GefStoffV (Gefahrstoffverordnung) overlay
- Canada WHMIS 2015 (Workplace Hazardous Materials Information System; HazCom alignment with GHS) overlay
- EU CAD (Chemical Agents Directive 98/24/EC) + CMRD (Carcinogens, Mutagens, Reprotoxic Directive 2004/37/EC) overlay
- Annex G machinery exposure scenarios per ISO 11014 detailed work
