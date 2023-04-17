#!/usr/bin/python3
""" Module that contains class Square,
inheritance of class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes instances """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Square User String representation"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            attrs_list = ['id', 'widht', 'height', 'x', 'y']
            if len(args) > 1:
                width = height = args[1]
                args = list(args)
                args[1:1 + 1] = [width, height]
                print(args)
            for i in range(len(args)):
                setattr(self, attrs_list[i], args[i])
        else:
            for k, v in kwargs.items():
                if k == 'size':
                    setattr(self, 'width', v)
                    setattr(self, 'height', v)
                else:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id, 'x': self.x, 'size': self.height, 'y': self.y}
