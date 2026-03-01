# Python - Starting

``` bash    
Summary: Today, you will learn the basics of the Python programming language.
Version: 1.3
```
Summary: Introductory Python exercises (`ex00` to `ex09`).

## Exercises Overview

| Exercise | File(s) | Topic |
|---|---|---|
| `ex00` | `Hello.py` | Basic Python containers and mutations |
| `ex01` | `format_ft_time.py` | Time formatting and scientific notation |
| `ex02` | `find_ft_type.py` | Detect object types |
| `ex03` | `NULL_not_found.py` | Null-like values and type handling |
| `ex04` | `whatis.py` | CLI arguments, integer parsing, odd/even |
| `ex05` | `building.py` | Character statistics in text |
| `ex06` | `ft_filter.py`, `filterstring.py` | Re-implement `filter`, filter words by length |
| `ex07` | `sos.py` | Encode text into Morse code |
| `ex08` | `Loading.py`, `tester.py` | Custom progress bar (`ft_tqdm`) |
| `ex09` | `ft_package/`, `pyproject.toml` | Build a simple installable package |

---

## ex00 to ex03 

``` bash 

# List - mutable, ordered, duplicates OK
my_list = [1, 2, 2, 3]
my_list[0] = 10  # ✅ Can modify

# Tuple - immutable, ordered, duplicates OK
my_tuple = (1, 2, 2, 3)
# my_tuple[0] = 10  # ❌ Error! Can't modify

# Set - mutable, unordered, NO duplicates
my_set = {1, 2, 2, 3}  # Becomes {1, 2, 3}
my_set.add(4)  # ✅ Can add

# Dictionary - mutable, ordered, key-value pairs
my_dict = {"name": "Ali", "age": 25}
my_dict["age"] = 26  # ✅ Can modify


```

## Comparison Table

| Feature | List | Tuple | Set | Dictionary |
|---------|------|-------|-----|------------|
| **Syntax** | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` | `{"a": 1, "b": 2}` |
| **Mutable** | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| **Ordered** | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes (Python 3.7+) |
| **Duplicates** | ✅ Allowed | ✅ Allowed | ❌ Not allowed | ❌ Keys must be unique |
| **Indexed** | ✅ `list[0]` | ✅ `tuple[0]` | ❌ No | ✅ `dict["key"]` |
| **Use Case** | General collection | Immutable data | Unique items | Key-value pairs |
| **Speed** | Medium | Fast (read) | Fast (lookup) | Fast (lookup) |

## Type Checking in Python

### Using type()
```python
# Check the type of any object
my_list = [1, 2, 3]
print(type(my_list))        # <class 'list'>

my_tuple = (1, 2, 3)
print(type(my_tuple))       # <class 'tuple'>

my_string = "hello"
print(type(my_string))      # <class 'str'>

my_dict = {"a": 1}
print(type(my_dict))        # <class 'dict'>
```

### Using isinstance()
```python
# isinstance(object, classinfo) -> bool

# Check single type
x = [1, 2, 3]
isinstance(x, list)         # True
isinstance(x, tuple)        # False

# Check multiple types
x = 42
isinstance(x, (int, float)) # True
```

### isinstance() vs type()
```python
my_list = [1, 2, 3]

# Method 1: type() - exact type match
if type(my_list) == list:
    print("It's a list!")

# Method 2: isinstance() - better (works with inheritance)
if isinstance(my_list, list):
    print("It's a list!")
```

**Tip:** Use `isinstance()` - it's more flexible and Pythonic! 🐍

## Understanding `__name__` in Python

### What is `__name__`?
`__name__` is a special built-in variable that tells you how the file is being used.

```python
# When you RUN the file directly:
# python script.py
# __name__ = "__main__"

# When you IMPORT the file:
# import script
# __name__ = "script" (the module name)
```

### Simple Example

**File: helper.py**
```python
print("My name is:", __name__)

if __name__ == "__main__":
    print("I'm the MAIN character! (running directly)")
else:
    print("I'm a supporting character (being imported)")
```

**Scenario 1: Run directly**
```bash
$ python helper.py
My name is: __main__
I'm the MAIN character! (running directly)
```

**Scenario 2: Import from another file**
```python
# In main.py
import helper

# Output:
# My name is: helper
# I'm a supporting character (being imported)
```

### Practical Use Case

```python
# helper.py
def add(a, b):
    return a + b

# Test code - only runs when testing this file directly
if __name__ == "__main__":
    print(add(2, 3))  # Only runs when: python helper.py
    # Won't run when: import helper
```

### Why Use It?

```python
import sys

# This code ALWAYS runs
print("This always runs")

# This code ONLY runs when executed directly
if __name__ == "__main__":
    print("This only runs when: python script.py")
```

**Summary:** `if __name__ == "__main__":` means "only run this code if the file is executed directly, not when imported" 🐍


These cover Python fundamentals:
- containers (`list`, `tuple`, `set`, `dict`)
- formatting values and dates
- checking types
- handling special/null-like values

---

## ex04 - whatis

**Goal:** Read one CLI argument, validate it as an integer, and print whether it is odd or even.

Run:

```bash
cd ex04
python whatis.py 42
python whatis.py 17
python whatis.py hello
```

---

## ex05 - building

**Goal:** Count characters in a text:
- upper letters
- lower letters
- punctuation marks
- spaces
- digits

Run:

```bash
cd ex05
python building.py "Hello World! 42"
```

Or interactive input (no argument):

```bash
python building.py
```

---

## ex06 - filterstring / ft_filter

**Goal:**
- create your own `ft_filter` generator in `ft_filter.py`
- filter words longer than `N` from a sentence in `filterstring.py`

Run:

```bash
cd ex06
python filterstring.py "Hello this is a simple test" 4
```

Expected behavior: prints words whose length is strictly greater than the given number.

---

## ex07 - sos

**Goal:** Convert input text to Morse code.

Supported characters:
- letters `A-Z` (case-insensitive)
- digits `0-9`
- spaces

Run:

```bash
cd ex07
python sos.py "sos 42"
```

If invalid characters are provided, the script prints:

```text
AssertionError: the arguments are bad
```

---

## ex08 - Loading / tester

**Goal:** Recreate a tqdm-like progress bar with `ft_tqdm`.

Files:
- `Loading.py`: custom generator with progress display
- `tester.py`: compares `ft_tqdm` output with `tqdm`

Run:

```bash
cd ex08
python tester.py
```

Install dependency if needed:

```bash
pip install tqdm
```

---

## ex09 - ft_package

**Goal:** Build a minimal Python package and use it.

Main function:

```python
count_in_list(lst: list, str) -> int
```

Run local test:

```bash
cd ex09
python test.py
```

Install package locally:

```bash
pip install .
```

Build distribution:

```bash
python -m build
```

---

## Notes

- Use one folder per exercise.
- Keep scripts runnable directly with Python.
- Follow exercise constraints for argument validation and error messages.
