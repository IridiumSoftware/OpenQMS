# Configuration

## CODEOWNERS

The `CODEOWNERS` file controls who must approve changes to controlled documents. Map each QMS directory to the appropriate reviewers:

```
qms-policy/    @my-org/quality-leadership
qms-sops/      @my-org/quality-team
product-*/     @my-org/engineering-lead @my-org/quality-team
```

GitHub will automatically request reviews from these teams when a PR touches their paths.

## QMS Config

`docs/qms-config.yml` controls automation behavior:

- **trainees:** GitHub usernames who receive training assignments when SOPs change
- **document_prefix:** Prefix for document numbering
- **retention_years:** Default retention period for quality records
- **regulatory_modules:** Which regulatory modules are active

## Branch Protection

The setup script configures:

- Require PR reviews before merging
- Dismiss stale reviews on new commits
- Require status checks to pass (document control, traceability)
- Disable force-push (protect audit trail)
- Enforce for administrators

## Labels

The setup script creates labels for QMS workflow:

| Label | Purpose |
|---|---|
| `capa` / `capa-open` | CAPA tracking; open CAPAs block releases |
| `ncr` / `ncr-open` | Nonconformance tracking; open NCRs block releases |
| `change-request` | Change control |
| `design-input` / `design-output` | Design control traceability |
| `training` | Training assignments |
| `release-blocker` | Blocks release gate |
| `verification` / `validation` | V&V tracking |
