#!/usr/bin/python3
"""Testing Python Input and Output"""


def read_file(filename=""):
    """
    function that reads a text file
    (UTF8) and prints it to stdout
    """
    with open(filename, encoding='utf-8') as fl:
        print(fl.read(),end="")
