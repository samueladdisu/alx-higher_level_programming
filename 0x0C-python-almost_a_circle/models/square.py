#!/usr/bin/python3
"""
Square Class
"""
from models.rectangle import Rectangle


class Square(Rectangle):

    """ Square Class """

    def __init__(self, size, x=0, y=0, id=None):

        """ initialize new square objects """
        super().__init__(size, size, x, y, id)

    def __str__(self):

        """ str representation of square """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    @property
    def size(self):

        """ Get width """
        return self.width

    @size.setter
    def size(self, value):

        """ set width and height of square """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):

        """ update square objects """
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):

        """ convert square to dict representation """
        ret = {}
        ret["id"] = self.id
        ret["size"] = self.width
        ret["x"] = self.x
        ret["y"] = self.y
        return ret
