#!/usr/bin/python3

"""Defines a class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """Check whether an object is an instance or inherited instance of a class

    Args:
        obj (any): the object to check
        a_class (type): the class to match the type of obj to
    Returns:
        True if obj is an instance or inherited instance of a class
        False if not
    """
    if isinstance(obj, a_class):
        return True
    return False
