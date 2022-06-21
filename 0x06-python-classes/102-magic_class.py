#!/usr/bin/python3
"""Magic class module"""
import math


class MagicClass:
    """Magic class

    Does some 'magic'
    """

    def __init__(self, radius=0):
        """Instantiates MagicClass"""
        self.__radius = 0

        radius_type = radius.__class__.__name__
        if radius_type != "int" and radius_type != "float":
            raise TypeError("radius must be a number")
        self.__radius = radius

    def circumference(self):
        """Finds circumference"""
        return 2 * math.pi * self.__radius

    def area(self):
        """Finds area"""
        return self.__radius ** 2 * math.pi
