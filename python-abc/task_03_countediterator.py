#!/usr/bin/python3
"""Module that contains a counted iterator class."""


class CountedIterator:
    """Defines a class that extends the built in iterator."""
    def __init__(self, data):
        self.data = iter(data)
        self.count = 0

    def get_count(self):
        """Returns the count of the number of iterations."""
        return self.count

    def __next__(self):
        """Returns the next item in the iteration."""
        try:
            item = next(self.data)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration
