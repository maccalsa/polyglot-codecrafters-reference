# TypeScript for a Java programmer

This is a **lookup sheet**, not a tutorial. Start with the concept you already know and translate into the language’s native shape.

## Commands

```bash
npm test
npm run dev     # project-dependent
npx tsc --noEmit
```

## Java-brain traps

- TypeScript disappears at runtime: JavaScript semantics still win.
- `number` is normally IEEE-754 double precision; it is not Java `int`/`long`.
- `Map`/`Set` differ from plain JS objects/arrays.
- Narrowing and discriminated unions are often a better fit than class hierarchies.
- Node APIs (`Buffer`, `net`, `fs`) are runtime APIs, not TypeScript language features.
- `async`/`await` is Promise-based cooperative async I/O, not Java threads.
- Be deliberate about `undefined` vs `null`; most TS APIs lean heavily on `undefined`.
- Node `net` is event-driven. `data` chunks are not message boundaries; you reassemble frames yourself.
- I/O snippets here are Node (`process`, `fs`, `net`). Deno, Bun, and the browser are different runtimes.

## Construct lookup

### Fundamentals

**Immutable binding**
```ts
const x = 42
```

**Constant**
```ts
const PORT = 6379
```

**Mutable variable**
```ts
let x = 1
x = 2
```

**Function**
```ts
function add(a: number, b: number): number {
  return a + b
}
```

**Anonymous function / lambda**
```ts
(x: number) => x * 2
```

**Generic function**
```ts
function id<T>(x: T): T { return x }
```

**Tuple / pair**
```ts
const p: [number, string] = [1, "a"]
```

### Types

**Data carrier / record**
```ts
type User = { name: string; age: number }
```

**Interface / trait / protocol**
```ts
interface Reader {
  read(): Uint8Array
}
```

**Enum / sum type**
```ts
type Msg =
  | { kind: "ping"; id: number }
  | { kind: "quit" }
```

**Optional / nullable**
```ts
let name: string | undefined
```

**Default when missing**
```ts
const n = value ?? "default"
```

### Control flow

**If / else**
```ts
if (x > 0) {
  ...
} else {
  ...
}
```

**Pattern match / switch**
```ts
switch (msg.kind) {
  case "ping": ...
}
```

**For each**
```ts
for (const x of xs) {
  ...
}
```

**Index + value iteration**
```ts
for (const [i, x] of xs.entries()) { ... }
```

**While loop**
```ts
while (condition) { ... }
```

**Early return**
```ts
if (bad) return result
```

### Collections

**List / dynamic sequence**
```ts
const xs: number[] = []
```

**Fixed / contiguous array**
```ts
const xs = new Int32Array(16)
```

**Map / dictionary creation**
```ts
const m = new Map<string, number>()
```

**Map lookup with presence**
```ts
const v = m.get(key)
if (v !== undefined) { ... }
```

**Set creation**
```ts
const s = new Set<string>()
```

**Filter**
```ts
const ys = xs.filter(x => x > 0)
```

**Map / transform**
```ts
const ys = xs.map(x => x * 2)
```

**Fold / reduce**
```ts
const total = xs.reduce((a, x) => a + x, 0)
```

### Strings & bytes

**String interpolation**
```ts
const s = `port=${port}`
```

**UTF-8 string → bytes**
```ts
const b = new TextEncoder().encode(s)
```

**Bytes → UTF-8 string**
```ts
const s = new TextDecoder().decode(b)
```

**Split string**
```ts
const parts = s.split(":")
```

**Parse integer**
```ts
const n = Number.parseInt(s, 10)
```

### Errors & resources

**Represent recoverable error**
```ts
function method(): T  // throw, or use an explicit Result union
```

**Propagate error**
```ts
return method() // thrown exception propagates
```

**Cleanup / defer**
```ts
// often try/finally; explicit resource management depends on runtime
```

**Assertion**
```ts
if (!(x > 0)) throw new Error("assertion failed")
```

### I/O & process

**CLI arguments**
```ts
const args = process.argv.slice(2) // Node
```

**Environment variable**
```ts
const v = process.env.PORT // Node
```

**Read whole text file**
```ts
const s = await readFile(path, "utf8") // node:fs/promises
```

### Testing

**Test**
```ts
test("parses", () => {
  expect(parse("1")).toBe(1)
}) // runner-dependent
```

**Run tests**
```ts
npm test  # project/runner-dependent
```

### Networking

**TCP listen**
```ts
const server = net.createServer(handler)
server.listen(port) // Node
```

**TCP accept / connection loop**
```ts
net.createServer(socket => {
  ...
}) // callback/event-driven Node
```

**Read bytes from TCP connection**
```ts
socket.on("data", (chunk: Buffer) => { ... }) // Node
```

**Write bytes to TCP connection**
```ts
socket.write(data) // Node
```

### Concurrency

**Spawn concurrent work**
```ts
// event loop for async I/O; Worker for CPU parallelism
```

**Channel / message passing**
```ts
// no built-in typed CSP channel; use async queues/libs
```
