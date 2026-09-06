# Odin for a Java programmer

This is a **lookup sheet**, not a tutorial. Start with the concept you already know and translate into the language’s native shape.

## Commands

```bash
odin test .
odin run .
odin check .
```

## Java-brain traps

- Odin is explicit and data-oriented. Don't try to rebuild Java's class/interface architecture.
- `::` declares constants/entities such as procedures and named types; `:=` declares inferred variables.
- Dynamic arrays and maps allocate; their lifetime/allocator matters. `defer delete(...)` is common when you own them.
- Strings are UTF-8 views with explicit byte/rune concerns; ownership and conversion semantics matter.
- Multiple return values and explicit error values are normal.
- `union` plus `switch x in value` is the natural tagged-union/pattern style.
- Read `core` source when docs are thin: Odin deliberately keeps the language/runtime relatively transparent.
- Odin is evolving; this reference is pinned conceptually to the September 2026 docs and should be compiler-checked when an API looks unfamiliar.
- Slices are views. Copy if a parser result must outlive the recv buffer.
- Socket timeouts and dial helpers are version-sensitive; compiler-check `core:net` before trusting a snippet.

## Construct lookup

### Fundamentals

**Immutable binding**
```odin
x := 42  // variable; use :: for constants
```

**Constant**
```odin
PORT :: 6379
```

**Mutable variable**
```odin
x := 1
x = 2
```

**Function**
```odin
add :: proc(a, b: int) -> int {
    return a + b
}
```

**Anonymous function / lambda**
```odin
proc(x: int) -> int { return x * 2 }
```

**Generic function**
```odin
id :: proc(x: $T) -> T { return x }
```

**Tuple / pair**
```odin
// no general first-class tuple type
// use a small struct, or multiple return values:
a, b := get_pair()
```

### Types

**Data carrier / record**
```odin
User :: struct {
    name: string,
    age: int,
}
```

**Interface / trait / protocol**
```odin
// no interface construct; use procedures,
// tagged unions, or procedure fields
```

**Enum / sum type**
```odin
Msg :: union { Ping, Quit }
```

**Optional / nullable**
```odin
name: Maybe(string)
// core APIs also commonly use (value, ok)
```

**Default when missing**
```odin
n := value.? or_else "default"  // for Maybe(string)
```

### Control flow

**If / else**
```odin
if x > 0 {
    ...
} else {
    ...
}
```

**Pattern match / switch**
```odin
switch v in msg {
case Ping:
    ...
case Quit:
    ...
}
```

**For each**
```odin
for x in xs {
    ...
}
```

**Index + value iteration**
```odin
for x, i in xs {
    ...
}
```

**While loop**
```odin
for condition {
    ...
}
```

**Early return**
```odin
if bad { return result }
```

### Collections

**List / dynamic sequence**
```odin
xs := make([dynamic]int)
defer delete(xs)
```

**Fixed / contiguous array**
```odin
xs: [16]int
```

**Map / dictionary creation**
```odin
m := make(map[string]int)
defer delete(m)
```

**Map lookup with presence**
```odin
v, ok := m[key]
if ok { ... }
```

**Set creation**
```odin
// idiom: map[T]struct{} or bit_set for enum-like keys
```

**Filter**
```odin
ys := make([dynamic]int)
for x in xs { if x > 0 { append(&ys, x) } }
```

**Map / transform**
```odin
ys := make([dynamic]int)
for x in xs { append(&ys, x*2) }
```

**Fold / reduce**
```odin
total := 0
for x in xs { total += x }
```

### Strings & bytes

**String interpolation**
```odin
s := fmt.tprintf("port=%d", port)
```

**UTF-8 string → bytes**
```odin
b := transmute([]u8)s  // view; do not mutate
// clone if ownership/mutation is needed
```

**Bytes → UTF-8 string**
```odin
s := string(b)  // conversion semantics matter; clone if lifetime requires
```

**Split string**
```odin
parts := strings.split(s, ":")
```

**Parse integer**
```odin
n, ok := strconv.parse_int(s)
// inspect returned type/options for your Odin version
```

### Errors & resources

**Represent recoverable error**
```odin
method :: proc() -> (T, Error)
// explicit multi-return is common
```

**Propagate error**
```odin
v, err := method()
if err != nil { return {}, err }
```

**Cleanup / defer**
```odin
r := open()
defer close(r)
```

**Assertion**
```odin
assert(x > 0)
```

### I/O & process

**CLI arguments**
```odin
args := os.args
```

**Environment variable**
```odin
v, found := os.lookup_env("PORT", context.allocator)
defer delete(v)
```

**Read whole text file**
```odin
data, err := os.read_entire_file(path, context.allocator)
defer delete(data)
```

### Testing

**Test**
```odin
@(test)
test_parses :: proc(t: ^testing.T) {
    testing.expect_value(t, parse("1"), 1)
}
```

**Run tests**
```odin
odin test .
```

### Networking

**TCP listen**
```odin
server, err := net.listen_tcp({net.IP4_Any, port})
```

**TCP accept / connection loop**
```odin
for {
    client, source, err := net.accept_tcp(server)
    ...
}
```

**Read bytes from TCP connection**
```odin
n, err := net.recv_tcp(client, buf)
```

**Write bytes to TCP connection**
```odin
n, err := net.send_tcp(client, data)
```

### Concurrency

**Spawn concurrent work**
```odin
thread.create_and_start(proc() { work() })
// exact API may vary; see core:thread
```

**Channel / message passing**
```odin
c, _ := chan.create(chan.Chan(MyType), context.allocator)
defer chan.destroy(c)
// core:sync/chan
```
