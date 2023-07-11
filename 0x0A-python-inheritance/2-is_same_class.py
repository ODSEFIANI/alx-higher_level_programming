#!/usr/bin/python3
""" function that returns True if it is exactly an istance
 otherwise False.
"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance"""
    return type(obj) == a_class
