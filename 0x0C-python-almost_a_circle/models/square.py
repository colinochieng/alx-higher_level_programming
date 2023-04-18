#!/usr/bin/python3
"""Python Almost a Circle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Derived class of rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes from Rectangle"""
        super().__init__(size, size, x=x, y=y, id=id)

    @property
    def size(self):
        """Return size of Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Resets dimensions of square models"""
        self.width = value
        self.height = value

    def __str__(self):
        """Square User String representation"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    def update(self, *args, **kwargs):
        """Updates the fields of the instances"""
        if args:
            attrs_list = ['id', 'widht', 'height', 'x', 'y']
            if len(args) > 1:
                width = height = args[1]
                args = list(args)
                args[1:1 + 1] = [width, height]
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
