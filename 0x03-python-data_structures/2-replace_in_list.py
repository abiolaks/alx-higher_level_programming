#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    This function replaces an element of a list at a specific position
    if idx is -ve, returns the original list
    if idx is out of range, return the original list
    """

    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
