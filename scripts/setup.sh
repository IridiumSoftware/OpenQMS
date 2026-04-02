#!/usr/bin/env bash
set -euo pipefail

# Open QMS — Repository Setup Script
# Configures branch protection, labels, and basic settings via GitHub CLI.
# Requires: gh (GitHub CLI), authenticated to your org.

echo "=== Open QMS Setup ==="
echo ""

# Check prerequisites
if ! command -v gh &> /dev/null; then
    echo "ERROR: GitHub CLI (gh) is required. Install: https://cli.github.com/"
    exit 1
fi

if ! gh auth status &> /dev/null; then
    echo "ERROR: Not authenticated. Run: gh auth login"
    exit 1
fi

REPO=$(gh repo view --json nameWithOwner -q '.nameWithOwner' 2>/dev/null || true)
if [ -z "$REPO" ]; then
    echo "ERROR: Not in a GitHub repository. Run this from the repo root."
    exit 1
fi

echo "Repository: $REPO"
echo ""

# --- Branch Protection ---
echo "Setting up branch protection for 'main'..."
gh api repos/$REPO/branches/main/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":["check-metadata","check-approvers"]}' \
  --field enforce_admins=true \
  --field required_pull_request_reviews='{"required_approving_review_count":1,"dismiss_stale_reviews":true}' \
  --field restrictions=null \
  --field allow_force_pushes=false \
  --field allow_deletions=false \
  2>/dev/null && echo "  Branch protection configured." || echo "  WARNING: Could not set branch protection (may need admin access or GitHub Pro/Enterprise)."

# --- Labels ---
echo "Creating QMS labels..."
labels=(
  "capa:Corrective/Preventive Action:#d93f0b"
  "capa-open:Open CAPA (release blocker):#b60205"
  "ncr:Nonconformance Report:#e4e669"
  "ncr-open:Open NCR (release blocker):#fbca04"
  "change-request:Change Request:#0075ca"
  "design-input:Design Input:#0e8a16"
  "design-output:Design Output:#006b75"
  "training:Training Assignment:#7057ff"
  "auto-generated:Created by automation:#ededed"
  "release-blocker:Blocks next release:#b60205"
  "verification:Verification activity:#1d76db"
  "validation:Validation activity:#5319e7"
)

for label_spec in "${labels[@]}"; do
  IFS=':' read -r name description color <<< "$label_spec"
  gh label create "$name" --description "$description" --color "${color#\#}" --force 2>/dev/null || true
done
echo "  Labels created."

# --- Issue Templates ---
echo "Verifying issue templates..."
template_count=$(ls .github/ISSUE_TEMPLATE/*.yml 2>/dev/null | wc -l)
echo "  Found $template_count issue templates."

# --- CODEOWNERS ---
if [ ! -f CODEOWNERS ] && [ ! -f .github/CODEOWNERS ]; then
  echo ""
  echo "WARNING: No CODEOWNERS file found."
  echo "  Create CODEOWNERS to route document approvals to the right reviewers."
  echo "  Example:"
  echo "    qms-policy/    @your-org/quality-team"
  echo "    qms-sops/      @your-org/quality-team"
  echo "    product-*/     @your-org/engineering-lead @your-org/quality-team"
fi

echo ""
echo "=== Setup complete ==="
echo ""
echo "Next steps:"
echo "  1. Create CODEOWNERS file (see templates/CODEOWNERS.example)"
echo "  2. Edit docs/qms-config.yml with your organization details"
echo "  3. Copy templates/ contents to your repo root as starting documents"
echo "  4. Enable GitHub Pages (Settings > Pages > Source: GitHub Actions)"
echo "  5. Validate the system per your applicable regulations"
