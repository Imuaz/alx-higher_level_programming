#!/usr/bin/python3

"""Define class Square"""


class Square:
    """
    initializing the class attributes
    """
    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """
        size attribute getter
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        size attribute setter
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Return the current square area
        """
        return (self.size * self.size)

    def my_print(self):
        """
        Print the square with the # character.
        """
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
