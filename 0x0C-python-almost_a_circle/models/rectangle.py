#!/usr/bin/python3
"""Python Almost a Circle"""
from models.base import Base


class Rectangle(Base):
    """Subclass of Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of rectangle"""
        return self.width * self.height

    def display(self):
        """
        prints in stdout the Rectangle
        instance with the character #
        """
        print('\n' * self.y, end='')
        for i in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width, end='')
            print()

    def __str__(self):
        """overriding the __str__"""
        r = f'[Rectangle] ({self.id}) {self.x}/{self.y}'
        r += f' - {self.width}/{self.height}'
        return r

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        attrs_list = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, attrs_list[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
