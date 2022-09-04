#!/usr/bin/python3
"""
print Square Module Doc
"""


def print_square(size):

    """ print square with symbol #
    Args:
        size(int): size of square
    Raises:
        TypeError: if type(size) is not int
        ValueError: if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
