# defining a function to print an integer in a list
#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    A function to print integer per line
    """
    for i in my_list:
        print("{:d}".format(my_list[i]))
