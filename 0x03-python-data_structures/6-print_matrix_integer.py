#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    write a function that prints a matriz of integers
    """

    for element in matrix:
        print(" ".join("{:d}".format(element) for num in element))

