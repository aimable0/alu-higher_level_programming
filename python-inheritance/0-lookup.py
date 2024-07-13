#!/usr/bin/python3
"""Module contains afunction that returns a list of atts and meths"""

def lookup(obj):
    """This function returns a list of all atts and meths of a class"""
    return dir(obj)
