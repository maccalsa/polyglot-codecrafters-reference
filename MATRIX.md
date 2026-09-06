# Java → Polyglot CodeCrafters Matrix

> Goal: you already know the programming concept. This answers **“what does it look like here?”** and flags places where there is no direct equivalent.

Targets: **Kotlin · Python · Go · TypeScript · Rust · Odin · Gleam**. Java is the reference column.

This file is generated from `reference.json` by `scripts/build.py`. Edit the JSON, then run the build.

This is deliberately CodeCrafters-oriented: bytes, parsing, files, sockets, tests, errors, and concurrency are included alongside language syntax.

59 constructs.

## Fundamentals

### Immutable binding — *partial match*

**Java**
```java
final var x = 42;
```

**Kotlin**
```kotlin
val x = 42
```

**Python**
```python
x = 42
```

> No language-level const; convention and discipline only.

**Go**
```go
x := 42
```

> The binding itself is mutable. There is no val/const for locals.

**TypeScript**
```ts
const x = 42
```

**Rust**
```rust
let x = 42;
```

**Odin**
```odin
x := 42
```

> := creates a variable. Use :: for compile-time constants.

**Gleam**
```gleam
let x = 42
```


### Constant

**Java**
```java
static final int PORT = 6379;
```

**Kotlin**
```kotlin
const val PORT = 6379
```

> const val is compile-time. Use val for runtime constants.

**Python**
```python
PORT = 6379
```

> Uppercase is convention only; the name remains assignable.

**Go**
```go
const Port = 6379
```

**TypeScript**
```ts
const PORT = 6379
```

**Rust**
```rust
const PORT: u16 = 6379;
```

**Odin**
```odin
PORT :: 6379
```

**Gleam**
```gleam
const port = 6379
```


### Mutable variable — *partial match*

**Java**
```java
var x = 1;
x = 2;
```

**Kotlin**
```kotlin
var x = 1
x = 2
```

**Python**
```python
x = 1
x = 2
```

**Go**
```go
x := 1
x = 2
```

**TypeScript**
```ts
let x = 1
x = 2
```

**Rust**
```rust
let mut x = 1;
x = 2;
```

**Odin**
```odin
x := 1
x = 2
```

**Gleam**
```gleam
let x = 1
let x = 2
```

> Bindings are immutable. Reusing the name is shadowing, not mutation.


### Function

**Java**
```java
int add(int a, int b) {
  return a + b;
}
```

**Kotlin**
```kotlin
fun add(a: Int, b: Int): Int = a + b
```

**Python**
```python
def add(a: int, b: int) -> int:
    return a + b
```

**Go**
```go
func add(a, b int) int {
    return a + b
}
```

**TypeScript**
```ts
function add(a: number, b: number): number {
  return a + b
}
```

**Rust**
```rust
fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

**Odin**
```odin
add :: proc(a, b: int) -> int {
    return a + b
}
```

**Gleam**
```gleam
fn add(a: Int, b: Int) -> Int {
  a + b
}
```


### Anonymous function / lambda

**Java**
```java
x -> x * 2
```

**Kotlin**
```kotlin
{ x -> x * 2 }
```

**Python**
```python
lambda x: x * 2
```

**Go**
```go
func(x int) int { return x * 2 }
```

**TypeScript**
```ts
(x: number) => x * 2
```

**Rust**
```rust
|x| x * 2
```

**Odin**
```odin
proc(x: int) -> int { return x * 2 }
```

**Gleam**
```gleam
fn(x) { x * 2 }
```


### Generic function

**Java**
```java
static <T> T id(T x) {
  return x;
}
```

**Kotlin**
```kotlin
fun <T> id(x: T): T = x
```

**Python**
```python
def id[T](x: T) -> T:
    return x
```

> Type-parameter syntax is 3.12+. Earlier: TypeVar.

**Go**
```go
func id[T any](x T) T {
    return x
}
```

**TypeScript**
```ts
function id<T>(x: T): T {
  return x
}
```

**Rust**
```rust
fn id<T>(x: T) -> T {
    x
}
```

**Odin**
```odin
id :: proc(x: $T) -> T {
    return x
}
```

**Gleam**
```gleam
fn id(x: a) -> a {
  x
}
```


### Tuple / pair — *partial match*

**Java**
```java
record Pair<A, B>(A first, B second) {}
```

**Kotlin**
```kotlin
val p = 1 to "a"
```

> to builds Pair<A, B>.

**Python**
```python
p = (1, "a")
```

**Go**
```go
return 1, "a"
```

> Multiple return values are the idiom; there is no first-class tuple.

**TypeScript**
```ts
const p: [number, string] = [1, "a"]
```

**Rust**
```rust
let p: (i32, &str) = (1, "a");
```

**Odin**
```odin
a, b := get_pair()
```

> No general tuple type. Use a small struct or multiple return values.

**Gleam**
```gleam
let p = #(1, "a")
```


### Entry point / main

**Java**
```java
public static void main(String[] args) {
  ...
}
```

**Kotlin**
```kotlin
fun main(args: Array<String>) {
  ...
}
```

**Python**
```python
def main() -> None:
    ...

if __name__ == "__main__":
    main()
```

**Go**
```go
func main() {
    ...
}
```

> Must live in package main.

**TypeScript**
```ts
async function main() {
  ...
}
main()
```

> Node treats the launched file as the entry. Browser/Deno differ.

**Rust**
```rust
fn main() {
    ...
}
```

**Odin**
```odin
main :: proc() {
    ...
}
```

**Gleam**
```gleam
pub fn main() {
  ...
}
```


## Types

### Data carrier / record

**Java**
```java
record User(String name, int age) {}
```

**Kotlin**
```kotlin
data class User(val name: String, val age: Int)
```

**Python**
```python
@dataclass
class User:
    name: str
    age: int
