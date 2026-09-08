#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

"$repo_root/scripts/verify-harness.sh"

if [ -d tests ]; then
    echo '+ uv run python -m unittest discover -s tests -p "test_*.py"'
    uv run python -m unittest discover -s tests -p "test_*.py"
else
    echo 'Brak katalogu tests/ — pominięto testy produktu. Sukces kontroli harnessu nie potwierdza walidacji produktu.'
fi

# Dodaj tutaj jawne komendy lint, typecheck lub build po skonfigurowaniu projektu.
