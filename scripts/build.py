#!/usr/bin/env python3
"""Inline reference.json into index.html and regenerate MATRIX.md."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = ["Java", "Kotlin", "Python", "Go", "TypeScript", "Rust", "Odin", "Gleam"]
FENCE = {
    "Java": "java",
    "Kotlin": "kotlin",
    "Python": "python",
    "Go": "go",
    "TypeScript": "ts",
    "Rust": "rust",
    "Odin": "odin",
    "Gleam": "gleam",
}
MATRIX_INTRO = """# Java → Polyglot CodeCrafters Matrix

> Goal: you already know the programming concept. This answers **“what does it look like here?”** and flags places where there is no direct equivalent.

Targets: **Kotlin · Python · Go · TypeScript · Rust · Odin · Gleam**. Java is the reference column.

This file is generated from `reference.json` by `scripts/build.py`. Edit the JSON, then run the build.

This is deliberately CodeCrafters-oriented: bytes, parsing, files, sockets, tests, errors, and concurrency are included alongside language syntax.

{count} constructs.
"""


def load_data() -> list[dict]:
    path = ROOT / "reference.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list) or not data:
        raise SystemExit("reference.json must be a non-empty array")
    ids = [entry.get("id") for entry in data]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate construct ids in reference.json")
    return data


def inject_html(data: list[dict]) -> None:
    path = ROOT / "index.html"
    html = path.read_text(encoding="utf-8")
    start_tag = '<script type="application/json" id="ref-data">'
    start = html.find(start_tag)
    if start < 0:
        raise SystemExit("index.html is missing the ref-data script tag")
    start = html.find(">", start) + 1
    end = html.find("</script>", start)
    if end < 0:
        raise SystemExit("index.html ref-data script tag is not closed")
    payload = json.dumps(data, indent=2, ensure_ascii=False)
    path.write_text(html[:start] + "\n" + payload + "\n    " + html[end:], encoding="utf-8")


def render_matrix(data: list[dict]) -> str:
    parts = [MATRIX_INTRO.format(count=len(data))]
    last = ""
    for entry in data:
        if entry["category"] != last:
            parts.append(f"## {entry['category']}\n")
            last = entry["category"]
        eq = entry.get("equivalence", "same")
        badge = ""
        if eq == "partial":
            badge = " — *partial match*"
        elif eq == "different":
            badge = " — *wrong Java model*"
        parts.append(f"### {entry['concept']}{badge}\n")
        notes = entry.get("notes") or {}
        for lang in LANGS:
            code = entry["snippets"].get(lang, "")
            parts.append(f"**{lang}**")
            parts.append(f"```{FENCE[lang]}")
            parts.append(code)
            parts.append("```\n")
            if lang in notes:
                parts.append(f"> {notes[lang]}\n")
        parts.append("")
    return "\n".join(parts).rstrip() + "\n"


def write_dist() -> None:
    dist = ROOT / "dist"
    if dist.exists():
        shutil.rmtree(dist)
    dist.mkdir()
    for name in (
        "index.html",
        "reference.json",
        ".nojekyll",
        "MATRIX.md",
        "CODECRAFTERS-WORKFLOW.md",
        "SOURCES.md",
        "README.md",
    ):
        src = ROOT / name
        if src.exists():
            shutil.copy2(src, dist / name)
    shutil.copytree(ROOT / "languages", dist / "languages")


def main() -> None:
    data = load_data()
    inject_html(data)
    (ROOT / "MATRIX.md").write_text(render_matrix(data), encoding="utf-8")
    write_dist()
    print(f"built {len(data)} constructs")


if __name__ == "__main__":
    main()
