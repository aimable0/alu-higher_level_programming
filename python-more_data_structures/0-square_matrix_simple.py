#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix =  []
    for item in matrix:
        new_matrix.append(list(map(lambda x: x * x, item)))
    return new_matrix
