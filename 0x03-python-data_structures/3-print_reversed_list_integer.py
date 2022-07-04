#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    This function prints all integers of a list in reverse order
    """

    size = len(my_list) + 1

    for i in range(1,size):
        print("{:d}".format(my_list[-i])
