#!/usr/bin/python3
"""
writes JSONe
"""


import json


def save_to_json_file(my_obj, filename):
    """
    writes JSON representation
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
