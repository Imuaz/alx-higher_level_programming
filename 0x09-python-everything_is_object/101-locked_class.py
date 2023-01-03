#!/usr/bin/python3

"""
Defines a class 'locked class'.
"""


class LockedClass:
    """
    LockedClass that prevents the user from dynamically creating new
    instance attributes, except if the new instance attribute 'first_name'
    """

    __slots__ = "first_name"
