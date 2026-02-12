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
