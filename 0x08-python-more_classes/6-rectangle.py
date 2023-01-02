#!/usr/bin/python3

""" Define the class Rectangle """


class Rectangle:
    """
    Initializing the rectanangle with height and width
    """

    def __init__(self, width=0, height=0):
        """
        Instantiation with optional width and height.
        Args:
            width (int): the rectanangle width
            height (int): the rectanangle height
        """
        Rectanagle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Geter for the rectanangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for rectanangle width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Geter for the rectanangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the rectanangle height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """the string that returns a rectangle with character #
        """
        rep_str = ""
        if self.__width != 0 and self.__height != 0:
            rep_str += "\n".join("#" * self.__width
                                 for i in range(self.__height))
        return rep_str

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """method: __del__
           deletes instance of Rectangle , and prints "Bye rectangle..."
        """
        Rectanagle.number_of_instances += 1
        print("Bye rectangle...")
