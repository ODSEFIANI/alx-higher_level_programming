#!/usr/bin/python3
"""
Lookup for file
"""


def append_after(filename="", search="", new=""):
    """
    Inserts a lines in the specified file,
    """
    updated_content = ""
    with open(filename, 'r+', encoding="utf-8") as file:
        while True:
            line = file.readline()
            updated_content += line
            if line == '':
                break
            if search in line:
                updated_content += new
        file.seek(0)
        file.truncate()
        file.write(updated_content)

