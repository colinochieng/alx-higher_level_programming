#!/usr/bin/python3

"""Module For Rectangle Class"""


class Rectangle:
    """Defining a Rectangle Object"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """User defined output"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect_str += "#"
            rect_str += '\n'
        return rect_str[:-1]

    def __repr__(self):
        """a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Deletion"""
        print("Bye rectangle...")