```

**Go**
```go
type User struct {
    Name string
    Age  int
}
```

**TypeScript**
```ts
type User = {
  name: string
  age: number
}
```

**Rust**
```rust
struct User {
    name: String,
    age: u32,
}
```

**Odin**
```odin
User :: struct {
    name: string,
    age: int,
}
```

**Gleam**
```gleam
pub type User {
  User(name: String, age: Int)
}
```


### Interface / trait / protocol — *wrong Java model*

**Java**
```java
interface Reader {
  byte[] read();
}
```

**Kotlin**
```kotlin
interface Reader {
  fun read(): ByteArray
}
```

**Python**
```python
class Reader(Protocol):
    def read(self) -> bytes: ...
```

**Go**
```go
type Reader interface {
    Read([]byte) (int, error)
}
```

> Satisfied implicitly; no implements clause.

**TypeScript**
```ts
interface Reader {
  read(): Uint8Array
}
```

**Rust**
```rust
trait Reader {
    fn read(&mut self) -> Vec<u8>;
}
```

**Odin**
```odin
Reader :: struct {
    read: proc(r: ^Reader) -> []u8,
}
```

> No interface construct. Use procedure fields, tagged unions, or plain procedures.

**Gleam**
```gleam
pub fn read(r: Reader) -> BitArray {
  r.read(r)
}
```

> No typeclasses. Pass functions and custom types; do not look for implements.


### Enum / sum type — *partial match*

**Java**
```java
sealed interface Msg permits Ping, Quit {}
record Ping(int id) implements Msg {}
record Quit() implements Msg {}
```

**Kotlin**
```kotlin
sealed interface Msg
data class Ping(val id: Int) : Msg
data object Quit : Msg
```

**Python**
```python
type Msg = Ping | Quit
```

> 3.12+ type alias. Define Ping/Quit as dataclasses or NamedTuples.

**Go**
```go
type Msg interface{ isMsg() }

type Ping struct{ ID int }
type Quit struct{}

func (Ping) isMsg() {}
func (Quit) isMsg() {}
```

> No native sum type. A sealed interface plus tagged structs is the usual stand-in.

**TypeScript**
```ts
type Msg =
  | { kind: "ping"; id: number }
  | { kind: "quit" }
```

**Rust**
```rust
enum Msg {
    Ping { id: i32 },
    Quit,
}
```

**Odin**
```odin
Msg :: union {
    Ping,
    Quit,
}
```

**Gleam**
```gleam
pub type Msg {
  Ping(id: Int)
  Quit
}
```


### Optional / nullable — *partial match*

**Java**
```java
Optional<String> name
```

**Kotlin**
```kotlin
val name: String?
```

**Python**
```python
name: str | None
```

**Go**
```go
var name *string
```

> Pointer or (value, ok). nil is not Optional.

**TypeScript**
```ts
let name: string | undefined
```

**Rust**
```rust
let name: Option<String>
```

**Odin**
```odin
name: Maybe(string)
```

> Maybe(T) exists; many core APIs still use (value, ok).

**Gleam**
```gleam
let name: Option(String)
```


### Default when missing — *partial match*

**Java**
```java
var n = opt.orElse("default");
```

**Kotlin**
```kotlin
val n = value ?: "default"
```

**Python**
```python
n = value if value is not None else "default"
```

**Go**
```go
if value == "" {
    value = "default"
}
```

> Empty string is not absence. Prefer comma-ok on maps and pointers for missing values.

**TypeScript**
```ts
const n = value ?? "default"
```

**Rust**
```rust
let n = value.unwrap_or("default");
```

**Odin**
```odin
n := value.? or_else "default"
```

> or_else is for Maybe(T). Comma-ok APIs need an explicit check.

**Gleam**
```gleam
let n = option.unwrap(value, "default")
```


## Control flow

### If / else — *partial match*

**Java**
```java
if (x > 0) {
  ...
} else {
  ...
}
```

**Kotlin**
```kotlin
if (x > 0) {
  ...
} else {
  ...
}
```

**Python**
```python
if x > 0:
    ...
else:
    ...
```

**Go**
```go
if x > 0 {
    ...
} else {
    ...
}
```

**TypeScript**
```ts
if (x > 0) {
  ...
} else {
  ...
}
```

**Rust**
```rust
if x > 0 {
    ...
} else {
    ...
}
```

**Odin**
```odin
if x > 0 {
    ...
} else {
    ...
}
```

**Gleam**
```gleam
case x > 0 {
  True -> ...
  False -> ...
}
```

> No if statement. case on Bool (or a richer type) is the branch.


### Pattern match / switch — *partial match*

**Java**
```java
switch (msg) {
  case Ping p -> handle(p);
  case Quit q -> stop();
}
```

**Kotlin**
```kotlin
when (msg) {
  is Ping -> handle(msg)
  Quit -> stop()
}
```

**Python**
```python
match msg:
    case Ping(id):
        ...
    case Quit():
        ...
```

**Go**
```go
switch v := msg.(type) {
case Ping:
    _ = v
case Quit:
    ...
}
```

**TypeScript**
```ts
switch (msg.kind) {
  case "ping":
    ...
    break
  case "quit":
    ...
}
```

**Rust**
```rust
match msg {
    Msg::Ping { id } => ...,
    Msg::Quit => ...,
}
```

**Odin**
```odin
switch v in msg {
case Ping:
    ...
case Quit:
    ...
}
```

**Gleam**
```gleam
case msg {
  Ping(id) -> ...
  Quit -> ...
}
```


### For each

**Java**
```java
for (var x : xs) {
  ...
}
```

**Kotlin**
```kotlin
for (x in xs) {
  ...
}
```

**Python**
```python
for x in xs:
    ...
