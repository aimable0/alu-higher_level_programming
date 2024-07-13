#!/usr/bin/python3
class Square:
    """This class represents a sqaure"""

    def __init__(self, size=0, position=(0, 0)):
        """initiation of attributes"""
        self.size = size
        self.position = position

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self._size = value
        else:
            raise TypeError('size must be na integer')

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if type(value) is tuple:
            self._position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')


    def area(self):
        return self._size * self._size

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print("")
            for i in range(self.size):
                print(' ' * self.position[0] + '#' * self.size)
