#!/usr/bin/python3

"""Defining class Square"""


class Square:
    """
    instantiating Square attributes
    """
    def __init__(self, size=0):
        """
        checking for int value
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        else if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
