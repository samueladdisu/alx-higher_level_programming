#!/usr/bin/python3
"""
Test Rectangle Class
"""
from models.rectangle import Rectangle
import unittest
from os.path import exists
import json
import os
from io import StringIO


class TestRectangle(unittest.TestCase):

    """ Test Rectangle """
    def setUp(self):

        """ initialize test fixture """
        self.rec = Rectangle(2, 2)

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

    def test_rect_two_args(self):

        """ test for 2 args """
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_rect_three_args(self):

        """ Test for three args """
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 0)

    def test_rect_four_args(self):

        """ test for 4 args """
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_for_invalid_width(self):

        """ test for invalid input """
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_for_invalid_height(self):

        """ test for invalid height """
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_invalid_x(self):

        """ test for invalid x"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_invalid_y(self):

        """ Test for invalid y """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_for_all_args(self):

        """ test for all args supplied """
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_for_value_width(self):

        """ test for Valueof Width """
        with self.assertRaises(ValueError):
            Rectangle(-1, 3)

    def test_Value_height(self):

        """ Test for Value of height"""
        with self.assertRaises(ValueError):
            Rectangle(1, -1)

    def test_for_value_x(self):

        """ test for proper value of x """
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1)

    def test_for_value_y(self):

        """ test for value of y"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -1)

    def test_for_width_0(self):

        """ Test for width = 0 """
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_for_heigh_0(self):

        """ Test for height = 0"""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_for_str(self):

        """ test for __str__ """
        R = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", R.__str__())

    def test_to_dictionary(self):

        """ test for to_dictionary function """
        R = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual({"id": 5, "width": 1, "height": 2, "x": 3, "y": 4},
                         R.to_dictionary())

    def test_update(self):

        """ Test for update """
        R = Rectangle(1, 1)
        R.update(2, 2, 2, 2, 2)
        self.assertEqual({"id": 2, "width": 2, "height": 2, "x": 2, "y": 2},
                         R.to_dictionary())

    def test_update_0(self):

        """ test for update with None """
        R = Rectangle(2, 2)
        R.update()
        self.assertEqual(R.width, 2)
        self.assertEqual(R.height, 2)

    def test_update_empty_dic(self):

        """ test for empty dict update """
        R = Rectangle(4, 6)
        R.update(**{})
        self.assertEqual(R.width, 4)
        self.assertEqual(R.height, 6)

    def test_update_1(self):

        """ test for 1 arg """
        R = Rectangle(2, 2)
        R.update(98)
        self.assertEqual(R.id, 98)

    def test_update_2(self):

        """ test for 2 args """
        R = Rectangle(2, 2)
        R.update(44, 88)
        self.assertEqual(R.id, 44)
        self.assertEqual(R.width, 88)

    def test_update_3(self):

        """ Test for 3 args """
        R = Rectangle(2, 2)
        R.update(55, 66, 77)
        self.assertEqual(R.id, 55)
        self.assertEqual(R.width, 66)
        self.assertEqual(R.height, 77)

    def test_update_4(self):

        """ Test for 4 args """
        R = Rectangle(2, 2)
        R.update(88, 99, 101, 202)
        self.assertEqual(R.id, 88)
        self.assertEqual(R.width, 99)
        self.assertEqual(R.height, 101)
        self.assertEqual(R.x, 202)

    def test_update_5(self):

        """ Test for 5 args """
        R = Rectangle(2, 2)
        R.update(11, 22, 33, 44, 55)
        self.assertEqual(R.id, 11)
        self.assertEqual(R.width, 22)
        self.assertEqual(R.height, 33)
        self.assertEqual(R.x, 44)
        self.assertEqual(R.y, 55)

    def test_update_kwargs_0(self):

        """ Test for update with kwargs """
        R = Rectangle(2, 2)
        R.update(**{"id": 34})
        self.assertEqual(R.id, 34)

    def test_update_kwargs_1(self):

        """ Test for update with kwargs """
        R = Rectangle(2, 2)
        R.update(**{"id": 34, "width": 45})
        self.assertEqual(R.id, 34)
        self.assertEqual(R.width, 45)

    def test_update_kwargs_3(self):

        """ Test for update with kwargs """
        R = Rectangle(2, 2)
        R.update(**{"id": 34, "width": 45, "height": 56})
        self.assertEqual(R.id, 34)
        self.assertEqual(R.width, 45)
        self.assertEqual(R.height, 56)

    def test_update_kwargs_4(self):

        """ Test for update with kwargs """
        R = Rectangle(2, 2)
        R.update(**{"id": 34, "width": 45, "height": 56, "x": 22})
        self.assertEqual(R.id, 34)
        self.assertEqual(R.width, 45)
        self.assertEqual(R.height, 56)
        self.assertEqual(R.x, 22)

    def test_update_kwargs_5(self):

        """ Test for update with kwargs """
        R = Rectangle(2, 2)
        R.update(**{"id": 34, "width": 45, "height": 56, "x": 22, "y": 5})
        self.assertEqual(R.id, 34)
        self.assertEqual(R.width, 45)
        self.assertEqual(R.height, 56)
        self.assertEqual(R.x, 22)
        self.assertEqual(R.y, 5)

    def test_create_kwargs_1(self):

        """ Test for update with kwargs """
        R = Rectangle(2, 2)
        R.update(**{"id": 34})
        self.assertEqual(R.id, 34)

    def test_create_kwargs_2(self):

        """ Test for update with kwargs """
        R = Rectangle(2, 2)
        R.update(**{"id": 34, "width": 45})
        self.assertEqual(R.id, 34)
        self.assertEqual(R.width, 45)

    def test_create_kwargs_3(self):

        """ Test for update with kwargs """
        R = Rectangle(2, 2)
        R.update(**{"id": 34, "width": 45, "height": 56})
        self.assertEqual(R.id, 34)
        self.assertEqual(R.width, 45)
        self.assertEqual(R.height, 56)

    def test_create_kwargs_4(self):

        """ Test for update with kwargs """
        R = Rectangle(2, 2)
        R.update(**{"id": 34, "width": 45, "height": 56, "x": 22})
        self.assertEqual(R.id, 34)
        self.assertEqual(R.width, 45)
        self.assertEqual(R.height, 56)
        self.assertEqual(R.x, 22)

    def test_create_kwargs_5(self):

        """ Test for update with kwargs """
        R = Rectangle(2, 2)
        R.update(**{"id": 34, "width": 45, "height": 56, "x": 22, "y": 5})
        self.assertEqual(R.id, 34)
        self.assertEqual(R.width, 45)
        self.assertEqual(R.height, 56)
        self.assertEqual(R.x, 22)
        self.assertEqual(R.y, 5)

    def test_save_to_file(self):

        """ Test for save to file """
        R = Rectangle(2, 2)
        R.save_to_file(None)
        self.assertTrue(exists("Rectangle.json"))
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_empty(self):

        """ Test for save file """
        R = Rectangle(2, 2)
        R.save_to_file([])
        self.assertTrue(exists("Rectangle.json"))
        with open("Rectangle.json") as f:
            self.assertEqual("[]", f.read())
        os.remove("Rectangle.json")

    def test_save_to_file_list(self):

        """ Test for normal list """
        R = Rectangle(2, 2)
        R.save_to_file([R])
        self.assertTrue(exists("Rectangle.json"))
        with open("Rectangle.json") as f:
            self.assertEqual(json.dumps([R.to_dictionary()]),
                             f.read())
        os.remove("Rectangle.json")

    def test_load_from_no_file(self):

        """ Test for No file """
        R = Rectangle(2, 2)
        self.assertEqual(R.load_from_file(), [])

    def test_load_from_file(self):

        """ Test load from file no file """
        R = Rectangle(2, 2)
        R.save_to_file([R])
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), json.dumps([R.to_dictionary()]))
        os.remove("Rectangle.json")

    def test_display(self):

        """ test for display """
        R = Rectangle(2, 2)
        import sys
        old_std = sys.stdout
        new_std = StringIO()
        sys.stdout = new_std
        R.display()
        sys.stdout = old_std
        self.assertEqual(new_std.getvalue(), "##\n##\n")

    def test_display_with_xy(self):

        """ Test with x y  ! = 0 """
        R = Rectangle(2, 2, 2, 2)
        import sys
        old_std = sys.stdout
        new_std = StringIO()
        sys.stdout = new_std
        R.display()
        sys.stdout = old_std
        self.assertEqual(new_std.getvalue(), "\n\n  ##\n  ##\n")
