#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    for number in sorted(my_list, reverse=True):
        print("{:d}".format(number))
