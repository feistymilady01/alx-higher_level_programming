#!/usr/bin/python3
"""
Module 5-text_indentation
"Tokenize" a string with specified delimiters
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after ".,?:"
    Args:
        text: (str)
    Raises:
        TypeError: text must be a string
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
