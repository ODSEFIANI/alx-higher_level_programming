#!/usr/bin/python3
""" Module JSONy
"""
import json


def from_json_string(my_str):
    """ Function that returns deserializations result

    Args:
        my_str: JSON string

    Raises:
        Exception: deserializations error

    """
    return json.loads(my_str)
