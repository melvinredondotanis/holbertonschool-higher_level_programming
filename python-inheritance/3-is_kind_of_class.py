#!/usr/bin/python3
"""Module that defines a function to check if an object
is an instance of, or inherited from, a class"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or inherited from, a class.

    Args:
        obj: object to check
        a_class: class to check against

    Returns:
        True if obj is an instance of, or inherited from, a_class,
        False otherwise
    """
    return isinstance(obj, a_class)
