#!/usr/bin/python3
"""
Module 3-say_my_name
prints name in the order of first_name and last_name
"""

def say_my_name(first_name, last_name=""):
    """
    Prints my name is <first_name> <last_name>
    Args:
        first_name (str)
        last_name (str, optional): Defaults as an empty string
    Raises:
        TypeError: if either first_name or last_name is not string
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {:s} {:s}".format(first_name, last_name))
