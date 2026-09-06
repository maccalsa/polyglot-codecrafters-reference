# Java → Polyglot CodeCrafters Matrix

> Goal: you already know the programming concept. This answers **“what does it look like here?”** and flags places where there is no direct equivalent.

Targets: **Kotlin · Python · Go · TypeScript · Rust · Odin · Gleam**. Java is the reference column.

This is deliberately CodeCrafters-oriented: bytes, parsing, files, sockets, tests, errors, and concurrency are included alongside language syntax.

## Fundamentals

### Immutable binding

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
x = 42  # no language-level const
```

**Go**
```go
x := 42  // binding itself is mutable
```

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
x := 42  // variable; use :: for constants
```

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

**Python**
```python
PORT = 6379  # convention: uppercase
```

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

### Mutable variable

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
// bindings are immutable
let x = 1
let x = 2  // shadowing
```

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
static <T> T id(T x) { return x; }
```

**Kotlin**
```kotlin
fun <T> id(x: T): T = x
```

**Python**
```python
def id[T](x: T) -> T:
    return x  # Python 3.12+
```

**Go**
```go
func id[T any](x T) T { return x }
```

**TypeScript**
```ts
function id<T>(x: T): T { return x }
```

**Rust**
```rust
fn id<T>(x: T) -> T { x }
```

**Odin**
```odin
id :: proc(x: $T) -> T { return x }
```

**Gleam**
```gleam
fn id(x: a) -> a { x }
```

### Tuple / pair

**Java**
```java
record Pair<A,B>(A first, B second) {}
```

**Kotlin**
```kotlin
val p = 1 to "a"
// Pair<Int, String>
```

**Python**
```python
p = (1, "a")
```

**Go**
```go
// multiple return values are idiomatic
return 1, "a"
```

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
// no general first-class tuple type
// use a small struct, or multiple return values:
a, b := get_pair()
```

**Gleam**
```gleam
let p = #(1, "a")
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
type User = { name: string; age: number }
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

### Interface / trait / protocol

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
// no interface construct; use procedures,
// tagged unions, or procedure fields
```

**Gleam**
```gleam
// no interfaces/typeclasses; model behaviour
// with functions and custom types
```

### Enum / sum type

**Java**
```java
sealed interface Msg permits Ping, Quit {}
record Ping(int id) implements Msg {}
record Quit() implements Msg {}
```

**Kotlin**
```kotlin
sealed interface Msg
data class Ping(val id: Int): Msg
data object Quit: Msg
```

**Python**
```python
type Msg = Ping | Quit  # 3.12 type alias
```

**Go**
```go
// usually tagged struct/interface; no native sum type
```

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
Msg :: union { Ping, Quit }
```

**Gleam**
```gleam
pub type Msg {
  Ping(id: Int)
  Quit
}
```

### Optional / nullable

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
// often pointer or (value, ok)
var name *string
```

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
// core APIs also commonly use (value, ok)
```

**Gleam**
```gleam
let name: Option(String)
```

### Default when missing

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
if value == "" { value = "default" }
```

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
n := value.? or_else "default"  // for Maybe(string)
```

**Gleam**
```gleam
let n = option.unwrap(value, "default")
```

## Control flow

### If / else

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

### Pattern match / switch

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
    case Ping(id): ...
    case Quit(): ...