```

**Go**
```go
for _, x := range xs {
    ...
}
```

**TypeScript**
```ts
for (const x of xs) {
  ...
}
```

**Rust**
```rust
for x in xs {
    ...
}
```

**Odin**
```odin
for x in xs {
    ...
}
```

**Gleam**
```gleam
list.each(xs, fn(x) { ... })
```

> list.each is for side effects. Prefer list.map / list.filter for values.


### Index + value iteration

**Java**
```java
for (int i = 0; i < xs.size(); i++) {
  var x = xs.get(i);
}
```

**Kotlin**
```kotlin
for ((i, x) in xs.withIndex()) {
  ...
}
```

**Python**
```python
for i, x in enumerate(xs):
    ...
```

**Go**
```go
for i, x := range xs {
    ...
}
```

**TypeScript**
```ts
for (const [i, x] of xs.entries()) {
  ...
}
```

**Rust**
```rust
for (i, x) in xs.iter().enumerate() {
    ...
}
```

**Odin**
```odin
for x, i in xs {
    ...
}
```

**Gleam**
```gleam
list.index_map(xs, fn(x, i) { ... })
```

> index_map returns a new list. It is not a side-effecting for-loop.


### While loop — *partial match*

**Java**
```java
while (condition) {
  ...
}
```

**Kotlin**
```kotlin
while (condition) {
  ...
}
```

**Python**
```python
while condition:
    ...
```

**Go**
```go
for condition {
    ...
}
```

> for is the only loop. while condition is for condition { }.

**TypeScript**
```ts
while (condition) {
  ...
}
```

**Rust**
```rust
while condition {
    ...
}
```

**Odin**
```odin
for condition {
    ...
}
```

> Same as Go: for is while when given only a condition.

**Gleam**
```gleam
fn loop(n: Int) -> Int {
  case n > 0 {
    True -> loop(n - 1)
    False -> n
  }
}
```

> No while. Recurse, or use list/iterator functions.


### Early return — *wrong Java model*

**Java**
```java
if (bad) {
  return result;
}
```

**Kotlin**
```kotlin
if (bad) return result
```

**Python**
```python
if bad:
    return result
```

**Go**
```go
if bad {
    return result
}
```

**TypeScript**
```ts
if (bad) return result
```

**Rust**
```rust
if bad {
    return result;
}
```

**Odin**
```odin
if bad {
    return result
}
```

**Gleam**
```gleam
use x <- result.try(parse(s))
use y <- result.try(validate(x))
Ok(y)
```

> No imperative early return. Structure with case or result.try pipelines.


## Collections

### List / dynamic sequence — *partial match*

**Java**
```java
var xs = new ArrayList<Integer>();
```

**Kotlin**
```kotlin
val xs = mutableListOf<Int>()
```

**Python**
```python
xs: list[int] = []
```

**Go**
```go
xs := []int{}
```

**TypeScript**
```ts
const xs: number[] = []
```

**Rust**
```rust
let mut xs: Vec<i32> = Vec::new();
```

**Odin**
```odin
xs := make([dynamic]int)
defer delete(xs)
```

> Dynamic arrays allocate. You own the memory until delete.

**Gleam**
```gleam
let xs: List(Int) = []
```

> Linked list, not a growable array. Prepend is cheap; append is not.


### Fixed / contiguous array — *partial match*

**Java**
```java
int[] xs = new int[16];
```

**Kotlin**
```kotlin
val xs = IntArray(16)
```

**Python**
```python
xs = [0] * 16
```

> list is the usual sequence. array.array / bytearray when you need packed storage.

**Go**
```go
var xs [16]int
```

**TypeScript**
```ts
const xs = new Int32Array(16)
```

**Rust**
```rust
let xs = [0i32; 16];
```

**Odin**
```odin
xs: [16]int
```

**Gleam**
```gleam
let bytes: BitArray = <<0, 0, 0, 0>>
```

> List is linked. BitArray is for bytes. No general mutable array in the core language.


### Map / dictionary creation

**Java**
```java
var m = new HashMap<String, Integer>();
```

**Kotlin**
```kotlin
val m = mutableMapOf<String, Int>()
```

**Python**
```python
m: dict[str, int] = {}
```

**Go**
```go
m := make(map[string]int)
```

**TypeScript**
```ts
const m = new Map<string, number>()
```

> Map is not a plain object. Objects do not have a reliable key order or typed keys.

**Rust**
```rust
let mut m = HashMap::<String, i32>::new();
```

**Odin**
```odin
m := make(map[string]int)
defer delete(m)
```

**Gleam**
```gleam
let m = dict.new()
```


### Map lookup with presence

**Java**
```java
var v = m.get(key);
if (v != null) {
  ...
}
```

**Kotlin**
```kotlin
val v = m[key]
if (v != null) {
  ...
}
```

**Python**
```python
if key in m:
    v = m[key]
