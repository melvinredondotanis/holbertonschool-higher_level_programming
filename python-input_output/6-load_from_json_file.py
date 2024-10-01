#!/usr/bin/python3
"""return a json file"""


def load_from_json_file(filename):
    """
    return a json file
    """
    import json

    with open(filename, "r") as f:
        return json.load(f)
