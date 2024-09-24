#!/usr/bin/python3
"""Module that defines a base geometry class"""


class BaseGeometry:
    """Defines methods for geometric shapes."""

    def area(self):
        """Calculate the area of a geometric shape.

        Raises:
            Exception: if the area method is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer value.

        Args:
            name (str): the name of the value.
            value (int): the value to validate.

        Raises:
            TypeError: if the value is not an integer.
            ValueError: if the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Defines a rectangle."""

    def __init__(self, width, height):
        """Initializes a rectangle.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
