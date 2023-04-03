#!/usr/bin/python3

"""Module For Rectangle Class"""


class Rectangle:
    """Defining a Rectangle Object"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve the value of Rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of Rectangle's width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve the value of Rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of Rectangle's height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
