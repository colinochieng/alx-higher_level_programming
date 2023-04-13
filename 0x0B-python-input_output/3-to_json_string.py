#!/usr/bin/python3
"""Testing Python Input and Output"""


import json


def to_json_string(my_obj):
    """
     function that returns the JSON representation of an object (string)
    :param my_obj: python data type
    :return: json string representation
    """
    return json.dumps(my_obj)
