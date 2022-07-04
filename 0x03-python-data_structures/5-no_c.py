#!/usr/bin/python3

def no_c(my_string):
    """
    function tha removes all character c and C form a string
    """
    string = ""

    for char in my_string:
        if char != 'c' and char != 'C':
            string = string + char
    return string
