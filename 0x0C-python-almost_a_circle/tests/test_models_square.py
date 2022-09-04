#!/usr/bin/python3
"""
Test Rectangle Class
"""
from models.square import Square
import unittest
from os.path import exists
import os
import json


class TestSquare(unittest.TestCase):

    """ Test Rectangle """
    def setUp(self):

        """ initialize test fixture """
        self.rec = Square(2)

    def test_width(self):

        self.rec.width = 40
        self.assertEqual(self.rec.width, 40)
        with self.assertRaises(TypeError):
            self.rec.width = "hello"
        with self.assertRaises(ValueError):
            self.rec.width = -1

    def test_height(self):
        self.rec.height = 4
        self.assertEqual(self.rec.height, 4)
        with self.assertRaises(TypeError):
            self.rec.height = "Hello"
        with self.assertRaises(ValueError):
            self.rec.height = -1

    def test_x(self):
        self.rec.x = 4
        self.assertEqual(self.rec.x, 4)
        with self.assertRaises(TypeError):
            self.rec.x = "Hello"
        with self.assertRaises(ValueError):
            self.rec.x = -1

    def test_y(self):
        self.rec.y = 4
        self.assertEqual(self.rec.y, 4)
        with self.assertRaises(TypeError):
            self.rec.y = "hello"
        with self.assertRaises(ValueError):
            self.rec.y = -1

    def test_area(self):

        """ Test for Area output """
        self.rec.height = 20
        self.rec.width = 10
        self.assertEqual(self.rec.area(), 200)

    def test_sq_1(self):

        """ Test for 1 arg"""
        s = Square(1)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)

    def test_to_dictionary(self):

        """ Test for to dictionary """
        s = Square(4, 6, 8, 10)
        self.assertEqual(s.to_dictionary(), {"id": 10, "size": 4, "x": 6, "y": 8})

    def test_sq_2(self):

        """ Test for 2 args """
        s = Square(2, 4)
        self.assertEqual(s.width, 2)
        self.assertEqual(s.height, 2)
        self.assertEqual(s.x, 4)

    def test_sq_3(self):

        """ Test for 3 args """
        s = Square(4, 6, 8)
        self.assertEqual(s.width, 4)
        self.assertEqual(s.height, 4)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 8)

    def test_sq_4(self):

        """ Test for 4 args """
        s = Square(3, 5, 6, 9)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 6)
        self.assertEqual(s.id, 9)

    def test_str(self):

        """ test __str__ """
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.__str__(), "[Square] (4) 2/3 - 1")

    def test_update_0(self):

        """ test for update with No input """
        s = Square(4)
        s.update()
        self.assertEqual(s.width, 4)
        self.assertEqual(s.height, 4)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_update_empty_dic(self):

        """ test for empty dic """
        s = Square(30)
        s.update(**{})
        self.assertEqual(s.width, 30)
        self.assertEqual(s.height, 30)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_update_1(self):

        """ test for 1 arg """
        s = Square(1)
        s.update(34)
        self.assertEqual(s.id, 34)

    def test_update_2(self):

        """ Test for 2 args """
        s = Square(1)
        s.update(45, 55)
        self.assertEqual(s.id, 45)
        self.assertEqual(s.width, 55)
        self.assertEqual(s.height, 55)

    def test_update_3(self):

        """ Test for 3 args """
        s = Square(1)
        s.update(3, 4, 5)
        self.assertEqual(s.id, 3)
        self.assertEqual(s.width, 4)
        self.assertEqual(s.height, 4)
        self.assertEqual(s.x, 5)

    def test_update_4(self):

        """ Test for 4 args """
        s = Square(1)
        s.update(33, 44, 55, 66)
        self.assertEqual(s.id, 33)
        self.assertEqual(s.width, 44)
        self.assertEqual(s.height, 44)
        self.assertEqual(s.x, 55)
        self.assertEqual(s.y, 66)

    def test_create_1(self):

        """ test for 1 arg """
        s = Square.create(**{"id": 34})
        self.assertEqual(s.id, 34)

    def test_create_2(self):

        """ Test for 2 args """
        s = Square.create(**{"id": 45, "size": 55})
        self.assertEqual(s.id, 45)
        self.assertEqual(s.width, 55)
        self.assertEqual(s.height, 55)

    def test_create_3(self):

        """ Test for 3 args """
        s = Square.create(**{"id": 3, "size": 4, "x": 5})
        self.assertEqual(s.id, 3)
        self.assertEqual(s.width, 4)
        self.assertEqual(s.height, 4)
        self.assertEqual(s.x, 5)

    def test_create_4(self):

        """ Test for 4 args """
        s = Square.create(**{"id": 33, "size": 44, "x": 55, "y": 66})
        self.assertEqual(s.id, 33)
        self.assertEqual(s.width, 44)
        self.assertEqual(s.height, 44)
        self.assertEqual(s.x, 55)
        self.assertEqual(s.y, 66)

    def test_update_dict1(self):

        """ test for 1 arg """
        s = Square(1)
        s.update(**{"id": 34})
        self.assertEqual(s.id, 34)

    def test_update_d2(self):

        """ Test for 2 args """
        s = Square(1)
        s.update(**{"id": 45, "size": 55})
        self.assertEqual(s.id, 45)
        self.assertEqual(s.width, 55)
        self.assertEqual(s.height, 55)

    def test_update_d3(self):

        """ Test for 3 args """
        s = Square(1)
        s.update(**{"id": 3, "size": 4, "x": 5})
        self.assertEqual(s.id, 3)
        self.assertEqual(s.width, 4)
        self.assertEqual(s.height, 4)
        self.assertEqual(s.x, 5)

    def test_update_d4(self):

        """ Test for 4 args """
        s = Square(1)
        s.update(**{"id": 33, "size": 44, "x": 55, "y": 66})
        self.assertEqual(s.id, 33)
        self.assertEqual(s.width, 44)
        self.assertEqual(s.height, 44)
        self.assertEqual(s.x, 55)
        self.assertEqual(s.y, 66)

    def test_type_width(self):

        """ Test for type check of width """
        with self.assertRaises(TypeError):
            Square("1")

    def test_type_x(self):

        """ Test for type check -x """
        with self.assertRaises(TypeError):
            Square(1, "3")

    def test_type_y(self):

        """ Test type check -y """
        with self.assertRaises(TypeError):
            Square(1, 2, "1")

    def test_value_width(self):

        """ Test value check -size """
        with self.assertRaises(ValueError):
            Square(-1)

    def test_value_width_0(self):

        """ Test value 0 of width """
        with self.assertRaises(ValueError):
            Square(0)

    def test_value_x(self):

        """ Test for value check x """
        with self.assertRaises(ValueError):
            Square(1, -1)

    def test_value_y(self):

        """ test value check -y """
        with self.assertRaises(ValueError):
            Square(1, 2, -1)

    def test_save_to_file(self):

        """ Test for save to file """
        R = Square(2)
        R.save_to_file(None)
        self.assertTrue(exists("Square.json"))
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

    def test_save_to_file_empty(self):

        """ Test for save file """
        R = Square(2, 2)
        R.save_to_file([])
        self.assertTrue(exists("Square.json"))
        with open("Square.json") as f:
            self.assertEqual("[]", f.read())
        os.remove("Square.json")

    def test_save_to_file_list(self):

        """ Test for normal list """
        R = Square(2, 2)
        R.save_to_file([R])
        self.assertTrue(exists("Square.json"))
        with open("Square.json") as f:
            self.assertEqual(json.dumps([R.to_dictionary()]),
                             f.read())
        os.remove("Square.json")

    def test_load_from_no_file(self):

        """ Test for No file """
        R = Square(2, 2)
        self.assertEqual(R.load_from_file(), [])

    def test_load_from_file(self):

        """ Test load from file no file """
        R = Square(2, 2)
        R.save_to_file([R])
        with open("Square.json") as f:
            self.assertEqual(f.read(), json.dumps([R.to_dictionary()]))
        os.remove("Square.json")
