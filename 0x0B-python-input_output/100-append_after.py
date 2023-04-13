#!/usr/bin/python3
"""Testing Python Input and Output"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file,
    after each line containing a search string."""
    with open(filename, mode='r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(filename, mode='w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
