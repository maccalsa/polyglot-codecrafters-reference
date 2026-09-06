# Polyglot CodeCrafters Reference

A Java-centric lookup tool for experienced programmers doing the same engineering problems across multiple languages.

**Languages:** Java (baseline), Kotlin, Python, Go, TypeScript, Rust, Odin, Gleam.

**59 constructs** across fundamentals, types, control flow, collections, strings/bytes, errors, I/O, tests, TCP, and concurrency.

## Start here

- **`index.html`** — searchable, filterable reference. Open it directly, or after `python3 scripts/build.py`.
- **`reference.json`** — source of truth. Edit this, then run the build.
- **`MATRIX.md`** — the complete reference as Markdown (generated).
- **`languages/`** — one-language views with Java-brain traps and command reminders.
- **`CODECRAFTERS-WORKFLOW.md`** — a workflow for using CodeCrafters as a 12-month polyglot programme.
- **`SOURCES.md`** — official documentation used to ground the reference.

## Edit and rebuild

```bash
python3 scripts/build.py
```

That inlines `reference.json` into `index.html` (so `file://` still works), regenerates `MATRIX.md`, and writes a `dist/` folder for GitHub Pages.

## GitHub Pages

Pushes to `main` deploy through [`.github/workflows/pages.yml`](.github/workflows/pages.yml).

One-time repo setting: **Settings → Pages → Source → GitHub Actions**.

## Design rule

The question is never “what is a loop?” It is:

> I know exactly what I want to do. What is the syntax, standard idiom, ownership/error model, and important trap in this language?

Where a direct translation would be misleading, the reference says so — in the UI as a **partial match** or **wrong Java model** badge, plus a note under the snippet.

## Scope

High-frequency constructs for CodeCrafters-style work:

- fundamentals, `main`, and functions
- data modelling / sum types
- null / option / result
- control flow and pattern matching
- collections and transformations
- strings, bytes, slices, buffers
- recoverable errors and cleanup
- CLI / files / environment / stdin
- tests
- TCP listen, accept, connect, framing, write-all, timeouts
- concurrency / message passing

## Accuracy policy

Stable language syntax is stated directly. APIs that are version-sensitive or runtime-specific are labelled in `notes`. This matters especially for **Odin** (rapidly evolving core packages) and **Gleam** (Erlang vs JavaScript targets and ecosystem packages for systems APIs).
