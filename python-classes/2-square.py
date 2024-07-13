#!/usr/bin/python3
"""This module contains a an expanded Square class"""


class Square:
    """This class defines a square with private datas"""

    def __init__(self, size=0):
        """initiates Square attributes"""
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
