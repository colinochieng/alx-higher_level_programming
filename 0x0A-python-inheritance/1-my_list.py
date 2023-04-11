#!/usr/bin/python3
"""Module for MyList"""


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        print(sorted(self))
