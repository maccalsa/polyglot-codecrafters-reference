# Gleam for a Java programmer

This is a **lookup sheet**, not a tutorial. Start with the concept you already know and translate into the language’s native shape.

## Commands

```bash
gleam test
gleam run
gleam check
gleam format
```

## Java-brain traps

- Gleam is immutable-first and expression-oriented. Imperative Java-shaped loops are usually the wrong translation.
- Custom types + `case` are the centre of modelling and control flow.
- `Result(a, e)` and `Option(a)` are ordinary algebraic data types; lean into them.
- Lists are immutable linked lists, not Java `ArrayList` equivalents.
- Gleam targets Erlang or JavaScript. Some practical APIs (files, sockets, processes) are target/runtime packages rather than `gleam_stdlib`.
- On BEAM, concurrency is actor/process-oriented rather than shared-memory threading.
- Prefer pipelines and small functions, but don't force a pipeline where a `case` communicates the branching more clearly.
- Files, env, argv, and TCP live in packages (`simplifile`, `envoy`, `argv`, `glisten`, `mug`) — never in `gleam_stdlib`.
- There is no accept-loop or `defer`. You write handlers and `result.try` pipelines.

## Construct lookup

### Fundamentals

**Immutable binding**
```gleam
let x = 42
```

**Constant**
```gleam
const port = 6379
```

**Mutable variable**
```gleam
// bindings are immutable
let x = 1
let x = 2  // shadowing
```

**Function**
```gleam
fn add(a: Int, b: Int) -> Int {
  a + b
}
```

**Anonymous function / lambda**
```gleam
fn(x) { x * 2 }
```

**Generic function**
```gleam
fn id(x: a) -> a { x }
```

**Tuple / pair**
```gleam
let p = #(1, "a")
```

### Types

**Data carrier / record**
```gleam
pub type User {
  User(name: String, age: Int)
}
```

**Interface / trait / protocol**
```gleam
// no interfaces/typeclasses; model behaviour
// with functions and custom types
```

**Enum / sum type**
```gleam
pub type Msg {
  Ping(id: Int)
  Quit
}
```

**Optional / nullable**
```gleam
let name: Option(String)
```

**Default when missing**
```gleam
let n = option.unwrap(value, "default")
```

### Control flow

**If / else**
```gleam
case x > 0 {
  True -> ...
  False -> ...
}
```

**Pattern match / switch**
```gleam
case msg {
  Ping(id) -> ...
  Quit -> ...
}
```

**For each**
```gleam
list.each(xs, fn(x) { ... })
```

**Index + value iteration**
```gleam
list.index_map(xs, fn(x, i) { ... })
```

**While loop**
```gleam
// no while loop; use recursion or iterator/list functions
```

**Early return**
```gleam
// structure with case/result pipelines; no imperative early-return idiom
```

### Collections

**List / dynamic sequence**
```gleam
let xs: List(Int) = []
```

**Fixed / contiguous array**
```gleam
// List is linked; BitArray for bytes.
// No general mutable array in core language.
```

**Map / dictionary creation**
```gleam
let m = dict.new()
```

**Map lookup with presence**
```gleam
case dict.get(m, key) {
  Ok(v) -> ...
  Error(Nil) -> ...
}
```

**Set creation**
```gleam
let s = set.new()
```

**Filter**
```gleam
let ys = list.filter(xs, fn(x) { x > 0 })
```

**Map / transform**
```gleam
let ys = list.map(xs, fn(x) { x * 2 })
```

**Fold / reduce**
```gleam
let total = list.fold(xs, 0, fn(acc, x) { acc + x })
```

### Strings & bytes

**String interpolation**
```gleam
let s = "port=" <> int.to_string(port)
```

**UTF-8 string → bytes**
```gleam
let b = bit_array.from_string(s)
```

**Bytes → UTF-8 string**
```gleam
let result = bit_array.to_string(b)  // Result(String, Nil)
```

**Split string**
```gleam
let parts = string.split(s, ":")
```

**Parse integer**
```gleam
let result = int.parse(s)  // Result(Int, Nil)
```

### Errors & resources

**Represent recoverable error**
```gleam
fn method() -> Result(T, E)
```

**Propagate error**
```gleam
use v <- result.try(method())
// or case method() { ... }
```

**Cleanup / defer**
```gleam
// immutable/managed runtime; resource APIs are library/runtime-specific
```

**Assertion**
```gleam
let assert True = x > 0
```

### I/O & process

**CLI arguments**
```gleam
// target/runtime-specific; on Erlang use gleam_erlang/os or starter helpers
```

**Environment variable**
```gleam
// target/runtime-specific; Erlang helpers live outside gleam_stdlib
```

**Read whole text file**
```gleam
// Erlang target: gleam_erlang/file; JS target: runtime FFI/package
```

### Testing

**Test**
```gleam
// in test/..._test.gleam
pub fn parses_test() {
  assert parse("1") == 1
}
// generated projects use gleeunit.main() as test main
```

**Run tests**
```gleam
gleam test
```

### Networking

**TCP listen**
```gleam
// no TCP API in gleam_stdlib. On BEAM, use a package such as glisten
// (or CodeCrafters starter/runtime FFI).
```

**TCP accept / connection loop**
```gleam
// package/runtime-specific; glisten manages acceptors and handlers
```

**Read bytes from TCP connection**
```gleam
// package/runtime-specific; typically BitArray messages/data
```

**Write bytes to TCP connection**
```gleam
// package/runtime-specific; e.g. glisten connection send APIs
```

### Concurrency

**Spawn concurrent work**
```gleam
process.spawn(fn() { work() }) // gleam_erlang on BEAM
```

**Channel / message passing**
```gleam
// BEAM processes + typed selectors/messages via gleam_erlang/OTP libraries
```
