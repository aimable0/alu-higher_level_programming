#!/usr/bin/python3
"""This module contains rectangle class model"""


class Rectangle:
    """a simple model of a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if type(self._width) is not int:
            raise TypeError('width must be integer')
        else:
            if self._width < 0:
                raise ValueError('width must be >= 0')
            else:
                self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if type(self._height) is not int:  # or isinstance(a, int)
            raise TypeError('height must be integer')
        else:
            if self._height < 0:
                raise ValueError('height must be >= 0')
            else:
                self._height = value

    def area(self):
        return self._height * self._width

    def perimeter(self):
        if self._width == 0 or self._height == 0:
            return 0
        return (self._width + self._height) * 2

    def __str__(self):
        rectangle = ""
        if self._width == 0 or self._height == 0:
            return ""

        for i in range(self._height):
            rectangle += str(self.print_symbol) * self._width + '\n'
        return rectangle.strip()

    def __repr__(self):
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        print('Bye rectangle...')
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle):
            a_1 = rect_1.area()
        else:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle):
            a_2 = rect_2.area()
        else:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if a_1 == a_2:
            return rect_1
        elif a_1 > a_2:
            return rect_1
        elif a_1 < a_2:
            return rect_2

    @classmethod
    def square(cls, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError('width must be >= 0')
            else:
                cls.width = size
                cls.height = size
        else:
            raise TypeError('width must be an integer')

        return Rectangle(cls.width, cls.height)
