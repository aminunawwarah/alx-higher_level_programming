#!/usr/bin/python3

"""Defines a class-checking function"""


def is_same_class(obj, a_class):
    """Check whether an object is exactly an instance of a class

    Args:
        obj (any): the object to check
        a_class (type): the class to match the type of obj to
    Returns:
        True if obj is exactly an instance of a class - True
        False if not
    """
    if type(obj) == a_class:
        return True
    return False
