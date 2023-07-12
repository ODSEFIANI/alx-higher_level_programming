#!/usr/bin/python3
"""
Write inside specific file
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)

    Args:
        filename (str):
        text (str):

    Returns:
        the number of characters printed
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
