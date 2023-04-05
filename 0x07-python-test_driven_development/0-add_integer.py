#!/usr/bin/python3

"""Module for fucntions to add int"""


def add_integer(a, b=98):
    """adds to int or floats"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
