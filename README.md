# Polyglot CodeCrafters Reference

A Java-centric lookup tool for experienced programmers doing the same engineering problems across multiple languages.

**Languages:** Java (baseline), Kotlin, Python, Go, TypeScript, Rust, Odin, Gleam.

## Start here

- **`index.html`** — searchable, filterable local reference. Open it directly in a browser; no server or dependencies required.
- **`MATRIX.md`** — the complete reference as Markdown.
- **`languages/`** — one-language views with Java-brain traps and command reminders.
- **`CODECRAFTERS-WORKFLOW.md`** — a workflow for using CodeCrafters as a 12-month polyglot programme.
- **`SOURCES.md`** — official documentation used to ground the reference.

## Design rule

The question is never “what is a loop?” It is:

> I know exactly what I want to do. What is the syntax, standard idiom, ownership/error model, and important trap in this language?

Where a direct translation would be misleading, the reference says so.

## Scope

The first edition covers roughly forty high-frequency constructs across:

- fundamentals and functions
- data modelling / sum types
- null / option / result
- control flow and pattern matching
- collections and transformations
- strings and bytes
- recoverable errors and cleanup
- CLI / files / environment
- tests
- TCP networking
- concurrency/message passing

## Accuracy policy

Stable language syntax is stated directly. APIs that are version-sensitive or runtime-specific are labelled. This matters especially for **Odin** (rapidly evolving core packages) and **Gleam** (Erlang vs JavaScript targets and ecosystem packages for systems APIs).
