#!/usr/bin/python3

def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj: object to check
        a_class: class to check against

    Returns:
        True if obj is exactly an instance of a_class, False otherwise
    """
    return type(obj) is a_class
