#!/usr/bin/python3
"""
Module for a class that prevents the creation of dynamic attribute

"""


class LockedClass():
    """Class to prevents the creation of dynamic attributes"""
    __slots__ = ['first_name']

    def __init__(self):
        """Init method"""
        pass
