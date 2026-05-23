---
document_id: SOUP-XXX-001
title: "[Software Item Name] — SOUP Register"
version: "1.0"
effective_date: YYYY-MM-DD
owner: "[Software Lead, Title]"
status: draft
approved_by: "[Software / QA Lead, Title]"
approval_date: YYYY-MM-DD
---

# SOUP-XXX-001: [Software Item Name] Software-of-Unknown-Provenance Register

Per IEC 62304 §5.3.3, §8.1.2, §8.2.2, §9.

## 1. Scope

[Lists every SOUP item incorporated into the software item — operating systems, libraries, frameworks, drivers, third-party services. SOUP = software that was not developed for the purpose of being incorporated into the medical device AND for which adequate records of development processes are not available.]

- **Software item:** [name + version]
- **Update cadence:** [how often this register is reviewed — typically per release + on Dependabot/CVE trigger]

## 2. SOUP item register

| ID | Name | Version | Source | License | Function in system | Required performance | Hardware/SW requirements assumed | Known anomalies / CVEs | Risk classification |
|---|---|---|---|---|---|---|---|---|---|
| SOUP-001 | [OpenSSL] | [3.0.13] | [openssl.org] | [Apache-2.0] | [TLS for telemetry] | [no known cryptographic weakness in ciphers used] | [POSIX, ≥256MB RAM] | [CVE-XXXX-YYYY — N/A: workaround documented] | [Medium — bounded by network segmentation] |

## 3. SOUP risk analysis methodology

[Per IEC 62304 §7.1.3 — for each SOUP item, evaluate its potential failure modes and the consequences if those failures propagated into the medical device. Document the analysis approach (e.g., FMEA against published CVE database + vendor anomaly list + in-house testing).]

## 4. SOUP update / monitoring procedure

[Per IEC 62304 §8.2.2 — describe how new versions, security advisories, and anomaly disclosures are monitored and acted on. Typical mechanisms: Dependabot or equivalent CVE feed subscription; quarterly registered-version review; vendor security mailing-list subscriptions.]

## 5. SOUP problem reports

[Per IEC 62304 §9 — log of SOUP-related problems discovered post-release. Each entry references the issue/PR that addressed it and the resulting CAPA if applicable.]

| Date | SOUP item | Issue | Linked problem report | Disposition |
|---|---|---|---|---|

## 6. References

- IEC 62304:2006+A1:2015 §5.3.3, §8.1.2, §8.2.2, §9.
- Linked artifacts: SAD-XXX-001; RMF-XXX-001.

## 7. Revision history

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Name] | Initial release. |
