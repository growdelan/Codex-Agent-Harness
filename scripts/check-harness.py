# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Kontrola pól szablonu i lokalnych linków; nie zastępuje semantycznego review."""

from pathlib import Path
import re
import sys
import tomllib
from urllib.parse import unquote, urlsplit


SKILLS = (
    "codex-flow-address-review", "codex-flow-compact-context", "codex-flow-create-prd",
    "codex-flow-implement-milestone", "codex-flow-plan-from-prd", "codex-flow-publish",
    "codex-flow-resume", "codex-flow-run-roadmap",
)
AGENTS = ("implementer", "planner", "reviewer")
LINK = re.compile(r"""
    \[[^\]\n]*\]\(\s*
    (?:<(?P<angle>[^>\n]+)>|(?P<plain>(?:[^\s()\\]|\\.|\([^\s()]*\))+))
    (?:\s+(?:"[^"\n]*"|'[^'\n]*'|\([^()\n]*\)))?\s*\)
""", re.X)


def check_links(path: Path) -> list[str]:
    text = re.sub(r"```.*?```", "", path.read_text(), flags=re.S)
    errors = []
    # Obsługujemy cele inline i opcjonalny tytuł. Pozostała składnia Markdown
    # jest poza tą kontrolą; nie interpretujemy jej jako nieistniejącej ścieżki.
    for match in LINK.finditer(text):
        target = match["angle"] or match["plain"]
        target = re.sub(r"\\([^\w])", r"\1", target)
        url = urlsplit(target)
        if url.scheme or url.netloc or not url.path:
            continue
        relative = Path(unquote(url.path))
        if relative.is_absolute() or not (path.parent / relative).exists():
            errors.append(f"{path}: niedostępny lub nieprzenośny link: {target}")
    return errors


def check_skill(path: Path) -> list[str]:
    errors = []
    text = path.read_text()
    header = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
    if header is None:
        return [f"{path}: brak frontmatter"]
    for field in ("name", "description"):
        values = re.findall(rf"^{field}:\s*(\S[^\n]*)$", header[1], re.M)
        if len(values) != 1:
            errors.append(f"{path}: wymagane jedno niepuste pole {field}")
        elif field == "name" and values[0] != path.parent.name:
            errors.append(f"{path}: name nie odpowiada nazwie katalogu")
    interface = path.parent / "agents/openai.yaml"
    if not interface.is_file():
        return errors + [f"{path}: brak agents/openai.yaml"]
    ui = interface.read_text()
    if len(re.findall(r"^interface:\s*$", ui, re.M)) != 1:
        errors.append(f"{interface}: wymagane jedno interface")
    for field in ("display_name", "short_description", "default_prompt"):
        # Szablon używa jednowierszowych wartości; to kontrola pól, nie parser YAML.
        values = re.findall(rf"^  {field}:\s*([\"'].+[\"'])\s*$", ui, re.M)
        if len(values) != 1:
            errors.append(f"{interface}: wymagane jedno cytowane pole {field}")
        elif field == "default_prompt" and f"${path.parent.name}" not in values[0]:
            errors.append(f"{interface}: prompt nie wskazuje własnego skilla")
    return errors


def check(root: Path) -> list[str]:
    errors = []
    skills = []
    for name in SKILLS:
        path = root / ".agents/skills" / name / "SKILL.md"
        if path.is_file():
            skills.append(path)
        else:
            errors.append(f"Brak skilla harnessu: {name}")
    names = {path.parent.name for path in (root / ".agents/skills").glob("*/SKILL.md")}
    for path in skills:
        errors.extend(check_skill(path))
    documents = [doc for path in skills for doc in path.parent.rglob("*.md")]
    for name in ("AGENTS.md", "README.md", "spec.md", "STATUS.md", "ROADMAP.md"):
        path = root / name
        if path.is_file():
            documents.append(path)
        else:
            errors.append(f"Brak {name}")
    for path in documents:
        errors.extend(check_links(path))
        for name in re.findall(r"\$(codex-flow-[a-z-]+)", path.read_text()):
            if name not in names:
                errors.append(f"{path}: odwołanie do brakującego skilla {name}")
    for name in AGENTS:
        path = root / ".codex/agents" / f"{name}.toml"
        if not path.is_file():
            errors.append(f"Brak konfiguracji agenta harnessu: {name}")
            continue
        try:
            data = tomllib.loads(path.read_text())
            for field in ("name", "description", "model", "model_reasoning_effort", "sandbox_mode", "developer_instructions"):
                if not isinstance(data.get(field), str) or not data[field].strip():
                    errors.append(f"{path}: brak niepustego pola {field}")
            if data.get("name") != path.stem:
                errors.append(f"{path}: name nie odpowiada nazwie pliku")
        except tomllib.TOMLDecodeError as exc:
            errors.append(f"{path}: błędny TOML: {exc}")
    return errors


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    errors = check(root)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        raise SystemExit(1)
    print("OK: pola skillów i agentów, odwołania do skillów oraz lokalne linki harnessu.")


if __name__ == "__main__":
    main()
