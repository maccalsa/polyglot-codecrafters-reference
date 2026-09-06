# Go for a Java programmer

This is a **lookup sheet**, not a tutorial. Start with the concept you already know and translate into the language’s native shape.

## Commands

```bash
go test ./...
go run .
```

## Java-brain traps

- The zero value matters. Many types are useful without constructors.
- Slices are descriptors over backing arrays; copying a slice does not copy its elements/backing storage.
- Maps return zero values for missing keys; use the comma-ok form when absence matters.
- Errors are ordinary values. Avoid recreating exception-style control flow with `panic`.
- Interfaces are implemented implicitly.
- Goroutines are cheap, but they still need ownership/cancellation/backpressure decisions.
- Strings are immutable byte sequences containing UTF-8 by convention; `range` over a string decodes runes.
- A slice passed downstream shares its backing array. `append` can mutate callers or leave a stale header.
- `conn.Write` can be a short write. Loop or use `io.Copy` / `io.ReadFull` for protocol framing.

## Construct lookup

### Fundamentals

**Immutable binding**
```go
x := 42  // binding itself is mutable
```

**Constant**
```go
const Port = 6379
```

**Mutable variable**
```go
x := 1
x = 2
```

**Function**
```go
func add(a, b int) int {
    return a + b
}
```

**Anonymous function / lambda**
```go
func(x int) int { return x * 2 }
```

**Generic function**
```go
func id[T any](x T) T { return x }
```

**Tuple / pair**
```go
// multiple return values are idiomatic
return 1, "a"
```

### Types

**Data carrier / record**
```go
type User struct {
    Name string
    Age  int
}
```

**Interface / trait / protocol**
```go
type Reader interface {
    Read([]byte) (int, error)
}
```

**Enum / sum type**
```go
// usually tagged struct/interface; no native sum type
```

**Optional / nullable**
```go
// often pointer or (value, ok)
var name *string
```

**Default when missing**
```go
if value == "" { value = "default" }
```

### Control flow

**If / else**
```go
if x > 0 {
    ...
} else {
    ...
}
```

**Pattern match / switch**
```go
switch v := msg.(type) {
case Ping:
    _ = v
}
```

**For each**
```go
for _, x := range xs {
    ...
}
```

**Index + value iteration**
```go
for i, x := range xs {
    ...
}
```

**While loop**
```go
for condition {
    ...
}
```

**Early return**
```go
if bad {
    return result
}
```

### Collections

**List / dynamic sequence**
```go
xs := []int{}
```

**Fixed / contiguous array**
```go
var xs [16]int
```

**Map / dictionary creation**
```go
m := make(map[string]int)
```

**Map lookup with presence**
```go
v, ok := m[key]
if ok { ... }
```

**Set creation**
```go
s := map[string]struct{}{}
```

**Filter**
```go
ys := make([]int, 0, len(xs))
for _, x := range xs { if x > 0 { ys = append(ys, x) } }
```

**Map / transform**
```go
ys := make([]int, len(xs))
for i, x := range xs { ys[i] = x * 2 }
```

**Fold / reduce**
```go
total := 0
for _, x := range xs { total += x }
```

### Strings & bytes

**String interpolation**
```go
s := fmt.Sprintf("port=%d", port)
```

**UTF-8 string → bytes**
```go
b := []byte(s)
```

**Bytes → UTF-8 string**
```go
s := string(b)
```

**Split string**
```go
parts := strings.Split(s, ":")
```

**Parse integer**
```go
n, err := strconv.Atoi(s)
```

### Errors & resources

**Represent recoverable error**
```go
func method() (T, error)
```

**Propagate error**
```go
v, err := method()
if err != nil { return zero, err }
```

**Cleanup / defer**
```go
r := open()
defer r.Close()
```

**Assertion**
```go
// no built-in assert; explicit if/panic or test helper
```

### I/O & process

**CLI arguments**
```go
args := os.Args[1:]
```

**Environment variable**
```go
v, ok := os.LookupEnv("PORT")
```

**Read whole text file**
```go
b, err := os.ReadFile(path)
s := string(b)
```

### Testing

**Test**
```go
func TestParse(t *testing.T) {
    if got := parse("1"); got != 1 { t.Fatal(got) }
}
```

**Run tests**
```go
go test ./...
```

### Networking

**TCP listen**
```go
ln, err := net.Listen("tcp", fmt.Sprintf(":%d", port))
```

**TCP accept / connection loop**
```go
for {
    conn, err := ln.Accept()
    ...
}
```

**Read bytes from TCP connection**
```go
n, err := conn.Read(buf)
```

**Write bytes to TCP connection**
```go
_, err := conn.Write(data)
```

### Concurrency

**Spawn concurrent work**
```go
go work()
```

**Channel / message passing**
```go
ch := make(chan T)
```
