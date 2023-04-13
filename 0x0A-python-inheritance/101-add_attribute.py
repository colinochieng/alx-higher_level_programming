#!/usr/bin/python3
"""Module for add attribute func"""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value
