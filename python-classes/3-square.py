#!/usr/bin/python3

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
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size

    def area(self):
        """
        The area method of the class Square returns the area of the square.

        Args:
            None

        Raises:
            None

        Returns:
            int: The area of the square
        """

        return (self._size ** 2)
