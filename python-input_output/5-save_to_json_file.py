#!/usr/bin/python3
"""Converts a JSON string to a Python object."""


def save_to_json_file(my_obj, filename):
    """
    Converts a JSON string to a Python object.
    """
    import json

    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
