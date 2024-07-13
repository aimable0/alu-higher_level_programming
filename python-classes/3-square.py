#!/usr/bin/python3
"""This module contains a an expanded Square class"""


class Square:
    """This class represents a sqaure"""

    def __init__(self, size=0):
        """initiation of attributes"""
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be na integer')

    def area(self):
        """returns a square of an object"""
        return self.__size * self.__size
