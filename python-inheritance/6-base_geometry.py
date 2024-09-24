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
