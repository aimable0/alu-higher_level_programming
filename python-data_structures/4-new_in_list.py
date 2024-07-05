#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < len(my_list):
        if idx > 0 or idx == 0:
            my_list_copy = my_list[:]
            my_list_copy[idx] = element
            return my_list_copy
        else:
            return my_list
    else:
        return my_list
