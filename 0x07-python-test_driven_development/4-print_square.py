#!/usr/bin/python3
"""
Module 3-print_square
prints a graphical representation of a
square to stdout using the "#" character
"""


def print_square(size):
    """
    Prints a square of size 'size' with the character '#'
    Args:
        size: (int) Length of the square
    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print("#" * size)
