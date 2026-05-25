---
document_id: LOG-SHIP-XXX
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Shipping / Logistics Lead]"
status: draft
---

# Dangerous Goods Shipping Paper

**Template for:** Multi-modal shipping paper / Multimodal Dangerous Goods Form per IMO/ILO/UNECE Guidelines — compatible with US DOT HMR shipping paper (49 CFR 172.202-205), IMDG DG Declaration (Part 5 Chapter 5.4), IATA Shipper's Declaration for Dangerous Goods (Section 8), ADR/RID shipping documentation (Part 5 Chapter 5.4).
**Scope:** All dangerous-goods shipments. Single-form approach reduces error risk vs. separate-per-mode forms when shipment travels multimodal.
**Compliance note:** For air shipments, IATA Shipper's Declaration Form 6300xx (red-diagonal-hatch bordered) is the regulator-preferred form; this template provides equivalent content for record-keeping + interline coordination.

---

## 1. Identification

| Field | Value |
|---|---|
| Shipping paper number | [unique per shipment] |
| Date | [YYYY-MM-DD] |
| Mode(s) of transport | [Road / Rail / Sea / Air / Multimodal — list all legs] |
| Booking / waybill / AWB / BoL reference | |

## 2. Shipper + Consignee

| Field | Shipper | Consignee |
|---|---|---|
| Name | | |
| Address | | |
| Country | | |
| 24-hour emergency response telephone (DOT §172.604) | | — |
| Contact during business hours | | |

## 3. Carrier(s)

| Leg | Mode | Carrier | Vehicle/Vessel/Flight | Departure | Arrival |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

## 4. Description of dangerous goods

Sequence required per DOT §172.202(a): **UN ID / Proper Shipping Name / Hazard Class or Division (subsidiary in parens) / Packing Group**. Add: Number + Type of packages, Net + Gross quantity, EmS code (IMDG), Tunnel code (ADR), Marine Pollutant indicator.

| Line | UN # | Proper Shipping Name (+ technical name for n.o.s.) | Class / Div. (sub.) | PG | # + type pkgs | Net qty | Gross qty | EmS (IMDG) | Tunnel (ADR) | Marine Poll. |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | UN | | | | | | | | | |
| 2 | UN | | | | | | | | | |
| 3 | UN | | | | | | | | | |

**Total dangerous goods.** Number of packages: [N]. Gross weight: [kg]. Net weight: [kg].

## 5. Special handling + segregation

| Item | Notes |
|---|---|
| Segregation requirements (IMDG §7.2.4 / ADR §7.5.2) | |
| Stowage category (IMDG §7.1) | |
| Limited-quantity exemption applies? (§3.4) | |
| Excepted-quantity exemption applies? (§3.5) | |
| Salvage packaging? | |
| Temperature control requirements | |

## 6. Air-mode supplement (only if any leg by air)

Per IATA DGR Section 8, additional fields required for air shipments:

| Field | Value |
|---|---|
| Aircraft variant (Passenger and Cargo / Cargo Aircraft Only) | |
| Airport of departure | |
| Airport of destination | |
| State + Operator variations applied | |
| Additional handling info | |
| All packed in one indication (if combination packaging) | |
| Overpack used + ID | |

## 7. Shipper's declaration / certification

**For US DOT shipments — §172.204(a):**

> I hereby declare that the contents of this consignment are fully and accurately described above by the proper shipping name, and are classified, packaged, marked and labeled/placarded, and are in all respects in proper condition for transport according to applicable international and national governmental regulations.

**For air shipments — IATA DGR §8.1.6.1 add:**

> I declare that all of the applicable air transport requirements have been met.

**For Cargo Aircraft Only shipments add:**

> This shipment is within the limitations prescribed for: ☐ Passenger and Cargo Aircraft ☐ Cargo Aircraft Only.

| Field | Value |
|---|---|
| Shipper name + title | |
| Shipper signature | |
| Date | |
| Place | |
| Telephone | |

## 8. Carrier acknowledgement

| Field | Value |
|---|---|
| Carrier name + agent | |
| Acceptance signature | |
| Date + time | |
| Place | |
| Acceptance check completed per IATA §9.6.1 / IMDG §5.4 / DOT §174.50? | ☐ Yes |
| Any non-conformances at acceptance + resolution | |

## 9. Emergency response telephone (DOT §172.604)

**24-hour-monitored emergency-response telephone number:** [number].

Telephone number is monitored at all times the hazardous material is in transportation, including storage incidental to transportation. Person answering has immediate access to comprehensive emergency-response information including the proper shipping name + hazard class + container size + nature of any other materials concurrently in shipment.

Registered service: [Chemtrec / Infotrac / 3E / in-house / other — name + contract number].

## 10. Attachments

- ERG (Emergency Response Guidebook) guide number(s): [numbers]
- SDS reference: [version + date for each dangerous good]
- Container Packing Certificate (IMDG §5.4.2 — if FCL/sealed unit)
- Approval certificates (special permits / Competent Authority approvals)

---

**Trace evidence.** This shipping paper addresses DOT-172-202-shipping-papers + IMDG-DG-declaration-5-4 + IATA-shippers-declaration-8 + ADR-RID-classification-Part-2 per `modules/transport-hazmat/module.yaml`.
