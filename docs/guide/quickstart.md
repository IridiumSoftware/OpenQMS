# Quick Start

## Prerequisites

- A GitHub organization (Free, Team, or Enterprise)
- [GitHub CLI](https://cli.github.com/) installed and authenticated
- Admin access to your organization

## Step 1: Create your QMS repository

```bash
# Option A: Use as template
gh repo create my-org/qms --template IridiumSoftware/open-qms --private

# Option B: Fork
gh repo fork IridiumSoftware/open-qms --org my-org --fork-name qms
```

## Step 2: Run setup

```bash
git clone git@github.com:my-org/qms.git
cd qms
./scripts/setup.sh
```

This configures branch protection, creates QMS labels, and verifies issue templates.

## Step 3: Configure your organization

1. Edit `CODEOWNERS` with your team structure
2. Edit `docs/qms-config.yml` with your organization details and trainee list
3. Copy documents from `templates/` to your repo root as starting points

## Step 4: Enable document rendering

1. Go to Settings > Pages
2. Set Source to "GitHub Actions"
3. The `deploy-docs.yml` workflow will publish your QMS as a browsable site

## Step 5: Start using it

- **Create a document:** Branch from main, add your document using a template, open a PR
- **Log a CAPA:** Use the CAPA issue template
- **Request a change:** Use the Change Request issue template
- **Release:** Tag with `v*` to trigger the release gate

## Step 6: Validate

Open QMS provides infrastructure, not a validated system. You must validate the system for your intended use. See the [validation guidance](../regulatory/overview.md) for what to cover.
