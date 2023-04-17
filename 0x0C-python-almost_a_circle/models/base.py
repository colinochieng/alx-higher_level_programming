#!/usr/bin/python3
"""Module for Class base"""
import json
import os
import csv


class Base:
    """The base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string
        representation of list_dictionaries
        """
        if list_dictionaries == None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        file = cls.__name__ + '.json'
        with open(file, mode='w', encoding='utf-8') as fi:
            """"""
            fi.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string == None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        file = cls.__name__ + '.json'
        if os.path.isfile(file):
            with open(file, mode='r', encoding='utf-8') as fi:
                """"""
                content = fi.read()
                dicts = cls.from_json_string(content)
                return [cls.create(**dics) for dics in dicts]
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        filename = cls.__name__ + '.csv'
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        else:
            fieldnames = ["id", "size", "x", "y"]

        rows = []
        for obj in list_objs:
            row = {key: getattr(obj, key) for key in fieldnames}
            rows.append(row)

        with open(filename, "w") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)          

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        filename = cls.__name__ + '.csv'

        if not os.path.exists(filename):
            return []

        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        objects = []
        for row in rows:
            kwargs = {key: int(value) for key, value in row.items()}
            obj = cls.create(**kwargs)
            objects.append(obj)
        return objects
