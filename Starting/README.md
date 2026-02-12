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
