#!/usr/bin/python3
""" Define Square Class"""


class Square:

    """ Square class"""
    def __init__(self, size=0):

        """ initialize new square object
        Args:
            size(int): size of new object
        """
        self.size = size

    @property
    def size(self):

        """ Get size of square"""
        return self.__size

    @size.setter
    def size(self, value):

        """ set size of square
        Args:
            value(int): value of new size
        """
        if not (isinstance(value, int) or isinstance(value, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):

        """ Calculate Area of Square"""
        return self.__size * self.__size

    def __lt__(self, other):

        """ Comapre less than
        Args:
            other(Square): other square object
        """
        return self.area() < other.area()

    def __le__(self, Other):

        """ Comapre less than or equal to
        Args:
            Other(Square): other square object
        """
        return self.area() <= Other.area()

    def __eq__(self, Other):

        """ Compare Equal to
        Args:
            Other(Square): other square object
        """
        return self.area() == Other.area()

    def __gt__(self, Other):

        """ Compare Greater than
        Args:
            Other(Square): other sqr object
        """
        return self.area() > Other.area()

    def __ge__(self, Other):

        """ compare Area
        Args:
            Other(Square): other square object
        """
        return self.area() >= Other.area()

    def __ne__(self, Other):

        """ Compare Not Equal to
        Args:
            Other(Square): Other sqr object
        """
        return self.area() != Other.area()
