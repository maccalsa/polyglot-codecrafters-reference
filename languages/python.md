# Python for a Java programmer

This is a **lookup sheet**, not a tutorial. Start with the concept you already know and translate into the language’s native shape.

## Commands

```bash
python -m pytest
python app.py
```

## Java-brain traps

- Type hints do not make Python statically typed at runtime. Run a type checker if you want that feedback.
- `list`, `dict`, and `set` are mutable reference objects; assignment aliases them.
- `bytes` is immutable; `bytearray` is mutable.
- Strings are Unicode text, not byte buffers. Protocol work usually means being explicit about encode/decode boundaries.
- Exceptions are the normal error mechanism.
- `asyncio`, OS threads, and processes solve different concurrency problems; don't treat `async` as parallel CPU execution.

## Construct lookup

### Fundamentals

**Immutable binding**
```python
x = 42  # no language-level const
```

**Constant**
```python
PORT = 6379  # convention: uppercase
```

**Mutable variable**
```python
x = 1
x = 2
```

**Function**
```python
def add(a: int, b: int) -> int:
    return a + b
```

**Anonymous function / lambda**
```python
lambda x: x * 2
```

**Generic function**
```python
def id[T](x: T) -> T:
    return x  # Python 3.12+
```

**Tuple / pair**
```python
p = (1, "a")
```

### Types

**Data carrier / record**
```python
@dataclass
class User:
    name: str
    age: int
```

**Interface / trait / protocol**
```python
class Reader(Protocol):
    def read(self) -> bytes: ...
```

**Enum / sum type**
```python
type Msg = Ping | Quit  # 3.12 type alias
```

**Optional / nullable**
```python
name: str | None
```

**Default when missing**
```python
n = value if value is not None else "default"
```

### Control flow

**If / else**
```python
if x > 0:
    ...
else:
    ...
```

**Pattern match / switch**
```python
match msg:
    case Ping(id): ...
    case Quit(): ...
```

**For each**
```python
for x in xs:
    ...
```

**Index + value iteration**
```python
for i, x in enumerate(xs):
    ...
```

**While loop**
```python
while condition:
    ...
```

**Early return**
```python
if bad:
    return result
```

### Collections

**List / dynamic sequence**
```python
xs: list[int] = []
```

**Fixed / contiguous array**
```python
# list is usual general sequence
xs = [0] * 16
```

**Map / dictionary creation**
```python
m: dict[str, int] = {}
```

**Map lookup with presence**
```python
if key in m:
    v = m[key]
```

**Set creation**
```python
s: set[str] = set()
```

**Filter**
```python
ys = [x for x in xs if x > 0]
```

**Map / transform**
```python
ys = [x * 2 for x in xs]
```

**Fold / reduce**
```python
total = sum(xs)
```

### Strings & bytes

**String interpolation**
```python
s = f"port={port}"
```

**UTF-8 string → bytes**
```python
b = s.encode("utf-8")
```

**Bytes → UTF-8 string**
```python
s = b.decode("utf-8")
```

**Split string**
```python
parts = s.split(":")
```

**Parse integer**
```python
n = int(s)
```

### Errors & resources

**Represent recoverable error**
```python
def method() -> T:  # raises exception
```

**Propagate error**
```python
return method()  # exception propagates
```

**Cleanup / defer**
```python
with open_resource() as resource:
    ...
```

**Assertion**
```python
assert x > 0
```

### I/O & process

**CLI arguments**
```python
args = sys.argv[1:]
```

**Environment variable**
```python
v = os.getenv("PORT")
```

**Read whole text file**
```python
s = Path(path).read_text()
```

### Testing

**Test**
```python
def test_parses():
    assert parse("1") == 1
```

**Run tests**
```python
pytest  # common
python -m unittest  # stdlib
```

### Networking

**TCP listen**
```python
s = socket.socket()
s.bind(("127.0.0.1", port))
s.listen()
```

**TCP accept / connection loop**
```python
while True:
    conn, addr = s.accept()
```

**Read bytes from TCP connection**
```python
data = conn.recv(4096)
```

**Write bytes to TCP connection**
```python
conn.sendall(data)
```

### Concurrency

**Spawn concurrent work**
```python
threading.Thread(target=work).start()
# or asyncio.create_task(...)
```

**Channel / message passing**
```python
q = queue.Queue()
```
