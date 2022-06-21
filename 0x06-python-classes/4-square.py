#!/usr/bin/python3
"""Square class

This module adds size getter and setter to the square class
"""


class Square:
    """A class that represents squares"""

    def __init__(self, size=0):
        """
        Instantiates a square

        Args:
            size: the size of the square sides
        """
        if size.__class__.__name__ != "int":
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Calculates square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """Fetches the value of square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value of square side

        Args:
            value: value to set for square side
        """
        if value.__class__.__name__ != "int":
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
