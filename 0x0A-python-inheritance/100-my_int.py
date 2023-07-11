#!/usr/bin/python3
""" class MyInt attributes int
"""


class MyInt(int):
    """ Class """
    def __eq__(self, other):
        return int(str(self)) != other

    def __ne__(self, other):
        return int(str(self)) == other
