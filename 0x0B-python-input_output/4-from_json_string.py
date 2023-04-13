#!/usr/bin/python3
"""Testing Python Input and Output"""


import json


def from_json_string(my_obj):
    """
    function that returns an object (Python data structure)
    represented by a JSON string
    :param my_obj: json data type
    :return: python data representation
    """
    return json.loads(my_obj)
