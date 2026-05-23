# Complaint handling

ISO 13485 §8.2.2 (feedback), 21 CFR 820.198 (complaint files), and EU MDR Articles 87–89 (vigilance) require structured intake, investigation, regulatory-reporting assessment, and retention of complaint records. Open QMS provides the intake template and CI infrastructure; **PHI/PII handling is an architectural decision the adopting organization makes**, documented below.

## Architecture decision: compartmentalize PHI/PII

Customer complaints and adverse-event reports routinely contain patient identifiers, complainant names and contact information, device serial-to-patient mappings, and other PHI/PII. GitHub repository-level access control (read/write/admin) is too coarse to safely keep these records in the same repository as the rest of the QMS — anyone with read access to the main repo can read every issue.

Open QMS's recommended architecture is to **compartmentalize PHI/PII into a separate access-restricted record**. The complaint intake template (`.github/ISSUE_TEMPLATE/complaint.yml`) captures only the triage metadata needed to dispatch and track; PHI-bearing detail lives elsewhere and is referenced from the issue by ID or path.

### Two compartmentalization patterns

**Pattern A — Sibling private repository.** Create `<org>/<product>-complaints-private` as a separate GitHub repo with restricted team membership. PHI-bearing complaint detail (complainant identity, contact, patient identifiers, full investigation records) lives there as controlled documents under the same Git discipline as the rest of the QMS. The main repo's complaint intake issue references the sibling-repo record by URL or document ID.

- *Benefits:* same Git/GitHub substrate; same review/approval discipline; same audit trail mechanism; familiar to engineering teams already on Open QMS.
- *Costs:* doubles CODEOWNERS / team management surface; requires discipline about cross-repo references; backup strategy must cover both repos.

**Pattern B — External eQMS or encrypted document store.** PHI-bearing complaint detail lives in a commercial eQMS, encrypted SharePoint/Box folder, or HIPAA-compliant document management system. The main repo's complaint intake issue references the external record by ID or URL.

- *Benefits:* external tooling typically ships with finer-grained access controls, built-in PHI handling, and audit-trail features designed for healthcare records.
- *Costs:* leaves the all-on-Git posture; auditors must follow links to verify evidence; introduces an external dependency outside the validated GitHub substrate.

Both patterns satisfy the regulatory requirements. Choose based on your organization's existing tooling and risk appetite. **Document the choice in your complaint-handling SOP** so that future personnel know where PHI-bearing records live.

## What's in this repo

- **Intake template** — `.github/ISSUE_TEMPLATE/complaint.yml`. Captures product, date received, source, severity, PHI-redacted description, regulatory reportability assessment, CAPA linkage, and a required PHI-handling confirmation.
- **Labels** — `complaint`, `complaint-open` (set automatically by the template).
- **Module binding** — the medical-devices regulatory module (`modules/medical-devices/module.yaml`) binds the complaint template to ISO 13485 §8.2.2 and 21 CFR 820.198.

## What's NOT in this repo

- Patient identifiers, complainant names, contact information, device serial-to-patient mappings, full clinical investigation records, or any other PHI/PII content. Route to your chosen compartmentalization pattern.

## Workflow

1. **Intake.** Anyone with issue-create permission opens a complaint issue using the template. The two PHI-handling confirmation checkboxes are required.
2. **Triage.** Assigned reviewer (per CODEOWNERS or label routing) assesses severity and regulatory reportability.
3. **Investigation.** Detailed investigation is captured in the PHI-bearing record (Pattern A: linked private repo; Pattern B: external eQMS). The main repo issue tracks status and references.
4. **CAPA dispatch.** If the investigation determines corrective action is warranted, open a CAPA issue (`capa.yml`) and link both ways (the complaint issue references the CAPA, the CAPA references the complaint).
5. **Regulatory reporting.** If reportable (MDR / Vigilance / MDPR / equivalent), the reporting record itself lives in the PHI-bearing artifact and follows the jurisdiction's submission process. The main repo issue tracks reporting status (submitted / acknowledged / closed).
6. **Closure.** Issue closed when investigation is complete, CAPA dispatched (if applicable), regulatory reporting complete (if applicable), and the PHI-bearing record is updated. Retention follows the organization's record-retention SOP (typically 15+ years for medical devices).

## Gotchas

- **The template's `description` field is "PHI-redacted".** If a reporter accidentally pastes PHI into the description, edit the issue and accept that Git history retains the original. For high-confidentiality contexts, prefer Pattern B (external eQMS) where the intake itself happens outside GitHub.
- **Issue email notifications.** GitHub issue creation triggers notifications to watchers and assignees. If your team subscribes via email, scrub the template body before notifications fire, or route complaint intake through a secure form that creates the issue server-side.
- **Closed issues retain content.** Closing an issue does not remove its content. If PHI was accidentally pasted, you need to edit the issue (and notify your privacy officer if your retention/notification policy requires).
- **Cross-repo linkage discipline.** Pattern A relies on linking from the main-repo issue to the private-repo record. If the private-repo URL changes (e.g. renamed), the link breaks. Use document IDs in addition to URLs.
