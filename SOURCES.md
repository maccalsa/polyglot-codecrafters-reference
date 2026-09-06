# Sources and version notes

This reference favours official language and standard-library documentation. It is intentionally a practical translation aid, not a substitute for specifications.

## Kotlin
- https://kotlinlang.org/docs/basic-syntax.html
- https://kotlinlang.org/docs/null-safety.html
- https://kotlinlang.org/docs/exceptions.html
- https://kotlinlang.org/docs/collections-overview.html

## Python
- https://docs.python.org/3/tutorial/
- https://docs.python.org/3/tutorial/datastructures.html
- https://docs.python.org/3/tutorial/errors.html
- https://docs.python.org/3/library/socket.html
- https://docs.python.org/3/library/unittest.html

## Go
- https://go.dev/ref/spec
- https://pkg.go.dev/net
- https://pkg.go.dev/testing
- https://go.dev/doc/effective_go

## TypeScript / Node
- https://www.typescriptlang.org/docs/handbook/
- https://www.typescriptlang.org/docs/handbook/2/narrowing.html
- https://www.typescriptlang.org/docs/handbook/2/generics.html
- https://nodejs.org/api/net.html
- https://nodejs.org/api/fs.html

## Rust
- https://doc.rust-lang.org/book/
- https://doc.rust-lang.org/std/collections/
- https://doc.rust-lang.org/std/net/
- https://doc.rust-lang.org/std/result/

## Odin
- https://odin-lang.org/docs/overview/
- https://odin-lang.org/docs/
- https://pkg.odin-lang.org/core/net/
- https://pkg.odin-lang.org/core/testing/

**Version note:** Odin evolves faster than Java/Kotlin/Go. The networking/testing notes here were checked against the September 2026 package docs. Treat exact package APIs as compiler-verified rather than timeless.

## Gleam
- https://gleam.run/documentation/
- https://gleam.run/documentation/command-line-reference/
- https://gleam-stdlib.hexdocs.pm/
- https://gleam-erlang.hexdocs.pm/
- https://hexdocs.pm/glisten/

**Runtime note:** Gleam has Erlang and JavaScript targets. Low-level networking, filesystem and process APIs are often supplied by target-specific packages/FFI rather than the core `gleam_stdlib`. The reference marks these explicitly instead of pretending there is one universal API.
