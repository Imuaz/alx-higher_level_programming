#!/usr/bin/python3

"""
Module with a function that writes a string
to a text file
"""


def write_file(filename="", text=""):
    """
   Function that writes a string to a text file (UTF8)
   and returns the number of characters written
   Args:
        filename: the name of the file
        text: text file
    Raises
        Exception: when the file can be opened
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
