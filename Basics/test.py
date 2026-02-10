#!/usr/bin/env python3

def print_name(name) -> str:
    if not isinstance(name, str):
        print("not str")
        exit(0) 
    return f"Hello, {name}!"


print(print_name(10))