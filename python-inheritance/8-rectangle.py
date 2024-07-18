#!/usr/bin/python3
# 8-rectangle.py

"""This represents a simple class that inherits from another class"""
class Rectangle(BaseGeometry):
    """a rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("height", height)
        self._height = height
        self.integer_validator("width", width)
        self._width = width
