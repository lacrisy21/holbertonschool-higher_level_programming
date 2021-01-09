#!/usr/bin/python3
"""
This is the module for
    print square
"""


def print_square(size):
    """
       print_square
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    i = 0
    j = 0
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