```

**Go**
```go
v, ok := m[key]
if ok {
    ...
}
```

> m[key] without ok returns the zero value for missing keys.

**TypeScript**
```ts
const v = m.get(key)
if (v !== undefined) {
  ...
}
```

**Rust**
```rust
if let Some(v) = m.get(&key) {
    ...
}
```

**Odin**
```odin
v, ok := m[key]
if ok {
    ...
}
```

**Gleam**
```gleam
case dict.get(m, key) {
  Ok(v) -> ...
  Error(Nil) -> ...
}
```


### Set creation — *partial match*

**Java**
```java
var s = new HashSet<String>();
```

**Kotlin**
```kotlin
val s = mutableSetOf<String>()
```

**Python**
```python
s: set[str] = set()
```

**Go**
```go
s := map[string]struct{}{}
```

> No set type. map[T]struct{} is the usual idiom.

**TypeScript**
```ts
const s = new Set<string>()
```

**Rust**
```rust
let mut s = HashSet::<String>::new();
```

**Odin**
```odin
s := make(map[string]struct{})
defer delete(s)
```

> Same map[T]struct{} idiom, or bit_set for enum-like keys.

**Gleam**
```gleam
let s = set.new()
```


### Filter

**Java**
```java
var ys = xs.stream()
    .filter(x -> x > 0)
    .toList();
```

**Kotlin**
```kotlin
val ys = xs.filter { it > 0 }
```

**Python**
```python
ys = [x for x in xs if x > 0]
```

**Go**
```go
ys := make([]int, 0, len(xs))
for _, x := range xs {
    if x > 0 {
        ys = append(ys, x)
    }
}
```

**TypeScript**
```ts
const ys = xs.filter(x => x > 0)
```

**Rust**
```rust
let ys: Vec<_> = xs.into_iter()
    .filter(|x| *x > 0)
    .collect();
```

**Odin**
```odin
ys := make([dynamic]int)
for x in xs {
    if x > 0 {
        append(&ys, x)
    }
}
```

**Gleam**
```gleam
let ys = list.filter(xs, fn(x) { x > 0 })
```


### Map / transform

**Java**
```java
var ys = xs.stream()
    .map(x -> x * 2)
    .toList();
```

**Kotlin**
```kotlin
val ys = xs.map { it * 2 }
```

**Python**
```python
ys = [x * 2 for x in xs]
```

**Go**
```go
ys := make([]int, len(xs))
for i, x := range xs {
    ys[i] = x * 2
}
```

**TypeScript**
```ts
const ys = xs.map(x => x * 2)
```

**Rust**
```rust
let ys: Vec<_> = xs.into_iter()
    .map(|x| x * 2)
    .collect();
