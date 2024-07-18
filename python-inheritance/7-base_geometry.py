#!/usr/bin/python3
"""this is a basegeometry class"""

class BaseGeometry:
    """simple base geometry model"""

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if isinstance(value, int):
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
        else:
            raise TypeError(f"{name} must be an integer")
