#!/usr/bin/python3
"""Module for Instantiation"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
    """

    if type(obj) == a_class:
        return False
    for cls in type(obj).mro():
        if cls == a_class:
            return True
    return False
