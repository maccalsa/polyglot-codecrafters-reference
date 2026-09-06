# Rust for a Java programmer

This is a **lookup sheet**, not a tutorial. Start with the concept you already know and translate into the language’s native shape.

## Commands

```bash
cargo test
cargo run
cargo check
```

## Java-brain traps

- Ownership and borrowing are not syntax trivia; they shape your program structure.
- `String` owns UTF-8 data; `&str` borrows string data. Learn this distinction early.
- `Vec<T>` is the usual growable contiguous collection.
- `Option<T>` and `Result<T,E>` replace huge classes of null/exception flows.
- `?` propagates compatible errors and is central to idiomatic Rust.
- Iteration has ownership choices: `iter()`, `iter_mut()`, `into_iter()`.
- `Drop` gives deterministic cleanup without `finally`/try-with-resources.
- Don't fight the borrow checker by cloning everything; first ask who should own the data.

## Construct lookup

### Fundamentals

**Immutable binding**
```rust
let x = 42;
```

**Constant**
```rust
const PORT: u16 = 6379;
```

**Mutable variable**
```rust
let mut x = 1;
x = 2;
```

**Function**
```rust
fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

**Anonymous function / lambda**
```rust
|x| x * 2
```

**Generic function**
```rust
fn id<T>(x: T) -> T { x }
```

**Tuple / pair**
```rust
let p: (i32, &str) = (1, "a");
```

### Types

**Data carrier / record**
```rust
struct User {
    name: String,
    age: u32,
}
```

**Interface / trait / protocol**
```rust
trait Reader {
    fn read(&mut self) -> Vec<u8>;
}
```

**Enum / sum type**
```rust
enum Msg {
    Ping { id: i32 },
    Quit,
}
```

**Optional / nullable**
```rust
let name: Option<String>
```

**Default when missing**
```rust
let n = value.unwrap_or("default");
```

### Control flow

**If / else**
```rust
if x > 0 {
    ...
} else {
    ...
}
```

**Pattern match / switch**
```rust
match msg {
    Msg::Ping { id } => ...,
    Msg::Quit => ...,
}
```

**For each**
```rust
for x in xs {
    ...
}
```

**Index + value iteration**
```rust
for (i, x) in xs.iter().enumerate() { ... }
```

**While loop**
```rust
while condition { ... }
```

**Early return**
```rust
if bad { return result; }
```

### Collections

**List / dynamic sequence**
```rust
let mut xs: Vec<i32> = Vec::new();
```

**Fixed / contiguous array**
```rust
let xs = [0i32; 16];
```

**Map / dictionary creation**
```rust
let mut m = HashMap::<String, i32>::new();
```

**Map lookup with presence**
```rust
if let Some(v) = m.get(&key) { ... }
```

**Set creation**
```rust
let mut s = HashSet::<String>::new();
```

**Filter**
```rust
let ys: Vec<_> = xs.into_iter().filter(|x| *x > 0).collect();
```

**Map / transform**
```rust
let ys: Vec<_> = xs.into_iter().map(|x| x * 2).collect();
```

**Fold / reduce**
```rust
let total: i32 = xs.iter().sum();
```

### Strings & bytes

**String interpolation**
```rust
let s = format!("port={port}");
```

**UTF-8 string → bytes**
```rust
let b = s.as_bytes();
```

**Bytes → UTF-8 string**
```rust
let s = std::str::from_utf8(&b)?;
```

**Split string**
```rust
let parts: Vec<_> = s.split(':').collect();
```

**Parse integer**
```rust
let n: i32 = s.parse()?;
```

### Errors & resources

**Represent recoverable error**
```rust
fn method() -> Result<T, E>
```

**Propagate error**
```rust
let v = method()?;
```

**Cleanup / defer**
```rust
let r = open()?;
// Drop runs at end of scope
```

**Assertion**
```rust
assert!(x > 0);
```

### I/O & process

**CLI arguments**
```rust
let args: Vec<String> = std::env::args().skip(1).collect();
```

**Environment variable**
```rust
let v = std::env::var("PORT");
```

**Read whole text file**
```rust
let s = std::fs::read_to_string(path)?;
```

### Testing

**Test**
```rust
#[test]
fn parses() {
    assert_eq!(1, parse("1"));
}
```

**Run tests**
```rust
cargo test
```

### Networking

**TCP listen**
```rust
let listener = TcpListener::bind(("127.0.0.1", port))?;
```

**TCP accept / connection loop**
```rust
for stream in listener.incoming() {
    let stream = stream?;
    ...
}
```

**Read bytes from TCP connection**
```rust
let n = stream.read(&mut buf)?;
```

**Write bytes to TCP connection**
```rust
stream.write_all(data)?;
```

### Concurrency

**Spawn concurrent work**
```rust
std::thread::spawn(|| work());
```

**Channel / message passing**
```rust
let (tx, rx) = std::sync::mpsc::channel();
```
