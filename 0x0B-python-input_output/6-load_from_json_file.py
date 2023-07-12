#!/usr/bin/python3
"""
JSON filee
"""


import json


def load_from_json_file(filename):
    """
    read  from a JSON
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return  = json.load(f)
