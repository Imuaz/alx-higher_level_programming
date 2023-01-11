#!/usr/bin/python3
"""
A Module Student that defines a student class
"""


class Student:
    """
    A class student defines student
    """
    def __init__(self, first_name, last_name, age):
        """
        __init__ method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        A method to_json
        """
        return self.__dict__
