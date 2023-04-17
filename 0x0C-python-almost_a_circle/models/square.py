#!/usr/bin/python3
"""Python Almost a Circle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Derived class of rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x=x, y=y, id=id)

    def __str__(self):
        """ str special method """
        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_square + str_id + str_xy + str_wh

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
