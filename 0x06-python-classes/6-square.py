#!/usr/bin/python3

"""Define class Square"""


class Square:
    """
    initializing the class attributes
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """
        size attribute getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size attribute setter
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the current position of the square.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Set the current position of the square.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Return the current area of the square.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        Print the square with the # character.
        """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
