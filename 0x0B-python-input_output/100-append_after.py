#!/usr/bin/python3

"""Defines function that inserts some text"""


def append_after(filename="", search_string="", new_string=""):
    """Insert some text after each line containing a given string in a file

    Args:
        filename (str): the file name
        search_string (str): the string in search for in the file
        new_string (str): the insert string
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
