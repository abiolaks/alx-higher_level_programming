#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    This function prints all integers of a list in reverse order
    """

    new_list = []

    for i in range(len(my_list)):
        a = -1 + i
        new_list.append(my_list[a])
        print("{:d}".format(new_list[i]))
