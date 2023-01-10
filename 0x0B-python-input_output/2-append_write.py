#!/usr/bin/python3

"""Defines a function that appends text to a file"""


def append_write(filename="", text=""):
    """Adds a string to the end of a text ifle

    Args:
        filename (str): the name of the file to append to
        text (str): the string to append to the file
    Returns:
        The number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
