# CodeCrafters polyglot workflow

Use this for each challenge/language pair.

## 1. First pass: translate only the skeleton

Before solving the challenge, locate these five things:

1. entry point and run command
2. byte/string boundary
3. error/result convention
4. test command
5. resource cleanup convention

Do **not** design a Java architecture in the new language yet.

## 2. Build the smallest protocol loop

For network challenges, prove this sequence first:

```text
listen -> accept -> read bytes -> parse minimum -> write bytes -> close
```

Then layer protocol features on top.

## 3. Keep a “native rewrite” checkpoint

When a stage passes, ask:

> I translated the Java-shaped solution. What would be structurally different if this were written naturally in this language?

Typical rewrites:

- Kotlin: nullability, sealed types, collection operations, coroutines where useful
- Python: simple data flow, generators/comprehensions, context managers
- Go: explicit errors, small interfaces, goroutines/channels only where justified
- TypeScript: discriminated unions, narrowing, Promise/event-loop APIs
- Rust: ownership boundaries, `Result`, enums, iterators, RAII
- Odin: explicit data, allocations, multiple returns, unions, procedural design
- Gleam: custom types, `case`, `Result`, immutable transformations, actor/process design on BEAM

## 4. Record only surprises

Don't make language notes that say “a for-loop uses X”. This reference already does that.

Record things that change your design:

```text
Rust: parser returns slices borrowing request buffer; buffer owner must outlive parsed request.
Go: a slice passed downstream may share the same backing array.
Gleam: this socket API is BEAM/package-specific, not a language/std-lib primitive.
Odin: this dynamic collection allocates from the current context allocator.
```

## 5. Suggested 12-month rotation

Avoid doing seven consecutive implementations of the exact same stage. Rotate languages so each gets repeated retrieval practice.

```text
Challenge A: Kotlin -> Rust -> Go
Challenge B: Python -> Odin -> TypeScript
Challenge C: Gleam -> Rust -> Kotlin
Challenge D: Go -> Python -> Odin
...
```

Use Java only when you want a baseline implementation or need to disambiguate the challenge itself.
