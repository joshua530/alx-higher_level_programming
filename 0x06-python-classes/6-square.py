#!/usr/bin/python3
"""Square class

This module adds position property to the square class
"""


class Square:
    """A class that represents squares"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Instantiates a square

        Args:
            size: the size of the square sides
            position: the current position
        """
        if size.__class__.__name__ != "int":
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

    def area(self):
        """Calculates square area

        Returns:
            the area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Fetches the value of square size

        Returns:
            the size of the square
        """
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

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print(
                "\n".join(
                    [
                        " " * self.__position[0] + "#" * self.__size
                        for rows in range(self.__size)
                    ]
                )
            )

    @property
    def position(self):
        """
        Gets the current position

        Returns: the current position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the current position

        Args:
            value: sets position to tuple if value is tuple of 2 positive ints
        """
        if (
            type(value) is not tuple
            or len(value) != 2
            or type(value[0]) is not int
            or type(value[1]) is not int
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
