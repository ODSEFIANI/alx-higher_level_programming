#!/usr/bin/python3
"""
Append thetext to a file
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file

    Args:
        filename (str):
        text (str):

    Returns:
        the number of characters appended
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return = f.write(text)
