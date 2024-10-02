#!/usr/bin/python3
"""Converts a class to a JSON string."""


def serialize_and_save_to_file(data, filename):
    """tkt"""
    import pickle
    with open(filename, "wb", encoding="utf-8") as f:
        f.write(pickle.dumps(data))


def load_and_deserialize(filename):
    """tkt"""
    import pickle
    with open(filename, "rb", encoding="utf-8") as f:
        data = pickle.loads(f.read())
    return data
