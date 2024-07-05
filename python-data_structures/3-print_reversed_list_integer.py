#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list[0] != " ":
        for number in sorted(my_list, reverse=True):
            print("{:d}".format(number))
    else:
        return None
