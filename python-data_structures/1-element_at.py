#!/usr/bin/python3
def element_at(my_list, idx):
    for element in my_list:
        if idx < len(my_list):
            if idx > 0 or idx == 0:
                if element == my_list[idx]:
                    return element
            else:
                return None
        else:
            return None
