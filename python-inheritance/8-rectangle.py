#!/usr/bin/python3
"""This module represents rectangle that inherits from another class"""


class Rectangle(BaseGeometry):
    """a rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initiates attributes"""
        self.integer_validator("height", height)
        self._height = height
        self.integer_validator("width", width)
        self._width = width
