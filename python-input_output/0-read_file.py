#!/usr/bin/python3


"""This contains a file opening and reading function"""
def read_file(filename="")
    """this function opens and reads a file"""

    with open(filename, encoding="utf-8") as f:
        """doc string"""
        read_data = f.read()
        print(read_data)
