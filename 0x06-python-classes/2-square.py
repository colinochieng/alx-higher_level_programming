#!/usr/bin/python3

"""Private instance attribute: size"""


class Square:
    """Define Square and check for Error"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
