#!/usr/bin/python3
"""Module for str function"""


def say_my_name(first_name, last_name=""):
    """Prints name of user"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
