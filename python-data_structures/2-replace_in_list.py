#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for list_element in my_list:
        if idx < len(my_list):
            if idx > 0 or idx == 0:
                if list_element == my_list[idx]:
                    my_list[idx] = element
                    return my_list
            else:
                return my_list
        else:
            return my_list
