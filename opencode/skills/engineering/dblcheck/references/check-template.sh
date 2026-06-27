#!/usr/bin/env bash
set -euo pipefail

# Minimal check template for .opencode/checks/
# Exit 0 = pass, non-zero = fail.

# ---
# Check: <what this check verifies>
# ---

# Main assertion
if <condition>; then
    echo "PASS: <message>"
    exit 0
else
    echo "FAIL: <message>"
    exit 1
fi
