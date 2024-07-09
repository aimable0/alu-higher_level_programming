#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    for list in matrix:
        for item in list:
            if i == (len(list) - 1):
                print('{:d}'.format(item))
                continue
            print('{:d} '.format(item), end="")
            i = i + 1
        i = 0
