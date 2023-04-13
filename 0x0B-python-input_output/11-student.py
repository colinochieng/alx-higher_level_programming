#!/usr/bin/python3
"""Testing Python Input and Output"""


class Student:
    """class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a"""
        if isinstance(attrs, list):
            for i in attrs:
                if not isinstance(i, str):
                    return self.__dict__
            my_dic = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    my_dic.update({k: v})
            return my_dic
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
