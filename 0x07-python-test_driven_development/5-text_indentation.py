#!/usr/bin/python3

"""
Contains a text indentation function
"""


def text_indentation(text):
    """
    adds newlines to text

    It prints two newlines after the characters . ? :

    Args:
        text: the text to print out

    Raises:
        TypeError: if text is not a string
    """
    if type(text) not in [str]:
        raise TypeError("text must be a string")
    for char in text:
        if char in ["?", ":", "."]:
            print(char, end="\n\n")
        else:
            print(char, end="")
