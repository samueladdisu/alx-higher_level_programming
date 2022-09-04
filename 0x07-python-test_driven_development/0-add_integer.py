#!/usr/bin/python3
"""
0-add_integer Mudule
"""


def add_integer(a, b=98):

    """
    Add two Numbers -> float and or  integer

    Args:
        a(int or float): first Number
        b(int or float): second Number
    Raises:
        TypeError: if a or b is not integer or float data type
    Returns:
        int: sum of Two numbers casted each to integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
