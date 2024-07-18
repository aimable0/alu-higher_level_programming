#!/usr/bin/python3
# 8-rectangle.py
"""Defines a class Rectangle that inherits from BaseGeometry."""


class Rectangle(BaseGeometry):
    """a rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """attribute initiation"""
        self.integer_validator("height", height)
        self._height = height
        self.integer_validator("width", width)
        self._width = width