```

**Go**
```go
switch v := msg.(type) {
case Ping:
    _ = v
}
```

**TypeScript**
```ts
switch (msg.kind) {
  case "ping": ...
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
for (var x : xs) { ... }
```

**Kotlin**
```kotlin
for (x in xs) { ... }
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

### Index + value iteration

**Java**
```java
for (int i = 0; i < xs.size(); i++) {
  var x = xs.get(i);
}
```

**Kotlin**
```kotlin
for ((i, x) in xs.withIndex()) { ... }
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
for (const [i, x] of xs.entries()) { ... }
```

**Rust**
```rust
for (i, x) in xs.iter().enumerate() { ... }
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

### While loop

**Java**
```java
while (condition) { ... }
```

**Kotlin**
```kotlin
while (condition) { ... }
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

**TypeScript**
```ts
while (condition) { ... }
```

**Rust**
```rust
while condition { ... }
```

**Odin**
```odin
for condition {
    ...
}
```

**Gleam**
```gleam
// no while loop; use recursion or iterator/list functions
```

### Early return

**Java**
```java
if (bad) return result;
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
if bad { return result; }
```

**Odin**
```odin
if bad { return result }
```

**Gleam**
```gleam
// structure with case/result pipelines; no imperative early-return idiom
```

## Collections

### List / dynamic sequence

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

**Gleam**
```gleam
let xs: List(Int) = []
```

### Fixed / contiguous array

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
# list is usual general sequence
xs = [0] * 16
```

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
// List is linked; BitArray for bytes.
// No general mutable array in core language.
```

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
if (v != null) { ... }
```

**Kotlin**
```kotlin
val v = m[key]
if (v != null) { ... }
```

**Python**
```python
if key in m:
    v = m[key]
```

**Go**
```go
v, ok := m[key]
if ok { ... }
```

**TypeScript**
```ts
const v = m.get(key)
if (v !== undefined) { ... }
```

**Rust**
```rust
if let Some(v) = m.get(&key) { ... }
```

**Odin**
```odin
v, ok := m[key]
if ok { ... }
```

**Gleam**
```gleam
case dict.get(m, key) {
  Ok(v) -> ...
  Error(Nil) -> ...
}
```

### Set creation

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
// idiom: map[T]struct{} or bit_set for enum-like keys
```

**Gleam**
```gleam
let s = set.new()
```

### Filter

**Java**
```java
var ys = xs.stream().filter(x -> x > 0).toList();
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
for _, x := range xs { if x > 0 { ys = append(ys, x) } }
```

**TypeScript**
```ts
const ys = xs.filter(x => x > 0)
```

**Rust**
```rust
let ys: Vec<_> = xs.into_iter().filter(|x| *x > 0).collect();
```

**Odin**
```odin
ys := make([dynamic]int)
for x in xs { if x > 0 { append(&ys, x) } }
```

**Gleam**
```gleam
let ys = list.filter(xs, fn(x) { x > 0 })
```

### Map / transform

**Java**
```java
var ys = xs.stream().map(x -> x * 2).toList();
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
for i, x := range xs { ys[i] = x * 2 }
```

**TypeScript**
```ts
const ys = xs.map(x => x * 2)
```

**Rust**
```rust
let ys: Vec<_> = xs.into_iter().map(|x| x * 2).collect();
```

**Odin**
```odin
ys := make([dynamic]int)
for x in xs { append(&ys, x*2) }
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
for _, x := range xs { total += x }
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
for x in xs { total += x }
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

### UTF-8 string → bytes

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

**Odin**
```odin
b := transmute([]u8)s  // view; do not mutate
// clone if ownership/mutation is needed
```

**Gleam**
```gleam
let b = bit_array.from_string(s)
```

### Bytes → UTF-8 string

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

**Odin**
```odin
s := string(b)  // conversion semantics matter; clone if lifetime requires
```

**Gleam**
```gleam
let result = bit_array.to_string(b)  // Result(String, Nil)
```

### Split string

**Java**
```java
var parts = s.split(":", -1);
```

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
// or toIntOrNull()
```

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

**Rust**
```rust
let n: i32 = s.parse()?;
```

**Odin**
```odin
n, ok := strconv.parse_int(s)
// inspect returned type/options for your Odin version
```

**Gleam**
```gleam
let result = int.parse(s)  // Result(Int, Nil)
```

## Errors & resources

### Represent recoverable error

**Java**
```java
T method() throws IOException
```

**Kotlin**
```kotlin
fun method(): T  // exceptions unchecked
```

**Python**
```python
def method() -> T:  # raises exception
```

**Go**
```go
func method() (T, error)
```

**TypeScript**
```ts
function method(): T  // throw, or use an explicit Result union
```

**Rust**
```rust
fn method() -> Result<T, E>
```

**Odin**
```odin
method :: proc() -> (T, Error)
// explicit multi-return is common
```

**Gleam**
```gleam
fn method() -> Result(T, E)
```

### Propagate error

**Java**
```java
return method(); // or throws
```

**Kotlin**
```kotlin
return method()  // exception propagates
```

**Python**
```python
return method()  # exception propagates
```

**Go**
```go
v, err := method()
if err != nil { return zero, err }
```

**TypeScript**
```ts
return method() // thrown exception propagates
```

**Rust**
```rust
let v = method()?;
```

**Odin**
```odin
v, err := method()
if err != nil { return {}, err }
```

**Gleam**
```gleam
use v <- result.try(method())
// or case method() { ... }
```

### Cleanup / defer

**Java**
```java
try (var in = open()) {
  ...
}
```

**Kotlin**
```kotlin
open().use { resource -> ... }
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
// often try/finally; explicit resource management depends on runtime
```

**Rust**
```rust
let r = open()?;
// Drop runs at end of scope
```

**Odin**
```odin
r := open()
defer close(r)
```

**Gleam**
```gleam
// immutable/managed runtime; resource APIs are library/runtime-specific
```

### Assertion

**Java**
```java
assert x > 0;
```

**Kotlin**
```kotlin
check(x > 0)
// assert(...) may be JVM-assertion dependent
```

**Python**
```python
assert x > 0
```

**Go**
```go
// no built-in assert; explicit if/panic or test helper
```

**TypeScript**
```ts
if (!(x > 0)) throw new Error("assertion failed")
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

### CLI arguments

**Java**
```java
var args = ... // main(String[] args)
```

**Kotlin**
```kotlin
fun main(args: Array<String>) { ... }
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
const args = process.argv.slice(2) // Node
```

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
// target/runtime-specific; on Erlang use gleam_erlang/os or starter helpers
```

### Environment variable

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
const v = process.env.PORT // Node
```

**Rust**
```rust
let v = std::env::var("PORT");
```

**Odin**
```odin
v, found := os.lookup_env("PORT", context.allocator)
defer delete(v)
```

**Gleam**
```gleam
// target/runtime-specific; Erlang helpers live outside gleam_stdlib
```

### Read whole text file

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
const s = await readFile(path, "utf8") // node:fs/promises
```

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
// Erlang target: gleam_erlang/file; JS target: runtime FFI/package
```

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
    if got := parse("1"); got != 1 { t.Fatal(got) }
}
```

**TypeScript**
```ts
test("parses", () => {
  expect(parse("1")).toBe(1)
}) // runner-dependent
```

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
// in test/..._test.gleam
pub fn parses_test() {
  assert parse("1") == 1
}
// generated projects use gleeunit.main() as test main
```

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
pytest  # common
python -m unittest  # stdlib
```

**Go**
```go
go test ./...
```

**TypeScript**
```ts
npm test  # project/runner-dependent
```

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

### TCP listen

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
server.listen(port) // Node
```

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
// no TCP API in gleam_stdlib. On BEAM, use a package such as glisten
// (or CodeCrafters starter/runtime FFI).
```

### TCP accept / connection loop

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
}
```

**Python**
```python
while True:
    conn, addr = s.accept()
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
}) // callback/event-driven Node
```

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
// package/runtime-specific; glisten manages acceptors and handlers
```

