#!/usr/bin/python3
"""
JSON Module
"""


import json


def to_json_string(my_obj):
    """
    returns JSON (string)

    Args:
        my_obj (object):

    Returns:
        the JSON serialization format (string)
    """
    return json.dumps(my_obj)
