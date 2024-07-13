#!/usr/bin/python3
"""This module contains a an expanded Square class"""


class Square:
    """This class represents a sqaure"""

    def __init__(self, size=0):
        """initiation of attributes"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be na integer')
 
    def area(self):
        """returns a square when called"""
        return self.__size * self.__size

    def my_print(self):
        """prints a square with # when called"""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for t in range(self.size):
                    print('#', end="")
                print()
