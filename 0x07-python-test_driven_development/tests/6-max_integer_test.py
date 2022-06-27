#!/usr/bin/python3

"""
Contains unit tests for max_integer
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_number(self):
        result = max_integer([1])
        self.assertEqual(1, result)

    def test_int_and_float(self):
        result = max_integer([1.2, 1])
        self.assertEqual(1.2, result)

    def test_negative_numbers(self):
        result = max_integer([-1, -2.2])
        self.assertEqual(-1, result)

    def test_multiple_numbers(self):
        result = max_integer([1.2, 3, 100.544, -20])
        self.assertEqual(100.544, result)
