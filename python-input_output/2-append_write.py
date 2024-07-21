#!/usr/bin/python3
"""
Module 2-append_write

Contains function that appends to text file and returns num chars added
"""


def write_file(filename="", text=""):
    """appends to text file and returns num chars written"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
