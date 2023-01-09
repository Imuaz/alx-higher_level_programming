#!/usr/bin/python3
"""
The print_square module provides a simple function print_square()
which prints a square with # character.
"""


def print_square(size):
    """Prints square with #.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
