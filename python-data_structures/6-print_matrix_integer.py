#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    loop = 0
    for each_matrix in matrix:
        for item in each_matrix:  
            loop = loop + 1
            if loop == 3:
                print("{:d} ".format(item))
            else:
                print("{:d} ".format(item), end="")
        loop = 0
