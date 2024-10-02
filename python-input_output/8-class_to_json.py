#!/usr/bin/python3
"""Converts a class to a JSON string."""


def class_to_json(obj):
    """
    Converts a class to a JSON string.
    """
    return obj.__dict__
