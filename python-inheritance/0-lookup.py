#!/usr/bin/python3
"""Module that defines a lookup function"""


def lookup(obj):
    """
    Function that returns the list of available
    attributes and methods of an object.

    Args:
        obj: object to lookup

    Returns:
        List of available attributes and methods
    """

    return dir(obj)
