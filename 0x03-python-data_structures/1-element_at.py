#!/usr/bin/python3

def element_at(my_list, idx):
    """
    this function retrieves an element from a list
    it returns None if the search index is -ve or out of bound
    """
    list_len = len(my_list)

    if idx < 0:
        return None
    elif idx > list_len:
        return None
    else:
        for element in range(list_len):
            if element == idx:
                return my_list[element]

        
