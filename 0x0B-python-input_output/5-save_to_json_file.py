#!/usr/bin/python3
"""Testing Python Input and Output"""


import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a
    text file, using a JSON representation
    :param my_obj: json data type
    :param filename: file to encode into
    :return: python data representation
    """
    with open(filename, 'w', encoding='utf-8') as fl:
        json.dump(my_obj, fl)
