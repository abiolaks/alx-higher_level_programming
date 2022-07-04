#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """

    A function to print integer per line

    """

    my_len = len(my_list)

    for i in range(my_len):
        print("{:d}".format(my_list[i]))
