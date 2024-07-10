#!/usr/bin/python3
def search_replace(my_list, search, replace):

    copy_list = my_list[:]
    n = 0
    for element in my_list:
        if element == search:
            copy_list[n] = replace
        n = n + 1
    return copy_list
