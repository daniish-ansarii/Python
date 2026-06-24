<div align="center">

```
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝

███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗
████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
```

**The Ultimate Python Reference — Every Concept · Master Cheatsheets · Examples · Revision**

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white&labelColor=1e1e2e)
![OOP](https://img.shields.io/badge/OOP-Complete-a855f7?style=flat-square&logo=python&logoColor=white&labelColor=1e1e2e)
![DSA](https://img.shields.io/badge/DSA-Ready-FFA116?style=flat-square&logo=leetcode&logoColor=white&labelColor=1e1e2e)
![Decorators](https://img.shields.io/badge/Decorators-Advanced-22c55e?style=flat-square&labelColor=1e1e2e)
![Async](https://img.shields.io/badge/Async-asyncio-6366f1?style=flat-square&labelColor=1e1e2e)
![License](https://img.shields.io/badge/License-MIT-38bdf8?style=flat-square&logo=opensourceinitiative&logoColor=white&labelColor=1e1e2e)

> *Python is executable pseudocode. Master it once, use it everywhere.*

</div>

---

## INDEX

    01   Python Architecture & How It Works
    02   Installation, Setup & Virtual Environments
    03   Variables, Data Types & Type System
    04   Numbers — int, float, complex, Decimal
    05   Strings — Methods, Formatting, f-strings
    06   Booleans & None
    07   Operators — All Types & Tricks
    08   Control Flow — if, elif, else, match
    09   Loops — for, while, break, continue, else
    10   Functions — def, args, kwargs, closures
    11   Lambda & Higher-Order Functions
    12   Comprehensions — list, dict, set, generator
    13   Lists — Methods, Tricks, Patterns
    14   Tuples — Immutable Sequences
    15   Dictionaries — Methods, Patterns, OrderedDict
    16   Sets & Frozensets
    17   Collections Module — Counter, deque, defaultdict, namedtuple
    18   Itertools Module — Complete Reference
    19   Functools Module — reduce, lru_cache, partial
    20   OOP — Classes & Objects
    21   OOP — Inheritance & MRO
    22   OOP — Polymorphism & Duck Typing
    23   OOP — Encapsulation & Properties
    24   OOP — Magic/Dunder Methods
    25   OOP — Abstract Classes & Interfaces
    26   OOP — Dataclasses & NamedTuple
    27   Decorators — Function & Class Decorators
    28   Generators & Iterators
    29   Context Managers — with statement
    30   Exception Handling — Complete Reference
    31   File I/O — Reading, Writing, Paths
    32   Modules & Packages
    33   Regular Expressions
    34   Date & Time
    35   Math & Random
    36   Sorting & Searching — Complete Guide
    37   Functional Programming
    38   Type Hints & Annotations (Python 3.10+)
    39   Concurrency — Threading, Multiprocessing, asyncio
    40   Memory Management & GC
    41   Python Internals — GIL, Bytecode, CPython
    42   Testing — unittest, pytest
    43   Common Standard Library Modules
    44   DSA Patterns in Python
    45   Python Master Cheatsheet — Quick Revision

---

## 01   PYTHON ARCHITECTURE & HOW IT WORKS

```
  SOURCE CODE EXECUTION FLOW
  ──────────────────────────────────────────────────────────────────────
  script.py  (source code)
       │
       │  Lexer / Tokenizer
       ▼
  Tokens  (keywords, identifiers, literals, operators)
       │
       │  Parser
       ▼
  AST  (Abstract Syntax Tree)
       │
       │  Compiler
       ▼
  Bytecode  (.pyc files in __pycache__/)
       │
       │  PVM (Python Virtual Machine / CPython interpreter)
       ▼
  Execution  (interpreted line by line from bytecode)

  PYTHON IMPLEMENTATIONS
  ──────────────────────────────────────────────────────────────────────
  CPython    → default, written in C, most compatible
  PyPy       → JIT compiled, 5-10x faster for loops
  Jython     → runs on JVM
  IronPython → runs on .NET CLR
  MicroPython→ for microcontrollers

  CPython INTERNALS
  ──────────────────────────────────────────────────────────────────────
  ┌─────────────────────────────────────────────────────────────────┐
  │                        CPython Architecture                     │
  │                                                                 │
  │  ┌──────────────┐   ┌────────────────────────────────────────┐  │
  │  │  Python Code │   │              Memory Manager            │  │
  │  │  .py files   │   │  ┌──────────────────────────────────┐  │  │
  │  └──────┬───────┘   │  │  Object Allocator (pymalloc)      │  │  │
  │         │           │  │  Reference Counting               │  │  │
  │  ┌──────▼───────┐   │  │  Cyclic Garbage Collector         │  │  │
  │  │  Compiler    │   │  └──────────────────────────────────┘  │  │
  │  │  AST→Bytecode│   └────────────────────────────────────────┘  │
  │  └──────┬───────┘                                               │
  │         │           ┌────────────────────────────────────────┐  │
  │  ┌──────▼───────┐   │             Built-in Objects            │  │
  │  │  Eval Loop   │   │  int  str  list  dict  tuple  set ...   │  │
  │  │  (ceval.c)   │   └────────────────────────────────────────┘  │
  │  └──────────────┘                                               │
  └─────────────────────────────────────────────────────────────────┘

  VIEW BYTECODE
  ──────────────────────────────────────────────────────────────────────
  import dis
  def add(a, b): return a + b
  dis.dis(add)
  # Shows: LOAD_FAST, BINARY_ADD, RETURN_VALUE etc.

  PYTHON VERSIONS TIMELINE
  ──────────────────────────────────────────────────────────────────────
  Python 2.7  → legacy, EOL 2020. print statement, no f-strings
  Python 3.0  → print(), unicode strings, new division
  Python 3.5  → async/await, type hints
  Python 3.6  → f-strings, dict ordered, __init_subclass__
  Python 3.7  → dataclasses, breakpoint(), dict guaranteed ordered
  Python 3.8  → walrus operator :=, positional-only params /
  Python 3.9  → dict merge |, list/dict/set type hints
  Python 3.10 → match/case, parenthesized context managers
  Python 3.11 → faster CPython, tomllib, exception notes
  Python 3.12 → f-string improvements, type aliases, @override
  Python 3.13 → free-threaded mode (no GIL!), JIT compiler (beta)
```

---

## 02   INSTALLATION, SETUP & VIRTUAL ENVIRONMENTS

```
  INSTALL PYTHON
  ──────────────────────────────────────────────────────────────────────
  # Check version
  python --version
  python3 --version

  # Check path
  which python3

  VIRTUAL ENVIRONMENTS
  ──────────────────────────────────────────────────────────────────────
  # Create venv
  python -m venv myenv
  python -m venv myenv --python=python3.12

  # Activate
  source myenv/bin/activate          # Linux/Mac
  myenv\Scripts\activate             # Windows

  # Deactivate
  deactivate

  PIP PACKAGE MANAGER
  ──────────────────────────────────────────────────────────────────────
  pip install requests               # install
  pip install requests==2.28.0       # specific version
  pip install "requests>=2.28"       # min version
  pip install -r requirements.txt    # from file
  pip uninstall requests
  pip list                           # all installed
  pip freeze > requirements.txt      # save current env
  pip show requests                  # package info
  pip search requests                # search (deprecated, use pypi.org)
  pip install --upgrade pip          # upgrade pip itself

  PROJECT STRUCTURE
  ──────────────────────────────────────────────────────────────────────
  my_project/
  ├── myenv/                  virtual environment (don't commit)
  ├── src/
  │   └── mypackage/
  │       ├── __init__.py
  │       ├── module1.py
  │       └── module2.py
  ├── tests/
  │   └── test_module1.py
  ├── requirements.txt
  ├── README.md
  └── setup.py / pyproject.toml

  PYPROJECT.TOML (modern packaging)
  ──────────────────────────────────────────────────────────────────────
  [build-system]
  requires = ["setuptools", "wheel"]
  build-backend = "setuptools.backends.legacy:build"

  [project]
  name = "mypackage"
  version = "1.0.0"
  dependencies = ["requests>=2.28"]

  USEFUL TOOLS
  ──────────────────────────────────────────────────────────────────────
  pyenv       → manage multiple Python versions
  poetry      → dependency management + packaging
  pipenv      → combines pip + virtualenv
  black       → code formatter
  isort       → import sorter
  flake8      → linter
  mypy        → static type checker
  pytest      → testing framework
```

---

## 03   VARIABLES, DATA TYPES & TYPE SYSTEM

```
  VARIABLE ASSIGNMENT
  ──────────────────────────────────────────────────────────────────────
  x = 10                    # integer
  name = "Alice"            # string
  pi = 3.14                 # float
  is_active = True          # bool
  nothing = None            # NoneType

  # Multiple assignment
  a = b = c = 0
  x, y, z = 1, 2, 3
  first, *rest = [1, 2, 3, 4, 5]   # first=1, rest=[2,3,4,5]
  *start, last = [1, 2, 3, 4, 5]   # start=[1,2,3,4], last=5
  a, b = b, a               # swap without temp ✨

  BUILT-IN DATA TYPES
  ──────────────────────────────────────────────────────────────────────
  Type          Example                    Mutable  Ordered  Notes
  ─────────────────────────────────────────────────────────────────────
  int           42, -7, 0                  No       —        arbitrary precision
  float         3.14, 1e10, -0.5           No       —        64-bit double
  complex       3+4j, complex(3,4)         No       —        real + imaginary
  bool          True, False                No       —        subclass of int
  str           "hello", 'world'           No       Yes      unicode
  bytes         b"hello"                   No       Yes      raw bytes
  bytearray     bytearray(b"hello")        Yes      Yes      mutable bytes
  list          [1, 2, 3]                  Yes      Yes      dynamic array
  tuple         (1, 2, 3)                  No       Yes      immutable list
  dict          {"a": 1}                   Yes      Yes*     *ordered Python 3.7+
  set           {1, 2, 3}                  Yes      No       unique elements
  frozenset     frozenset({1, 2, 3})       No       No       immutable set
  NoneType      None                       No       —        singleton

  TYPE CHECKING
  ──────────────────────────────────────────────────────────────────────
  type(42)                  # <class 'int'>
  type("hi")                # <class 'str'>
  type(3.14)                # <class 'float'>
  isinstance(42, int)       # True
  isinstance(True, int)     # True  (bool IS int)
  isinstance(42, (int, float))  # True — check multiple

  TYPE CONVERSION
  ──────────────────────────────────────────────────────────────────────
  int("42")                 # 42
  int(3.9)                  # 3  (truncates)
  int("FF", 16)             # 255  (hex string)
  int("1010", 2)            # 10  (binary string)
  float("3.14")             # 3.14
  float(42)                 # 42.0
  str(42)                   # "42"
  str(3.14)                 # "3.14"
  bool(0)                   # False
  bool("")                  # False
  bool([])                  # False
  bool(None)                # False
  bool(1)                   # True
  bool("hi")                # True
  bool([1])                 # True
  list("hello")             # ['h','e','l','l','o']
  list((1,2,3))             # [1, 2, 3]
  list({1,2,3})             # [1, 2, 3]  (order not guaranteed)
  tuple([1,2,3])            # (1, 2, 3)
  set([1,2,2,3])            # {1, 2, 3}
  dict([("a",1),("b",2)])   # {'a': 1, 'b': 2}

  FALSY VALUES (evaluate to False in boolean context)
  ──────────────────────────────────────────────────────────────────────
  False   None   0   0.0   0j   ""   []   ()   {}   set()   b""

  EVERYTHING ELSE IS TRUTHY

  IDENTITY vs EQUALITY
  ──────────────────────────────────────────────────────────────────────
  a == b      → same VALUE (uses __eq__)
  a is b      → same OBJECT in memory (same id())

  x = [1, 2, 3]
  y = [1, 2, 3]
  x == y      → True   (same values)
  x is y      → False  (different objects)

  x = y = [1, 2, 3]
  x is y      → True   (same object)

  # Small int caching (-5 to 256 are cached)
  a = 256; b = 256; a is b  → True
  a = 257; b = 257; a is b  → False  (not cached)

  VARIABLE SCOPE — LEGB RULE
  ──────────────────────────────────────────────────────────────────────
  L  Local     → inside function
  E  Enclosing → enclosing function (closures)
  G  Global    → module level
  B  Built-in  → Python built-ins (len, print, etc.)

  x = "global"

  def outer():
      x = "enclosing"
      def inner():
          x = "local"
          print(x)       # local
      inner()
      print(x)           # enclosing

  outer()
  print(x)               # global

  # global keyword
  def modify_global():
      global x
      x = "modified"

  # nonlocal keyword (access enclosing scope)
  def counter():
      count = 0
      def increment():
          nonlocal count
          count += 1
          return count
      return increment

  CONSTANTS CONVENTION
  ──────────────────────────────────────────────────────────────────────
  MAX_SIZE = 100           # ALL_CAPS = constant by convention
  PI = 3.14159
  # Python has no true constants — convention only
```

---

## 04   NUMBERS — int, float, complex, Decimal

```
  INTEGERS
  ──────────────────────────────────────────────────────────────────────
  # Python ints have UNLIMITED precision
  big = 99999999999999999999999999999999 ** 2   # no overflow!
  factorial_100 = 1
  for i in range(1, 101): factorial_100 *= i

  # Bases
  binary  = 0b1010          # 10
  octal   = 0o17            # 15
  hex_num = 0xFF            # 255
  million = 1_000_000       # underscore separator

  # Base conversion
  bin(10)           # '0b1010'
  oct(8)            # '0o10'
  hex(255)          # '0xff'
  format(255, 'b')  # '11111111'  (no prefix)
  format(255, 'x')  # 'ff'

  # Integer methods
  abs(-5)           # 5
  pow(2, 10)        # 1024
  pow(2, 10, 1000)  # 24  (modular exponentiation, fast!)
  divmod(17, 5)     # (3, 2)  → (quotient, remainder)
  (-7) // 2         # -4  (floor division, rounds toward -inf)
  (-7) % 2          # 1   (always non-negative for positive divisor)

  FLOATS
  ──────────────────────────────────────────────────────────────────────
  import math

  3.14
  1e10          # 10000000000.0
  1.5e-3        # 0.0015
  float('inf')  # positive infinity
  float('-inf') # negative infinity
  float('nan')  # Not a Number

  # Floating point precision issue
  0.1 + 0.2             # 0.30000000000000004
  0.1 + 0.2 == 0.3      # False!

  # Correct comparison
  import math
  math.isclose(0.1 + 0.2, 0.3)  # True
  abs(0.1 + 0.2 - 0.3) < 1e-9   # True

  # Float methods
  round(3.14159, 2)     # 3.14
  round(2.5)            # 2  (banker's rounding — rounds to even)
  round(3.5)            # 4
  math.floor(3.7)       # 3
  math.ceil(3.2)        # 4
  math.trunc(3.9)       # 3  (toward zero)
  math.isnan(float('nan'))   # True
  math.isinf(float('inf'))   # True
  math.isfinite(3.14)        # True

  # Float representation
  (3.14).as_integer_ratio()  # (7070651414971679, 2251799813685248)
  (3.14).is_integer()        # False
  (3.0).is_integer()         # True

  MATH MODULE
  ──────────────────────────────────────────────────────────────────────
  import math

  math.pi           # 3.141592653589793
  math.e            # 2.718281828459045
  math.tau          # 6.283185307179586  (2*pi)
  math.inf          # inf
  math.nan          # nan

  math.sqrt(16)     # 4.0
  math.isqrt(16)    # 4  (integer square root, no float)
  math.pow(2, 10)   # 1024.0
  math.exp(1)       # 2.718...
  math.log(math.e)  # 1.0
  math.log(100, 10) # 2.0  (log base 10)
  math.log2(8)      # 3.0
  math.log10(1000)  # 3.0
  math.factorial(5) # 120
  math.gcd(12, 8)   # 4
  math.lcm(4, 6)    # 12  (Python 3.9+)
  math.comb(5, 2)   # 10  (combinations)
  math.perm(5, 2)   # 20  (permutations)

  math.sin(math.pi/2)  # 1.0
  math.cos(0)          # 1.0
  math.tan(math.pi/4)  # ~1.0
  math.degrees(math.pi)# 180.0
  math.radians(180)    # 3.14...

  math.hypot(3, 4)     # 5.0  (Euclidean distance)
  math.dist([0,0],[3,4])# 5.0  (Python 3.8+)
  math.fsum([0.1]*10)  # 1.0  (accurate float sum)

  COMPLEX NUMBERS
  ──────────────────────────────────────────────────────────────────────
  z = 3 + 4j
  z.real            # 3.0
  z.imag            # 4.0
  z.conjugate()     # (3-4j)
  abs(z)            # 5.0  (magnitude)
  z1 + z2           # add
  z1 * z2           # multiply

  import cmath
  cmath.sqrt(-1)    # 1j
  cmath.phase(z)    # angle in radians
  cmath.polar(z)    # (magnitude, phase)

  DECIMAL (exact decimal arithmetic)
  ──────────────────────────────────────────────────────────────────────
  from decimal import Decimal, getcontext

  getcontext().prec = 50         # set precision

  a = Decimal("0.1")
  b = Decimal("0.2")
  a + b                          # Decimal('0.3')  ← exact!
  Decimal("1") / Decimal("3")    # Decimal('0.333...') to 50 digits

  # Useful for financial calculations
  price = Decimal("19.99")
  tax   = Decimal("0.08")
  total = price * (1 + tax)      # Decimal('21.5892')

  FRACTIONS
  ──────────────────────────────────────────────────────────────────────
  from fractions import Fraction

  f = Fraction(1, 3)             # 1/3
  f + Fraction(1, 6)             # 1/2
  Fraction(0.1)                  # Fraction(3602879701896397, 36028797018963968) ← float imprecision
  Fraction("0.1")                # Fraction(1, 10)  ← exact
```

---

## 05   STRINGS — Methods, Formatting, f-strings

```
  STRING CREATION
  ──────────────────────────────────────────────────────────────────────
  s1 = 'single quotes'
  s2 = "double quotes"
  s3 = """triple double
          multiline"""
  s4 = '''triple single
          multiline'''
  raw = r"C:\Users\name"          # raw string, backslash not escape
  byte = b"bytes"                 # bytes literal
  f_str = f"value = {1+1}"        # f-string

  # String is a sequence of Unicode code points
  len("hello")          # 5
  "hello"[0]            # 'h'
  "hello"[-1]           # 'o'
  "hello"[1:3]          # 'el'
  "hello"[::-1]         # 'olleh'  (reverse)
  "hello"[::2]          # 'hlo'    (every 2nd char)

  # Strings are immutable
  s = "hello"
  s[0] = 'H'            # TypeError! can't modify

  STRING METHODS — COMPLETE REFERENCE
  ──────────────────────────────────────────────────────────────────────
  s = "  Hello, World!  "

  # Case
  s.upper()             # "  HELLO, WORLD!  "
  s.lower()             # "  hello, world!  "
  s.title()             # "  Hello, World!  "
  s.capitalize()        # "  hello, world!  " (only first char upper)
  s.swapcase()          # "  hELLO, wORLD!  "
  s.casefold()          # aggressive lower, for comparison (ß→ss)

  # Strip
  s.strip()             # "Hello, World!"
  s.lstrip()            # "Hello, World!  "
  s.rstrip()            # "  Hello, World!"
  s.strip("!")          # strip specific chars from both ends

  # Search
  s.find("World")       # 9   (-1 if not found)
  s.rfind("l")          # 12  (right-most)
  s.index("World")      # 9   (ValueError if not found)
  s.rindex("l")         # 12
  s.count("l")          # 3
  s.startswith("  He")  # True
  s.endswith("!  ")     # True
  s.startswith(("He","Hi"))  # tuple of prefixes

  # Check
  "hello123".isalpha()      # False  (has digits)
  "hello".isalpha()         # True
  "123".isdigit()           # True
  "123.4".isnumeric()       # False
  "hello123".isalnum()      # True
  "   ".isspace()           # True
  "Hello World".istitle()   # True
  "HELLO".isupper()         # True
  "hello".islower()         # True
  "".isidentifier()         # False
  "my_var".isidentifier()   # True

  # Split / Join
  "a,b,c".split(",")        # ['a','b','c']
  "a,b,c".split(",", 1)     # ['a','b,c']  (max 1 split)
  "a  b  c".split()         # ['a','b','c']  (any whitespace)
  "a,b,c".rsplit(",", 1)    # ['a,b','c']
  "a\nb\nc".splitlines()    # ['a','b','c']
  ",".join(["a","b","c"])   # "a,b,c"
  "".join(["h","i"])        # "hi"

  # Replace
  "hello".replace("l", "r")         # "herro"
  "hello".replace("l", "r", 1)      # "herlo"  (max 1)

  # Align / Pad
  "hi".center(10)           # "    hi    "
  "hi".center(10, "*")      # "****hi****"
  "hi".ljust(10)            # "hi        "
  "hi".ljust(10, "-")       # "hi--------"
  "hi".rjust(10)            # "        hi"
  "42".zfill(5)             # "00042"

  # Encode / Decode
  "hello".encode("utf-8")   # b'hello'
  b"hello".decode("utf-8")  # 'hello'
  "héllo".encode("utf-8")   # b'h\xc3\xa9llo'

  # Other
  "  ".expandtabs(4)        # expand tabs to spaces
  "abc".maketrans("abc","xyz")  # translation table
  "abc".translate(str.maketrans("abc","xyz"))  # "xyz"
  "hello world".partition(" ")   # ('hello', ' ', 'world')
  "hello world".rpartition(" ")  # ('hello', ' ', 'world')
  "\n".join(["line1","line2"])    # "line1\nline2"
  str.removeprefix("hello","hel")  # "lo"   (Python 3.9+)
  str.removesuffix("hello","lo")   # "hel"  (Python 3.9+)
  "hello".removeprefix("hel")      # "lo"
  "hello".removesuffix("lo")       # "hel"

  STRING FORMATTING — 4 WAYS
  ──────────────────────────────────────────────────────────────────────
  name = "Alice"
  age  = 30
  pi   = 3.14159

  # 1. % formatting (old, avoid)
  "%s is %d years old" % (name, age)   # "Alice is 30 years old"
  "%.2f" % pi                           # "3.14"

  # 2. str.format() (Python 2.7+)
  "{} is {} years old".format(name, age)
  "{name} is {age}".format(name=name, age=age)
  "{0} and {1} and {0}".format("a","b")   # "a and b and a"
  "{:.2f}".format(pi)                     # "3.14"
  "{:>10}".format("hi")                   # "        hi"
  "{:0>5}".format(42)                     # "00042"
  "{:,}".format(1000000)                  # "1,000,000"

  # 3. f-strings (Python 3.6+) ← prefer this
  f"{name} is {age} years old"
  f"{pi:.2f}"                # "3.14"
  f"{pi:.4e}"                # "3.1416e+00"
  f"{1000000:,}"             # "1,000,000"
  f"{0.5:.0%}"               # "50%"
  f"{'hi':>10}"              # "        hi"
  f"{'hi':^10}"              # "    hi    "
  f"{'hi':*^10}"             # "****hi****"
  f"{42:08b}"                # "00101010"  (binary with leading 0s)
  f"{42:08x}"                # "0000002a"  (hex)
  f"{name!r}"                # "'Alice'"   (!r calls repr())
  f"{name!s}"                # "Alice"     (!s calls str())
  f"{name!a}"                # "'Alice'"   (!a calls ascii())

  # f-string expressions
  f"{2 ** 10}"               # "1024"
  f"{name.upper()}"          # "ALICE"
  f"Result: {1+2=}"          # "Result: 1+2=3"  (Python 3.8+ debug)

  # Multiline f-string
  msg = (
      f"Name: {name}\n"
      f"Age:  {age}\n"
      f"Pi:   {pi:.4f}"
  )

  # 4. Template strings (safe for user input)
  from string import Template
  t = Template("$name is $age years old")
  t.substitute(name=name, age=age)

  FORMAT SPEC MINI-LANGUAGE
  ──────────────────────────────────────────────────────────────────────
  [[fill]align][sign][z][#][0][width][grouping][.precision][type]

  align:  < (left)  > (right)  ^ (center)  = (sign padding)
  sign:   + (always)  - (only negative)  (space)
  type:   d (decimal)  b (binary)  o (octal)  x/X (hex)
          f (float)   e/E (scientific)  % (percent)  s (string)
          n (locale)  g/G (shortest)

  Examples:
  f"{42:+d}"          # "+42"
  f"{-42:+d}"         # "-42"
  f"{42:08d}"         # "00000042"
  f"{3.14159:10.3f}"  # "     3.142"
  f"{255:#x}"         # "0xff"
  f"{255:#010x}"      # "0x000000ff"
  f"{0.25:.0%}"       # "25%"

  COMMON STRING PATTERNS
  ──────────────────────────────────────────────────────────────────────
  # Reverse
  "hello"[::-1]              # "olleh"

  # Check palindrome
  s == s[::-1]

  # Count char frequency
  from collections import Counter
  Counter("hello")            # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

  # Remove duplicates while preserving order
  "".join(dict.fromkeys("abcabc"))   # "abc"

  # Most common char
  Counter("hello").most_common(1)    # [('l', 2)]

  # Split camelCase → words
  import re
  re.sub(r'(?<!^)(?=[A-Z])', ' ', 'camelCase')  # 'camel Case'

  # Anagram check
  sorted("listen") == sorted("silent")  # True
  Counter("listen") == Counter("silent") # True

  # All permutations
  from itertools import permutations
  list(permutations("abc", 2))   # [('a','b'),('a','c'),('b','a')...]
```

---

## 06   BOOLEANS & NONE

```
  BOOLEANS
  ──────────────────────────────────────────────────────────────────────
  True   False             # capitalized keywords

  # bool is subclass of int
  True  + True             # 2
  True  * 5                # 5
  False + 1                # 1
  int(True)                # 1
  int(False)               # 0

  BOOLEAN OPERATORS
  ──────────────────────────────────────────────────────────────────────
  and   or   not

  # Short-circuit evaluation
  True  or  expensive()    # expensive() never called
  False and expensive()    # expensive() never called

  # Returns actual values (not just True/False!)
  "hello" and "world"      # "world"  (last truthy, or first falsy)
  ""      and "world"      # ""       (first falsy)
  "hello" or  "world"      # "hello"  (first truthy)
  ""      or  "default"    # "default"(first truthy)
  not ""                   # True

  # Common patterns
  x = x or default_value   # set default if x is falsy
  x and x.method()         # safe call (guard pattern)

  COMPARISON OPERATORS
  ──────────────────────────────────────────────────────────────────────
  ==   !=   <   >   <=   >=   is   is not   in   not in

  # Chained comparisons (Pythonic!)
  1 < x < 10                   # True if 1 < x AND x < 10
  0 <= i < len(arr)            # valid index check
  a == b == c                  # all equal

  NONE
  ──────────────────────────────────────────────────────────────────────
  None                          # singleton, only one None object
  type(None)                    # <class 'NoneType'>
  x is None                     # check for None (use is, not ==)
  x is not None                 # check not None

  # Function returns None implicitly
  def do_something():
      pass                      # returns None

  # None in conditionals
  if result is not None:
      use(result)
```

---

## 07   OPERATORS — ALL TYPES & TRICKS

```
  ARITHMETIC OPERATORS
  ──────────────────────────────────────────────────────────────────────
  +   addition          5 + 3   = 8
  -   subtraction       5 - 3   = 2
  *   multiplication    5 * 3   = 15
  **  exponentiation    5 ** 3  = 125
  /   true division     7 / 2   = 3.5   (always float)
  //  floor division    7 // 2  = 3     (int toward -inf)
  %   modulus           7 % 2   = 1

  # Integer division tricks
  -7 // 2   = -4  (floor toward -inf, not truncate!)
  -7 % 2    = 1   (result has sign of divisor)
  7 % -2    = -1  (result has sign of divisor)

  AUGMENTED ASSIGNMENT
  ──────────────────────────────────────────────────────────────────────
  x += 1    x -= 1    x *= 2    x **= 2
  x /= 2    x //= 2   x %= 3
  x &= mask  x |= flags  x ^= bits
  x <<= 1    x >>= 1

  BITWISE OPERATORS
  ──────────────────────────────────────────────────────────────────────
  &     AND         0b1100 & 0b1010  = 0b1000  (8)
  |     OR          0b1100 | 0b1010  = 0b1110  (14)
  ^     XOR         0b1100 ^ 0b1010  = 0b0110  (6)
  ~     NOT         ~5               = -6       (~n = -n-1)
  <<    left shift  1 << 3           = 8        (multiply by 2^n)
  >>    right shift 8 >> 2           = 2        (divide by 2^n)

  BITWISE TRICKS (LeetCode Gold)
  ──────────────────────────────────────────────────────────────────────
  n & 1                → is odd? (1=odd, 0=even)
  n & (n-1)            → clear lowest set bit
  n & (n-1) == 0       → is power of 2? (n > 0)
  n & -n               → isolate lowest set bit
  n | (1 << k)         → set k-th bit
  n & ~(1 << k)        → clear k-th bit
  n ^ (1 << k)         → toggle k-th bit
  (n >> k) & 1         → get k-th bit
  n ^ n                → 0  (XOR with self)
  n ^ 0                → n  (XOR with 0)
  a ^ b ^ a            → b  (find unique)
  bin(n).count('1')    → count set bits
  n.bit_length()       → number of bits

  # Find single non-duplicate in array
  from functools import reduce
  reduce(lambda a,b: a^b, [1,2,3,2,1])  # 3

  WALRUS OPERATOR := (Python 3.8+)
  ──────────────────────────────────────────────────────────────────────
  # Assign and use in same expression
  while chunk := file.read(8192):
      process(chunk)

  if m := re.match(r'\d+', s):
      print(m.group())

  data = [y := compute(), y**2, y**3]

  # In comprehension
  results = [y for x in data if (y := transform(x)) > 0]

  OPERATOR PRECEDENCE (high to low)
  ──────────────────────────────────────────────────────────────────────
  1.  ()                           grouping
  2.  **                           exponentiation (right assoc.)
  3.  +x  -x  ~x                   unary
  4.  *  @  /  //  %               multiplicative
  5.  +  -                         additive
  6.  <<  >>                       shift
  7.  &                            bitwise AND
  8.  ^                            bitwise XOR
  9.  |                            bitwise OR
  10. in  not in  is  is not  < <= > >= == !=   comparison
  11. not                          logical NOT
  12. and                          logical AND
  13. or                           logical OR
  14. := (walrus)                  assignment expression
  15. lambda                       lambda

  MATRIX MULTIPLICATION OPERATOR
  ──────────────────────────────────────────────────────────────────────
  @     matrix multiplication (Python 3.5+)
  # Used by numpy: C = A @ B  (instead of np.dot(A, B))
```

---

## 08   CONTROL FLOW — if, elif, else, match

```
  IF / ELIF / ELSE
  ──────────────────────────────────────────────────────────────────────
  x = 42

  if x > 100:
      print("big")
  elif x > 50:
      print("medium")
  elif x > 0:
      print("small")
  else:
      print("non-positive")

  # One-liner (ternary)
  result = "even" if x % 2 == 0 else "odd"
  abs_val = x if x >= 0 else -x

  # Nested ternary (readable limit)
  grade = "A" if score>=90 else "B" if score>=80 else "C"

  MATCH / CASE (Python 3.10+) — Structural Pattern Matching
  ──────────────────────────────────────────────────────────────────────
  command = "quit"

  match command:
      case "quit" | "exit" | "q":
          print("Quitting")
      case "help":
          print("Showing help")
      case _:                          # default (wildcard)
          print("Unknown command")

  # Match with capture
  point = (1, 2)
  match point:
      case (0, 0):
          print("Origin")
      case (x, 0):
          print(f"On x-axis at {x}")
      case (0, y):
          print(f"On y-axis at {y}")
      case (x, y):
          print(f"Point at ({x}, {y})")

  # Match with class patterns
  class Point:
      def __init__(self, x, y):
          self.x = x
          self.y = y

  match point:
      case Point(x=0, y=0):
          print("Origin")
      case Point(x=x, y=y):
          print(f"({x}, {y})")

  # Match with guards
  match value:
      case n if n < 0:
          print("negative")
      case n if n == 0:
          print("zero")
      case n:
          print(f"positive: {n}")

  # Match sequences
  match command.split():
      case ["go", direction]:
          go(direction)
      case ["pick", "up", item]:
          pick_up(item)
      case ["drop", *items]:
          drop(items)

  # Match mappings
  match response:
      case {"status": 200, "data": data}:
          process(data)
      case {"status": 404}:
          not_found()
      case {"status": status}:
          print(f"Error: {status}")
```

---

## 09   LOOPS — for, while, break, continue, else

```
  FOR LOOP
  ──────────────────────────────────────────────────────────────────────
  # Iterate over any iterable
  for i in range(5):           # 0 1 2 3 4
      print(i)

  for i in range(2, 10, 2):   # 2 4 6 8
      print(i)

  for i in range(10, 0, -1):  # 10 9 8 ... 1
      print(i)

  for char in "hello":
      print(char)

  for item in [1, 2, 3]:
      print(item)

  # enumerate — index + value
  for i, val in enumerate(["a","b","c"]):
      print(i, val)              # 0 a, 1 b, 2 c

  for i, val in enumerate(["a","b","c"], start=1):
      print(i, val)              # 1 a, 2 b, 3 c

  # zip — parallel iteration
  names = ["Alice","Bob","Carol"]
  scores = [95, 87, 92]
  for name, score in zip(names, scores):
      print(f"{name}: {score}")

  # zip_longest (fill missing with None or fillvalue)
  from itertools import zip_longest
  for a, b in zip_longest([1,2,3],[4,5], fillvalue=0):
      print(a, b)               # 1 4, 2 5, 3 0

  # Iterate dict
  d = {"a":1, "b":2}
  for key in d:                  # keys only
  for key in d.keys():           # keys
  for val in d.values():         # values
  for k, v in d.items():         # key-value pairs

  # Unpack in loop
  pairs = [(1,2),(3,4),(5,6)]
  for x, y in pairs:
      print(x + y)

  # Nested loops
  for i in range(3):
      for j in range(3):
          print(f"({i},{j})", end=" ")
      print()

  WHILE LOOP
  ──────────────────────────────────────────────────────────────────────
  n = 10
  while n > 0:
      print(n)
      n -= 1

  # Infinite loop with break
  while True:
      data = input("Enter: ")
      if data == "quit":
          break
      process(data)

  # While with assignment (Python 3.8+)
  while line := file.readline():
      process(line)

  BREAK / CONTINUE / ELSE
  ──────────────────────────────────────────────────────────────────────
  # break — exit loop immediately
  for i in range(10):
      if i == 5:
          break            # exits at 5

  # continue — skip to next iteration
  for i in range(10):
      if i % 2 == 0:
          continue         # skip even numbers

  # else clause — runs if loop completed without break
  for i in range(5):
      if i == 10:
          break
  else:
      print("Loop completed normally")  # prints this

  for i in range(5):
      if i == 3:
          break
  else:
      print("Won't print")  # break was hit

  # Classic use: search with for/else
  def find_prime(numbers):
      for n in numbers:
          for factor in range(2, int(n**0.5)+1):
              if n % factor == 0:
                  break          # n is not prime
          else:
              return n           # loop completed = prime found
      return None

  LOOP TRICKS
  ──────────────────────────────────────────────────────────────────────
  # reversed()
  for i in reversed(range(5)):  # 4 3 2 1 0
      print(i)

  # sorted()
  for item in sorted(my_list):
      print(item)

  for item in sorted(my_list, reverse=True):
      print(item)

  for item in sorted(my_list, key=lambda x: x.name):
      print(item)

  # Iterate with index and skip
  for i, val in enumerate(arr):
      if val < 0:
          continue
      arr[i] = val * 2

  # Flatten nested list
  matrix = [[1,2,3],[4,5,6],[7,8,9]]
  flat = [x for row in matrix for x in row]

  # Loop n times without index
  for _ in range(5):
      do_something()
```

---

## 10   FUNCTIONS — def, args, kwargs, closures

```
  FUNCTION BASICS
  ──────────────────────────────────────────────────────────────────────
  def greet(name):
      """Docstring: explain what function does."""
      return f"Hello, {name}!"

  result = greet("Alice")         # "Hello, Alice!"
  greet.__doc__                   # "Docstring: ..."
  greet.__name__                  # "greet"

  # Multiple return values (actually returns tuple)
  def min_max(lst):
      return min(lst), max(lst)   # tuple

  lo, hi = min_max([3,1,4,1,5,9])

  # Default parameters
  def power(base, exp=2):
      return base ** exp

  power(3)        # 9   (exp defaults to 2)
  power(3, 3)     # 27

  # CAUTION: mutable defaults are shared!
  def bad(lst=[]):           # BUG: lst is shared across calls
      lst.append(1)
      return lst

  def good(lst=None):        # CORRECT pattern
      if lst is None:
          lst = []
      lst.append(1)
      return lst

  ARGUMENT TYPES
  ──────────────────────────────────────────────────────────────────────
  def func(pos1, pos2, /, normal, *, kw_only1, kw_only2):
      pass

  #  pos1, pos2  → positional-only (before /)
  #  normal      → positional or keyword
  #  kw_only1/2  → keyword-only (after *)

  # *args — variable positional args (tuple)
  def add(*args):
      return sum(args)

  add(1, 2, 3, 4, 5)         # 15
  add(*[1,2,3])               # 15  (unpack)

  # **kwargs — variable keyword args (dict)
  def info(**kwargs):
      for k, v in kwargs.items():
          print(f"{k}: {v}")

  info(name="Alice", age=30)
  info(**{"name":"Alice","age":30})  # unpack dict

  # Combined (order matters!)
  def full(pos_only, /, normal, *args, kw_only, **kwargs):
      pass

  # Calling with unpacking
  def add(a, b, c): return a + b + c
  nums = [1, 2, 3]
  add(*nums)                  # 6

  def greet(first, last): ...
  data = {"first":"Alice","last":"Smith"}
  greet(**data)               # same as greet(first="Alice",last="Smith")

  FIRST-CLASS FUNCTIONS
  ──────────────────────────────────────────────────────────────────────
  # Functions are objects
  def double(x): return x * 2

  f = double            # assign to variable
  f(5)                  # 10

  funcs = [double, abs, str]   # store in list
  for fn in funcs:
      print(fn(-3))

  def apply(func, value):      # pass as argument
      return func(value)

  apply(double, 5)             # 10

  def make_adder(n):           # return function
      def adder(x):
          return x + n
      return adder

  add5 = make_adder(5)
  add5(3)              # 8

  CLOSURES
  ──────────────────────────────────────────────────────────────────────
  def make_counter(start=0):
      count = start            # captured by inner function

      def increment(by=1):
          nonlocal count       # modify enclosing scope
          count += by
          return count

      def reset():
          nonlocal count
          count = start

      def get():
          return count

      return increment, reset, get

  inc, rst, get = make_counter(10)
  inc()    # 11
  inc()    # 12
  inc(5)   # 17
  get()    # 17
  rst()
  get()    # 10

  RECURSION
  ──────────────────────────────────────────────────────────────────────
  # Always: base case + recursive case
  def factorial(n):
      if n <= 1: return 1         # base case
      return n * factorial(n-1)  # recursive

  def fibonacci(n):
      if n <= 1: return n
      return fibonacci(n-1) + fibonacci(n-2)

  # With memoization
  from functools import lru_cache

  @lru_cache(maxsize=None)
  def fib(n):
      if n <= 1: return n
      return fib(n-1) + fib(n-2)

  fib(100)         # instant
  fib.cache_info() # CacheInfo(hits=98, misses=101, ...)

  # Tail recursion (Python doesn't optimize TCO, use iteration)
  import sys
  sys.setrecursionlimit(10000)   # default 1000

  FUNCTION ANNOTATIONS
  ──────────────────────────────────────────────────────────────────────
  def greet(name: str, age: int = 0) -> str:
      return f"{name} is {age}"

  greet.__annotations__   # {'name': str, 'age': int, 'return': str}
  # Annotations are metadata only — Python doesn't enforce them
  # Use mypy or pyright for static type checking
```

---

## 11   LAMBDA & HIGHER-ORDER FUNCTIONS

```
  LAMBDA EXPRESSIONS
  ──────────────────────────────────────────────────────────────────────
  # lambda params: expression  (single expression, returns it)
  square   = lambda x: x ** 2
  add      = lambda x, y: x + y
  identity = lambda x: x
  constant = lambda: 42

  square(5)      # 25
  add(3, 4)      # 7

  # Use cases: quick inline functions
  sorted(people, key=lambda p: p.age)
  sorted(words, key=lambda w: len(w))
  sorted(pairs, key=lambda pair: (pair[1], pair[0]))
  filter(lambda x: x > 0, nums)
  map(lambda x: x*2, nums)

  # Lambda with default
  multiply = lambda x, factor=2: x * factor
  multiply(5)       # 10
  multiply(5, 3)    # 15

  MAP, FILTER, REDUCE
  ──────────────────────────────────────────────────────────────────────
  nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  # map(func, iterable) → iterator
  doubled = list(map(lambda x: x*2, nums))
  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

  # Equivalent comprehension (more Pythonic)
  doubled = [x*2 for x in nums]

  # map with multiple iterables
  sums = list(map(lambda a,b: a+b, [1,2,3],[4,5,6]))
  # [5, 7, 9]

  # filter(func, iterable) → iterator
  evens = list(filter(lambda x: x%2==0, nums))
  # [2, 4, 6, 8, 10]

  # Equivalent
  evens = [x for x in nums if x%2==0]

  # reduce — fold to single value
  from functools import reduce
  total = reduce(lambda acc, x: acc+x, nums)        # 55
  product = reduce(lambda acc, x: acc*x, nums, 1)  # with initial 1

  SORTED, MIN, MAX WITH KEY
  ──────────────────────────────────────────────────────────────────────
  words = ["banana","apple","cherry","date"]

  sorted(words)                            # alphabetical
  sorted(words, key=len)                   # by length
  sorted(words, key=len, reverse=True)     # by length desc
  sorted(words, key=lambda w: w[-1])       # by last char
  sorted(words, key=str.lower)             # case-insensitive

  # Multi-key sort
  students = [("Alice",90),("Bob",85),("Carol",90)]
  sorted(students, key=lambda s: (-s[1], s[0]))
  # Sort by score desc, then name asc

  min(words, key=len)     # "date" (shortest)
  max(words, key=len)     # "banana" (longest)

  # Using operator module (faster than lambda for simple ops)
  import operator
  sorted(students, key=operator.itemgetter(1))    # by index 1
  sorted(objects, key=operator.attrgetter("age")) # by attribute

  ANY, ALL
  ──────────────────────────────────────────────────────────────────────
  any([False, True, False])  # True  (at least one truthy)
  any([False, False])        # False
  all([True, True, True])    # True  (all truthy)
  all([True, False, True])   # False

  # Short-circuits
  any(x > 0 for x in nums)      # generator, lazy
  all(x >= 0 for x in nums)     # generator, lazy

  any([])                        # False
  all([])                        # True  (vacuously true)
```

---

## 12   COMPREHENSIONS — list, dict, set, generator

```
  LIST COMPREHENSION
  ──────────────────────────────────────────────────────────────────────
  # [expression for item in iterable if condition]

  squares  = [x**2 for x in range(10)]
  evens    = [x for x in range(20) if x%2==0]
  words    = [w.upper() for w in "hello world".split()]
  flat     = [x for row in matrix for x in row]   # flatten
  pairs    = [(x,y) for x in range(3) for y in range(3)]

  # With condition on both sides
  clamped = [max(0, min(100, x)) for x in scores]

  # Nested
  matrix = [[i*j for j in range(1,4)] for i in range(1,4)]
  # [[1,2,3],[2,4,6],[3,6,9]]

  # With function call
  cleaned = [s.strip().lower() for s in raw_strings]

  # Conditional expression
  labels = ["even" if x%2==0 else "odd" for x in range(10)]

  DICT COMPREHENSION
  ──────────────────────────────────────────────────────────────────────
  # {key: value for item in iterable if condition}

  squares_dict = {x: x**2 for x in range(5)}
  # {0:0, 1:1, 2:4, 3:9, 4:16}

  word_lengths = {w: len(w) for w in words}

  # Invert dictionary
  inv = {v: k for k, v in d.items()}

  # Filter dictionary
  filtered = {k: v for k, v in d.items() if v > 0}

  # From two lists
  keys   = ["a","b","c"]
  values = [1, 2, 3]
  d = {k: v for k, v in zip(keys, values)}
  # or: dict(zip(keys, values))

  SET COMPREHENSION
  ──────────────────────────────────────────────────────────────────────
  # {expression for item in iterable if condition}

  unique_squares = {x**2 for x in range(-5, 6)}
  # {0, 1, 4, 9, 16, 25}

  vowels = {c for c in "hello world" if c in "aeiou"}
  # {'e', 'o'}

  GENERATOR EXPRESSION
  ──────────────────────────────────────────────────────────────────────
  # (expression for item in iterable if condition)
  # Lazy evaluation — generates values one at a time

  gen = (x**2 for x in range(1000000))   # no memory for all values
  next(gen)        # 0
  next(gen)        # 1
  sum(gen)         # sum rest  (exhausted after)

  # Use in function calls directly
  total = sum(x**2 for x in range(100))
  result = max(len(w) for w in words)
  found = any(x > 100 for x in nums)

  # vs list comprehension
  sum([x**2 for x in range(100)])    # creates full list first
  sum(x**2 for x in range(100))      # generator, memory efficient

  COMPREHENSION PERFORMANCE TIPS
  ──────────────────────────────────────────────────────────────────────
  # List comp is faster than equivalent for loop
  # Generator is more memory efficient than list comp
  # Dict comp is faster than dict(zip(...)) for large data

  # Avoid side effects in comprehensions
  [print(x) for x in range(5)]  # bad style — use loop

  # Use walrus for expensive operations
  [y for x in data if (y := transform(x)) is not None]
```

---

## 13   LISTS — Methods, Tricks, Patterns

```
  LIST CREATION
  ──────────────────────────────────────────────────────────────────────
  empty   = []
  nums    = [1, 2, 3, 4, 5]
  mixed   = [1, "two", 3.0, True, None]
  nested  = [[1,2],[3,4],[5,6]]
  zeros   = [0] * 5              # [0,0,0,0,0]
  matrix  = [[0]*3 for _ in range(3)]   # 3x3 zeros (correct way)
  # NOT: [[0]*3]*3  (same inner list referenced!)

  from_range   = list(range(10))
  from_string  = list("hello")   # ['h','e','l','l','o']
  from_map     = list(map(str, range(5)))

  LIST METHODS — COMPLETE
  ──────────────────────────────────────────────────────────────────────
  lst = [3, 1, 4, 1, 5, 9, 2, 6]

  lst.append(7)             # add to end: [3,1,4,1,5,9,2,6,7]
  lst.extend([8,9])         # add all from iterable
  lst.insert(0, 0)          # insert at index 0
  lst.pop()                 # remove & return last: 9
  lst.pop(0)                # remove & return at index 0
  lst.remove(1)             # remove first occurrence of 1
  lst.clear()               # remove all elements
  lst.index(5)              # index of first 5
  lst.count(1)              # count occurrences of 1
  lst.sort()                # in-place sort (modifies!)
  lst.sort(reverse=True)    # in-place descending
  lst.sort(key=abs)         # sort by absolute value
  lst.reverse()             # in-place reverse
  lst.copy()                # shallow copy
  lst.__len__()             # len(lst)

  # Non-mutating (return new list)
  sorted(lst)               # new sorted list
  sorted(lst, reverse=True)
  reversed(lst)             # iterator (not list)
  list(reversed(lst))

  SLICING
  ──────────────────────────────────────────────────────────────────────
  lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  lst[2]          # 2
  lst[-1]         # 9
  lst[-2]         # 8
  lst[2:5]        # [2, 3, 4]
  lst[:5]         # [0, 1, 2, 3, 4]
  lst[5:]         # [5, 6, 7, 8, 9]
  lst[:]          # [0,1,2,...,9]  (copy)
  lst[::2]        # [0, 2, 4, 6, 8]
  lst[1::2]       # [1, 3, 5, 7, 9]
  lst[::-1]       # [9, 8, 7,..., 0]  (reversed)
  lst[2:8:2]      # [2, 4, 6]
  lst[-3:]        # [7, 8, 9]
  lst[:-3]        # [0, 1, 2, 3, 4, 5, 6]

  # Slice assignment
  lst[2:5] = [20, 30, 40]   # replace slice
  lst[::2] = [0]*5           # replace every other

  # slice object
  s = slice(2, 8, 2)
  lst[s]                     # [2, 4, 6]

  USEFUL PATTERNS
  ──────────────────────────────────────────────────────────────────────
  # Flatten one level
  nested = [[1,2],[3,4],[5,6]]
  flat = sum(nested, [])          # [[1,2]+[3,4]+[5,6]]
  flat = [x for row in nested for x in row]

  # Transpose matrix
  matrix = [[1,2,3],[4,5,6],[7,8,9]]
  transposed = list(map(list, zip(*matrix)))
  # [[1,4,7],[2,5,8],[3,6,9]]

  # Chunk list into sublists of size n
  def chunks(lst, n):
      return [lst[i:i+n] for i in range(0, len(lst), n)]

  chunks([1,2,3,4,5,6,7], 3)  # [[1,2,3],[4,5,6],[7]]

  # Remove duplicates preserving order
  seen = set()
  unique = [x for x in lst if not (x in seen or seen.add(x))]

  # Rotate list by k
  k = 2
  rotated = lst[-k:] + lst[:-k]

  # Find all indices of a value
  val = 1
  indices = [i for i, x in enumerate(lst) if x == val]

  # Flatten arbitrarily nested list
  def flatten(lst):
      result = []
      for item in lst:
          if isinstance(item, list):
              result.extend(flatten(item))
          else:
              result.append(item)
      return result

  # Running sum
  import itertools
  list(itertools.accumulate([1,2,3,4,5]))  # [1,3,6,10,15]

  # Zip with index
  list(enumerate("hello"))   # [(0,'h'),(1,'e'),(2,'l'),(3,'l'),(4,'o')]

  # Stack operations (use list)
  stack = []
  stack.append(1)    # push
  stack.append(2)
  stack.pop()        # pop  → 2
  stack[-1]          # peek → 1

  # Queue operations (use deque for O(1) popleft)
  from collections import deque
  q = deque([1,2,3])
  q.append(4)        # enqueue right
  q.popleft()        # dequeue left  → 1
  q.appendleft(0)    # enqueue left
  q.pop()            # dequeue right
```

---

## 14   TUPLES — Immutable Sequences

```
  TUPLE CREATION
  ──────────────────────────────────────────────────────────────────────
  empty   = ()
  single  = (1,)              # comma required for single element!
  single2 = 1,                # also valid
  t       = (1, 2, 3)
  t2      = 1, 2, 3           # parentheses optional

  from_list = tuple([1,2,3])
  from_str  = tuple("abc")    # ('a','b','c')

  TUPLE METHODS
  ──────────────────────────────────────────────────────────────────────
  t = (1, 2, 3, 2, 1)
  t.count(2)          # 2
  t.index(3)          # 2

  # Everything else from sequences works
  len(t)              # 5
  t[0]                # 1
  t[-1]               # 1
  t[1:3]              # (2, 3)
  t + (4, 5)          # (1,2,3,2,1,4,5)
  t * 2               # (1,2,3,2,1,1,2,3,2,1)
  3 in t              # True
  max(t), min(t)      # 3, 1
  sorted(t)           # [1,1,2,2,3]  (returns LIST)

  UNPACKING
  ──────────────────────────────────────────────────────────────────────
  x, y, z = (1, 2, 3)
  first, *rest = (1, 2, 3, 4)     # first=1, rest=[2,3,4]
  *start, last = (1, 2, 3, 4)     # start=[1,2,3], last=4
  a, *mid, z = (1,2,3,4,5)        # a=1, mid=[2,3,4], z=5

  # Swap
  a, b = b, a

  # Return multiple values
  def divmod2(a, b):
      return a//b, a%b        # returns tuple

  q, r = divmod2(17, 5)       # q=3, r=2

  # Nested unpacking
  (a, b), c = (1, 2), 3
  [[x, y], z] = [[1, 2], 3]

  TUPLE vs LIST
  ──────────────────────────────────────────────────────────────────────
  Tuple               List
  ────────────────────────────────────────────
  Immutable           Mutable
  Hashable (can be dict key, set element)
  Slightly faster     Slightly slower
  Less memory         More memory
  For heterogeneous data (record-like)
  For homogeneous data (collection)

  # Tuples as dict keys (hashable!)
  d = {(0,0): "origin", (1,0): "right"}
  d[(0,0)]     # "origin"

  # Named access with namedtuple
  from collections import namedtuple
  Point = namedtuple("Point", ["x","y"])
  p = Point(3, 4)
  p.x          # 3
  p.y          # 4
  p[0]         # 3  (also index access)
  p._replace(x=10)   # new Point(10, 4)
  p._asdict()         # OrderedDict
```

---

## 15   DICTIONARIES — Methods, Patterns, OrderedDict

```
  DICT CREATION
  ──────────────────────────────────────────────────────────────────────
  empty = {}
  d     = {"a":1, "b":2, "c":3}
  d2    = dict(a=1, b=2, c=3)
  d3    = dict([("a",1),("b",2)])
  d4    = dict(zip("abc",[1,2,3]))

  # From keys with default value
  d = dict.fromkeys(["a","b","c"], 0)   # {'a':0,'b':0,'c':0}

  DICT METHODS — COMPLETE
  ──────────────────────────────────────────────────────────────────────
  d = {"a":1, "b":2, "c":3}

  d["a"]                      # 1   (KeyError if missing)
  d.get("a")                  # 1
  d.get("z")                  # None
  d.get("z", 0)               # 0   (default value)

  d["d"] = 4                  # add/update
  d.update({"e":5, "f":6})    # merge
  d.update(e=5, f=6)          # also valid

  d.pop("a")                  # remove & return value, KeyError if missing
  d.pop("z", None)            # safe remove
  d.popitem()                 # remove & return last (key,val) pair

  d.keys()                    # dict_keys view
  d.values()                  # dict_values view
  d.items()                   # dict_items view

  list(d.keys())
  list(d.values())
  list(d.items())             # [('a',1),('b',2)...]

  d.setdefault("x", 99)       # set if not exists, return value
  d.copy()                    # shallow copy
  d.clear()                   # empty dict
  len(d)                      # number of keys
  "a" in d                    # key membership test
  "a" not in d

  # Merge (Python 3.9+)
  merged = d1 | d2            # new dict
  d1 |= d2                    # update in place

  DICT COMPREHENSION
  ──────────────────────────────────────────────────────────────────────
  squares   = {x: x**2 for x in range(10)}
  inv       = {v: k for k,v in d.items()}
  filtered  = {k: v for k,v in d.items() if v > 0}

  COMMON DICT PATTERNS
  ──────────────────────────────────────────────────────────────────────
  # Frequency count
  from collections import Counter
  freq = Counter("abracadabra")   # Counter({'a':5,'b':2,'r':2,'c':1,'d':1})

  # Group by key
  from collections import defaultdict
  groups = defaultdict(list)
  for name, grade in students:
      groups[grade].append(name)

  # Nested dict
  nested = {"outer": {"inner": 42}}
  nested["outer"]["inner"]        # 42
  nested.get("outer", {}).get("missing", 0)   # safe nested get

  # Sort dict by value
  sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))
  sorted_d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

  # Sort by key
  sorted_d = dict(sorted(d.items()))

  # Invert multi-value dict
  inv = {}
  for k, v in d.items():
      inv.setdefault(v, []).append(k)

  # Merge list of dicts
  from functools import reduce
  merged = reduce(lambda a,b: {**a,**b}, list_of_dicts)

  # Dict from two lists
  dict(zip(keys, values))

  # Check if two dicts have same keys
  set(d1.keys()) == set(d2.keys())

  # Deep copy
  import copy
  deep = copy.deepcopy(d)

  ORDERED OPERATIONS
  ──────────────────────────────────────────────────────────────────────
  # Python 3.7+ dicts maintain insertion order

  from collections import OrderedDict
  od = OrderedDict()
  od["z"] = 1
  od["a"] = 2
  od["m"] = 3
  od.move_to_end("z")         # move to end
  od.move_to_end("z", last=False)  # move to front
  od.popitem(last=True)       # remove last
  od.popitem(last=False)      # remove first

  # LRU cache using OrderedDict
  class LRUCache:
      def __init__(self, capacity):
          self.cache = OrderedDict()
          self.cap = capacity

      def get(self, key):
          if key not in self.cache: return -1
          self.cache.move_to_end(key)
          return self.cache[key]

      def put(self, key, value):
          if key in self.cache:
              self.cache.move_to_end(key)
          self.cache[key] = value
          if len(self.cache) > self.cap:
              self.cache.popitem(last=False)
```

---

## 16   SETS & FROZENSETS

```
  SET CREATION
  ──────────────────────────────────────────────────────────────────────
  empty   = set()             # NOT {} — that's empty dict!
  s       = {1, 2, 3}
  s2      = set([1,2,2,3,3])  # {1,2,3} — deduplicates
  s3      = set("hello")      # {'h','e','l','o'}
  chars   = set("abcabc")     # {'a','b','c'}

  SET METHODS
  ──────────────────────────────────────────────────────────────────────
  s = {1, 2, 3, 4, 5}

  s.add(6)              # add element
  s.remove(3)           # remove (KeyError if missing)
  s.discard(3)          # remove (no error if missing)
  s.pop()               # remove & return arbitrary element
  s.clear()             # remove all

  s.update([6,7,8])     # add multiple (like extend)
  s.copy()              # shallow copy
  len(s)                # size
  3 in s                # membership test O(1)!
  3 not in s

  SET OPERATIONS
  ──────────────────────────────────────────────────────────────────────
  a = {1, 2, 3, 4}
  b = {3, 4, 5, 6}

  # Union — all elements from both
  a | b                 # {1,2,3,4,5,6}
  a.union(b)

  # Intersection — only common elements
  a & b                 # {3,4}
  a.intersection(b)

  # Difference — in a but not b
  a - b                 # {1,2}
  a.difference(b)

  # Symmetric difference — in either but not both
  a ^ b                 # {1,2,5,6}
  a.symmetric_difference(b)

  # Subset / Superset
  {1,2}.issubset({1,2,3})        # True
  {1,2,3}.issuperset({1,2})      # True
  {1,2} <= {1,2,3}               # True (subset)
  {1,2} < {1,2,3}                # True (proper subset)
  {1,2,3} >= {1,2}               # True (superset)

  # Disjoint
  {1,2}.isdisjoint({3,4})        # True (no common elements)

  # Update in place
  a |= b       # union update
  a &= b       # intersection update
  a -= b       # difference update
  a ^= b       # symmetric difference update

  FROZENSET — immutable, hashable set
  ──────────────────────────────────────────────────────────────────────
  fs = frozenset([1, 2, 3])
  fs | frozenset([3,4])   # frozenset({1,2,3,4})
  # All set operations work except mutating ones
  # Can be used as dict key or element of another set

  d = {frozenset({1,2}): "pair"}  # valid dict key

  COMMON SET PATTERNS
  ──────────────────────────────────────────────────────────────────────
  # Remove duplicates from list (order lost)
  unique = list(set(lst))

  # Check if all unique
  len(lst) == len(set(lst))

  # Find duplicates
  dups = {x for x in lst if lst.count(x) > 1}
  # Better:
  seen, dups = set(), set()
  for x in lst:
      if x in seen: dups.add(x)
      else: seen.add(x)

  # Common elements of two lists
  common = set(list1) & set(list2)

  # Elements in list1 not in list2
  diff = set(list1) - set(list2)
```

---

## 17   COLLECTIONS MODULE

```
  from collections import (
      Counter, defaultdict, OrderedDict,
      deque, namedtuple, ChainMap, UserDict
  )

  COUNTER
  ──────────────────────────────────────────────────────────────────────
  from collections import Counter

  c = Counter("abracadabra")
  # Counter({'a':5,'b':2,'r':2,'c':1,'d':1})

  c["a"]                    # 5
  c["z"]                    # 0  (missing keys return 0!)
  c.most_common(3)          # [('a',5),('b',2),('r',2)]
  c.most_common()[:-3:-1]   # 2 least common
  list(c.elements())        # ['a','a','a','a','a','b','b',...]
  c.total()                 # 11  (Python 3.10+)

  # Arithmetic
  c1 = Counter(a=3, b=1)
  c2 = Counter(a=1, b=2)
  c1 + c2          # Counter({'a':4,'b':3})
  c1 - c2          # Counter({'a':2})  (only positive)
  c1 & c2          # Counter({'a':1,'b':1})  (min)
  c1 | c2          # Counter({'a':3,'b':2})  (max)

  # Update
  c.update("aab")           # add counts
  c.subtract("aab")         # subtract counts (can go negative)

  # Common patterns
  words = "the cat sat on the mat".split()
  freq = Counter(words)
  freq.most_common(1)        # [('the', 2)]

  # k most common words
  Counter(words).most_common(3)

  # Check anagram
  Counter("listen") == Counter("silent")   # True

  DEFAULTDICT
  ──────────────────────────────────────────────────────────────────────
  from collections import defaultdict

  # Provide default factory function
  dd_list  = defaultdict(list)    # missing key → []
  dd_int   = defaultdict(int)     # missing key → 0
  dd_set   = defaultdict(set)     # missing key → set()
  dd_dict  = defaultdict(dict)    # missing key → {}
  dd_str   = defaultdict(str)     # missing key → ""
  dd_const = defaultdict(lambda: "N/A")  # custom default

  # No KeyError on missing keys
  dd_list["key"].append(1)     # creates [] then appends
  dd_int["count"] += 1        # creates 0 then increments

  # Group by
  students = [("Alice","Math"),("Bob","CS"),("Carol","Math")]
  groups = defaultdict(list)
  for name, subject in students:
      groups[subject].append(name)
  # {'Math': ['Alice','Carol'], 'CS': ['Bob']}

  # Graph adjacency list
  graph = defaultdict(list)
  edges = [(1,2),(1,3),(2,4),(3,4)]
  for u, v in edges:
      graph[u].append(v)
      graph[v].append(u)

  DEQUE
  ──────────────────────────────────────────────────────────────────────
  from collections import deque

  d = deque([1,2,3,4,5])
  d = deque(maxlen=3)         # bounded deque (auto-removes from other end)

  d.append(6)                 # add right  O(1)
  d.appendleft(0)             # add left   O(1)
  d.pop()                     # remove right O(1)
  d.popleft()                 # remove left  O(1)  ← use over list.pop(0)!
  d.extend([7,8])             # extend right
  d.extendleft([9,10])        # extend left (each appendleft)
  d.rotate(2)                 # rotate right by 2
  d.rotate(-2)                # rotate left by 2
  d.count(1)                  # count occurrences
  d.remove(3)                 # remove first occurrence
  d.reverse()                 # reverse in place
  d.copy()                    # shallow copy
  d.clear()                   # empty

  # BFS queue pattern
  from collections import deque
  queue = deque([(start, 0)])  # (node, distance)
  visited = set([start])
  while queue:
      node, dist = queue.popleft()
      for neighbor in graph[node]:
          if neighbor not in visited:
              visited.add(neighbor)
              queue.append((neighbor, dist+1))

  # Sliding window maximum
  def max_sliding_window(nums, k):
      dq = deque()    # stores indices, decreasing order of values
      result = []
      for i, n in enumerate(nums):
          while dq and nums[dq[-1]] <= n:
              dq.pop()
          dq.append(i)
          if dq[0] == i - k:
              dq.popleft()
          if i >= k - 1:
              result.append(nums[dq[0]])
      return result

  NAMEDTUPLE
  ──────────────────────────────────────────────────────────────────────
  from collections import namedtuple

  Point   = namedtuple("Point", ["x","y"])
  Point   = namedtuple("Point", "x y")         # space separated
  Color   = namedtuple("Color", "red green blue", defaults=[0,0,0])

  p = Point(3, 4)
  p.x          # 3   (attribute access)
  p[0]         # 3   (index access)
  p.x, p.y     # 3, 4
  len(p)       # 2
  p._replace(x=10)       # Point(x=10, y=4) — new instance
  p._asdict()             # {'x':3,'y':4}
  Point._fields          # ('x','y')
  Point._make([3,4])     # Point(x=3, y=4)  from iterable

  # Useful for returning structured data
  def get_bounds(lst):
      Bounds = namedtuple("Bounds", "min max mean")
      return Bounds(min(lst), max(lst), sum(lst)/len(lst))

  b = get_bounds([1,2,3,4,5])
  b.min    # 1
  b.max    # 5
  b.mean   # 3.0

  CHAINMAP
  ──────────────────────────────────────────────────────────────────────
  from collections import ChainMap

  defaults = {"color":"red", "user":"guest"}
  user_config = {"color":"blue"}
  env = {"debug": True}

  config = ChainMap(user_config, env, defaults)
  config["color"]    # "blue"  (first map wins)
  config["debug"]    # True
  config["user"]     # "guest"

  config.maps                 # list of underlying dicts
  config.new_child({"x":1})  # new ChainMap with extra dict in front
  config.parents              # ChainMap without first dict

  # Use case: command line > environment > defaults
```

---

## 18   ITERTOOLS MODULE — Complete Reference

```
  import itertools

  INFINITE ITERATORS
  ──────────────────────────────────────────────────────────────────────
  itertools.count(10, 2)            # 10, 12, 14, 16, ...
  itertools.cycle([1,2,3])          # 1,2,3,1,2,3,...
  itertools.repeat(5, 3)            # 5, 5, 5  (limited)
  itertools.repeat(5)               # 5, 5, 5, ...  (infinite)

  TERMINATING ITERATORS
  ──────────────────────────────────────────────────────────────────────
  # accumulate — running totals
  list(itertools.accumulate([1,2,3,4]))        # [1,3,6,10]
  list(itertools.accumulate([1,2,3,4], max))   # [1,2,3,4]  (running max)
  list(itertools.accumulate([1,2,3,4], lambda a,b: a*b))  # [1,2,6,24]

  # chain — combine iterables
  list(itertools.chain([1,2],[3,4],[5,6]))      # [1,2,3,4,5,6]
  list(itertools.chain.from_iterable([[1,2],[3,4]]))  # [1,2,3,4]

  # compress — filter by mask
  list(itertools.compress("ABCDEF",[1,0,1,0,1,1]))  # ['A','C','E','F']

  # dropwhile / takewhile
  list(itertools.dropwhile(lambda x: x<5, [1,4,6,4,1]))  # [6,4,1]
  list(itertools.takewhile(lambda x: x<5, [1,4,6,4,1]))  # [1,4]

  # filterfalse
  list(itertools.filterfalse(lambda x: x%2, range(10)))  # [0,2,4,6,8]

  # groupby (requires sorted input!)
  data = [("M","Alice"),("M","Bob"),("F","Carol"),("F","Dana")]
  data.sort(key=lambda x: x[0])
  for key, group in itertools.groupby(data, key=lambda x: x[0]):
      print(key, list(group))
  # M [('M','Alice'),('M','Bob')]
  # F [('F','Carol'),('F','Dana')]

  # islice — slice any iterator
  list(itertools.islice(range(100), 5))            # [0,1,2,3,4]
  list(itertools.islice(range(100), 2, 8, 2))      # [2,4,6]
  list(itertools.islice(itertools.count(), 5))     # [0,1,2,3,4]

  # pairwise (Python 3.10+)
  list(itertools.pairwise([1,2,3,4]))   # [(1,2),(2,3),(3,4)]

  # starmap
  list(itertools.starmap(pow, [(2,3),(3,2),(4,2)]))  # [8,9,16]

  # zip_longest
  list(itertools.zip_longest([1,2,3],[4,5],fillvalue=0))
  # [(1,4),(2,5),(3,0)]

  COMBINATORIAL ITERATORS
  ──────────────────────────────────────────────────────────────────────
  # product — Cartesian product (nested for loops)
  list(itertools.product("AB","CD"))
  # [('A','C'),('A','D'),('B','C'),('B','D')]
  list(itertools.product(range(2), repeat=3))
  # all 3-bit binary numbers

  # permutations — ordered arrangements
  list(itertools.permutations("ABC", 2))
  # [('A','B'),('A','C'),('B','A'),('B','C'),('C','A'),('C','B')]
  # n! / (n-r)! arrangements, no repeated elements

  # combinations — unordered selections
  list(itertools.combinations("ABC", 2))
  # [('A','B'),('A','C'),('B','C')]
  # C(n,r) = n! / (r!(n-r)!)

  # combinations_with_replacement
  list(itertools.combinations_with_replacement("AB", 2))
  # [('A','A'),('A','B'),('B','B')]

  PRACTICAL EXAMPLES
  ──────────────────────────────────────────────────────────────────────
  # Flatten nested list
  nested = [[1,2],[3,[4,5]],[6]]
  flat = list(itertools.chain.from_iterable(nested))

  # Round-robin from multiple iterables
  def roundrobin(*iterables):
      nexts = itertools.cycle(iter(it).__next__ for it in iterables)
      pending = len(iterables)
      while pending:
          try:
              for nxt in nexts:
                  yield nxt()
          except StopIteration:
              pending -= 1
              nexts = itertools.cycle(itertools.islice(nexts, pending))

  # n-grams
  def ngrams(seq, n):
      return list(zip(*(itertools.islice(seq, i, None) for i in range(n))))

  ngrams("hello", 2)  # [('h','e'),('e','l'),('l','l'),('l','o')]

  # All subsets
  def all_subsets(lst):
      return list(itertools.chain.from_iterable(
          itertools.combinations(lst, r) for r in range(len(lst)+1)))
```

---

## 19   FUNCTOOLS MODULE

```
  import functools

  LRU_CACHE / CACHE
  ──────────────────────────────────────────────────────────────────────
  @functools.lru_cache(maxsize=128)   # cache last 128 results
  def expensive(n):
      return sum(range(n))

  @functools.lru_cache(maxsize=None)  # unbounded cache
  def fib(n):
      if n < 2: return n
      return fib(n-1) + fib(n-2)

  @functools.cache                    # Python 3.9+ same as lru_cache(None)
  def fib(n):
      if n < 2: return n
      return fib(n-1) + fib(n-2)

  fib.cache_info()   # CacheInfo(hits=..., misses=..., maxsize=..., currsize=...)
  fib.cache_clear()  # clear cache

  REDUCE
  ──────────────────────────────────────────────────────────────────────
  from functools import reduce

  reduce(lambda a,b: a+b, [1,2,3,4,5])        # 15
  reduce(lambda a,b: a*b, [1,2,3,4,5], 1)     # 120  (with initial)
  reduce(max, [3,1,4,1,5,9])                   # 9
  reduce(lambda a,b: a if a>b else b, lst)     # max

  PARTIAL
  ──────────────────────────────────────────────────────────────────────
  from functools import partial

  def power(base, exp):
      return base ** exp

  square = partial(power, exp=2)    # fix exp=2
  cube   = partial(power, exp=3)

  square(5)    # 25
  cube(3)      # 27

  # Common use: simplify repeated calls
  import json
  dumps = partial(json.dumps, indent=2, sort_keys=True)
  dumps({"b":2,"a":1})   # nicely formatted

  # With print
  print_sep = partial(print, sep=" | ")
  print_sep("a","b","c")   # a | b | c

  TOTAL_ORDERING
  ──────────────────────────────────────────────────────────────────────
  from functools import total_ordering

  @total_ordering
  class Student:
      def __init__(self, name, grade):
          self.name = name
          self.grade = grade

      def __eq__(self, other):
          return self.grade == other.grade

      def __lt__(self, other):
          return self.grade < other.grade

  # total_ordering fills in >, >=, <= automatically

  WRAPS (preserve function metadata in decorators)
  ──────────────────────────────────────────────────────────────────────
  from functools import wraps

  def my_decorator(func):
      @wraps(func)               # preserves __name__, __doc__ etc.
      def wrapper(*args, **kwargs):
          print("Before")
          result = func(*args, **kwargs)
          print("After")
          return result
      return wrapper

  SINGLEDISPATCH (function overloading by type)
  ──────────────────────────────────────────────────────────────────────
  from functools import singledispatch

  @singledispatch
  def process(data):
      raise NotImplementedError(f"No handler for {type(data)}")

  @process.register(int)
  def _(data):
      return f"int: {data}"

  @process.register(str)
  def _(data):
      return f"str: {data.upper()}"

  @process.register(list)
  def _(data):
      return f"list of {len(data)}"

  process(42)       # "int: 42"
  process("hi")     # "str: HI"
  process([1,2,3])  # "list of 3"
```

---

## 20   OOP — CLASSES & OBJECTS

```
  CLASS ANATOMY
  ──────────────────────────────────────────────────────────────────────
  class Animal:
      """Docstring: base class for all animals."""

      # Class variable (shared by all instances)
      count = 0
      kingdom = "Animalia"

      def __init__(self, name: str, age: int):
          """Constructor — called when object created."""
          self.name = name           # instance variable
          self.age  = age            # instance variable
          Animal.count += 1          # access class variable

      def speak(self):               # instance method
          """Override in subclasses."""
          return f"{self.name} makes a sound."

      @classmethod
      def get_count(cls):            # class method (receives class)
          return cls.count

      @staticmethod
      def is_animal(obj):            # static method (no self/cls)
          return isinstance(obj, Animal)

      def __repr__(self):            # developer repr
          return f"Animal(name={self.name!r}, age={self.age})"

      def __str__(self):             # user-friendly str
          return f"{self.name} (age {self.age})"

      def __del__(self):             # destructor (avoid relying on this)
          Animal.count -= 1

  # Create objects
  a = Animal("Lion", 5)
  print(a)                    # Lion (age 5)        — __str__
  repr(a)                     # Animal(name='Lion', age=5) — __repr__
  Animal.count                # 1
  Animal.get_count()          # 1
  Animal.is_animal(a)         # True

  # Access / modify
  a.name                      # "Lion"
  a.name = "Tiger"            # set
  hasattr(a, "name")          # True
  getattr(a, "name")          # "Tiger"
  setattr(a, "name", "Bear")
  delattr(a, "name")          # delete attribute

  # Introspection
  type(a)                     # <class 'Animal'>
  isinstance(a, Animal)       # True
  a.__class__                 # <class 'Animal'>
  a.__dict__                  # {'name':'Bear','age':5}
  Animal.__dict__             # class namespace dict
  dir(a)                      # all attributes and methods
  vars(a)                     # same as __dict__

  CLASS VARIABLE vs INSTANCE VARIABLE
  ──────────────────────────────────────────────────────────────────────
  class Dog:
      species = "Canis lupus"    # class variable

      def __init__(self, name):
          self.name = name       # instance variable

  d1 = Dog("Rex")
  d2 = Dog("Buddy")

  Dog.species         # "Canis lupus"
  d1.species          # "Canis lupus"   (looks up class)
  d1.species = "X"    # creates INSTANCE variable, shadows class var
  d1.species          # "X"
  Dog.species         # "Canis lupus"  (class var unchanged!)
  d2.species          # "Canis lupus"

  SLOTS (memory optimization)
  ──────────────────────────────────────────────────────────────────────
  class Point:
      __slots__ = ("x", "y")    # pre-declare all attributes

      def __init__(self, x, y):
          self.x = x
          self.y = y

  # Benefits: less memory, faster attribute access
  # Drawback: can't add new attributes, no __dict__

  p = Point(3, 4)
  p.x                # 3
  p.z = 5            # AttributeError!
```

---

## 21   OOP — INHERITANCE & MRO

```
  SINGLE INHERITANCE
  ──────────────────────────────────────────────────────────────────────
  class Dog(Animal):

      def __init__(self, name, age, breed):
          super().__init__(name, age)  # call parent __init__
          self.breed = breed

      def speak(self):                 # override
          return f"{self.name} says: Woof!"

      def fetch(self):                 # new method
          return f"{self.name} fetches the ball!"

  dog = Dog("Rex", 3, "Lab")
  dog.speak()          # "Rex says: Woof!"
  dog.fetch()          # "Rex fetches the ball!"
  dog.name             # "Rex"  (inherited)

  isinstance(dog, Dog)     # True
  isinstance(dog, Animal)  # True  (is-a relationship)
  issubclass(Dog, Animal)  # True

  MULTIPLE INHERITANCE
  ──────────────────────────────────────────────────────────────────────
  class Flyable:
      def fly(self):
          return "Flying!"

      def move(self):
          return "Flyable move"

  class Swimmable:
      def swim(self):
          return "Swimming!"

      def move(self):
          return "Swimmable move"

  class Duck(Animal, Flyable, Swimmable):
      def speak(self):
          return "Quack!"

  duck = Duck("Donald", 2)
  duck.fly()     # "Flying!"
  duck.swim()    # "Swimming!"
  duck.move()    # "Flyable move"  (MRO: Duck→Animal→Flyable→Swimmable)

  METHOD RESOLUTION ORDER (MRO) — C3 Linearization
  ──────────────────────────────────────────────────────────────────────
  Duck.__mro__
  # (<class 'Duck'>, <class 'Animal'>, <class 'Flyable'>,
  #  <class 'Swimmable'>, <class 'object'>)

  Duck.mro()      # same as list

  # MRO determines which method is called with multiple inheritance
  # C3 algorithm: left-to-right, depth-first, consistent linearization

  # super() follows MRO
  class A:
      def greet(self): return "A"

  class B(A):
      def greet(self): return "B→" + super().greet()

  class C(A):
      def greet(self): return "C→" + super().greet()

  class D(B, C):
      def greet(self): return "D→" + super().greet()

  D().greet()   # "D→B→C→A"  (MRO: D→B→C→A)
  D.__mro__     # (D, B, C, A, object)

  ABSTRACT CLASSES
  ──────────────────────────────────────────────────────────────────────
  from abc import ABC, abstractmethod

  class Shape(ABC):
      @abstractmethod
      def area(self) -> float:
          """Must be implemented by subclasses."""
          pass

      @abstractmethod
      def perimeter(self) -> float:
          pass

      def describe(self):               # concrete method
          return f"Area={self.area():.2f}, Perimeter={self.perimeter():.2f}"

  class Circle(Shape):
      def __init__(self, radius):
          self.radius = radius

      def area(self):
          import math
          return math.pi * self.radius ** 2

      def perimeter(self):
          import math
          return 2 * math.pi * self.radius

  c = Circle(5)
  c.area()         # 78.53...
  c.describe()     # "Area=78.54, Perimeter=31.42"

  # Shape()  → TypeError: Can't instantiate abstract class

  MIXINS
  ──────────────────────────────────────────────────────────────────────
  class JSONMixin:
      """Add JSON serialization to any class."""
      import json

      def to_json(self):
          import json
          return json.dumps(self.__dict__, indent=2)

      @classmethod
      def from_json(cls, json_str):
          import json
          data = json.loads(json_str)
          obj = cls.__new__(cls)
          obj.__dict__.update(data)
          return obj

  class ReprMixin:
      """Auto __repr__ using all instance attributes."""
      def __repr__(self):
          attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
          return f"{self.__class__.__name__}({attrs})"

  class User(JSONMixin, ReprMixin):
      def __init__(self, name, email):
          self.name = name
          self.email = email

  u = User("Alice", "alice@example.com")
  repr(u)        # "User(name='Alice', email='alice@example.com')"
  u.to_json()    # {"name": "Alice", "email": "alice@example.com"}
```

---

## 22   OOP — POLYMORPHISM & DUCK TYPING

```
  DUCK TYPING
  ──────────────────────────────────────────────────────────────────────
  # "If it walks like a duck and quacks like a duck, it's a duck"
  # Python cares about METHODS not TYPES

  class Cat:
      def speak(self): return "Meow!"

  class Dog:
      def speak(self): return "Woof!"

  class Robot:
      def speak(self): return "Beep boop"

  def make_speak(obj):
      return obj.speak()          # works for ANY object with speak()

  for animal in [Cat(), Dog(), Robot()]:
      print(make_speak(animal))   # all work!

  OPERATOR OVERLOADING (via dunder methods)
  ──────────────────────────────────────────────────────────────────────
  class Vector:
      def __init__(self, x, y):
          self.x = x
          self.y = y

      def __add__(self, other):        # v1 + v2
          return Vector(self.x+other.x, self.y+other.y)

      def __sub__(self, other):        # v1 - v2
          return Vector(self.x-other.x, self.y-other.y)

      def __mul__(self, scalar):       # v * 3
          return Vector(self.x*scalar, self.y*scalar)

      def __rmul__(self, scalar):      # 3 * v
          return self.__mul__(scalar)

      def __neg__(self):               # -v
          return Vector(-self.x, -self.y)

      def __abs__(self):               # abs(v)
          return (self.x**2 + self.y**2) ** 0.5

      def __eq__(self, other):         # v1 == v2
          return self.x == other.x and self.y == other.y

      def __repr__(self):
          return f"Vector({self.x}, {self.y})"

  v1 = Vector(1, 2)
  v2 = Vector(3, 4)
  v1 + v2          # Vector(4, 6)
  v1 - v2          # Vector(-2, -2)
  v1 * 3           # Vector(3, 6)
  3 * v1           # Vector(3, 6)
  abs(v2)          # 5.0

  PROTOCOLS (Structural Subtyping)
  ──────────────────────────────────────────────────────────────────────
  # Any object implementing required methods satisfies the protocol
  # No explicit inheritance needed

  # Iterable protocol: __iter__ + __next__
  # Context manager: __enter__ + __exit__
  # Comparable: __eq__, __lt__, etc.
  # Hashable: __hash__
  # Callable: __call__
  # Sequence: __getitem__, __len__
  # Mapping: __getitem__, __setitem__, __delitem__, __len__, __iter__
```

---

## 23   OOP — ENCAPSULATION & PROPERTIES

```
  NAME MANGLING & ACCESS CONTROL
  ──────────────────────────────────────────────────────────────────────
  class BankAccount:
      def __init__(self, balance):
          self.owner = "Alice"     # public
          self._balance = balance  # protected (convention, not enforced)
          self.__pin = 1234        # private (name mangled to _BankAccount__pin)

  acc = BankAccount(1000)
  acc.owner               # "Alice"    ✅
  acc._balance            # 1000       ✅ (accessible but shouldn't be)
  acc.__pin               # AttributeError  ❌ name mangled
  acc._BankAccount__pin   # 1234       (can still access if needed)

  PROPERTY DECORATOR
  ──────────────────────────────────────────────────────────────────────
  class Temperature:
      def __init__(self, celsius=0):
          self._celsius = celsius

      @property
      def celsius(self):              # getter
          return self._celsius

      @celsius.setter
      def celsius(self, value):       # setter with validation
          if value < -273.15:
              raise ValueError(f"Temperature {value}°C below absolute zero!")
          self._celsius = value

      @celsius.deleter
      def celsius(self):              # deleter
          del self._celsius

      @property
      def fahrenheit(self):           # computed property (no setter)
          return self._celsius * 9/5 + 32

      @property
      def kelvin(self):
          return self._celsius + 273.15

  t = Temperature(100)
  t.celsius               # 100       (calls getter)
  t.celsius = 200         # (calls setter, validates)
  t.fahrenheit            # 212.0     (computed)
  t.celsius = -300        # ValueError!
  del t.celsius           # (calls deleter)

  # Read-only property
  class Circle:
      def __init__(self, radius):
          self._radius = radius

      @property
      def radius(self):
          return self._radius

      @property
      def area(self):
          import math
          return math.pi * self._radius ** 2

      # No setter → read-only
      # c.area = 10  → AttributeError

  DESCRIPTORS (advanced property mechanism)
  ──────────────────────────────────────────────────────────────────────
  class Validator:
      """Descriptor for validated attributes."""

      def __set_name__(self, owner, name):
          self.name = name

      def __get__(self, obj, objtype=None):
          if obj is None: return self
          return obj.__dict__.get(self.name)

      def __set__(self, obj, value):
          self.validate(value)
          obj.__dict__[self.name] = value

      def validate(self, value):
          pass

  class PositiveNumber(Validator):
      def validate(self, value):
          if value <= 0:
              raise ValueError(f"{self.name} must be positive, got {value}")

  class BoundedInt(Validator):
      def __init__(self, lo, hi):
          self.lo = lo
          self.hi = hi

      def validate(self, value):
          if not (self.lo <= value <= self.hi):
              raise ValueError(f"{self.name} must be in [{self.lo},{self.hi}]")

  class Product:
      price    = PositiveNumber()
      quantity = BoundedInt(0, 1000)

      def __init__(self, name, price, quantity):
          self.name = name
          self.price = price
          self.quantity = quantity

  p = Product("Widget", 9.99, 50)
  p.price = -1     # ValueError: price must be positive, got -1
```

---

## 24   OOP — MAGIC/DUNDER METHODS

```
  COMPLETE DUNDER REFERENCE
  ──────────────────────────────────────────────────────────────────────
  CONSTRUCTION / DESTRUCTION
  __new__(cls, ...)      → called before __init__, returns instance
  __init__(self, ...)    → initializer, sets up object
  __del__(self)          → destructor (not guaranteed to run)

  REPRESENTATION
  __repr__(self)         → unambiguous repr for developers
  __str__(self)          → human-readable string
  __bytes__(self)        → bytes()
  __format__(self, spec) → format() and f-strings
  __hash__(self)         → hash()  (if defined, must be consistent with __eq__)

  COMPARISON
  __eq__(self, other)    → == 
  __ne__(self, other)    → != (auto from __eq__ if not defined)
  __lt__(self, other)    → <
  __le__(self, other)    → <=
  __gt__(self, other)    → >
  __ge__(self, other)    → >=

  NUMERIC (arithmetic)
  __add__(self, other)   → self + other
  __radd__(self, other)  → other + self  (reflected, when other doesn't handle it)
  __iadd__(self, other)  → self += other  (in-place)
  __sub__, __rsub__, __isub__
  __mul__, __rmul__, __imul__
  __truediv__, __rtruediv__, __itruediv__
  __floordiv__, __rfloordiv__, __ifloordiv__
  __mod__, __rmod__, __imod__
  __pow__, __rpow__, __ipow__
  __neg__(self)          → -self
  __pos__(self)          → +self
  __abs__(self)          → abs(self)
  __round__(self, n)     → round(self, n)
  __floor__(self)        → math.floor(self)
  __ceil__(self)         → math.ceil(self)
  __trunc__(self)        → math.trunc(self)
  __int__(self)          → int(self)
  __float__(self)        → float(self)
  __complex__(self)      → complex(self)
  __bool__(self)         → bool(self)  (truthiness)
  __index__(self)        → as integer index

  BITWISE
  __and__, __rand__, __iand__    → &
  __or__, __ror__, __ior__       → |
  __xor__, __rxor__, __ixor__    → ^
  __lshift__, __rlshift__        → <<
  __rshift__, __rrshift__        → >>
  __invert__(self)               → ~self

  CONTAINER / SEQUENCE
  __len__(self)           → len(obj)
  __getitem__(self, key)  → obj[key]
  __setitem__(self, key, val) → obj[key] = val
  __delitem__(self, key)  → del obj[key]
  __contains__(self, item)→ item in obj
  __missing__(self, key)  → called by dict when key missing
  __iter__(self)          → iter(obj), returns iterator
  __next__(self)          → next(iterator)
  __reversed__(self)      → reversed(obj)

  CALLABLE
  __call__(self, *args, **kwargs)  → obj() — makes instance callable

  CONTEXT MANAGER
  __enter__(self)         → what's returned by 'as'
  __exit__(self, exc_type, exc_val, exc_tb) → return True suppresses exception

  ATTRIBUTE ACCESS
  __getattr__(self, name)       → called when attribute NOT found normally
  __getattribute__(self, name)  → called for EVERY attribute access
  __setattr__(self, name, val)  → obj.name = val
  __delattr__(self, name)       → del obj.name
  __dir__(self)                 → dir(obj)

  CLASS CREATION
  __init_subclass__(cls, **kwargs) → called when class is subclassed
  __class_getitem__(cls, item)     → cls[item] (generic type syntax)

  PRACTICAL EXAMPLES
  ──────────────────────────────────────────────────────────────────────
  class Matrix:
      def __init__(self, data):
          self.data = data
          self.rows = len(data)
          self.cols = len(data[0])

      def __repr__(self):
          rows = ["[" + ", ".join(map(str, row)) + "]" for row in self.data]
          return "Matrix([\n  " + ",\n  ".join(rows) + "\n])"

      def __len__(self): return self.rows * self.cols

      def __getitem__(self, key):
          r, c = key
          return self.data[r][c]

      def __setitem__(self, key, val):
          r, c = key
          self.data[r][c] = val

      def __add__(self, other):
          result = [[self.data[i][j]+other.data[i][j]
                     for j in range(self.cols)]
                    for i in range(self.rows)]
          return Matrix(result)

      def __mul__(self, scalar):
          return Matrix([[x*scalar for x in row] for row in self.data])

      def __iter__(self):
          for row in self.data:
              for val in row:
                  yield val

      def __eq__(self, other):
          return self.data == other.data

      def __bool__(self):
          return any(any(row) for row in self.data)

  m = Matrix([[1,2,3],[4,5,6],[7,8,9]])
  m[0,0]          # 1
  m[1,2] = 99
  len(m)          # 9
  for val in m: print(val)   # iterate all values
  m2 = m + m
  m3 = m * 2

  # Callable object (function-like class)
  class Adder:
      def __init__(self, n):
          self.n = n

      def __call__(self, x):
          return x + self.n

  add5 = Adder(5)
  add5(10)     # 15
  add5(20)     # 25
  callable(add5)  # True
```

---

## 25   OOP — ABSTRACT CLASSES & INTERFACES

```
  (see section 21 for ABC example)

  PROTOCOL (Python 3.8+ — structural subtyping)
  ──────────────────────────────────────────────────────────────────────
  from typing import Protocol, runtime_checkable

  @runtime_checkable
  class Drawable(Protocol):
      def draw(self) -> None: ...
      def resize(self, factor: float) -> None: ...

  class Circle:                    # No explicit inheritance!
      def draw(self): print("⭕")
      def resize(self, f): self.radius *= f

  class Square:
      def draw(self): print("⬜")
      def resize(self, f): self.side *= f

  def render(shape: Drawable):
      shape.draw()

  render(Circle())   # works — Circle has draw() and resize()
  render(Square())   # works — Square has draw() and resize()

  # runtime_checkable allows isinstance
  isinstance(Circle(), Drawable)   # True

  ABSTRACT BASE CLASSES (formal interface)
  ──────────────────────────────────────────────────────────────────────
  from abc import ABC, abstractmethod, abstractproperty

  class Collection(ABC):
      @abstractmethod
      def add(self, item): ...

      @abstractmethod
      def remove(self, item): ...

      @abstractmethod
      def __len__(self): ...

      @abstractmethod
      def __iter__(self): ...

      @property
      @abstractmethod
      def empty(self): ...

      def __contains__(self, item):  # concrete method using abstracts
          return any(x == item for x in self)

      def size(self):
          return len(self)
```

---

## 26   OOP — DATACLASSES & NAMEDTUPLE

```
  DATACLASSES (Python 3.7+)
  ──────────────────────────────────────────────────────────────────────
  from dataclasses import dataclass, field, asdict, astuple

  @dataclass
  class Point:
      x: float
      y: float

  p = Point(3.0, 4.0)
  p.x            # 3.0
  repr(p)        # "Point(x=3.0, y=4.0)"
  p == Point(3, 4)  # True  (__eq__ auto-generated)

  @dataclass
  class Student:
      name: str
      grade: int = 0                        # default value
      subjects: list = field(default_factory=list)  # mutable default!
      _id: int = field(default=0, repr=False)  # hidden from repr

      def average(self):
          return sum(self.subjects) / len(self.subjects) if self.subjects else 0

  s = Student("Alice", 90, [85, 92, 88])
  asdict(s)      # {'name':'Alice','grade':90,'subjects':[85,92,88],'_id':0}
  astuple(s)     # ('Alice', 90, [85,92,88], 0)

  # Frozen (immutable) dataclass
  @dataclass(frozen=True)
  class FrozenPoint:
      x: float
      y: float

  fp = FrozenPoint(3, 4)
  fp.x = 5       # FrozenError!
  hash(fp)       # hashable because frozen

  # Ordered dataclass (for sorting)
  @dataclass(order=True)
  class Card:
      rank: int
      suit: str

  Card(10, "hearts") > Card(5, "spades")   # True (compares rank first)

  # Post-init
  @dataclass
  class Rectangle:
      width: float
      height: float
      area: float = field(init=False)

      def __post_init__(self):
          self.area = self.width * self.height

  r = Rectangle(3, 4)
  r.area     # 12.0

  # Slots dataclass (Python 3.10+)
  @dataclass(slots=True)
  class FastPoint:
      x: float
      y: float

  TYPING_EXTENSIONS / TYPED NAMEDTUPLE
  ──────────────────────────────────────────────────────────────────────
  from typing import NamedTuple

  class Point(NamedTuple):
      x: float
      y: float = 0.0              # default

  p = Point(3.0)
  p.x         # 3.0
  p.y         # 0.0
  p._asdict() # {'x': 3.0, 'y': 0.0}
```

---

## 27   DECORATORS

```
  FUNCTION DECORATORS
  ──────────────────────────────────────────────────────────────────────
  # Decorator = function that wraps another function

  def my_decorator(func):
      from functools import wraps
      @wraps(func)                      # preserve metadata
      def wrapper(*args, **kwargs):
          print(f"Calling {func.__name__}")
          result = func(*args, **kwargs)
          print(f"Done {func.__name__}")
          return result
      return wrapper

  @my_decorator
  def greet(name):
      return f"Hello, {name}!"

  greet("Alice")   # equivalent to: my_decorator(greet)("Alice")

  TIMER DECORATOR
  ──────────────────────────────────────────────────────────────────────
  import time
  from functools import wraps

  def timer(func):
      @wraps(func)
      def wrapper(*args, **kwargs):
          start = time.perf_counter()
          result = func(*args, **kwargs)
          end = time.perf_counter()
          print(f"{func.__name__} took {end-start:.4f}s")
          return result
      return wrapper

  @timer
  def slow_function():
      time.sleep(0.1)

  RETRY DECORATOR
  ──────────────────────────────────────────────────────────────────────
  def retry(max_attempts=3, exceptions=(Exception,)):
      def decorator(func):
          @wraps(func)
          def wrapper(*args, **kwargs):
              for attempt in range(max_attempts):
                  try:
                      return func(*args, **kwargs)
                  except exceptions as e:
                      if attempt == max_attempts - 1:
                          raise
                      print(f"Attempt {attempt+1} failed: {e}")
          return wrapper
      return decorator

  @retry(max_attempts=3, exceptions=(ValueError, IOError))
  def fetch_data(url):
      # might fail sometimes
      pass

  CACHE DECORATOR
  ──────────────────────────────────────────────────────────────────────
  def memoize(func):
      cache = {}
      @wraps(func)
      def wrapper(*args):
          if args not in cache:
              cache[args] = func(*args)
          return cache[args]
      return wrapper

  @memoize
  def fib(n):
      if n < 2: return n
      return fib(n-1) + fib(n-2)

  VALIDATE TYPES DECORATOR
  ──────────────────────────────────────────────────────────────────────
  def validate_types(func):
      import inspect
      hints = func.__annotations__
      @wraps(func)
      def wrapper(*args, **kwargs):
          sig = inspect.signature(func)
          bound = sig.bind(*args, **kwargs)
          for param_name, value in bound.arguments.items():
              if param_name in hints:
                  expected = hints[param_name]
                  if not isinstance(value, expected):
                      raise TypeError(
                          f"{param_name} must be {expected.__name__}, "
                          f"got {type(value).__name__}")
          return func(*args, **kwargs)
      return wrapper

  @validate_types
  def add(a: int, b: int) -> int:
      return a + b

  add(1, 2)      # 3
  add(1, "2")    # TypeError!

  STACKING DECORATORS
  ──────────────────────────────────────────────────────────────────────
  @timer
  @retry(3)
  @validate_types
  def process(x: int):
      return x * 2

  # Applied bottom-up: validate_types → retry → timer

  CLASS DECORATORS
  ──────────────────────────────────────────────────────────────────────
  def singleton(cls):
      """Ensure only one instance of a class."""
      instances = {}
      @wraps(cls)
      def get_instance(*args, **kwargs):
          if cls not in instances:
              instances[cls] = cls(*args, **kwargs)
          return instances[cls]
      return get_instance

  @singleton
  class Config:
      def __init__(self):
          self.debug = False

  c1 = Config()
  c2 = Config()
  c1 is c2    # True

  DECORATOR CLASS
  ──────────────────────────────────────────────────────────────────────
  class repeat:
      def __init__(self, n):
          self.n = n

      def __call__(self, func):
          @wraps(func)
          def wrapper(*args, **kwargs):
              for _ in range(self.n):
                  result = func(*args, **kwargs)
              return result
          return wrapper

  @repeat(3)
  def greet():
      print("Hello!")

  greet()   # prints Hello! three times
```

---

## 28   GENERATORS & ITERATORS

```
  ITERATORS
  ──────────────────────────────────────────────────────────────────────
  # Iterator protocol: __iter__() and __next__()

  class CountUp:
      def __init__(self, start, stop):
          self.current = start
          self.stop = stop

      def __iter__(self):     # return self (is its own iterator)
          return self

      def __next__(self):
          if self.current > self.stop:
              raise StopIteration
          val = self.current
          self.current += 1
          return val

  for n in CountUp(1, 5):
      print(n)   # 1 2 3 4 5

  it = iter([1,2,3])     # get iterator from list
  next(it)               # 1
  next(it)               # 2
  next(it)               # 3
  next(it)               # StopIteration
  next(it, "done")       # "done"  (default, no exception)

  GENERATORS (simpler way to create iterators)
  ──────────────────────────────────────────────────────────────────────
  # Use yield — pauses function, saves state

  def count_up(start, stop):
      current = start
      while current <= stop:
          yield current
          current += 1

  gen = count_up(1, 5)
  next(gen)    # 1
  next(gen)    # 2
  list(gen)    # [3, 4, 5]  (exhausted)

  # Generator auto-raises StopIteration when function returns

  def fibonacci():
      a, b = 0, 1
      while True:                    # infinite generator!
          yield a
          a, b = b, a + b

  import itertools
  list(itertools.islice(fibonacci(), 10))  # [0,1,1,2,3,5,8,13,21,34]

  def read_large_file(path):
      with open(path) as f:
          for line in f:
              yield line.strip()     # one line at a time — memory efficient!

  YIELD FROM (Python 3.3+)
  ──────────────────────────────────────────────────────────────────────
  def chain(*iterables):
      for it in iterables:
          yield from it              # delegating generator

  list(chain([1,2],[3,4],[5,6]))     # [1,2,3,4,5,6]

  def flatten(nested):
      for item in nested:
          if isinstance(item, list):
              yield from flatten(item)
          else:
              yield item

  list(flatten([1,[2,[3,4]],[5,6]]))  # [1,2,3,4,5,6]

  SEND / THROW (coroutine-style generators)
  ──────────────────────────────────────────────────────────────────────
  def accumulator():
      total = 0
      while True:
          value = yield total        # yield AND receive
          if value is None:
              break
          total += value

  acc = accumulator()
  next(acc)         # 0   (prime the generator)
  acc.send(10)      # 10
  acc.send(20)      # 30
  acc.send(5)       # 35
  acc.throw(GeneratorExit)  # close

  GENERATOR EXPRESSIONS
  ──────────────────────────────────────────────────────────────────────
  # (expression for item in iterable if condition)

  squares_gen = (x**2 for x in range(1000000))  # lazy, no memory
  next(squares_gen)    # 0
  sum(squares_gen)     # sum rest

  # Pass directly to functions that accept iterables
  sum(x**2 for x in range(100))
  max(len(line) for line in open("file.txt"))

  GENERATOR PIPELINES
  ──────────────────────────────────────────────────────────────────────
  def read_file(path):
      with open(path) as f:
          yield from f

  def strip_lines(lines):
      for line in lines:
          yield line.strip()

  def filter_empty(lines):
      for line in lines:
          if line:
              yield line

  def parse_csv(lines):
      for line in lines:
          yield line.split(",")

  # Pipeline composition
  lines     = read_file("data.csv")
  stripped  = strip_lines(lines)
  filtered  = filter_empty(stripped)
  parsed    = parse_csv(filtered)

  for row in parsed:
      process(row)    # processes one row at a time — memory efficient!
```

---

## 29   CONTEXT MANAGERS

```
  WITH STATEMENT
  ──────────────────────────────────────────────────────────────────────
  # Guarantees __exit__ is called even if exception occurs

  with open("file.txt", "r") as f:
      content = f.read()
  # f.close() called automatically

  # Multiple context managers
  with open("in.txt") as fin, open("out.txt","w") as fout:
      fout.write(fin.read().upper())

  # Python 3.10+: parenthesized
  with (
      open("in.txt") as fin,
      open("out.txt","w") as fout
  ):
      ...

  CUSTOM CONTEXT MANAGER (class-based)
  ──────────────────────────────────────────────────────────────────────
  class Timer:
      import time

      def __enter__(self):
          import time
          self.start = time.perf_counter()
          return self              # what 'as' binds to

      def __exit__(self, exc_type, exc_val, exc_tb):
          import time
          self.elapsed = time.perf_counter() - self.start
          print(f"Elapsed: {self.elapsed:.4f}s")
          return False             # False = don't suppress exceptions

  with Timer() as t:
      sum(range(1000000))

  t.elapsed   # access after with block

  class SuppressErrors:
      def __init__(self, *exceptions):
          self.exceptions = exceptions

      def __enter__(self):
          return self

      def __exit__(self, exc_type, exc_val, exc_tb):
          return exc_type in self.exceptions   # True = suppress

  with SuppressErrors(FileNotFoundError, PermissionError):
      open("nonexistent.txt")   # suppressed, no error

  CUSTOM CONTEXT MANAGER (generator-based)
  ──────────────────────────────────────────────────────────────────────
  from contextlib import contextmanager

  @contextmanager
  def timer():
      import time
      start = time.perf_counter()
      try:
          yield                    # code inside with block runs here
      finally:
          elapsed = time.perf_counter() - start
          print(f"Elapsed: {elapsed:.4f}s")

  with timer():
      sum(range(1000000))

  @contextmanager
  def managed_resource(name):
      print(f"Acquiring {name}")
      try:
          yield name               # yields value for 'as'
      except Exception as e:
          print(f"Error with {name}: {e}")
          raise
      finally:
          print(f"Releasing {name}")

  with managed_resource("database") as db:
      use(db)

  CONTEXTLIB UTILITIES
  ──────────────────────────────────────────────────────────────────────
  from contextlib import (
      suppress, redirect_stdout, redirect_stderr,
      ExitStack, nullcontext, closing
  )

  # suppress — ignore specific exceptions
  with suppress(FileNotFoundError):
      os.remove("nonexistent.txt")

  # redirect output
  import io
  buf = io.StringIO()
  with redirect_stdout(buf):
      print("This goes to buffer!")
  output = buf.getvalue()     # "This goes to buffer!\n"

  # ExitStack — dynamic context managers
  with ExitStack() as stack:
      files = [stack.enter_context(open(f)) for f in filenames]
      # all files auto-closed on exit

  # nullcontext — no-op context manager
  cm = some_cm if condition else nullcontext()
  with cm:
      do_stuff()
```

---

## 30   EXCEPTION HANDLING — Complete Reference

```
  EXCEPTION HIERARCHY
  ──────────────────────────────────────────────────────────────────────
                        BaseException
                       /      |       \
                  SystemExit  KeyboardInterrupt  Exception
                                                     │
                               ┌─────────────────────┼──────────────────────┐
                               │                     │                      │
                        ArithmeticError       LookupError            ValueError
                         /          \          /       \               │
                    ZeroDivision  Overflow  IndexError KeyError   UnicodeError
                                                                       │
                          ┌───────────────┐       AttributeError  FileNotFoundError
                          │               │       NameError       PermissionError
                    TypeError     RuntimeError    ImportError     IsADirectoryError
                                    /      \      OSError
                               StopIteration  RecursionError

  TRY / EXCEPT / ELSE / FINALLY
  ──────────────────────────────────────────────────────────────────────
  try:
      risky_operation()
  except ValueError as e:
      print(f"Value error: {e}")
  except (TypeError, KeyError) as e:
      print(f"Type or Key error: {e}")
  except Exception as e:              # catch-all (keep last)
      print(f"Unexpected: {type(e).__name__}: {e}")
  else:
      print("No exception occurred")  # runs if try succeeded
  finally:
      cleanup()                       # ALWAYS runs (exception or not)

  # Reraise
  try:
      do_something()
  except Exception as e:
      log(e)
      raise                           # reraise same exception

  # Raise from (chain exceptions)
  try:
      do_something()
  except OSError as e:
      raise RuntimeError("Processing failed") from e
      # preserves original exception as __cause__

  # Suppress context
  raise RuntimeError("error") from None   # no __context__

  CUSTOM EXCEPTIONS
  ──────────────────────────────────────────────────────────────────────
  class AppError(Exception):
      """Base exception for this application."""
      pass

  class ValidationError(AppError):
      def __init__(self, field, message):
          self.field = field
          self.message = message
          super().__init__(f"Validation error on '{field}': {message}")

  class DatabaseError(AppError):
      def __init__(self, query, original):
          self.query = query
          self.original = original
          super().__init__(f"DB error executing '{query}': {original}")
          self.__cause__ = original

  # Usage
  try:
      validate_email("not-an-email")
  except ValidationError as e:
      print(e.field)    # "email"
      print(e.message)  # "Invalid format"

  EXCEPTION NOTES (Python 3.11+)
  ──────────────────────────────────────────────────────────────────────
  try:
      do_something()
  except Exception as e:
      e.add_note("Additional context: this happened during startup")
      raise

  EXCEPTION GROUPS (Python 3.11+)
  ──────────────────────────────────────────────────────────────────────
  # For handling multiple concurrent exceptions
  try:
      raise ExceptionGroup("multiple failures", [
          ValueError("bad value"),
          TypeError("wrong type"),
      ])
  except* ValueError as eg:
      print("Handling ValueErrors:", eg.exceptions)
  except* TypeError as eg:
      print("Handling TypeErrors:", eg.exceptions)

  BEST PRACTICES
  ──────────────────────────────────────────────────────────────────────
  ✅ Catch specific exceptions, not bare except
  ✅ Use else clause for success path
  ✅ Use finally for cleanup
  ✅ Create custom exception hierarchy
  ✅ Include relevant info in exception message
  ✅ Use from to chain exceptions
  ❌ Never: except: pass  (silent failure)
  ❌ Don't catch BaseException or KeyboardInterrupt
  ❌ Don't use exceptions for normal flow control
```

---

## 31   FILE I/O — Reading, Writing, Paths

```
  PATHLIB (modern, prefer this)
  ──────────────────────────────────────────────────────────────────────
  from pathlib import Path

  p = Path("/home/user/docs/file.txt")
  p = Path.home() / "docs" / "file.txt"    # / operator for joining
  p = Path(".")                             # current directory

  p.name                  # "file.txt"
  p.stem                  # "file"
  p.suffix                # ".txt"
  p.suffixes              # [".txt"]
  p.parent                # Path("/home/user/docs")
  p.parents[0]            # Path("/home/user/docs")
  p.parents[1]            # Path("/home/user")
  p.parts                 # ('/', 'home', 'user', 'docs', 'file.txt')

  p.exists()              # True/False
  p.is_file()             # True
  p.is_dir()              # False
  p.stat().st_size        # file size in bytes
  p.stat().st_mtime       # modification time

  p.read_text()           # read entire file as string
  p.read_bytes()          # read as bytes
  p.write_text("hello")   # write string (overwrites!)
  p.write_bytes(b"hello") # write bytes

  p.resolve()             # absolute path, resolve symlinks
  p.relative_to("/home")  # Path("user/docs/file.txt")

  p.mkdir(parents=True, exist_ok=True)   # create directory
  p.unlink(missing_ok=True)              # delete file
  p.rmdir()                              # delete empty dir
  p.rename(new_path)                     # rename/move
  p.replace(new_path)                    # rename (overwrite if exists)

  # Glob
  list(Path(".").glob("*.py"))            # all .py in current dir
  list(Path(".").glob("**/*.py"))         # all .py recursively
  list(Path(".").rglob("*.py"))           # same as **/*.py

  # Iterate directory
  for item in Path(".").iterdir():
      if item.is_file():
          print(item.name)

  READING FILES
  ──────────────────────────────────────────────────────────────────────
  # Read entire file
  with open("file.txt", "r", encoding="utf-8") as f:
      content = f.read()

  # Read lines (list)
  with open("file.txt") as f:
      lines = f.readlines()            # ['line1\n','line2\n',...]

  # Read lines without newlines
  with open("file.txt") as f:
      lines = [line.rstrip() for line in f]

  # Iterate line by line (memory efficient)
  with open("file.txt") as f:
      for line in f:
          process(line.strip())

  # Read with pathlib
  content = Path("file.txt").read_text(encoding="utf-8")
  lines = content.splitlines()

  WRITING FILES
  ──────────────────────────────────────────────────────────────────────
  # Overwrite
  with open("file.txt", "w", encoding="utf-8") as f:
      f.write("Hello\n")
      f.writelines(["line1\n","line2\n","line3\n"])

  # Append
  with open("file.txt", "a") as f:
      f.write("appended line\n")

  # Write with pathlib
  Path("file.txt").write_text("Hello World", encoding="utf-8")

  FILE MODES
  ──────────────────────────────────────────────────────────────────────
  "r"   read (default)
  "w"   write (truncate)
  "a"   append
  "x"   exclusive creation (fail if exists)
  "b"   binary mode
  "t"   text mode (default)
  "+    read+write
  "rb"  read binary
  "wb"  write binary
  "r+"  read+write (no truncate)
  "w+"  read+write (truncate)

  CSV
  ──────────────────────────────────────────────────────────────────────
  import csv

  # Read
  with open("data.csv", newline="") as f:
      reader = csv.reader(f)
      for row in reader:
          print(row)              # list of strings

  # DictReader
  with open("data.csv", newline="") as f:
      reader = csv.DictReader(f)
      for row in reader:
          print(row["name"], row["age"])   # access by header name

  # Write
  with open("out.csv","w",newline="") as f:
      writer = csv.writer(f)
      writer.writerow(["name","age","city"])
      writer.writerows([
          ["Alice",30,"NYC"],
          ["Bob",25,"LA"],
      ])

  # DictWriter
  with open("out.csv","w",newline="") as f:
      writer = csv.DictWriter(f, fieldnames=["name","age"])
      writer.writeheader()
      writer.writerow({"name":"Alice","age":30})

  JSON
  ──────────────────────────────────────────────────────────────────────
  import json

  # Serialize
  data = {"name":"Alice","age":30,"scores":[95,87,92]}
  json_str = json.dumps(data)
  json_str = json.dumps(data, indent=2, sort_keys=True)

  # Deserialize
  data = json.loads(json_str)

  # Read from file
  with open("data.json") as f:
      data = json.load(f)

  # Write to file
  with open("data.json","w") as f:
      json.dump(data, f, indent=2)

  # Custom encoder
  class DateEncoder(json.JSONEncoder):
      def default(self, obj):
          from datetime import datetime, date
          if isinstance(obj, (datetime, date)):
              return obj.isoformat()
          return super().default(obj)

  json.dumps({"date": datetime.now()}, cls=DateEncoder)

  PICKLE (Python object serialization)
  ──────────────────────────────────────────────────────────────────────
  import pickle

  data = {"key": [1,2,3], "nested": {"a":1}}
  with open("data.pkl","wb") as f:
      pickle.dump(data, f)

  with open("data.pkl","rb") as f:
      loaded = pickle.load(f)

  # In memory
  serialized = pickle.dumps(data)
  loaded = pickle.loads(serialized)

  # WARNING: never unpickle untrusted data (security risk!)
```

---

## 32   MODULES & PACKAGES

```
  IMPORTING
  ──────────────────────────────────────────────────────────────────────
  import math                      # import module
  import numpy as np               # alias
  from math import sqrt, pi        # specific items
  from math import *               # all (avoid in production)
  from . import sibling            # relative import
  from ..parent import thing       # relative import up

  math.sqrt(16)                    # 4.0
  sqrt(16)                         # 4.0 (after from import)

  CREATING MODULES
  ──────────────────────────────────────────────────────────────────────
  # mymodule.py
  """Module docstring."""

  __version__ = "1.0.0"
  __author__ = "Alice"

  def public_function():
      pass

  def _private_function():         # convention: not exported
      pass

  class PublicClass:
      pass

  if __name__ == "__main__":       # only runs when executed directly
      test_code()

  PACKAGES
  ──────────────────────────────────────────────────────────────────────
  mypackage/
  ├── __init__.py          # makes it a package
  ├── module1.py
  ├── module2.py
  └── subpackage/
      ├── __init__.py
      └── module3.py

  # __init__.py can import to simplify access
  # mypackage/__init__.py:
  from .module1 import useful_function
  from .module2 import UsefulClass
  __all__ = ["useful_function", "UsefulClass"]

  # Now users can:
  from mypackage import useful_function   # instead of mypackage.module1

  __ALL__ AND IMPORT *
  ──────────────────────────────────────────────────────────────────────
  # In module:
  __all__ = ["PublicClass", "public_function"]
  # from module import * only imports items in __all__

  IMPORTLIB (dynamic imports)
  ──────────────────────────────────────────────────────────────────────
  import importlib

  module = importlib.import_module("json")
  module.dumps({"a":1})

  # Reload module (useful in development)
  importlib.reload(my_module)

  sys.path — where Python looks for modules
  ──────────────────────────────────────────────────────────────────────
  import sys
  sys.path              # list of directories
  sys.path.append("/my/custom/path")
  sys.path.insert(0, "/priority/path")
```

---

## 33   REGULAR EXPRESSIONS

```
  import re

  BASIC PATTERNS
  ──────────────────────────────────────────────────────────────────────
  .        any character except newline
  \d       digit [0-9]
  \D       non-digit
  \w       word char [a-zA-Z0-9_]
  \W       non-word char
  \s       whitespace [ \t\n\r\f\v]
  \S       non-whitespace
  \b       word boundary
  \B       non-word boundary
  ^        start of string (or line with MULTILINE)
  $        end of string (or line with MULTILINE)
  \A       start of string (never multiline)
  \Z       end of string (never multiline)

  QUANTIFIERS
  ──────────────────────────────────────────────────────────────────────
  *        0 or more (greedy)
  +        1 or more (greedy)
  ?        0 or 1   (greedy)
  {n}      exactly n
  {n,}     n or more
  {n,m}    n to m
  *?       0 or more (lazy/non-greedy)
  +?       1 or more (lazy)
  ??       0 or 1   (lazy)
  {n,m}?   n to m  (lazy)

  CHARACTER CLASSES
  ──────────────────────────────────────────────────────────────────────
  [abc]    a or b or c
  [^abc]   not a, b, or c
  [a-z]    a through z
  [A-Za-z0-9]
  [^0-9]   not a digit

  GROUPS
  ──────────────────────────────────────────────────────────────────────
  (abc)      capturing group
  (?:abc)    non-capturing group
  (?P<name>abc)  named group
  (?=abc)    positive lookahead
  (?!abc)    negative lookahead
  (?<=abc)   positive lookbehind
  (?<!abc)   negative lookbehind
  (a|b)      alternation

  RE FUNCTIONS
  ──────────────────────────────────────────────────────────────────────
  re.match(pattern, string)    # match at START only
  re.search(pattern, string)   # match ANYWHERE
  re.fullmatch(pattern, string)# must match ENTIRE string
  re.findall(pattern, string)  # list of all matches
  re.finditer(pattern, string) # iterator of match objects
  re.sub(pattern, repl, string, count=0)  # replace
  re.subn(pattern, repl, string)  # (new_string, num_replacements)
  re.split(pattern, string)    # split by pattern
  re.compile(pattern, flags)   # compile for reuse

  # Flags
  re.IGNORECASE  re.I    → case-insensitive
  re.MULTILINE   re.M    → ^ $ match line boundaries
  re.DOTALL      re.S    → . matches \n too
  re.VERBOSE     re.X    → allow whitespace and comments
  re.ASCII       re.A    → \w \d etc. match ASCII only

  MATCH OBJECTS
  ──────────────────────────────────────────────────────────────────────
  m = re.search(r"(\d{4})-(\d{2})-(\d{2})", "Date: 2024-06-15")

  m.group()         # "2024-06-15"  (entire match)
  m.group(0)        # "2024-06-15"  (same)
  m.group(1)        # "2024"        (group 1)
  m.group(2)        # "06"
  m.group(3)        # "15"
  m.groups()        # ("2024","06","15")
  m.start()         # 6  (start index)
  m.end()           # 16 (end index)
  m.span()          # (6, 16)

  # Named groups
  m = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})", "2024-06")
  m.group("year")   # "2024"
  m.groupdict()     # {"year":"2024","month":"06"}

  EXAMPLES
  ──────────────────────────────────────────────────────────────────────
  # Email validation
  email_re = re.compile(r"^[\w.+-]+@[\w-]+\.[\w.-]+$", re.I)
  email_re.match("user@example.com")     # match
  email_re.match("not-an-email")         # None

  # Extract all numbers
  re.findall(r"\d+", "I have 3 cats and 12 dogs")  # ['3','12']

  # Replace with function
  def double_digits(m):
      return str(int(m.group()) * 2)
  re.sub(r"\d+", double_digits, "abc 3 def 12")  # "abc 6 def 24"

  # Split on multiple delimiters
  re.split(r"[,;:|]+", "a,b;;c:d|e")  # ['a','b','c','d','e']

  # Verbose pattern
  phone = re.compile(r"""
      (\+\d{1,3})?    # country code
      \s*             # optional space
      (\d{3})         # area code
      [-.\s]?         # separator
      (\d{3})         # exchange
      [-.\s]?         # separator
      (\d{4})         # number
  """, re.VERBOSE)
```

---

## 34   DATE & TIME

```
  from datetime import datetime, date, time, timedelta, timezone
  import zoneinfo

  DATE
  ──────────────────────────────────────────────────────────────────────
  today = date.today()               # 2024-06-15
  d = date(2024, 6, 15)

  d.year         # 2024
  d.month        # 6
  d.day          # 15
  d.weekday()    # 0=Mon ... 6=Sun
  d.isoweekday() # 1=Mon ... 7=Sun
  d.isoformat()  # "2024-06-15"
  d.strftime("%d/%m/%Y")   # "15/06/2024"
  date.fromisoformat("2024-06-15")
  date.fromtimestamp(1718409600)

  DATE ARITHMETIC
  ──────────────────────────────────────────────────────────────────────
  d + timedelta(days=7)              # one week later
  d - timedelta(days=30)             # 30 days ago
  d2 - d1                            # timedelta

  td = timedelta(days=5, hours=3, minutes=30)
  td.days           # 5
  td.seconds        # 12600
  td.total_seconds()# 444600.0

  DATETIME
  ──────────────────────────────────────────────────────────────────────
  now = datetime.now()               # local time
  utcnow = datetime.now(timezone.utc)# UTC time
  dt = datetime(2024, 6, 15, 10, 30, 0)

  dt.year, dt.month, dt.day
  dt.hour, dt.minute, dt.second, dt.microsecond
  dt.date()     # date part
  dt.time()     # time part

  dt.isoformat()                   # "2024-06-15T10:30:00"
  dt.strftime("%Y-%m-%d %H:%M:%S") # "2024-06-15 10:30:00"
  datetime.strptime("2024-06-15", "%Y-%m-%d")  # parse

  # Timestamp
  datetime.fromtimestamp(1718409600)
  dt.timestamp()

  STRFTIME FORMAT CODES
  ──────────────────────────────────────────────────────────────────────
  %Y   4-digit year       %m   month 01-12    %d   day 01-31
  %H   hour 00-23         %M   minute 00-59   %S   second 00-59
  %f   microsecond        %A   weekday name   %B   month name
  %a   short weekday      %b   short month    %p   AM/PM
  %I   12-hour clock      %z   UTC offset     %Z   timezone name
  %j   day of year        %U   week of year   %c   locale datetime
  %x   locale date        %X   locale time

  TIMEZONE (Python 3.9+)
  ──────────────────────────────────────────────────────────────────────
  from zoneinfo import ZoneInfo

  tz_ist = ZoneInfo("Asia/Kolkata")
  tz_utc = timezone.utc

  now_ist = datetime.now(tz_ist)
  now_utc = datetime.now(tz_utc)
  now_ist.astimezone(tz_utc)        # convert timezone

  TIMEDELTA EXAMPLES
  ──────────────────────────────────────────────────────────────────────
  # Age calculation
  birthday = date(1990, 6, 15)
  age_days = (date.today() - birthday).days
  age_years = age_days // 365

  # Days until event
  event = date(2024, 12, 31)
  days_left = (event - date.today()).days

  # Format duration
  def format_duration(td):
      total = int(td.total_seconds())
      hours, rem = divmod(total, 3600)
      minutes, seconds = divmod(rem, 60)
      return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
```

---

## 35   MATH & RANDOM

```
  import math, random, statistics

  MATH — FULL REFERENCE
  ──────────────────────────────────────────────────────────────────────
  # Constants
  math.pi        # 3.14159...
  math.e         # 2.71828...
  math.tau       # 6.28318...  (2π)
  math.inf       # infinity
  math.nan       # not a number

  # Basic
  math.sqrt(x)   math.cbrt(x)      # Python 3.11+
  math.pow(x,y)  math.exp(x)
  math.log(x)    math.log(x, base)  math.log2(x)  math.log10(x)
  math.factorial(n)  math.gcd(a,b)  math.lcm(a,b)
  math.isqrt(n)  # integer sqrt, no float
  math.comb(n,k) # C(n,k) combinations
  math.perm(n,k) # P(n,k) permutations

  # Rounding
  math.floor(x)  math.ceil(x)  math.trunc(x)  round(x, n)

  # Trig
  math.sin(x)  math.cos(x)  math.tan(x)
  math.asin(x)  math.acos(x)  math.atan(x)  math.atan2(y,x)
  math.degrees(x)  math.radians(x)
  math.hypot(x,y)   # sqrt(x²+y²)
  math.dist(p,q)    # Euclidean distance

  # Special
  math.fabs(x)       # absolute value (float)
  math.fsum(iter)    # accurate float sum
  math.prod(iter)    # product  (Python 3.8+)
  math.fmod(x,y)     # C-style fmod
  math.copysign(x,y) # magnitude of x, sign of y
  math.frexp(x)      # (mantissa, exponent)
  math.ldexp(x,i)    # x * (2**i)
  math.modf(x)       # (fractional, integer) parts
  math.isnan(x)  math.isinf(x)  math.isfinite(x)
  math.isclose(a,b,rel_tol=1e-9,abs_tol=0.0)

  RANDOM
  ──────────────────────────────────────────────────────────────────────
  import random

  random.seed(42)              # reproducible results

  random.random()              # float [0.0, 1.0)
  random.uniform(1, 10)        # float [1.0, 10.0]
  random.randint(1, 6)         # int [1, 6] inclusive
  random.randrange(0, 10, 2)   # 0,2,4,6,8 (like range)
  random.gauss(mu=0, sigma=1)  # normal distribution
  random.expovariate(1)        # exponential distribution

  lst = [1,2,3,4,5]
  random.choice(lst)           # pick one
  random.choices(lst, k=3)     # pick 3 with replacement
  random.choices(lst, weights=[1,2,3,2,1], k=3)  # weighted
  random.sample(lst, k=3)      # pick 3 without replacement
  random.shuffle(lst)          # shuffle in place (returns None)

  # Secure random (cryptography)
  import secrets
  secrets.token_hex(16)        # "secure" random hex string
  secrets.choice(lst)
  secrets.randbelow(100)

  STATISTICS
  ──────────────────────────────────────────────────────────────────────
  import statistics

  data = [2, 4, 4, 4, 5, 5, 7, 9]

  statistics.mean(data)          # 5.0
  statistics.median(data)        # 4.5
  statistics.median_low(data)    # 4
  statistics.median_high(data)   # 5
  statistics.mode(data)          # 4
  statistics.multimode(data)     # [4]
  statistics.stdev(data)         # 2.138...  (sample)
  statistics.pstdev(data)        # 2.0       (population)
  statistics.variance(data)      # 4.571...
  statistics.pvariance(data)     # 4.0
  statistics.harmonic_mean(data) # 4.32...
  statistics.geometric_mean(data)# 4.46...  (Python 3.8+)
  statistics.quantiles(data, n=4)# quartiles
  statistics.correlation(x, y)   # Python 3.10+
  statistics.linear_regression(x,y) # Python 3.10+

  # NormalDist (Python 3.8+)
  dist = statistics.NormalDist(mu=0, sigma=1)
  dist.pdf(0)          # 0.3989...
  dist.cdf(1.96)       # 0.975...
  dist.overlap(dist2)  # overlap area
```

---

## 36   SORTING & SEARCHING — Complete Guide

```
  PYTHON SORT ALGORITHM
  ──────────────────────────────────────────────────────────────────────
  # Timsort — O(n log n) worst case, O(n) best case (already sorted)
  # Stable — preserves relative order of equal elements

  # Sort list in place
  lst.sort()                       # ascending
  lst.sort(reverse=True)           # descending
  lst.sort(key=len)                # by length
  lst.sort(key=lambda x: x[1])     # by second element
  lst.sort(key=lambda x: (-x[1], x[0]))  # multi-key: score desc, name asc

  # sorted() — returns new list
  sorted(iterable)
  sorted(iterable, reverse=True)
  sorted(iterable, key=func)

  # Sort stability
  students.sort(key=lambda s: s.grade)
  students.sort(key=lambda s: s.name)   # stable: same grade stays grade-sorted

  KEY FUNCTIONS
  ──────────────────────────────────────────────────────────────────────
  import operator

  operator.itemgetter(1)           # get index 1
  operator.attrgetter("name")      # get .name attribute
  operator.methodcaller("lower")   # call .lower()

  sorted(lst, key=operator.itemgetter(1))
  sorted(objs, key=operator.attrgetter("name","age"))  # multi-attr

  # str.lower — case-insensitive
  sorted(words, key=str.lower)

  CUSTOM SORT (Comparator)
  ──────────────────────────────────────────────────────────────────────
  import functools

  # Python doesn't support compare function directly
  # Use cmp_to_key to convert compare function

  def compare(a, b):
      if a < b: return -1
      if a > b: return  1
      return 0

  sorted(lst, key=functools.cmp_to_key(compare))

  # Custom sort for LeetCode (e.g. largest number)
  def compare_nums(a, b):
      return int(a+b) - int(b+a)   # "9" "30" → "930" vs "309"

  nums = ["3","30","9"]
  sorted(nums, key=functools.cmp_to_key(compare_nums), reverse=True)
  # ["9","3","30"]

  BINARY SEARCH (bisect module)
  ──────────────────────────────────────────────────────────────────────
  import bisect

  # Requires sorted list
  arr = [1, 3, 5, 7, 9, 11]

  bisect.bisect_left(arr, 5)       # 2  (insert left of existing)
  bisect.bisect_right(arr, 5)      # 3  (insert right of existing)
  bisect.bisect(arr, 5)            # 3  (same as bisect_right)
  bisect.insort_left(arr, 6)       # insert and maintain sort
  bisect.insort(arr, 6)            # insert right

  # Check if element exists
  def binary_search(arr, target):
      i = bisect.bisect_left(arr, target)
      return i < len(arr) and arr[i] == target

  binary_search(arr, 5)  # True
  binary_search(arr, 4)  # False

  # Find insertion point = lower bound
  def lower_bound(arr, target):
      return bisect.bisect_left(arr, target)

  def upper_bound(arr, target):
      return bisect.bisect_right(arr, target)

  # Count occurrences in sorted array
  def count_range(arr, lo, hi):
      return bisect.bisect_right(arr, hi) - bisect.bisect_left(arr, lo)

  count_range([1,2,2,3,3,3,4], 2, 3)  # 5

  MANUAL BINARY SEARCH
  ──────────────────────────────────────────────────────────────────────
  def binary_search(arr, target):
      lo, hi = 0, len(arr) - 1
      while lo <= hi:
          mid = (lo + hi) // 2
          if arr[mid] == target:
              return mid
          elif arr[mid] < target:
              lo = mid + 1
          else:
              hi = mid - 1
      return -1

  # Find leftmost position (lower_bound)
  def lower_bound(arr, target):
      lo, hi = 0, len(arr)
      while lo < hi:
          mid = (lo + hi) // 2
          if arr[mid] < target:
              lo = mid + 1
          else:
              hi = mid
      return lo

  # Binary search on answer space
  def feasible(mid): ...  # predicate function

  lo, hi = 0, max_val
  while lo < hi:
      mid = (lo + hi) // 2
      if feasible(mid):
          hi = mid
      else:
          lo = mid + 1
  return lo
```

---

## 37   FUNCTIONAL PROGRAMMING

```
  PURE FUNCTIONS
  ──────────────────────────────────────────────────────────────────────
  # Pure: same input → same output, no side effects
  def add(a, b): return a + b          # pure

  # Impure: modifies external state
  total = 0
  def add_to_total(x): total += x     # impure (modifies global)

  IMMUTABILITY
  ──────────────────────────────────────────────────────────────────────
  # Prefer immutable data structures
  # tuple > list for fixed data
  # frozenset > set for fixed set
  # Use copy instead of mutation

  import copy
  original = [1,[2,3],[4,5]]
  shallow = original.copy()       # nested lists still shared
  deep = copy.deepcopy(original)  # completely independent

  FUNCTION COMPOSITION
  ──────────────────────────────────────────────────────────────────────
  def compose(*funcs):
      """Compose functions right to left: compose(f,g,h)(x) = f(g(h(x)))"""
      def composed(x):
          for f in reversed(funcs):
              x = f(x)
          return x
      return composed

  double = lambda x: x * 2
  add_one = lambda x: x + 1
  square = lambda x: x ** 2

  transform = compose(double, add_one, square)
  transform(3)   # double(add_one(square(3))) = double(add_one(9)) = double(10) = 20

  # Pipe (left to right)
  def pipe(*funcs):
      return compose(*reversed(funcs))

  CURRYING
  ──────────────────────────────────────────────────────────────────────
  def curry(func):
      """Automatic currying via functools.partial."""
      import functools
      def curried(*args, **kwargs):
          try:
              return func(*args, **kwargs)
          except TypeError:
              return functools.partial(curried, *args, **kwargs)
      return curried

  @curry
  def add(a, b, c):
      return a + b + c

  add(1,2,3)     # 6
  add(1)(2)(3)   # 6
  add_1 = add(1)
  add_1_2 = add_1(2)
  add_1_2(3)     # 6

  MONAD-LIKE PATTERNS
  ──────────────────────────────────────────────────────────────────────
  # Maybe/Option pattern
  class Maybe:
      def __init__(self, value):
          self._value = value

      @classmethod
      def just(cls, value):
          return cls(value)

      @classmethod
      def nothing(cls):
          return cls(None)

      def bind(self, func):
          if self._value is None:
              return Maybe.nothing()
          return Maybe.just(func(self._value))

      def get_or(self, default):
          return self._value if self._value is not None else default

  result = (Maybe.just({"user": {"name": "Alice"}})
            .bind(lambda d: d.get("user"))
            .bind(lambda u: u.get("name"))
            .bind(str.upper)
            .get_or("UNKNOWN"))
  # "ALICE"
```

---

## 38   TYPE HINTS & ANNOTATIONS

```
  BASIC ANNOTATIONS
  ──────────────────────────────────────────────────────────────────────
  from typing import Optional, Union, List, Dict, Tuple, Set
  from typing import Callable, Any, TypeVar, Generic
  from typing import Iterator, Generator, Iterable, Sequence

  # Python 3.9+ can use built-ins directly
  def greet(name: str, age: int = 0) -> str:
      return f"Hello {name}"

  def first(lst: list[int]) -> int:    # Python 3.9+
      return lst[0]

  def lookup(d: dict[str, int], key: str) -> int | None:  # Python 3.10+
      return d.get(key)

  OPTIONAL AND UNION
  ──────────────────────────────────────────────────────────────────────
  # Optional[X] = X | None
  def find(lst: list[int], target: int) -> Optional[int]:
      try: return lst.index(target)
      except ValueError: return None

  # Union (Python 3.10+ use X | Y syntax)
  def process(data: Union[str, bytes]) -> str:
      return data.decode() if isinstance(data, bytes) else data

  def process(data: str | bytes) -> str:    # Python 3.10+
      return data.decode() if isinstance(data, bytes) else data

  CALLABLE
  ──────────────────────────────────────────────────────────────────────
  from typing import Callable

  def apply(func: Callable[[int], int], x: int) -> int:
      return func(x)

  def make_adder(n: int) -> Callable[[int], int]:
      return lambda x: x + n

  TYPE VARIABLES (Generics)
  ──────────────────────────────────────────────────────────────────────
  from typing import TypeVar, Generic

  T = TypeVar("T")
  K = TypeVar("K")
  V = TypeVar("V")

  def first(lst: list[T]) -> T:
      return lst[0]

  class Stack(Generic[T]):
      def __init__(self) -> None:
          self._data: list[T] = []

      def push(self, item: T) -> None:
          self._data.append(item)

      def pop(self) -> T:
          return self._data.pop()

  s: Stack[int] = Stack()
  s.push(1)
  s.pop()      # int

  LITERAL AND FINAL
  ──────────────────────────────────────────────────────────────────────
  from typing import Literal, Final

  def set_direction(dir: Literal["N","S","E","W"]) -> None:
      ...

  MAX_SIZE: Final = 100     # cannot be reassigned

  TYPE ALIASES
  ──────────────────────────────────────────────────────────────────────
  # Python 3.12+
  type Point = tuple[float, float]
  type Matrix = list[list[float]]

  # Older way
  from typing import TypeAlias
  Point: TypeAlias = tuple[float, float]

  PROTOCOLS FOR STRUCTURAL TYPING
  ──────────────────────────────────────────────────────────────────────
  from typing import Protocol

  class Sortable(Protocol):
      def __lt__(self, other: "Sortable") -> bool: ...

  def sort_items(items: list[Sortable]) -> list[Sortable]:
      return sorted(items)

  ANNOTATIONS TRICKS
  ──────────────────────────────────────────────────────────────────────
  from __future__ import annotations   # forward references as strings (Python 3.7+)

  class Node:
      next: Node | None = None         # would fail without __future__ import

  # Get annotations at runtime
  def func(x: int) -> str: ...
  import typing
  typing.get_type_hints(func)   # {'x': <class 'int'>, 'return': <class 'str'>}
```

---

## 39   CONCURRENCY — Threading, Multiprocessing, asyncio

```
  GIL (Global Interpreter Lock)
  ──────────────────────────────────────────────────────────────────────
  # CPython has GIL: only one thread executes Python at a time
  # I/O-bound tasks → use threading (GIL released during I/O)
  # CPU-bound tasks → use multiprocessing (separate processes)
  # Python 3.13+ → free-threaded mode (no GIL, experimental)

  THREADING
  ──────────────────────────────────────────────────────────────────────
  import threading

  def worker(name, count):
      for i in range(count):
          print(f"{name}: {i}")
          import time; time.sleep(0.1)

  t1 = threading.Thread(target=worker, args=("A",3))
  t2 = threading.Thread(target=worker, args=("B",3))
  t1.start()
  t2.start()
  t1.join()   # wait for t1
  t2.join()

  # Daemon thread (dies when main thread dies)
  t = threading.Thread(target=worker, args=("C",100), daemon=True)
  t.start()

  # Thread with result
  class ResultThread(threading.Thread):
      def run(self):
          self.result = expensive_computation()

  t = ResultThread()
  t.start()
  t.join()
  print(t.result)

  # Lock (mutex)
  lock = threading.Lock()
  counter = 0

  def safe_increment():
      global counter
      with lock:                  # acquire/release automatically
          counter += 1

  # RLock (reentrant lock — same thread can acquire multiple times)
  rlock = threading.RLock()

  # Semaphore (limit concurrent access)
  semaphore = threading.Semaphore(3)  # max 3 threads

  def limited_access():
      with semaphore:
          do_work()

  # Event (signal between threads)
  ready = threading.Event()

  def producer():
      do_work()
      ready.set()

  def consumer():
      ready.wait()      # block until set
      use_result()

  # Condition
  cond = threading.Condition()

  # Queue (thread-safe)
  from queue import Queue
  q = Queue(maxsize=10)
  q.put(item)            # blocks if full
  q.get()                # blocks if empty
  q.task_done()          # signal item processed
  q.join()               # wait until all tasks done

  CONCURRENT.FUTURES (high-level)
  ──────────────────────────────────────────────────────────────────────
  from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

  # ThreadPool — I/O bound
  with ThreadPoolExecutor(max_workers=4) as executor:
      futures = [executor.submit(fetch_url, url) for url in urls]
      for future in as_completed(futures):
          result = future.result()

  # Map (simpler)
  with ThreadPoolExecutor(max_workers=4) as executor:
      results = list(executor.map(process, items))

  # ProcessPool — CPU bound
  with ProcessPoolExecutor(max_workers=4) as executor:
      results = list(executor.map(heavy_compute, range(100)))

  ASYNCIO (cooperative multitasking)
  ──────────────────────────────────────────────────────────────────────
  import asyncio

  async def fetch(url):
      async with aiohttp.ClientSession() as session:
          async with session.get(url) as response:
              return await response.text()

  async def main():
      urls = ["http://example.com", "http://python.org"]
      tasks = [asyncio.create_task(fetch(url)) for url in urls]
      results = await asyncio.gather(*tasks)
      return results

  asyncio.run(main())

  # async for
  async def count():
      async for i in async_generator():
          print(i)

  # async with
  async def use_resource():
      async with AsyncResource() as r:
          await r.do_stuff()

  # asyncio primitives
  lock = asyncio.Lock()
  event = asyncio.Event()
  queue = asyncio.Queue()
  semaphore = asyncio.Semaphore(3)

  async def limited():
      async with semaphore:
          await do_work()

  # Timeout
  async def with_timeout():
      try:
          result = await asyncio.wait_for(slow_coroutine(), timeout=5.0)
      except asyncio.TimeoutError:
          print("Timed out!")

  # asyncio.gather vs asyncio.wait
  # gather: run all, wait for all
  results = await asyncio.gather(*coros)

  # wait: more control, can wait for first, first exception, etc.
  done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
```

---

## 40   MEMORY MANAGEMENT & GC

```
  REFERENCE COUNTING
  ──────────────────────────────────────────────────────────────────────
  import sys

  x = [1,2,3]
  sys.getrefcount(x)    # ref count (always +1 for the call itself)

  # When ref count drops to 0 → object deallocated immediately
  x = None              # ref count drops, list might be freed

  CYCLIC GARBAGE COLLECTOR
  ──────────────────────────────────────────────────────────────────────
  import gc

  # Reference cycles aren't caught by ref counting
  # a = {}; a["self"] = a  → cycle!

  gc.collect()           # manually trigger GC
  gc.disable()           # disable GC (for performance)
  gc.enable()            # re-enable
  gc.isenabled()         # True/False
  gc.get_count()         # (gen0, gen1, gen2)  objects in each generation
  gc.get_threshold()     # (700, 10, 10)  thresholds
  gc.set_threshold(500, 5, 5)

  # Three generations
  # Gen 0: newly created objects (collected most often)
  # Gen 1: survived one gen 0 collection
  # Gen 2: long-lived objects (collected rarely)

  MEMORY PROFILING
  ──────────────────────────────────────────────────────────────────────
  # Object size
  import sys
  sys.getsizeof([1,2,3])    # 88 bytes (just the list, not contents)
  sys.getsizeof("hello")    # 54 bytes

  # Total size (recursive)
  def total_size(obj):
      seen = set()
      def size(o):
          oid = id(o)
          if oid in seen: return 0
          seen.add(oid)
          s = sys.getsizeof(o)
          if isinstance(o, dict):
              s += sum(size(k)+size(v) for k,v in o.items())
          elif hasattr(o, "__iter__") and not isinstance(o, (str,bytes)):
              s += sum(size(i) for i in o)
          return s
      return size(obj)

  # Memory-efficient patterns
  __slots__ = ["x","y"]         # no __dict__, saves ~50 bytes per instance

  # Generators vs lists
  sum(x**2 for x in range(1000000))  # O(1) memory
  sum([x**2 for x in range(1000000)])# O(n) memory

  WEAK REFERENCES
  ──────────────────────────────────────────────────────────────────────
  import weakref

  class Cache:
      def __init__(self):
          self._cache = weakref.WeakValueDictionary()  # values GC'd when no other refs

      def get(self, key):
          return self._cache.get(key)

      def set(self, key, value):
          self._cache[key] = value

  # WeakRef — doesn't prevent GC
  obj = SomeClass()
  ref = weakref.ref(obj)

  ref()      # returns obj if still alive
  del obj
  ref()      # returns None (obj was GC'd)
```

---

## 41   PYTHON INTERNALS

```
  EVERYTHING IS AN OBJECT
  ──────────────────────────────────────────────────────────────────────
  # Functions, classes, modules — all objects
  id(42)              # memory address
  id("hello")
  type(42)            # <class 'int'>
  type(int)           # <class 'type'>
  type(type)          # <class 'type'>  (type is its own metaclass!)

  # Classes are instances of metaclass 'type'
  class MyClass: pass
  type(MyClass)       # <class 'type'>

  BYTECODE
  ──────────────────────────────────────────────────────────────────────
  import dis, inspect

  def add(a, b):
      return a + b

  dis.dis(add)
  # 2  0 LOAD_FAST         0 (a)
  #    2 LOAD_FAST         1 (b)
  #    4 BINARY_ADD
  #    6 RETURN_VALUE

  code = add.__code__
  code.co_varnames    # ('a', 'b')
  code.co_consts      # (None,)
  code.co_filename
  code.co_firstlineno

  DECORATING WITHOUT FUNCTOOLS.WRAPS
  ──────────────────────────────────────────────────────────────────────
  # Without @wraps:
  def decorated(func):
      def wrapper(*a, **kw): return func(*a, **kw)
      return wrapper

  @decorated
  def my_func(): pass

  my_func.__name__      # "wrapper"  (wrong!)

  # With @wraps:
  from functools import wraps
  def decorated(func):
      @wraps(func)
      def wrapper(*a, **kw): return func(*a, **kw)
      return wrapper

  my_func.__name__      # "my_func"  (correct)

  ATTRIBUTE LOOKUP ORDER
  ──────────────────────────────────────────────────────────────────────
  # obj.attr lookup:
  # 1. Data descriptors in type(obj).__mro__
  # 2. obj.__dict__
  # 3. Non-data descriptors + other class attributes in mro
  # 4. __getattr__ (if defined)

  SLOTS VS DICT
  ──────────────────────────────────────────────────────────────────────
  # Without __slots__: each instance has __dict__
  class Normal:
      def __init__(self): self.x = 1

  # With __slots__: no __dict__, fixed attributes
  class Slotted:
      __slots__ = ("x",)
      def __init__(self): self.x = 1

  # Slotted uses ~40-50% less memory per instance
  # Attribute access slightly faster (no dict lookup)
```

---

## 42   TESTING — unittest, pytest

```
  UNITTEST
  ──────────────────────────────────────────────────────────────────────
  import unittest

  def add(a, b): return a + b
  def divide(a, b): return a / b

  class TestMath(unittest.TestCase):

      def setUp(self):              # runs before each test
          self.nums = [1, 2, 3, 4]

      def tearDown(self):           # runs after each test
          pass

      def test_add_positive(self):
          self.assertEqual(add(1, 2), 3)

      def test_add_negative(self):
          self.assertEqual(add(-1, -2), -3)

      def test_divide(self):
          self.assertAlmostEqual(divide(1, 3), 0.333, places=3)

      def test_divide_by_zero(self):
          with self.assertRaises(ZeroDivisionError):
              divide(1, 0)

      def test_types(self):
          self.assertIsInstance(add(1,2), int)
          self.assertIsNone(None)
          self.assertTrue(1 < 2)
          self.assertFalse(2 < 1)
          self.assertIn(1, self.nums)
          self.assertNotIn(5, self.nums)
          self.assertEqual(len(self.nums), 4)

  if __name__ == "__main__":
      unittest.main()

  PYTEST STYLE
  ──────────────────────────────────────────────────────────────────────
  # pip install pytest

  import pytest

  def test_add():
      assert add(1, 2) == 3

  def test_divide_by_zero():
      with pytest.raises(ZeroDivisionError):
          divide(1, 0)

  def test_approx():
      assert divide(1, 3) == pytest.approx(0.333, rel=1e-3)

  # Fixtures
  @pytest.fixture
  def sample_list():
      return [1, 2, 3, 4, 5]

  def test_sum(sample_list):
      assert sum(sample_list) == 15

  # Parametrize
  @pytest.mark.parametrize("a,b,expected", [
      (1, 2, 3),
      (-1, 1, 0),
      (0, 0, 0),
      (100, -50, 50),
  ])
  def test_add_many(a, b, expected):
      assert add(a, b) == expected

  # Skip / xfail
  @pytest.mark.skip(reason="not implemented yet")
  def test_future():
      pass

  @pytest.mark.xfail
  def test_known_bug():
      assert broken_function() == "works"

  # Run:
  # pytest                   all tests
  # pytest test_file.py      specific file
  # pytest -v                verbose
  # pytest -k "add"          only tests with "add" in name
  # pytest --tb=short        shorter tracebacks

  MOCKING
  ──────────────────────────────────────────────────────────────────────
  from unittest.mock import Mock, MagicMock, patch

  # Mock object
  m = Mock()
  m.method(1, 2)
  m.method.assert_called_once_with(1, 2)
  m.method.call_count        # 1

  # Patch — replace real function with mock
  @patch("module.expensive_function")
  def test_with_mock(mock_func):
      mock_func.return_value = 42
      result = code_that_calls_expensive()
      assert result == 42
      mock_func.assert_called_once()

  # Context manager style
  with patch("os.path.exists", return_value=True):
      assert file_exists()
```

---

## 43   COMMON STANDARD LIBRARY MODULES

```
  OS MODULE
  ──────────────────────────────────────────────────────────────────────
  import os

  os.getcwd()                         # current directory
  os.chdir("/path")                   # change directory
  os.listdir(".")                     # list directory
  os.mkdir("newdir")                  # create dir
  os.makedirs("a/b/c", exist_ok=True) # create nested
  os.remove("file.txt")               # delete file
  os.rmdir("emptydir")                # delete dir
  os.rename("old", "new")
  os.path.exists("file")
  os.path.isfile("file")
  os.path.isdir("dir")
  os.path.join("a", "b", "c.txt")     # "a/b/c.txt"
  os.path.split("a/b/c.txt")          # ("a/b", "c.txt")
  os.path.splitext("file.txt")        # ("file", ".txt")
  os.path.basename("a/b/c.txt")       # "c.txt"
  os.path.dirname("a/b/c.txt")        # "a/b"
  os.path.abspath("file.txt")         # absolute path
  os.walk(".")                        # recursive dir walk
  os.environ                          # environment variables dict
  os.environ.get("HOME")
  os.environ.get("PATH", "")

  SYS MODULE
  ──────────────────────────────────────────────────────────────────────
  import sys

  sys.argv                 # command line args list
  sys.path                 # module search paths
  sys.version              # Python version string
  sys.version_info         # (3, 12, 0, 'final', 0)
  sys.platform             # "linux", "darwin", "win32"
  sys.exit(0)              # exit with code
  sys.stdin                # standard input
  sys.stdout               # standard output
  sys.stderr               # standard error
  sys.getrefcount(obj)     # reference count
  sys.getsizeof(obj)       # bytes
  sys.setrecursionlimit(n)
  sys.getrecursionlimit()  # 1000 default

  SUBPROCESS
  ──────────────────────────────────────────────────────────────────────
  import subprocess

  # Run command
  result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
  result.stdout        # output string
  result.stderr        # error string
  result.returncode    # 0 = success

  # Shell command (security risk with user input!)
  subprocess.run("ls -la", shell=True)

  # Check for errors
  subprocess.run(["false"], check=True)   # raises CalledProcessError

  ARGPARSE
  ──────────────────────────────────────────────────────────────────────
  import argparse

  parser = argparse.ArgumentParser(description="My tool")
  parser.add_argument("filename", help="input file")
  parser.add_argument("-n","--count", type=int, default=10)
  parser.add_argument("-v","--verbose", action="store_true")
  parser.add_argument("--output", "-o", default="out.txt")

  args = parser.parse_args()
  args.filename   # positional
  args.count      # -n/--count
  args.verbose    # flag

  LOGGING
  ──────────────────────────────────────────────────────────────────────
  import logging

  logging.basicConfig(
      level=logging.DEBUG,
      format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
      datefmt="%Y-%m-%d %H:%M:%S",
  )

  logger = logging.getLogger(__name__)

  logger.debug("Debug info")      # lowest level
  logger.info("Info message")
  logger.warning("Warning!")
  logger.error("Error occurred")
  logger.critical("Critical!")
  logger.exception("With traceback", exc_info=True)

  # Log to file
  logging.basicConfig(filename="app.log", level=logging.INFO)

  # Structured logging
  logger.info("User login", extra={"user_id": 123, "ip": "1.2.3.4"})

  HASHLIB (cryptographic hashing)
  ──────────────────────────────────────────────────────────────────────
  import hashlib

  h = hashlib.sha256(b"hello world")
  h.hexdigest()    # "b94d27b9..."
  h.digest()       # bytes

  hashlib.md5(b"data").hexdigest()
  hashlib.sha512(b"data").hexdigest()

  # File hash
  def file_hash(path):
      h = hashlib.sha256()
      with open(path, "rb") as f:
          for chunk in iter(lambda: f.read(65536), b""):
              h.update(chunk)
      return h.hexdigest()
```

---

## 44   DSA PATTERNS IN PYTHON

```
  TWO POINTERS
  ──────────────────────────────────────────────────────────────────────
  # Two sum in sorted array
  def two_sum_sorted(arr, target):
      l, r = 0, len(arr) - 1
      while l < r:
          s = arr[l] + arr[r]
          if s == target: return [l, r]
          elif s < target: l += 1
          else: r -= 1
      return []

  SLIDING WINDOW
  ──────────────────────────────────────────────────────────────────────
  # Longest substring without repeating characters
  def length_of_longest_substring(s):
      char_idx = {}
      max_len = l = 0
      for r, c in enumerate(s):
          if c in char_idx and char_idx[c] >= l:
              l = char_idx[c] + 1
          char_idx[c] = r
          max_len = max(max_len, r - l + 1)
      return max_len

  # Maximum sum subarray of size k
  def max_sum_subarray(arr, k):
      window_sum = sum(arr[:k])
      max_sum = window_sum
      for i in range(k, len(arr)):
          window_sum += arr[i] - arr[i-k]
          max_sum = max(max_sum, window_sum)
      return max_sum

  FAST & SLOW POINTERS (Floyd's Cycle)
  ──────────────────────────────────────────────────────────────────────
  def has_cycle(head):
      slow = fast = head
      while fast and fast.next:
          slow = slow.next
          fast = fast.next.next
          if slow is fast:
              return True
      return False

  def find_cycle_start(head):
      slow = fast = head
      while fast and fast.next:
          slow = slow.next
          fast = fast.next.next
          if slow is fast:
              break
      slow = head
      while slow is not fast:
          slow = slow.next
          fast = fast.next
      return slow

  BFS TEMPLATE
  ──────────────────────────────────────────────────────────────────────
  from collections import deque

  def bfs(graph, start):
      visited = {start}
      queue = deque([start])
      while queue:
          node = queue.popleft()
          for neighbor in graph[node]:
              if neighbor not in visited:
                  visited.add(neighbor)
                  queue.append(neighbor)

  # BFS with levels
  def bfs_levels(graph, start):
      visited = {start}
      queue = deque([start])
      level = 0
      while queue:
          for _ in range(len(queue)):
              node = queue.popleft()
              process(node, level)
              for nb in graph[node]:
                  if nb not in visited:
                      visited.add(nb)
                      queue.append(nb)
          level += 1

  DFS TEMPLATES
  ──────────────────────────────────────────────────────────────────────
  def dfs_recursive(graph, node, visited=None):
      if visited is None: visited = set()
      visited.add(node)
      for neighbor in graph[node]:
          if neighbor not in visited:
              dfs_recursive(graph, neighbor, visited)

  def dfs_iterative(graph, start):
      visited = set()
      stack = [start]
      while stack:
          node = stack.pop()
          if node in visited: continue
          visited.add(node)
          for neighbor in graph[node]:
              if neighbor not in visited:
                  stack.append(neighbor)

  DYNAMIC PROGRAMMING
  ──────────────────────────────────────────────────────────────────────
  # Fibonacci — bottom up
  def fib(n):
      if n <= 1: return n
      dp = [0, 1]
      for i in range(2, n+1):
          dp.append(dp[-1] + dp[-2])
      return dp[n]

  # Space optimized
  def fib(n):
      a, b = 0, 1
      for _ in range(n):
          a, b = b, a + b
      return a

  # Longest common subsequence
  def lcs(s1, s2):
      m, n = len(s1), len(s2)
      dp = [[0]*(n+1) for _ in range(m+1)]
      for i in range(1, m+1):
          for j in range(1, n+1):
              if s1[i-1] == s2[j-1]:
                  dp[i][j] = dp[i-1][j-1] + 1
              else:
                  dp[i][j] = max(dp[i-1][j], dp[i][j-1])
      return dp[m][n]

  # 0/1 Knapsack
  def knapsack(weights, values, capacity):
      n = len(weights)
      dp = [[0]*(capacity+1) for _ in range(n+1)]
      for i in range(1, n+1):
          for w in range(capacity+1):
              dp[i][w] = dp[i-1][w]
              if weights[i-1] <= w:
                  dp[i][w] = max(dp[i][w], dp[i-1][w-weights[i-1]] + values[i-1])
      return dp[n][capacity]

  BACKTRACKING TEMPLATE
  ──────────────────────────────────────────────────────────────────────
  def backtrack(path, choices):
      if is_complete(path):
          result.append(path[:])
          return
      for choice in choices:
          if is_valid(choice, path):
              path.append(choice)
              backtrack(path, choices)
              path.pop()             # undo choice

  # Permutations
  def permutations(nums):
      result = []
      def bt(path, remaining):
          if not remaining:
              result.append(path[:])
              return
          for i, n in enumerate(remaining):
              path.append(n)
              bt(path, remaining[:i] + remaining[i+1:])
              path.pop()
      bt([], nums)
      return result

  # Subsets
  def subsets(nums):
      result = [[]]
      for n in nums:
          result += [s+[n] for s in result]
      return result

  HEAP / PRIORITY QUEUE PATTERNS
  ──────────────────────────────────────────────────────────────────────
  import heapq

  # Min heap
  heap = [3, 1, 4, 1, 5, 9]
  heapq.heapify(heap)
  heapq.heappush(heap, 2)
  heapq.heappop(heap)           # smallest
  heap[0]                       # peek smallest

  # Max heap (negate values)
  max_heap = [-x for x in [3,1,4,1,5]]
  heapq.heapify(max_heap)
  -heapq.heappop(max_heap)      # largest

  # K smallest elements
  heapq.nsmallest(3, lst)       # [1,1,2]
  heapq.nlargest(3, lst)        # [9,5,4]

  # K closest points to origin
  def k_closest(points, k):
      return heapq.nsmallest(k, points, key=lambda p: p[0]**2+p[1]**2)

  # Merge k sorted lists
  def merge_k_sorted(lists):
      heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
      heapq.heapify(heap)
      result = []
      while heap:
          val, li, idx = heapq.heappop(heap)
          result.append(val)
          if idx + 1 < len(lists[li]):
              heapq.heappush(heap, (lists[li][idx+1], li, idx+1))
      return result

  UNION-FIND (Disjoint Set)
  ──────────────────────────────────────────────────────────────────────
  class UnionFind:
      def __init__(self, n):
          self.parent = list(range(n))
          self.rank   = [0] * n
          self.count  = n

      def find(self, x):
          if self.parent[x] != x:
              self.parent[x] = self.find(self.parent[x])  # path compression
          return self.parent[x]

      def union(self, x, y):
          px, py = self.find(x), self.find(y)
          if px == py: return False
          if self.rank[px] < self.rank[py]: px, py = py, px
          self.parent[py] = px
          if self.rank[px] == self.rank[py]:
              self.rank[px] += 1
          self.count -= 1
          return True

      def connected(self, x, y):
          return self.find(x) == self.find(y)

  TRIE
  ──────────────────────────────────────────────────────────────────────
  class TrieNode:
      def __init__(self):
          self.children = {}
          self.is_end = False

  class Trie:
      def __init__(self):
          self.root = TrieNode()

      def insert(self, word):
          node = self.root
          for c in word:
              node = node.children.setdefault(c, TrieNode())
          node.is_end = True

      def search(self, word):
          node = self.root
          for c in word:
              if c not in node.children: return False
              node = node.children[c]
          return node.is_end

      def startsWith(self, prefix):
          node = self.root
          for c in prefix:
              if c not in node.children: return False
              node = node.children[c]
          return True

  SEGMENT TREE
  ──────────────────────────────────────────────────────────────────────
  class SegmentTree:
      def __init__(self, nums):
          self.n = len(nums)
          self.tree = [0] * (4 * self.n)
          self.build(nums, 0, 0, self.n - 1)

      def build(self, nums, node, start, end):
          if start == end:
              self.tree[node] = nums[start]
          else:
              mid = (start + end) // 2
              self.build(nums, 2*node+1, start, mid)
              self.build(nums, 2*node+2, mid+1, end)
              self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

      def query(self, node, start, end, l, r):
          if r < start or end < l: return 0
          if l <= start and end <= r: return self.tree[node]
          mid = (start + end) // 2
          return (self.query(2*node+1, start, mid, l, r) +
                  self.query(2*node+2, mid+1, end, l, r))

      def update(self, node, start, end, idx, val):
          if start == end:
              self.tree[node] = val
          else:
              mid = (start + end) // 2
              if idx <= mid: self.update(2*node+1, start, mid, idx, val)
              else:          self.update(2*node+2, mid+1, end, idx, val)
              self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]
```

---

## 45   PYTHON MASTER CHEATSHEET — QUICK REVISION

```
  DATA TYPE OPERATIONS
  ──────────────────────────────────────────────────────────────────────
  LIST             SET              DICT               TUPLE
  ───────────────  ───────────────  ─────────────────  ──────────────
  l.append(x)      s.add(x)         d[k]=v             (immutable)
  l.extend(it)     s.update(it)     d.update({})       t.count(x)
  l.insert(i,x)    s.remove(x)      d.get(k,def)       t.index(x)
  l.pop(i)         s.discard(x)     d.pop(k)
  l.remove(x)      s.pop()          d.popitem()
  l.index(x)       s|t  s&t         d.keys()
  l.count(x)       s-t  s^t         d.values()
  l.sort()         s<=t s>=t        d.items()
  l.reverse()      s.isdisjoint(t)  d.setdefault(k,v)
  l.copy()         s.copy()         d.copy()
  l.clear()        s.clear()        d.clear()
  l[i:j:k]         x in s  O(1)     k in d   O(1)

  COMPLEXITY REFERENCE
  ──────────────────────────────────────────────────────────────────────
  Operation          list     dict     set      heapq
  ──────────────────────────────────────────────────────────────────
  Access    [i]      O(1)      —        —         —
  Search    in       O(n)     O(1)     O(1)       —
  Insert end         O(1)*    O(1)     O(1)      O(log n)
  Insert mid         O(n)      —        —         —
  Delete end         O(1)      —        —         —
  Delete mid         O(n)     O(1)     O(1)       —
  Min/Max            O(n)      —        —        O(1) peek
  Sort               O(nlogn)  —        —         —

  COMMON ONE-LINERS
  ──────────────────────────────────────────────────────────────────────
  # Flatten
  flat = [x for row in matrix for x in row]
  import itertools; flat = list(itertools.chain.from_iterable(matrix))

  # Unique preserving order
  seen = set(); unique = [x for x in lst if not (x in seen or seen.add(x))]
  unique = list(dict.fromkeys(lst))

  # Transpose matrix
  T = list(map(list, zip(*matrix)))

  # Frequency count
  from collections import Counter; freq = Counter(lst)

  # Chunk list
  chunks = [lst[i:i+k] for i in range(0, len(lst), k)]

  # Running max
  running = list(itertools.accumulate(lst, max))

  # Rotate left by k
  rotated = lst[k:] + lst[:k]

  # Swap vars
  a, b = b, a

  # Check palindrome
  s == s[::-1]

  # Integer to list of digits
  digits = [int(d) for d in str(n)]

  # List of digits to integer
  num = int("".join(map(str, digits)))

  # All substrings
  subs = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]

  # Group consecutive
  import itertools
  groups = [list(g) for _,g in itertools.groupby([1,1,2,3,3,3,4])]
  # [[1,1],[2],[3,3,3],[4]]

  # Max by attribute
  max(people, key=lambda p: p.age)

  # Sort dict by value
  dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

  # Invert dict
  inv = {v: k for k, v in d.items()}

  # Zip two lists into dict
  d = dict(zip(keys, values))

  # Default dict pattern
  from collections import defaultdict
  groups = defaultdict(list)
  for k, v in pairs: groups[k].append(v)

  PYTHON TRICKS
  ──────────────────────────────────────────────────────────────────────
  # Walrus operator
  while chunk := f.read(8192): process(chunk)
  if m := re.match(pat, s): use(m.group())

  # Conditional import
  try: import ujson as json
  except ImportError: import json

  # Mutable default
  def f(lst=None): lst = lst or []

  # Safe dict access
  d.get("key", {}).get("nested", default)

  # Short-circuit default
  name = user_input or "Anonymous"

  # Ternary
  val = x if condition else y

  # Unpack ignore
  first, *_, last = [1,2,3,4,5]   # first=1, last=5

  # Starred in function call
  print(*[1,2,3], sep=", ")        # "1, 2, 3"

  # Dict merge (Python 3.9+)
  merged = {**d1, **d2}
  merged = d1 | d2

  # F-string debug (Python 3.8+)
  x = 42; print(f"{x=}")           # x=42

  INTERVIEW QUICK FACTS
  ──────────────────────────────────────────────────────────────────────
  ✅ Python list is dynamic array (not linked list)
  ✅ dict and set use hash tables internally
  ✅ list.sort() and sorted() use Timsort O(n log n) stable
  ✅ Python integers are arbitrary precision
  ✅ Strings are immutable Unicode sequences
  ✅ GIL means threading doesn't help CPU-bound tasks
  ✅ Generators are lazy — use for large data
  ✅ list comp is faster than for loop (C speed)
  ✅ set lookup is O(1) — use for membership tests
  ✅ dict keys must be hashable (immutable)
  ✅ tuple is hashable if all elements are hashable
  ✅ heapq implements min-heap — negate for max-heap
  ✅ collections.deque is O(1) for both ends
  ✅ functools.lru_cache is thread-safe
  ✅ deepcopy is needed for nested mutable structures
  ✅ == compares values; is compares identity
  ✅ None, 0, "", [], {}, set() are all falsy
  ✅ Exception hierarchy: BaseException → Exception
  ✅ with statement ensures cleanup via __exit__

  NUMBER SYSTEM CONVERSIONS
  ──────────────────────────────────────────────────────────────────────
  # int → other bases
  bin(42)         # "0b101010"
  oct(42)         # "0o52"
  hex(42)         # "0x2a"
  format(42,"b")  # "101010"  (no prefix)
  format(42,"o")  # "52"
  format(42,"x")  # "2a"
  format(42,"08b")# "00101010"

  # other bases → int
  int("101010", 2)     # 42
  int("52", 8)         # 42
  int("2a", 16)        # 42
  int("0b101010", 0)   # auto-detect base

  USEFUL RECIPES
  ──────────────────────────────────────────────────────────────────────
  # Power set
  from itertools import combinations
  def power_set(s):
      return [c for r in range(len(s)+1) for c in combinations(s, r)]

  # nth Fibonacci
  def fib(n, a=0, b=1):
      return a if n==0 else fib(n-1, b, a+b)

  # GCD / LCM
  from math import gcd
  lcm = lambda a,b: a*b//gcd(a,b)

  # Flatten arbitrarily nested
  def flatten(x):
      if isinstance(x, list): return [a for i in x for a in flatten(i)]
      return [x]

  # Binary search
  def bs(arr, target):
      lo, hi = 0, len(arr)-1
      while lo <= hi:
          mid = (lo+hi)//2
          if arr[mid]==target: return mid
          lo, hi = (mid+1, hi) if arr[mid]<target else (lo, mid-1)
      return -1

  # Two sum
  def two_sum(nums, target):
      seen = {}
      for i, n in enumerate(nums):
          if target-n in seen: return [seen[target-n], i]
          seen[n] = i

  # Valid parentheses
  def is_valid(s):
      stack, pairs = [], {")":"(","]":"[","}":"{"}
      for c in s:
          if c in "([{": stack.append(c)
          elif not stack or stack[-1] != pairs[c]: return False
          else: stack.pop()
      return not stack
```

---

<div align="center">

```
  ╔────────────────────────────────────────────────────────────────────╗
  │   "Simple is better than complex.                                  │
  │    Readability counts. — The Zen of Python"                        │
  ╚────────────────────────────────────────────────────────────────────╝
```

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white&labelColor=1e1e2e)
![Complete](https://img.shields.io/badge/Concepts-45+_Sections-a855f7?style=flat-square&labelColor=1e1e2e)
![DSA](https://img.shields.io/badge/DSA-Patterns_Included-FFA116?style=flat-square&labelColor=1e1e2e)
![Maintained](https://img.shields.io/badge/Maintained-Yes-22c55e?style=flat-square&labelColor=1e1e2e)

**Made with 💜 · Keep grinding 🔥 · Star ⭐ if this helped**

</div>
EOF
echo "Done — $(wc -l < /mnt/user-data/outputs/PYTHON_README.md) lines"
Output
