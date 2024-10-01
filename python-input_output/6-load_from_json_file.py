#!/usr/bin/python3
"""return a json file"""


def save_to_json_file(my_obj, filename):
    """
    return a json file
    """
    import json

    with open(filename, "r") as f:
        return json.load(f)
