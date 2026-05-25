# Document routing — CODEOWNERS-based review chains

**Audience:** anyone raising a PR or reviewing one; specifically engineers who need to know "who reviews this?" and quality managers who need to design + maintain the routing.

**Goal:** explain how PR review routing works in a GitHub-native QMS — which is to say, how `CODEOWNERS` + branch-protection + GitHub teams compose into the multi-signer / segregation-of-duties primitive that traditional eQMS systems implement with a workflow engine.

---

## Why this matters at audit

Traditional eQMS systems have explicit workflow engines: "this document type routes to that approver group on creation, then to that other group on revision." Regulators expect the equivalent in any QMS — segregation of duties + role-based approval is a §820.40 + ISO 13485 §4.2.4 + Part 11 §11.10 expectation.

**The GitHub-native equivalent is CODEOWNERS + branch-protection rules.** The two together give you:

| Traditional eQMS concept | GitHub-native equivalent |
|---|---|
| Document type → approver group routing | Path pattern → team mapping in `CODEOWNERS` |
| "Approver group must include ≥ N members" | Branch-protection "Require approvals from N people" |
| "Approver cannot be the author" | Branch-protection "Dismiss stale reviews when new commits are pushed" + "Require review from CODEOWNERS" |
| Workflow state machine | PR state (open / draft / changes-requested / approved / merged) |
| Signature meaning at each state | Commit `Signature-Meaning:` trailer per [`docs/guide/signature-meaning.md`](signature-meaning.md) |
| Workflow audit log | Git log + GitHub audit log |

---

## The `CODEOWNERS` file

Lives at `.github/CODEOWNERS` (or `CODEOWNERS` at repo root, or `docs/CODEOWNERS`). One line per path-pattern → owner mapping.

Syntax is path-glob + team(s) or user(s). Example structure for an Open QMS deployment:

```
# .github/CODEOWNERS — Open QMS adopter example
# Order matters: LAST match wins for any given path.

# Default catch-all — always at least the Quality team reviews everything
*                               @my-org/quality-team

# Engine + tests — engineering owns; quality reviews
/engine/                        @my-org/engineering-team @my-org/quality-team
/engine/tests/                  @my-org/engineering-team

# Modules — vertical-specific quality leads
/modules/medical-devices/       @my-org/quality-medical-devices
/modules/pharma/                @my-org/quality-pharma
/modules/aerospace/             @my-org/quality-aerospace
/modules/automotive/            @my-org/quality-automotive
/modules/iso-27001/             @my-org/security-team @my-org/quality-team
/modules/hipaa/                 @my-org/privacy-officer @my-org/security-team
/modules/regulated-ai/          @my-org/ml-team @my-org/quality-team

# Templates — by group
/templates/qms-policy/          @my-org/quality-team @my-org/legal
/templates/qms-bcms/            @my-org/it-security @my-org/quality-team
/templates/qms-privacy/         @my-org/privacy-officer @my-org/quality-team
/templates/qms-hipaa/           @my-org/privacy-officer @my-org/quality-team
/templates/product-pharma/      @my-org/quality-pharma
/templates/product-dhf/         @my-org/quality-medical-devices @my-org/engineering-team
/templates/product-sw/          @my-org/engineering-team @my-org/quality-team

# Bundles — operational scope decisions; quality leads
/bundles/                       @my-org/quality-team

# Registry — careful change; quality lead + RA
/registry/                      @my-org/quality-team @my-org/regulatory-affairs

# BUSINESS — spec discipline; quality + project lead
/BUSINESS/                      @my-org/quality-team @my-org/project-lead

# CI workflows — IT/Security owns; quality reviews
/.github/workflows/             @my-org/it-security @my-org/quality-team

# Issue templates — quality owns; IT/Security reviews when affecting access/identity
/.github/ISSUE_TEMPLATE/        @my-org/quality-team
/.github/ISSUE_TEMPLATE/access-review.yml          @my-org/it-security @my-org/quality-team
/.github/ISSUE_TEMPLATE/restoration-test.yml       @my-org/it-security @my-org/quality-team

# CODEOWNERS itself — admin-only change (this is the routing-of-routing)
/.github/CODEOWNERS             @my-org/quality-team @my-org/it-security
```

**Order matters:** in CODEOWNERS, the last matching line wins for any given path. The default catch-all comes first; specific overrides come later.

**Multiple teams on one line means ALL of them must approve** (when paired with branch-protection "Require approval from CODEOWNERS"). This is the multi-signer / segregation-of-duties primitive.

---

## Branch-protection rules that make CODEOWNERS load-bearing

CODEOWNERS by itself only suggests reviewers; it doesn't enforce. Branch-protection rules turn suggestion into enforcement. Configure on the protected branch (typically `main`):

