#!/usr/bin/python3
"""
COPY teh text form file streamline to the stdout
"""


def read_file(filename=""):
    """
    reads the text file (UTF8)
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
