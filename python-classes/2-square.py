#!/usr/bin/python3
""" This module contains an empty class Square that defines a square. """


class Square:
    """
    This is an empty class Square that defines a square.
    """
    def __init__(self, size=0):
        """
        The __init__ method of the class Square initializes the instance.

        Args:
            size (int): The size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0

        Returns:
            None
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
