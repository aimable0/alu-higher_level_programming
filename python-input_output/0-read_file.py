#!/usr/bin/python3
"""
Module 0-read_file

contains a file opening and reading function
"""


def read_file(filename="")
    """this function opens and reads a file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read().strip())
