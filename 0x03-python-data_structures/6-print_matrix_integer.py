#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    write a function that prints a matriz of integers
    """

    for each_list in matrix:
        for row in each_list:
            print("{:d}".format(row), end=" ")
        print()
