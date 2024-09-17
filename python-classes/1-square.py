#!/usr/bin/python3
""" This module contains an empty class Square that defines a square. """


class Square:
    """
    This is an empty class Square that defines a square.
    """
    def __init__(self, size):
        """
        The __init__ method of the class Square
        initializes the instance.

        Args:
            size (int): The size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0

        Returns:
            None
        """

        self.__size = size
