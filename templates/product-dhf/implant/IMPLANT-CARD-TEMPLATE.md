---
document_id: IC-XXX
title: "[Product Name] — Implant Card"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Regulatory Affairs, Title]"
status: draft
approved_by: "[QA / Medical Affairs Lead, Title]"
approval_date: YYYY-MM-DD
---

# IC-XXX: [Product Name] Implant Card

Per EU MDR 2017/745 Annex I §23.4 (information for patients with implants). The implant card is provided to the patient with the implanted device. The information must be written in a way easily understood by a lay person and translated into the official language(s) of the EU Member State(s) where the device is supplied.

The implant card is **mandatory for all implantable devices** under MDR, except where exempted by Article 18(3) (sutures, staples, dental fillings, dental braces, tooth crowns, screws, wedges, plates, wires, pins, clips, connectors).

## 1. Patient-facing implant card content

The physical card given to the patient shall contain:

### Section A — Device identification

- **Manufacturer name:** [legal name]
- **Manufacturer address:** [registered address]
- **Authorized representative (if outside EU):** [name + address]
- **Device name / model:** [brand name, model identifier]
- **Serial number / lot number / production date / expiry date** (as applicable): [unique identifiers for THIS implanted unit; populated at point of implantation]
- **UDI (Unique Device Identifier):** [UDI-DI + UDI-PI for the specific implanted unit]

### Section B — Cautions and precautions for the patient

[Plain-language list of:
- Activities or environments the patient should avoid (e.g. MRI compatibility, contact sports, certain electromagnetic environments).
- Expected device lifetime.
- Symptoms that indicate device malfunction and require medical attention.
- Anything that interferes with the device.]

### Section C — Healthcare professional contact

- **For device-related questions:** [manufacturer contact information for HCPs]
- **For adverse events:** [vigilance contact, EUDAMED reporting URL]

## 2. Information for patients (separate, accompanying document)

Per Annex I §23.4(d), additional information shall be made available to the patient, which can be:

- Information about whether the patient is to be informed of replacement frequency or anticipated lifetime.
- Information on devices used in combination (e.g. ICD leads with the ICD).
- Detailed information regarding compatibility with diagnostic procedures (MRI, CT, ultrasound interactions).

## 3. Implementation notes

- **Production-time population:** Serial-number, UDI-PI, lot-number, production-date, and expiry-date fields are populated at the point of manufacture / implantation. The implant card template ships with `[placeholder]` markers in those fields.
- **Translations:** The implant card must be provided in the official language(s) of the Member State where the device is supplied. Adopters maintain a translation matrix per Member State.
- **EUDAMED registration:** Implant cards (template version, not individual cards) may need to be registered in EUDAMED per Article 31.

## 4. Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Regulatory Affairs | | | |
| Medical Affairs | | | |
| QA | | | |

## 5. References

- EU MDR 2017/745 Article 18 — Implant card and information to be supplied to the patient with an implanted device.
- EU MDR 2017/745 Annex I §23.4 — Information supplied with the device (specifically for implants).
- MDCG 2019-8 rev 1 — Guidance document on implant card.
- Linked artifacts: SSCP-XXX (Summary of Safety and Clinical Performance), labeling spec, IFU.

## 6. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
