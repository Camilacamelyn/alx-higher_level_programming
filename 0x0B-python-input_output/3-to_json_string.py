#!/usr/bin/python3
"""To JSON string"""


import json


def to_json_string(my_obj):
    """function that retuns representation of json of an object(string)"""

    return json.dumbs(my_obj)
