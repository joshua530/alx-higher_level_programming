#!/usr/bin/python3

"""
Contains definition for print_square
"""


def print_square(size):
    """
    Prints out a square

    Args:
        size: the size of the square's sides

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero
    """
    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
