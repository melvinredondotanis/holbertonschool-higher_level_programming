#!/usr/bin/python3

def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited
    from a_class.

    Args:
        obj: object to check
        a_class: class to check against

    Returns:
        True if obj is an instance of a class that inherited from a_class,
        False otherwise
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
