#!/usr/bin/python3
"""objects to a text file"""


import json


def save_to_json_file(my_obj, filename):
    """function that writes an object to a file"""

    with open(filename, 'a') as f:
        f.write(json.dumps(my_str))
