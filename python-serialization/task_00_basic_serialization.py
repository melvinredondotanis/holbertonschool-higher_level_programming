#!/usr/bin/python3
"""Converts a class to a JSON string."""


def serialize_and_save_to_file(data, filename):
    """Serialize data to JSON and save to file."""
    import json
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load data from file and deserialize from JSON."""
    import json
    with open(filename, "r") as f:
        data = json.load(f)
    return data
