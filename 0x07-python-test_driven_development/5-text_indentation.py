#!/usr/bin/python3
"""Module dealing with ., ? and :"""


def text_indentation(text):
    """prints a text with 2 new lines after each of the char"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        print(i, end="")
        if i == "." or i == "?" or i == ":":
            print('\n')
