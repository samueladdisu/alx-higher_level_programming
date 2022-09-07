#!/usr/bin/python3
"""
Base Class
"""
import json


class Base:

    """
    Base Class
    """
    __nb_objects = 0

    def __init__(self, id=None):

        """
        Initialize new objects
        Args:
            id : id of  new objects
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):

        """ convert to json string """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        ret = []
        for o in list_dictionaries:
            if type(o) == dict:
                ret.append(o)
            elif isinstance(o, Base):
                ret.append(o.to_dictionary())
            else:
                pass
        return json.dumps(ret)

    @classmethod
    def save_to_file(cls, list_objs):

        """ save json str to file """
        filename = cls.__name__+".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(Base.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):

        """ get objects from json """
        import json
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):

        """ Create new objects """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):

        """ Load from file """
        filename = cls.__name__ + ".json"
        try:
            f = open(filename)
        except FileNotFoundError:
            return []
        else:
            obj = Base.from_json_string(f.read())
            ret = [cls.create(**d) for d in obj]
            return ret

    @classmethod
    def save_to_file_csv(cls, list_objs):

        """ Save to Csv file """
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if cls.__name__ == "Rectangle":
                for r in list_objs:
                    f.write(str(r.id) + ","
                            + str(r.width) + ","
                            + str(r.height) + ","
                            + str(r.x) + ","
                            + str(r.y))
                    f.write("\n")
            if cls.__name__ == "Square":
                for r in list_objs:
                    f.write(str(r.id) + ","
                            + str(r.size) + ","
                            + str(r.x) + ","
                            + str(r.y))
                    f.write("\n")

    @classmethod
    def load_from_file_csv(cls):

        """ Load from csv file """
        filename = cls.__name__ + ".csv"
        objs = []
        with open(filename) as f:
            dic = {}
            if cls.__name__ == "Rectangle":
                for line in f.readlines():
                    L = line.split(",")
                    dic["id"] = int(L[0])
                    dic["width"] = int(L[1])
                    dic["height"] = int(L[2])
                    dic["x"] = int(L[3])
                    dic["y"] = int(L[4])
                    objs.append(cls.create(**dic))
            if cls.__name__ == "Square":
                for line in f.readlines():
                    L = line.split(",")
                    dic["id"] = int(L[0])
                    dic["size"] = int(L[1])
                    dic["x"] = int(L[2])
                    dic["y"] = int(L[3])
                    objs.append(cls.create(**dic))
            return objs
