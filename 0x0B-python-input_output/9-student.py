#!/usr/bin/python3
"""Defines Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiates a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a Student instance's dictionary representation"""
        return self.__dict__
