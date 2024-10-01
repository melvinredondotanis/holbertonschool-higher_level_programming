#!/usr/bin/python3
"""Converts a JSON string to a Python object."""


def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.
    """
    import json
    return json.loads(my_str)
