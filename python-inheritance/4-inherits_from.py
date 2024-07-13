#!/usr/bin/python3
"""doc string"""

def inherits_from(obj, a_class):
    """this check for inheritance of an object or not"""
    return isinstance(obj, a_class) and type(obj) != a_class
