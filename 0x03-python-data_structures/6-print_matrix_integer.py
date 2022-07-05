#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    write a function that prints a matriz of integers
    """

    for row in matrix:
        for val in row:
            print('{:4}'.format(val))
            print

