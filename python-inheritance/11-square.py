#!/usr/bin/python3
"""Module that defines a Square class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.
    """
    def __init__(self, size):
        """
        Initializes a Square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Computes the area of a Square instance.
        """
        return self.__size ** 2

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
