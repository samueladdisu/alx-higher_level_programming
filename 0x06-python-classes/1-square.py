#!/usr/bin/python3
""" Create Class Square that defines a square private
    instance attribute size
"""


class Square:
    """ Define square in private
    """
    def __init__(self, size):
        """
        Instantiation with size
        Args:
        size: size of the square
        """
        self.__size = size