### Read bytes from TCP connection

**Java**
```java
int n = in.read(buffer);
```

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
socket.on("data", (chunk: Buffer) => { ... }) // Node
```

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
// package/runtime-specific; typically BitArray messages/data
```

### Write bytes to TCP connection

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

**Go**
```go
_, err := conn.Write(data)
```

**TypeScript**
```ts
socket.write(data) // Node
```

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
// package/runtime-specific; e.g. glisten connection send APIs
```

## Concurrency

### Spawn concurrent work

**Java**
```java
Thread.startVirtualThread(() -> work());
```

**Kotlin**
```kotlin
launch { work() } // coroutine scope
```

**Python**
```python
threading.Thread(target=work).start()
# or asyncio.create_task(...)
```

**Go**
```go
go work()
```

**TypeScript**
```ts
// event loop for async I/O; Worker for CPU parallelism
```

**Rust**
```rust
std::thread::spawn(|| work());
```

**Odin**
```odin
thread.create_and_start(proc() { work() })
// exact API may vary; see core:thread
```

**Gleam**
```gleam
process.spawn(fn() { work() }) // gleam_erlang on BEAM
```

### Channel / message passing

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
// no built-in typed CSP channel; use async queues/libs
```

**Rust**
```rust
let (tx, rx) = std::sync::mpsc::channel();
```

**Odin**
```odin
c, _ := chan.create(chan.Chan(MyType), context.allocator)
defer chan.destroy(c)
// core:sync/chan
```

**Gleam**
```gleam
// BEAM processes + typed selectors/messages via gleam_erlang/OTP libraries
```
