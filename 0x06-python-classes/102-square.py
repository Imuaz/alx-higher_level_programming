#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """The class that defines a square"""

    def __init__(self, size=0):
        """Initializer function for a Square.
        Args:
            size (int): Size of the Square.
            position (tuple): Position of the Square.
        """
        self.size = size

    def __lt__(self, other):
        """Less Than Comparator, x < y
        Args:
            size (Square): Current intstance of the Class
            other (Square): Other intstance of the Class
        """
        return self.size < other.size

    def __le__(self, other):
        """Less Than or Equal To Comparator, x <= y
        Args:
            size (Square): Current intstance of the Class
            other (Square): Other intstance of the Class
        """
        return self.size <= other.size

    def __eq__(self, other):
        """Is Equal Comparator
        Args:
            size (Square): Current intstance of the Class
            other (Square): Other intstance of the Class
        """
        return self.size is other.size

    def __ne__(self, other):
        """Is Not Equal Comparator, x != y
        Args:
            size (Square): Current intstance of the Class
            other (Square): Other intstance of the Class
        """
        return self.size is not other.size

    def __gt__(self, other):
        """Greater Than Comparator, x > y
        Args:
            size (Square): Current intstance of the Class
            other (Square): Other intstance of the Class
        """
        return self.size > other.size

    def __ge__(self, other):
        """Greater Than or Equal To Comparator, x >= y
        Args:
            size (Square): Current intstance of the Class
            other (Square): Other intstance of the Class
        """
        return self.size >= other.size

    @property
    def size(self):
        """" Gets private __size attribute.
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets a new value for __size attribute.
        Args:
            value (int): The value of the new size.
        """
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculates the area of the Square.
        Returns:
            The area of the Square.
        """
        return self.size ** 2
