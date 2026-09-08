# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Fingerprint końcowej treści jawnie wskazanych plików, bez zmiany indeksu Git."""

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import stat
import subprocess


def git(root: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(root), *args], text=True, stderr=subprocess.PIPE
    ).strip()


def fingerprint(root: Path, base: str, paths: list[str]) -> str:
    empty_tree = subprocess.check_output(
        ["git", "-C", str(root), "hash-object", "-t", "tree", "--stdin"], input=b""
    ).decode().strip()
    base_sha = empty_tree if base == empty_tree else git(root, "rev-parse", "--verify", f"{base}^{{commit}}")
    records = []
    for name in sorted(set(paths)):
        relative = PurePosixPath(name)
        if relative.is_absolute() or ".." in relative.parts or str(relative) != name:
            raise ValueError(f"Wymagana dokładna ścieżka względna: {name}")
        if not relative.parts or relative.parts[0] == ".git":
            raise ValueError(f"Niedozwolona ścieżka: {name}")
        path = root / name
        if any(parent.is_symlink() for parent in path.parents if parent != root and root in parent.parents):
            raise ValueError(f"Katalog nadrzędny jest dowiązaniem: {name}")
        try:
            mode = path.lstat().st_mode
        except FileNotFoundError:
            records.append([name, "missing"])
            continue
        if stat.S_ISLNK(mode):
            records.append([name, "symlink", os.readlink(path)])
        elif stat.S_ISREG(mode):
            records.append([
                name,
                "executable" if mode & stat.S_IXUSR else "file",
                hashlib.sha256(path.read_bytes()).hexdigest(),
            ])
        else:
            raise ValueError(f"Podaj plik, nie katalog/submoduł ani plik specjalny: {name}")
    payload = json.dumps([base_sha, records], ensure_ascii=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("base", help="Stały commit review_base lub SHA pustego drzewa dla repo bez historii")
    parser.add_argument("paths", nargs="+", help="Jawne ścieżki względem katalogu repo")
    args = parser.parse_args()
    try:
        root = Path(git(Path.cwd(), "rev-parse", "--show-toplevel"))
        print(fingerprint(root, args.base, args.paths))
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"Błąd snapshotu: {exc}\n")


if __name__ == "__main__":
    main()
