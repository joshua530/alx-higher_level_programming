#!/usr/bin/python3
"""
This module contains rectangle class definition

It adds __repr__ to Rectangle
"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """instantiates the rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value    

    def area(self):
        """returns rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """returns string representation of rectangle"""
        rect = []
        for row in range(self.__height):
            tmp = ["#" for row in range(self.__width)]
            rect.append(''.join(tmp))
        return "\n".join(rect)

    def __repr__(self):
        """returns canonical string representation of rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """called when Rectangle instance is destroyed"""
        print("Bye rectangle...")