| Rule | Setting | Why |
|---|---|---|
| Require a pull request before merging | Enabled | Prevents direct push to protected branch |
| Require approvals | Enabled, N ≥ 1 (≥ 2 for high-risk paths) | Multi-signer threshold |
| Dismiss stale pull request approvals when new commits are pushed | Enabled | Prevents approve-then-push-changes pattern |
| Require review from Code Owners | **Enabled** | Without this, CODEOWNERS is just a hint |
| Require status checks to pass before merging | Enabled — list: engine-tests, doc-control, signature-check (if active), traceability | Substrate-level enforcement |
| Require branches to be up to date before merging | Enabled | Prevents merge-of-stale-base race |
| Require conversation resolution before merging | Enabled | Forces follow-through on review comments |
| Require signed commits | **Enabled** | Without this, the §11.100 attribution chain breaks |
| Require linear history | Enabled | Prevents merge-commit confusion; squash or rebase merges only |
| Restrict who can push to matching branches | Limited to admin team only | Belt-and-suspenders against branch-protection bypass |
| Allow force pushes | **Disabled** | OQ-022 immutability claim depends on this |
| Allow deletions | **Disabled** | Same reason |

**Test your branch protection** — see compliance-architecture forward-work P11 (`openqms verify-deployment` script, planned). For now, manually verify in GitHub Settings → Branches → Branch protection rules.

---

## Routing patterns by document type

### CAPA / NCR / Complaint

- The **author** opens the issue (anyone can; no permission gate).
- The **investigator** is typically the engineer or process-owner closest to the issue; they comment on the issue with investigation findings.
- The **approver** of the CAPA closure (per `Signature-Meaning: Approved` trailer) is the Quality Manager or designee.
- Segregation-of-duties rule: the closer should not be the same person who originally opened the issue if it's a CAPA touching their own work. For small orgs this can be hard to enforce; document the exception rationale in the close comment if it cannot be avoided.

### Controlled-document PR (templates, modules, policies)

- The **author** opens the PR.
- CODEOWNERS routes to the appropriate Quality + functional team.
- **Required: at least one Quality team approval + at least one functional team approval** (when CODEOWNERS lists both).
- The merge commit carries `Signature-Meaning: Approved` from the merger (typically Quality Manager).

### Engine / code PR

- The **author** opens the PR.
- CODEOWNERS routes to Engineering + Quality.
- **Required: at least one Engineering approval + at least one Quality approval.**
- CI must be green.

### Module YAML PR

- Most rigorous routing — controlled doc + has compliance implications.
- CODEOWNERS routes to the **vertical-specific quality lead** (e.g., `quality-medical-devices` for `modules/medical-devices/`).
- **Required: vertical-quality approval + main Quality team approval.**
- Lint + tests must pass.

### Identity-mapping register changes

- Lives outside the public repo (per IDENTITY-MAPPING-SOP §2) so doesn't route through GitHub PRs.
- But the CODEOWNERS file itself, which determines who reviews access-relevant paths, is admin-only-change per the example above.

---

## Edge cases + their handling

| Scenario | Recommended pattern |
|---|---|
| Solo founder / single-person org | CODEOWNERS still useful for documentation; branch protection still applies; the segregation-of-duties requirement is acknowledged as a constraint to revisit when the team grows. Document explicit exception rationale in the relevant SOP. |
| Reviewer on vacation | Either an explicit backup-reviewer pattern via CODEOWNERS (list two teams; either suffices) OR temporary CODEOWNERS PR by admin to add a stand-in reviewer for the duration. Time-bound the change. |
| Emergency fix needed; CODEOWNERS reviewer unreachable | Use the "Allow specified actors to bypass required pull requests" branch-protection setting **sparingly**, documented per use; this is the regulated equivalent of "manual override with audit log entry." |
| External contributor (not in any team) | They cannot satisfy CODEOWNERS by themselves; their PR sits until a team-member reviews + approves. The team-member's approval is the routing-satisfaction signal. |
| Path needs to be added that doesn't exist in CODEOWNERS | The PR adding the path will route to the catch-all team; the same PR should add the CODEOWNERS line for future PRs to that path. |

---

## How to extend the routing as your org grows

1. **Start simple.** Don't over-engineer CODEOWNERS at small team size. Default-catch-all + one or two specific overrides is enough.
2. **Refine on incident.** When a PR routes to the wrong team or no team, that's the trigger to add a CODEOWNERS line.
3. **Document the routing in your Quality Manual.** The CODEOWNERS file is the operational ground truth, but a high-level routing diagram in the Quality Manual makes it auditor-accessible.
4. **Review routing quarterly** as part of the Access Review (q.v.). Stale CODEOWNERS lines pointing to defunct teams are a real failure mode.

---

## Linkage to other Open QMS controls

- **OQ-020** PR + required reviewers — operationalized by CODEOWNERS + branch-protection
- **OQ-021** branch protection prevents merge without CI + approvals — the second half of the routing primitive
- **OQ-022** force-push-disabled — preserves the routing history
- **OQ-119** §6 permissions / access controls — this guide implements the role-based-approval mechanism
- **`templates/qms-policy/IDENTITY-MAPPING-SOP-TEMPLATE.md`** §1 roles + responsibilities — the team structure CODEOWNERS routes to
- **Future P11** `openqms verify-deployment` — will verify CODEOWNERS coverage automatically