```

**Odin**
```odin
ys := make([dynamic]int)
for x in xs {
    append(&ys, x * 2)
}
```

**Gleam**
```gleam
let ys = list.map(xs, fn(x) { x * 2 })
```


### Fold / reduce

**Java**
```java
var total = xs.stream().reduce(0, Integer::sum);
```

**Kotlin**
```kotlin
val total = xs.fold(0) { acc, x -> acc + x }
```

**Python**
```python
total = sum(xs)
```

**Go**
```go
total := 0
for _, x := range xs {
    total += x
}
```

**TypeScript**
```ts
const total = xs.reduce((a, x) => a + x, 0)
```

**Rust**
```rust
let total: i32 = xs.iter().sum();
```

**Odin**
```odin
total := 0
for x in xs {
    total += x
}
```

**Gleam**
```gleam
let total = list.fold(xs, 0, fn(acc, x) { acc + x })
```


## Strings & bytes

### String interpolation

**Java**
```java
var s = "port=" + port;
```

> No interpolation in everyday Java. STR templates exist but are still preview/unstable across versions.

**Kotlin**
```kotlin
val s = "port=$port"
```

**Python**
```python
s = f"port={port}"
```

**Go**
```go
s := fmt.Sprintf("port=%d", port)
```

**TypeScript**
```ts
const s = `port=${port}`
```

**Rust**
```rust
let s = format!("port={port}");
```

**Odin**
```odin
s := fmt.tprintf("port=%d", port)
```

**Gleam**
```gleam
let s = "port=" <> int.to_string(port)
```


### UTF-8 string → bytes — *partial match*

**Java**
```java
byte[] b = s.getBytes(StandardCharsets.UTF_8);
```

**Kotlin**
```kotlin
val b = s.encodeToByteArray()
```

**Python**
```python
b = s.encode("utf-8")
```

**Go**
```go
b := []byte(s)
```

**TypeScript**
```ts
const b = new TextEncoder().encode(s)
```

**Rust**
```rust
let b = s.as_bytes();
```

> as_bytes borrows. Clone with s.into_bytes() if you need an owned Vec<u8>.

**Odin**
```odin
b := transmute([]u8)s
```

> transmute is a view. Do not mutate. Clone if you need ownership.

**Gleam**
```gleam
let b = bit_array.from_string(s)
```


### Bytes → UTF-8 string — *partial match*

**Java**
```java
var s = new String(b, StandardCharsets.UTF_8);
```

**Kotlin**
```kotlin
val s = b.decodeToString()
```

**Python**
```python
s = b.decode("utf-8")
```

**Go**
```go
s := string(b)
```

**TypeScript**
```ts
const s = new TextDecoder().decode(b)
```

**Rust**
```rust
let s = std::str::from_utf8(&b)?;
```

> Fails on invalid UTF-8. Use from_utf8_lossy if you want replacement.

**Odin**
```odin
s := string(b)
```

> Conversion semantics and lifetime matter; clone if the bytes will move.

**Gleam**
```gleam
let result = bit_array.to_string(b)
```

> Result(String, Nil).


### Split string

**Java**
```java
var parts = s.split(":", -1);
```

> Limit -1 keeps trailing empty strings. The no-limit overload discards them.

**Kotlin**
```kotlin
val parts = s.split(":")
```

**Python**
```python
parts = s.split(":")
```

**Go**
```go
parts := strings.Split(s, ":")
```

**TypeScript**
```ts
const parts = s.split(":")
```

**Rust**
```rust
let parts: Vec<_> = s.split(':').collect();
```

**Odin**
```odin
parts := strings.split(s, ":")
```

**Gleam**
```gleam
let parts = string.split(s, ":")
```


### Parse integer

**Java**
```java
int n = Integer.parseInt(s);
```

**Kotlin**
```kotlin
val n = s.toInt()
```

> toInt() throws. toIntOrNull() if absence is expected.

**Python**
```python
n = int(s)
```

**Go**
```go
n, err := strconv.Atoi(s)
```

**TypeScript**
```ts
const n = Number.parseInt(s, 10)
```

> Always pass radix 10. parseInt("08") without it is not your friend in older JS.

**Rust**
```rust
let n: i32 = s.parse()?;
```

**Odin**
```odin
n, ok := strconv.parse_int(s)
```

> Inspect the returned type/options for your compiler version.

**Gleam**
```gleam
let result = int.parse(s)
```

> Result(Int, Nil).


### Starts-with / prefix

**Java**
```java
s.startsWith("+")
```

**Kotlin**
```kotlin
s.startsWith("+")
```

**Python**
```python
s.startswith("+")
```

**Go**
```go
strings.HasPrefix(s, "+")
```

**TypeScript**
```ts
s.startsWith("+")
```

**Rust**
```rust
s.starts_with('+')
```

**Odin**
```odin
strings.has_prefix(s, "+")
```

**Gleam**
```gleam
string.starts_with(s, "+")
```


### Trim whitespace

**Java**
```java
s.trim()
```

**Kotlin**
```kotlin
s.trim()
```

**Python**
```python
s.strip()
```

**Go**
```go
strings.TrimSpace(s)
```

**TypeScript**
```ts
s.trim()
```

**Rust**
```rust
s.trim()
```

**Odin**
```odin
strings.trim_space(s)
```

**Gleam**
```gleam
string.trim(s)
```


### Byte / string slice — *wrong Java model*

**Java**
```java
var part = s.substring(i, j);
var bytes = Arrays.copyOfRange(b, i, j);
```

**Kotlin**
```kotlin
val part = s.substring(i, j)
val bytes = b.copyOfRange(i, j)
```

**Python**
```python
part = s[i:j]
bytes = b[i:j]
```

**Go**
```go
part := s[i:j]
bytes := b[i:j]
```

> Slices share the backing array. A downstream append can mutate callers.

**TypeScript**
```ts
const part = s.slice(i, j)
const bytes = b.subarray(i, j)
```

> subarray is a view; slice() on Uint8Array copies.

**Rust**
```rust
let part = &s[i..j];
let bytes = &b[i..j];
```

> This is a borrow. The owner of s/b must outlive the slice.

**Odin**
```odin
part := s[i:j]
bytes := b[i:j]
```

> Slices are views. Copy if you need an independent buffer.

**Gleam**
```gleam
let part = string.slice(s, i, j - i)
let bytes = bit_array.slice(b, i, j - i)
```

> slice takes start + length, not start + end.


### Append bytes to a buffer — *partial match*

**Java**
```java
var buf = new ByteArrayOutputStream();
buf.write(data);
```

**Kotlin**
```kotlin
val buf = ByteArrayOutputStream()
buf.write(data)
```

**Python**
```python
buf = bytearray()
buf.extend(data)
```

**Go**
```go
buf = append(buf, data...)
```

> append may reallocate. Reassign the result; the old slice header can be stale.

**TypeScript**
```ts
buf = Buffer.concat([buf, data])
```

> Node Buffer. In the browser, concatenate Uint8Array manually.

**Rust**
```rust
buf.extend_from_slice(data);
```

**Odin**
```odin
append(&buf, ..data)
```

**Gleam**
```gleam
let buf = bit_array.append(buf, data)
```

> Immutable. append returns a new BitArray.


## Errors & resources

### Represent recoverable error — *wrong Java model*

**Java**
```java
T method() throws IOException
```

**Kotlin**
```kotlin
fun method(): T
```

> Exceptions are unchecked. There is no throws clause.

**Python**
```python
def method() -> T:
```

> Raise an exception. Typing does not encode failure.

**Go**
```go
func method() (T, error)
```

**TypeScript**
```ts
function method(): T
```

> throw, or make failure explicit with a Result union.

**Rust**
```rust
fn method() -> Result<T, E>
```

**Odin**
```odin
method :: proc() -> (T, Error)
```

> Explicit multi-return is the common shape.

**Gleam**
```gleam
fn method() -> Result(T, E)
```


### Propagate error — *wrong Java model*

**Java**
```java
return method();
```

> Or declare throws and let it escape.

**Kotlin**
```kotlin
return method()
```

> Unchecked exceptions propagate automatically.

**Python**
```python
return method()
```

> Exceptions propagate automatically.

**Go**
```go
v, err := method()
if err != nil {
    return zero, err
}
```

**TypeScript**
```ts
return method()
```

> Thrown exceptions propagate. Result unions do not.

**Rust**
```rust
let v = method()?;
```

**Odin**
```odin
v, err := method()
if err != nil {
    return {}, err
}
```

**Gleam**
```gleam
use v <- result.try(method())
```

> Or case method() { Ok(v) -> ... Error(e) -> Error(e) }.


### Cleanup / defer — *partial match*

**Java**
```java
try (var in = open()) {
  ...
}
```

**Kotlin**
```kotlin
open().use { resource ->
  ...
}
```

**Python**
```python
with open_resource() as resource:
    ...
