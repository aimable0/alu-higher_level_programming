#!/usr/bin/python3
"""
Module 0-read_file

Contains a file opening and reading function
"""


def read_file(filename=""):
    """Read and print text from file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
