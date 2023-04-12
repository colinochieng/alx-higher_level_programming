#!/usr/bin/python3
"""Elevating  BaseGeometry Module for Geometry"""


class BaseGeometry:
    """Simple Geometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
