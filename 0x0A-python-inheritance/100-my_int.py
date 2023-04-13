#!/usr/bin/python3
"""Inheritance"""


class MyInt(int):
    """inherits from int"""
    def __init__(self, value):
        self.__value = value
        super().__init__()

    def __eq__(self, other):
        """Reverse functionality"""
        return self.__value != other

    def __ne__(self, other):
        """Reverse functionality"""
        return self.__value == other
