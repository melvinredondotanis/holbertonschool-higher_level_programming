#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self._size = size
        self._position = position

    def area(self):
        return (self._size ** 2)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def my_print(self):
        if self._size == 0:
            print()
            return

        for i in range(self.position[1]):
            print()
        for i in range(self._size):
            for j in range(self.position[0]):
                print(" ", end="")
            for k in range(self._size):
                print("#", end="")
            print()
