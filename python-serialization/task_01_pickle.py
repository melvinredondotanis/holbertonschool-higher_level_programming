#!/usr/bin/python3
"""Converts a class to a JSON string."""


class CustomObject:
    """Custom class to be serialized."""
    def __init__(self, name, age, is_student):
        """Initialize object attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize object to file."""
        import pickle
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize object from file."""
        import pickle
        with open(filename, "rb") as f:
            data = pickle.load(f)
        return data
