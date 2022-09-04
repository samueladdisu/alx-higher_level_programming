#!/usr/bin/python3
""" Define Square Class ."""


class Square:

    """ Represent Square Class. """
    def __init__(self, size=0):

        """ initialize new Object Creation
        Args:
            size(int): size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):

        """ claculate area of square object"""
        return self.__size * self.__size
