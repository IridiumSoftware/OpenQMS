#!/usr/bin/env bash
# verify-deployment.sh — thin wrapper around `openqms verify-deployment`.
#
# Closes compliance-architecture forward-work P11 at v0.62.0.
#
# Usage:
#   ./scripts/verify-deployment.sh [path/to/deployment-policy.yaml]
#
# Default policy path: ./deployment-policy.yaml
#
# Exit code 0 = clean; exit code 1 = at least one error.

set -euo pipefail

POLICY="${1:-deployment-policy.yaml}"

if [ ! -f "$POLICY" ]; then
  echo "error: deployment policy not found at $POLICY" >&2
  echo "  copy deployment-policy.example.yaml to $POLICY and adjust for your fork" >&2
  exit 2
fi

if ! command -v gh >/dev/null 2>&1; then
  echo "error: gh CLI not found. install: https://cli.github.com/ + run 'gh auth login'" >&2
  exit 2
fi

if ! command -v openqms >/dev/null 2>&1; then
  echo "error: openqms not found in PATH." >&2
  echo "  install engine: cd engine && pip install -e ." >&2
  exit 2
fi

exec openqms verify-deployment --policy "$POLICY"
