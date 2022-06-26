#!/usr/bin/python3

"""
runs tests for add_integer

Link: https://pymotw.com/3/doctest/
"""


import unittest
import doctest

add_integer = __import__('0-add_integer').add_integer

suite = unittest.TestSuite()
suite.addTest(doctest.DocFileSuite('tests/0-add_integer.txt'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
