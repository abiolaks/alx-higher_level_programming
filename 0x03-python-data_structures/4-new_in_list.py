#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    replaces an element in a list at a spcicif position without modify
    the originals
    """

    list_copy = my_list[:]
    size = len(list_copy)

    if idx < 0:
        return list_copy
    elif idx >= size:
        return list_copy
    else:
        list_copy[idx] = element
        return list_copy
