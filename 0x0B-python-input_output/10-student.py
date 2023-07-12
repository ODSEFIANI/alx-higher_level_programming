#!/usr/bin/python3
""" Module defining class Student """

class Student:
    """ Class for student instances """

    def __init__(self, first_name, last_name, age):
        """ Initialize method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return directory description """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for attr in attrs:
                if type(attr) is not str:
                    return obj

            d_list = {}

            for attr in range(len(attrs)):
                for key in obj:
                    if attrs[attr] == key:
                        d_list[key] = obj[key]
            return d_list

        return obj

