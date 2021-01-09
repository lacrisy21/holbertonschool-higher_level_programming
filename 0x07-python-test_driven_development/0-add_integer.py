#!/usr/bin/python3
"""
This is the module for
    add_integer
"""


def add_integer(a, b):
    """
        add_integer' that add two number
    """
    if isinstance(a, int) or isinstance(a, float):
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, int) or isinstance(b, float):
        b = int(b)
    else:
        raise TypeError("b must be an integer")
    return a + b
