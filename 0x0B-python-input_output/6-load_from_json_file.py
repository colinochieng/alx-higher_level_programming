#!/usr/bin/python3
"""Testing Python Input and Output"""


import json


def load_from_json_file(filename):
    """
    function that writes an Object to a
    text file, using a JSON representation
    :param filename: file to decode from
    :return: python data representation
    """
    with open(filename, 'r', encoding='utf-8') as fl:
        return json.load(fl)
