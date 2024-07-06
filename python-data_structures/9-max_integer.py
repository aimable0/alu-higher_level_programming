#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        max_int = sorted(my_list, reverse=True)
        return max_int[0]
