#!/usr/bin/python3
"""Counts number of lines in a file.
"""


def number_of_lines(filename=""):
    """Counts lines in filename.

    Args:
        - filename: name of the file

    Returns:
        - number of lines
    """

    count = 0

    with open(filename) as f:
        text = f.readlines()
        for line in text:
            count += 1

    return count
