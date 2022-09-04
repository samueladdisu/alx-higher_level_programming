#!/usr/bin/python3
"""
Rectangle Class
"""
from .base import Base


class Rectangle(Base):

    """
    Rectangle Class
    """
    def __init__(self, width, height, x=0, y=0, id=None):

        """
        initialize new Rectangle objects
        Args:
            width: width of Rectangle
            height: height of Rectangle
            x: location of corner of Rectangle in x axis
            y: location of corner of Rectangle in y axis
            id: id of Rectangle object
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):

        """ Get width """
        return self.__width

    @width.setter
    def width(self, value):

        """ set width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Get height """
        return self.__height

    @height.setter
    def height(self, value):

        """ set height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):

        """ Get x """
        return self.__x

    @x.setter
    def x(self, value):

        """ Set x """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):

        """ Get y """
        return self.__y

    @y.setter
    def y(self, value):

        """ set y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):

        """ Get area of rectangle object """
        return self.__height * self.__width

    def display(self):

        """ print Rectangle """
        for i in range(self.y):
            print()
        for i in range(self.__height):
            print(" " * self.x, end="")
            print("#" * self.__width)

    def __str__(self):

        """ str representation of Rectangle object """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):

        """ update rectangle properties """
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):

        """ convert to dictionary representation"""
        ret = {}
        ret["id"] = self.id
        ret["width"] = self.width
        ret["height"] = self.height
        ret["x"] = self.x
        ret["y"] = self.y
        return ret
