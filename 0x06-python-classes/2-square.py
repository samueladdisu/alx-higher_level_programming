#!/usr/bin/python3
""" Define Square Class ."""


class Square:

    """ Represent Squre Class. """
    def __init__(self, size=0):

        """ initialize new Object
        Args:
            size(int): size of new square
        Raises:
            TypeError: if type of size is not integer
            ValueError: if value < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
