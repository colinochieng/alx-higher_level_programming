#!/usr/bin/python3
"""Testing Python Input and Output"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file
    (UTF8) and returns the number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as fl:
        return fl.write(text)
