#!/usr/bin/python3

"""
Unittest for max_integer
"""
import unittest
max_int = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """
    Class for testing max_integer function
    """

    def test_empty(self):

        """
        Test for empty list
        """
        self.assertEqual(max_int([]), None)

    def test_string(self):

        """ test for string input"""
        s = "Getacher"
        self.assertEqual(max_int(s), 't')

    def test_max_start(self):

        """ Test max at start"""
        ls = [6, 3, 5, 1, 0]
        self.assertEqual(max_int(ls), 6)

    def test_orderd_list(self):

        """ test for orderd list"""
        ls = [3, 5, 7, 12, 59]
        self.assertEqual(max_int(ls), 59)

    def test_unorderd_list(self):

        """ test for unordered list"""
        ls = [3, 7, 132, 3, 12, 452, 23, -4]
        self.assertEqual(max_int(ls), 452)

    def test_for_float_and_int(self):

        """ test for mix of float and int"""
        ls = [4, 6.9, 24.5, -56.3, 67.6]
        self.assertEqual(max_int(ls), 67.6)

    def test_for_all_negative(self):

        """ test for all negativ input"""
        ls = [-4, -5.8, -5, -44, -3.8]
        self.assertEqual(max_int(ls), -3.8)

    def test_for_string_array(self):

        """ test for string array"""
        ls = ["abc", "def", "lkj", "ijk"]
        self.assertEqual(max_int(ls), "lkj")

    def test_for_one_negative(self):

        """ test for one negative"""
        ls = [4, 6, -5, 7, 12]
        self.assertEqual(max_int(ls), 12)

    def test_for_one_element(self):

        """ test for only one element"""
        ls = [5]
        self.assertEqual(max_int(ls), 5)
