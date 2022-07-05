#!/usr/bin/python3

def multiple_returns(sentence):
    """
    This returns a tuple with the length of a string
    and it firt character
    """
    size = len(sentence)

    if sentence == "":
        sentence[0] = None
    
    return (size, sentence[0])

