# Kotlin for a Java programmer

This is a **lookup sheet**, not a tutorial. Start with the concept you already know and translate into the language’s native shape.

## Commands

```bash
./gradlew test
./gradlew run   # if application plugin/starter supports it
```

## Java-brain traps

- `val` means the reference cannot be reassigned; the object may still be mutable.
- Nullability is part of the type system (`T` vs `T?`). Prefer `?.`, `?:`, and explicit checks over `!!`.
- Collections have read-only and mutable interfaces; `List<T>` is not the same promise as Java's `List<T>`.
- Exceptions are unchecked. There is no Java-style checked-exception contract.
- Extension functions are statically dispatched; they do not add virtual methods to the receiver.
- For JVM CodeCrafters challenges, Java networking/file APIs remain available, but prefer Kotlin idioms around them.

## Construct lookup

### Fundamentals

**Immutable binding**
```kotlin
val x = 42
```

**Constant**
```kotlin
const val PORT = 6379
```

**Mutable variable**
```kotlin
var x = 1
x = 2
```

**Function**
```kotlin
fun add(a: Int, b: Int): Int = a + b
```

**Anonymous function / lambda**
```kotlin
{ x -> x * 2 }
```

**Generic function**
```kotlin
fun <T> id(x: T): T = x
```

**Tuple / pair**
```kotlin
val p = 1 to "a"
// Pair<Int, String>
```

### Types

**Data carrier / record**
```kotlin
data class User(val name: String, val age: Int)
```

**Interface / trait / protocol**
```kotlin
interface Reader {
  fun read(): ByteArray
}
```

**Enum / sum type**
```kotlin
sealed interface Msg
data class Ping(val id: Int): Msg
data object Quit: Msg
```

**Optional / nullable**
```kotlin
val name: String?
```

**Default when missing**
```kotlin
val n = value ?: "default"
```

### Control flow

**If / else**
```kotlin
if (x > 0) {
  ...
} else {
  ...
}
```

**Pattern match / switch**
```kotlin
when (msg) {
  is Ping -> handle(msg)
  Quit -> stop()
}
```

**For each**
```kotlin
for (x in xs) { ... }
```

**Index + value iteration**
```kotlin
for ((i, x) in xs.withIndex()) { ... }
```

**While loop**
```kotlin
while (condition) { ... }
```

**Early return**
```kotlin
if (bad) return result
```

### Collections

**List / dynamic sequence**
```kotlin
val xs = mutableListOf<Int>()
```

**Fixed / contiguous array**
```kotlin
val xs = IntArray(16)
```

**Map / dictionary creation**
```kotlin
val m = mutableMapOf<String, Int>()
```

**Map lookup with presence**
```kotlin
val v = m[key]
if (v != null) { ... }
```

**Set creation**
```kotlin
val s = mutableSetOf<String>()
```

**Filter**
```kotlin
val ys = xs.filter { it > 0 }
```

**Map / transform**
```kotlin
val ys = xs.map { it * 2 }
```

**Fold / reduce**
```kotlin
val total = xs.fold(0) { acc, x -> acc + x }
```

### Strings & bytes

**String interpolation**
```kotlin
val s = "port=$port"
```

**UTF-8 string → bytes**
```kotlin
val b = s.encodeToByteArray()
```

**Bytes → UTF-8 string**
```kotlin
val s = b.decodeToString()
```

**Split string**
```kotlin
val parts = s.split(":")
```

**Parse integer**
```kotlin
val n = s.toInt()
// or toIntOrNull()
```

### Errors & resources

**Represent recoverable error**
```kotlin
fun method(): T  // exceptions unchecked
```

**Propagate error**
```kotlin
return method()  // exception propagates
```

**Cleanup / defer**
```kotlin
open().use { resource -> ... }
```

**Assertion**
```kotlin
check(x > 0)
// assert(...) may be JVM-assertion dependent
```

### I/O & process

**CLI arguments**
```kotlin
fun main(args: Array<String>) { ... }
```

**Environment variable**
```kotlin
val v = System.getenv("PORT")
```

**Read whole text file**
```kotlin
val s = File(path).readText()
```

### Testing

**Test**
```kotlin
@Test
fun parses() {
  assertEquals(1, parse("1"))
}
```

**Run tests**
```kotlin
./gradlew test
```

### Networking

**TCP listen**
```kotlin
val server = ServerSocket(port)
```

**TCP accept / connection loop**
```kotlin
while (true) {
  val socket = server.accept()
}
```

**Read bytes from TCP connection**
```kotlin
val n = input.read(buffer)
```

**Write bytes to TCP connection**
```kotlin
output.write(bytes)
```

### Concurrency

**Spawn concurrent work**
```kotlin
launch { work() } // coroutine scope
```

**Channel / message passing**
```kotlin
val ch = Channel<T>()
```
