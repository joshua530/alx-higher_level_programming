#!/usr/bin/python3
"""Defines Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiates a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a Student instance's dictionary representation

        Args:
            attrs: list of attributes to obtain

        Returns:
            provided attributes if attrs is a list of strings, else all the
            attributes are returned"""
        if not isinstance(attrs, list):
            return self.__dict__
        else:
            dict_attrs = {}
            for attr in attrs:
                if attr in self.__dict__.keys():
                    dict_attrs[attr] = self.__dict__[attr]
            return dict_attrs

    def reload_from_json(self, json):
        """Loads instance attributes from provided json dictionary

        Args:
            json: dictionary of attributes to set for the object"""
        for k, v in json.items():
            if k in self.__dict__.keys():
                setattr(self, k, v)
