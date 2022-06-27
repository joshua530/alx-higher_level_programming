#!/usr/bin/python3
"""
This module contains rectangle class definition

adds static method bigger_or_equal
"""


class Rectangle:
    """
    Rectangle class
    
    Attributes:
        number_of_instances: total number of instantiated rectangles
        print_symbol: symbol[s] used when representing rectangle as a string
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """instantiates the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares two rectangles using their area
        
        Returns:
            the larger rectangle or rect_1 if the areas are the same
            
        Throws:
            TypeError: if either of the rectangles is not a Rectangle instance
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 > area_2:
            return rect_1
        if area_2 > area_1:
            return rect_2
        return area_1

    def __str__(self):
        """returns string representation of rectangle"""
        rect = []
        print_symbol = str(self.print_symbol)

        for row in range(self.__height):
            tmp = [print_symbol for row in range(self.__width)]
            rect.append(''.join(tmp))
        return "\n".join(rect)

    def __repr__(self):
        """returns canonical string representation of rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """called when Rectangle instance is destroyed"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
