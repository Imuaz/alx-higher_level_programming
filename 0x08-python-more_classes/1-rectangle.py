#!/usr/bin/python3

""" Define the class Rectangle """


class Rectangle:
    """ Initializing the rectanangle with height and width """

    de __init__(self, width=0, height=0):
        """Instantiation with optional width and height """
        self.width = width
        self.height = height

        @property
        def width(self):
            """ Geter for the rectanangle width """
            return self.__width

        @width.setter
        def width(self, value):
            """ setter for rectanangle width """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.width = value

            @property
            def height(self):
                """ Geter for the rectanangle height"""
                return self.__height

            @height.setter
            def height(self, value):
                """ setter for the rectanangle height """
                if not isinstance(value, int):
                    raise TypeError("height must be an integer")
                if value < 0:
                    raise ValueError("height must be >= 0")
                self.__height = value
