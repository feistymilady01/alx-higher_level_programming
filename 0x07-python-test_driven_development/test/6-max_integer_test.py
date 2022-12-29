#!/usr/bin/python3
"""
Unittest for max_integer module
"""

import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Defines test cases for the max_integer function """

    def test_max_integer(self):
        """ Test a regular listof integers ordered or unordered """
        self.assertTrue(max_integer([1, 2, 3, 4]), 4)
        self.assertTrue(max_integer([17, 28, 53, 47]), 53)

    def test_max_floats(self):
        """ Tests a list of floats """
        self.assertTrue(max_integer([1.5, 6.7, 8.2, 12.8]), 12.8)

    def test_negative_integers(self):
        """ Test a list of negative integers """
        self.assertTrue(max_integer([-10, -12, -13, -4]), -4)

    def test_max_strings(self):
        """ Test a list containing strings """
        self.assertTrue(max_integer(['the', 'school', 'is', 'far']), 'the')

    def test_max_listOf_list(self):
        """ Test a list of list """
        self.assertTrue(max_integer([[1, 9, 18], [8, 16, 32], [8, 16, 32]]))

    def test_empty_list(self):
        """ Tests an empty list """
        self.assertEqual(max_integer([]), None)

    def test_empty_String(self):
        """ Test an empty string """
        self.assertEqual(max_integer(''), None)

    def test_type(self):
        """ Test for TypeError exceptions """
        self.assertRaises(TypeError, max_integer, 8, 12)
        self.assertRaises(TypeError, max_integer, ['She', 'he', 71])


if __name__ == '__main__':
    unittest.main()
