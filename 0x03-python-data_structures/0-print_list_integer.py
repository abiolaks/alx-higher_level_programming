# defining a function to print an integer in a list

def print_list_integer(my_list=[]):
    """
    A function to print integer per line
    import is not allow
    casting of integer into strings
    str.format() to print integers
    """
    for i in my_list:
        print("{:d}".format(my_list[i]))
