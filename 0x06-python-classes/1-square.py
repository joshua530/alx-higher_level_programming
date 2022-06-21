#!/usr/bin/python3
"""Square class definition

This module adds an __init__ method to the square class
"""


class Square:
    """A class that represents squares"""

    def __init__(self, size):
        """
        Instantiates a square

        Args:
            size: the size of the square sides
        """
        self.__size = size
