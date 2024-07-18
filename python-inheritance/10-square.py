#!/usr/bin/python3
"""doc string"""
Rectangle = __import__(9-rectangle.py).Rectangle


class Square(Rectangle):
    """this is a square class that inherits from class rectangle"""

    def __init__(self, size):
        self.integer_validator('size', size)
        self._size = size

    def area(self):
        return self._size ** 2
