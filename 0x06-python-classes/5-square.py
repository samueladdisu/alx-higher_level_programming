#!/usr/bin/python3
""" Define Square Class"""


class Square:

    """ Blue print for square Objects"""
    def __init__(self, size=0):

        """ initialize new Objects

        Args:
            size(int): size of new object
        """
        self.size = size

    @property
    def size(self):

        """ Get size of object"""
        return self.__size

    @size.setter
    def size(self, value):

        """ set size of object

        Args:
            size(int): new size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):

        """ Get area of object"""
        return self.__size * self.__size

    def my_print(self):

        """ print square of size with # symbol"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
