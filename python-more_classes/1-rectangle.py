#!/usr/bin/python3
"""This module contains a class that represents a rectangle"""


class Rectangle:
    """this class represents a simple rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self._Rectangle__width = value
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError('height must be >= 0')
            else:
                self._Rectangle__height = value
        else:
            raise TypeError('height must be an integer')
