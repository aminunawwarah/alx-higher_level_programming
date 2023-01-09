#!/usr/bin/python3

"""Defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """Reprsent base geometry"""

    def area(self):
        """Not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Make a parameter as an integer.

        Args:
            name (str): the name of the parameter
            value (int): the parameter to validate
        Raises:
            TypeError: if value isn't an integer
            ValueError: if value is 0 or less
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
