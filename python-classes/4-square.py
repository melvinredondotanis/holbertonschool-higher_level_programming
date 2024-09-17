#!/usr/bin/python3

class Square:
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
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size

    def area(self):
        return (self._size ** 2)

    @property
    def size(self):
        """
        The size getter method of the class Square
        returns the size of the square.

        Args:
            None

        Raises:
            None

        Returns:
            int: The size of the square
        """

        return self._size

    @size.setter
    def size(self, value):
        """
        The size setter method of the class Square
        sets the size of the square.

        Args:
            value (int): The size of the square

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0

        Returns:
            None
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value
