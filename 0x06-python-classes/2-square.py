#!/usr/bin/python3


class Square:
    """
    class square that has attributes:
        size
    some attributes are protected from input.
    """
    def __init__(self, size=0):
        """Constructor of the Square class"""
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
            return

        if size < 0:
            raise ValueError("size must be >= 0")
            return

        self.__size = size
