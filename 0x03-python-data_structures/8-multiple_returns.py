#!/usr/bin/python3

def multiple_returns(sentence):
    """
    This returns a tuple with the length of a string
    and it firt character
    """

    return (len(sentence), sentence[0] if len(sentence) > 0 else None)
