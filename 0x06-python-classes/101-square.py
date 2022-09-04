#!/usr/bin/python3
""" Define Class Square"""


class Square:

    """ Blue print for square objects"""
    def __init__(self, size=0, position=(0, 0)):

        """ initialize square Object
        Args:
            size(int): new size
            position(tuple): new position
        """
        self.size = size
        self.position = position

    @property
    def size(self):

        """ Get size of Object"""
        return self.__size

    @size.setter
    def size(self, value):

        """ set size of square object
        Args:
            size(int): new size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):

        """ Get Position"""
        return self.__position

    @position.setter
    def position(self, value):

        """ set position
        Args:
            value(tuple): new position
        """
        if not isinstance(value, tuple)\
                or len(value) != 2\
                or any(not isinstance(i, int) for i in value)\
                or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):

        """ Get Area of square"""
        return self.__size * self.__size

    def my_print(self):

        """ print square"""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for k in range(self.__position[0])]
            [print("#", end="") for j in range(self.__size)]
            print("")

    def __str__(self):

        """ str representation of object as my print"""
        if self.__size != 0:
            [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for k in range(self.__position[0])]
            [print("#", end="") for j in range(self.__size)]
            if i != self.__size - 1:
                print("")
        return ""
