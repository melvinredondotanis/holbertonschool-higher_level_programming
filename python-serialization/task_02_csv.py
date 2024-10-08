#!/usr/bin/python3
"""Converts a CSV file to a Python object."""


def convert_csv_to_json(csv_file):
    """
    Converts a CSV file to a Python object.
    """
    import csv
    import json

    data = []
    try:
        with open(csv_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("file not found")
        return False

    with open("data.json", "w") as f:
        f.write(json.dumps(data))
    return True