```

**Go**
```go
r := open()
defer r.Close()
```

**TypeScript**
```ts
const r = open()
try {
  ...
} finally {
  r.close()
}
```

> No language-level defer. try/finally, or runtime helpers (using, Disposable).

**Rust**
```rust
let r = open()?;
```

> Drop runs at end of scope. No finally needed for owned resources.

**Odin**
```odin
r := open()
defer close(r)
```

**Gleam**
```gleam
use _ <- result.try(open())
```

> Managed runtime. Resource APIs are library-specific; there is no defer.


### Assertion — *partial match*

**Java**
```java
assert x > 0;
```

> JVM assertions are off unless -ea.

**Kotlin**
```kotlin
check(x > 0)
```

> check throws. assert may depend on JVM -ea.

**Python**
```python
assert x > 0
```

**Go**
```go
if x <= 0 {
    panic("assert")
}
```

> No built-in assert. Use an explicit if / panic, or a test helper.

**TypeScript**
```ts
if (!(x > 0)) {
  throw new Error("assertion failed")
}
```

**Rust**
```rust
assert!(x > 0);
```

**Odin**
```odin
assert(x > 0)
```

**Gleam**
```gleam
let assert True = x > 0
```


## I/O & process

### CLI arguments — *partial match*

**Java**
```java
public static void main(String[] args) {
  ...
}
```

**Kotlin**
```kotlin
fun main(args: Array<String>) {
  ...
}
```

**Python**
```python
args = sys.argv[1:]
```

**Go**
```go
args := os.Args[1:]
```

**TypeScript**
```ts
const args = process.argv.slice(2)
```

> Node. Deno uses Deno.args.

**Rust**
```rust
let args: Vec<String> = std::env::args().skip(1).collect();
```

**Odin**
```odin
args := os.args
```

**Gleam**
```gleam
let args = argv.load().arguments
```

> argv package, or gleam_erlang/os. Not in gleam_stdlib.


### Environment variable — *partial match*

**Java**
```java
var v = System.getenv("PORT");
```

**Kotlin**
```kotlin
val v = System.getenv("PORT")
```

**Python**
```python
v = os.getenv("PORT")
```

**Go**
```go
v, ok := os.LookupEnv("PORT")
```

**TypeScript**
```ts
const v = process.env.PORT
```

> Node. Deno uses Deno.env.get.

**Rust**
```rust
let v = std::env::var("PORT");
```

> Result. Err if unset.

**Odin**
```odin
v, found := os.lookup_env("PORT", context.allocator)
defer delete(v)
```

**Gleam**
```gleam
let result = envoy.get("PORT")
```

> envoy or gleam_erlang. Target-specific; not in gleam_stdlib.


### Read whole text file — *partial match*

**Java**
```java
var s = Files.readString(path);
```

**Kotlin**
```kotlin
val s = File(path).readText()
```

**Python**
```python
s = Path(path).read_text()
```

**Go**
```go
b, err := os.ReadFile(path)
s := string(b)
```

**TypeScript**
```ts
const s = await readFile(path, "utf8")
```

> node:fs/promises. Browser has no filesystem.

**Rust**
```rust
let s = std::fs::read_to_string(path)?;
```

**Odin**
```odin
data, err := os.read_entire_file(path, context.allocator)
defer delete(data)
```

**Gleam**
```gleam
let result = simplifile.read(path)
```

> simplifile is the usual package. Erlang vs JS backends differ.


### Stdin / stdout

**Java**
```java
var line = new BufferedReader(
    new InputStreamReader(System.in)).readLine();
System.out.print(s);
```

**Kotlin**
```kotlin
val line = readln()
print(s)
```

**Python**
```python
line = sys.stdin.readline()
sys.stdout.write(s)
```

**Go**
```go
line, err := bufio.NewReader(os.Stdin).ReadString('\n')
fmt.Print(s)
```

**TypeScript**
```ts
const line = await once(process.stdin, "data")
process.stdout.write(s)
```

> Node streams. once() is node:events.

**Rust**
```rust
io::stdin().read_line(&mut line)?;
print!("{s}");
```

**Odin**
```odin
fmt.print(s)
// read from os.stdin with a buffered helper
```

**Gleam**
```gleam
io.println(s)
```

> gleam/io covers stdout. Stdin is target/package-specific.


### Read binary file — *partial match*

**Java**
```java
byte[] b = Files.readAllBytes(path);
```

**Kotlin**
```kotlin
val b = File(path).readBytes()
```

**Python**
```python
b = Path(path).read_bytes()
```

**Go**
```go
b, err := os.ReadFile(path)
```

**TypeScript**
```ts
const b = await readFile(path)
```

> node:fs/promises returns Buffer.

**Rust**
```rust
let b = std::fs::read(path)?;
```

**Odin**
```odin
data, err := os.read_entire_file(path, context.allocator)
defer delete(data)
```

**Gleam**
```gleam
let result = simplifile.read_bits(path)
```

> simplifile.read_bits. Confirm the name for your package version.


### Write file — *partial match*

**Java**
```java
Files.write(path, bytes);
```

**Kotlin**
```kotlin
File(path).writeBytes(bytes)
```

**Python**
```python
Path(path).write_bytes(data)
```

**Go**
```go
err := os.WriteFile(path, data, 0644)
```

**TypeScript**
```ts
await writeFile(path, data)
```

> node:fs/promises.

**Rust**
```rust
std::fs::write(path, data)?;
```

**Odin**
```odin
ok := os.write_entire_file(path, data)
```

> Confirm the exact write helper for your compiler version.

**Gleam**
```gleam
let result = simplifile.write_bits(path, data)
```

> simplifile. Erlang vs JS backends differ.


## Testing

### Test

**Java**
```java
@Test
void parses() {
  assertEquals(1, parse("1"));
}
```

**Kotlin**
```kotlin
@Test
fun parses() {
  assertEquals(1, parse("1"))
}
```

**Python**
```python
def test_parses():
    assert parse("1") == 1
