#!/usr/bin/python3
"""This module contains a simple square class"""
Rectangle = __import__(9-rectangle.py).Rectangle


class Square(Rectangle):
    """this is a square class that inherits from class rectangle
    attributes
    size: size of the square
    methodes
    area: which return the square of size
    """

    def __init__(self, size):
        self.integer_validator('size', size)
        self._size = size

    def area(self):
        return self._size ** 2
