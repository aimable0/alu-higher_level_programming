#!/usr/bin/python3
def no_c(var):
    new_string = ""
    for letter in var:
        if letter != 'c' and letter != 'C':
            new_string += letter
    return new_string