```

**Go**
```go
func TestParse(t *testing.T) {
    if got := parse("1"); got != 1 {
        t.Fatal(got)
    }
}
```

**TypeScript**
```ts
test("parses", () => {
  expect(parse("1")).toBe(1)
})
```

> Runner-dependent (node:test, vitest, jest).

**Rust**
```rust
#[test]
fn parses() {
    assert_eq!(1, parse("1"));
}
```

**Odin**
```odin
@(test)
test_parses :: proc(t: ^testing.T) {
    testing.expect_value(t, parse("1"), 1)
}
```

**Gleam**
```gleam
pub fn parses_test() {
  assert parse("1") == 1
}
```

> File lives under test/ and ends in _test.gleam. Generated projects call gleeunit.main().


### Run tests

**Java**
```java
./gradlew test
```

**Kotlin**
```kotlin
./gradlew test
```

**Python**
```python
pytest
python -m unittest
```

> pytest is common; unittest is stdlib.

**Go**
```go
go test ./...
```

**TypeScript**
```ts
npm test
```

> Script and runner are project-dependent.

**Rust**
```rust
cargo test
```

**Odin**
```odin
odin test .
```

**Gleam**
```gleam
gleam test
```


## Networking

### TCP listen — *partial match*

**Java**
```java
var server = new ServerSocket(port);
```

**Kotlin**
```kotlin
val server = ServerSocket(port)
```

**Python**
```python
s = socket.socket()
s.bind(("127.0.0.1", port))
s.listen()
```

**Go**
```go
ln, err := net.Listen("tcp", fmt.Sprintf(":%d", port))
```

**TypeScript**
```ts
const server = net.createServer(handler)
server.listen(port)
```

> Node net. createServer already takes the connection handler.

**Rust**
```rust
let listener = TcpListener::bind(("127.0.0.1", port))?;
```

**Odin**
```odin
server, err := net.listen_tcp({net.IP4_Any, port})
```

**Gleam**
```gleam
glisten.new(init, loop)
|> glisten.start(port)
```

> No TCP in gleam_stdlib. On BEAM, glisten (or the CodeCrafters starter). Confirm the builder API for your version.


### TCP accept / connection loop — *wrong Java model*

**Java**
```java
while (true) {
  var socket = server.accept();
  ...
}
```

**Kotlin**
```kotlin
while (true) {
  val socket = server.accept()
  ...
}
```

**Python**
```python
while True:
    conn, addr = s.accept()
    ...
```

**Go**
```go
for {
    conn, err := ln.Accept()
    ...
}
```

**TypeScript**
```ts
net.createServer(socket => {
  ...
})
```

> Node registers a callback. There is no blocking accept loop.

**Rust**
```rust
for stream in listener.incoming() {
    let stream = stream?;
    ...
}
```

**Odin**
```odin
for {
    client, source, err := net.accept_tcp(server)
    ...
}
```

**Gleam**
```gleam
fn loop(state, msg, conn) {
  // glisten calls this per connection event
}
```

> glisten owns acceptors. You write a handler, not an accept loop.


### Read bytes from TCP connection — *partial match*

**Java**
```java
int n = in.read(buffer);
```

> n == -1 is EOF. n may be smaller than buffer.length.

**Kotlin**
```kotlin
val n = input.read(buffer)
```

**Python**
```python
data = conn.recv(4096)
```

**Go**
```go
n, err := conn.Read(buf)
```

**TypeScript**
```ts
socket.on("data", (chunk: Buffer) => {
  ...
})
```

> Push, not pull. You accumulate chunks; you do not call read().

**Rust**
```rust
let n = stream.read(&mut buf)?;
```

**Odin**
```odin
n, err := net.recv_tcp(client, buf)
```

**Gleam**
```gleam
Packet(data) -> {
  // BitArray from the connection
}
```

> Package-specific messages, typically BitArray.


### Write bytes to TCP connection — *partial match*

**Java**
```java
out.write(bytes);
```

**Kotlin**
```kotlin
output.write(bytes)
```

**Python**
```python
conn.sendall(data)
```

> sendall retries until all bytes are queued.

**Go**
```go
_, err := conn.Write(data)
```

> Write can be short. See write-all.

**TypeScript**
```ts
socket.write(data)
```

> Node. write() may buffer; listen for drain if you flood the socket.

**Rust**
```rust
stream.write_all(data)?;
```

**Odin**
```odin
n, err := net.send_tcp(client, data)
```

**Gleam**
```gleam
glisten.send(conn, data)
```

> Name and arguments are package-version specific.


### TCP client connect — *partial match*

**Java**
```java
var socket = new Socket("127.0.0.1", port);
```

**Kotlin**
```kotlin
val socket = Socket("127.0.0.1", port)
```

**Python**
```python
conn = socket.create_connection(("127.0.0.1", port))
```

**Go**
```go
conn, err := net.Dial("tcp", addr)
```

**TypeScript**
```ts
const socket = net.createConnection({ host, port })
```

> Node net.

**Rust**
```rust
let stream = TcpStream::connect(("127.0.0.1", port))?;
```

**Odin**
```odin
client, err := net.dial_tcp({net.IP4_Loopback, port})
```

> Confirm dial helper and address type for your compiler version.

**Gleam**
```gleam
// gleam add mug
mug.connect(host, port, timeout_ms)
```

> No stdlib client. mug is a common BEAM TCP client; confirm the API.


### Close / shutdown connection

**Java**
```java
socket.close();
```

**Kotlin**
```kotlin
socket.close()
```

**Python**
```python
conn.close()
```

**Go**
```go
conn.Close()
```

**TypeScript**
```ts
socket.end()
```

> end() half-closes after flushing. destroy() is abrupt.

**Rust**
```rust
stream.shutdown(Shutdown::Both)?;
```

> Drop also closes. shutdown is explicit half/full close.

**Odin**
```odin
net.close(client)
```

**Gleam**
```gleam
glisten.close(conn)
```

> Package-specific. Confirm the close helper.


### Read until delimiter or N bytes — *partial match*

**Java**
```java
var reader = new BufferedReader(
    new InputStreamReader(in, StandardCharsets.UTF_8));
