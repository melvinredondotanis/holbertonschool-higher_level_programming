#!/usr/bin/python3
"""tkt"""

from sys import argv
from os import path


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
my_obj = []


if __name__ == "__main__":
    """
    tkt
    """
    if path.exists(filename):
        my_obj = load_from_json_file(filename)

    if len(argv) > 1:
        for i in argv[1:]:
            my_obj.append(i)

    save_to_json_file(my_obj, filename)
