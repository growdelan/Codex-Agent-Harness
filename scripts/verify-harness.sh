#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

for script in scripts/check-context-size.sh scripts/verify-harness.sh scripts/verify.sh; do
    bash -n "$script"
done
./scripts/check-context-size.sh

if ! command -v uv >/dev/null 2>&1; then
    echo 'Błąd: brak uv. Instalacja: https://docs.astral.sh/uv/getting-started/installation/' >&2
    exit 1
fi

uv run --script scripts/check-harness.py
