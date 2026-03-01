# ex09 - ft_package

Small Python package exercise for creating and using a local package named `ft_package`.

## Contents

- `ft_package/count_in_list.py`: function implementation
- `ft_package/__init__.py`: package export
- `pyproject.toml`: package metadata and build configuration
- `test.py`: quick usage test

## Function

```python
count_in_list(lst: list, str) -> int
```

Returns how many times the given string appears in the list.

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
print(count_in_list(["toto", "tata", "toto"], "tutu"))
```

Expected output:

```text
2
0
```

## Install locally

From the `ex09` directory:

```bash
pip install .
```


This is why when you do : 

```bash
pip install build
```
```bash
python -m build
```
you get:

```bash

dist/ft_package-0.0.1.tar.gz
dist/ft_package-0.0.1-py3-none-any.whl
```
```bash
pip 
```
does this automatically when installing from 
```bash
.
```

Then run:

```bash
python test.py
```

## Build package

```bash
python -m build
```

This creates distribution files in a `dist/` folder.
