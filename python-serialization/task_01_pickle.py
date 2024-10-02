#!/usr/bin/python3
"""Converts a class to a JSON string."""


class CustomObject:
    """Custom class to be serialized."""
    def __init__(self, name, age, is_student):
        """Initialize object attributes."""
        self.name = int(name)
        self.age = int(age)
        self.is_student = bool(is_student)

    def display(self):
        """Display object attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize object to file."""
        import pickle
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (FileNotFoundError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize object from file."""
        import pickle
        try:
            with open(filename, "rb") as f:
                data = pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError):
            return None
        return data
