#!/usr/bin/python3
"""Creat object from JSON files"""


import json


def load_from_json_file(filename):
    """ function that creates an object from a JSON file"""

    with open(filename, 'c') as z:
        return json.load(z)