String line = reader.readLine();
```

> readLine() strips the newline and returns null at EOF.

**Kotlin**
```kotlin
val line = input.bufferedReader().readLine()
```

**Python**
```python
line = conn.makefile().readline()
chunk = conn.recv(n)
```

**Go**
```go
r := bufio.NewReader(conn)
line, err := r.ReadBytes('\n')
chunk := make([]byte, n)
_, err = io.ReadFull(r, chunk)
```

**TypeScript**
```ts
buf = Buffer.concat([buf, chunk])
const i = buf.indexOf("\n")
if (i >= 0) {
  const line = buf.subarray(0, i)
  buf = buf.subarray(i + 1)
}
```

> You must reassemble frames. data events are not message boundaries.

**Rust**
```rust
let mut r = BufReader::new(&stream);
r.read_until(b'\n', &mut line)?;
r.read_exact(&mut chunk)?;
```

**Odin**
```odin
// accumulate in a buffer; scan for \n
n, err := net.recv_tcp(client, buf[filled:])
```

> No std bufio. Keep a filled count and compact the buffer after each frame.

**Gleam**
```gleam
let combined = bit_array.append(buf, chunk)
// split on <<"\n">> yourself
```

> If the package already delivers messages, still buffer if a frame can split.


### Write-all / short writes — *partial match*

**Java**
```java
out.write(bytes);
out.flush();
```

> OutputStream.write(byte[]) writes the whole array or throws. Still flush sockets.

**Kotlin**
```kotlin
output.write(bytes)
output.flush()
```

**Python**
```python
conn.sendall(data)
```

**Go**
```go
_, err := io.Copy(conn, bytes.NewReader(data))
```

> conn.Write can return a short write without err == nil. Loop or use io.Copy.

**TypeScript**
```ts
const ok = socket.write(data)
if (!ok) socket.once("drain", resume)
```

> write() returning false means the kernel buffer is full, not that data was lost.

**Rust**
```rust
stream.write_all(data)?;
```

**Odin**
```odin
for remaining := data; len(remaining) > 0; {
    n, err := net.send_tcp(client, remaining)
    remaining = remaining[n:]
}
```

**Gleam**
```gleam
glisten.send(conn, data)
```

> Treat send as package-defined; do not assume POSIX short writes.


### Timeout / deadline — *partial match*

**Java**
```java
socket.setSoTimeout(1000);
```

> SoTimeout applies to blocking reads; it throws SocketTimeoutException.

**Kotlin**
```kotlin
socket.soTimeout = 1000
```

**Python**
```python
conn.settimeout(1.0)
```

**Go**
```go
conn.SetDeadline(time.Now().Add(time.Second))
```

> Deadline is absolute. Reset it on each request if you want a per-read timeout.

**TypeScript**
```ts
socket.setTimeout(1000)
```

> Fires a timeout event; it does not throw from write().

**Rust**
```rust
stream.set_read_timeout(Some(Duration::from_secs(1)))?;
```

**Odin**
```odin
net.set_option(client, net.Receive_Timeout, 1 * time.Second)
```

> Option names are version-sensitive. Compiler-check this.

**Gleam**
```gleam
process.send_after(self(), 1000, Timeout)
```

> BEAM process timers, not socket options. Package APIs may wrap this.


## Concurrency

### Spawn concurrent work — *wrong Java model*

**Java**
```java
Thread.startVirtualThread(() -> work());
```

> Virtual threads are Java 21+. Older: new Thread(work).start().

**Kotlin**
```kotlin
launch { work() }
```

> Needs a coroutine scope. launch is not a language keyword you can call anywhere.

**Python**
```python
threading.Thread(target=work).start()
```

> Or asyncio.create_task(...) for cooperative async.

**Go**
```go
go work()
```

**TypeScript**
```ts
await work()
```

> The event loop already interleaves I/O. Use Worker for CPU parallelism.

**Rust**
```rust
std::thread::spawn(|| work());
```

**Odin**
```odin
thread.create_and_start(proc() { work() })
```

> See core:thread; exact helpers vary by version.

**Gleam**
```gleam
process.spawn(fn() { work() })
```

> gleam_erlang on BEAM. JS target has no process.spawn.


### Channel / message passing — *wrong Java model*

**Java**
```java
var q = new LinkedBlockingQueue<T>();
```

**Kotlin**
```kotlin
val ch = Channel<T>()
```

**Python**
```python
q = queue.Queue()
```

**Go**
```go
ch := make(chan T)
```

**TypeScript**
```ts
const q: T[] = []
```

> No built-in CSP channel. Use an async queue or a library.

**Rust**
```rust
let (tx, rx) = std::sync::mpsc::channel();
```

**Odin**
```odin
c, _ := chan.create(chan.Chan(MyType), context.allocator)
defer chan.destroy(c)
```

> core:sync/chan. Confirm create/destroy for your version.

**Gleam**
```gleam
process.send(pid, msg)
let selector = process.new_selector()
```

> BEAM processes plus typed selectors via gleam_erlang / OTP libraries.
