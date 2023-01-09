#!/usr/bin/python3

"""Defines an object attribute--lookup function"""


def lookup(obj):
    """Retrieves a list of an object's available in the attributes"""
    return (dir(obj))
