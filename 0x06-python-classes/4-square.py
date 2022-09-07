#!/usr/bin/python3
""" Define Square Class"""


class Square:

    """ Blue print for Squre Objects """
    def __init__(self, size=0):

        """ initialize new Objects
        Args:
            size(int): size of new square object
        """
        self.size = size

    @property
    def size(self):

        """ Get size of Square"""
        return self.__size

    @size.setter
    def size(self, value):

        """ set size of square
        Args:
            size(int): new size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        """ Calculate Area of Square"""
        return self.__size * self.__size
