#!/usr/bin/python3
"""Module for restricted class"""


class LockedClass:
    """A class prevents the user from dynamically creating
    new instance attributes,
    except if the new instance attribute is called first_name"""
    __slots__ = ['first_name']
