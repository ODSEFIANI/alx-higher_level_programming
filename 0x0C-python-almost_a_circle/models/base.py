#!/usr/bin/python3
"""BASE CLASS."""
import json
import csv
import turtle


class Base:
    """Represent the base model.

    Attributes:
        __nb_objects (int): The nued Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
