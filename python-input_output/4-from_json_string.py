#!/usr/bin/python3
"""
Module permettant de convertir une chaîne JSON en objet Python.
"""


import json


def from_json_string(my_str):
    """
    Convertit une chaîne de caractères au format JSON en objet Python.

    Args:
        my_str (str): La chaîne JSON à convertir.

    Returns:
        any: L'objet Python obtenu après conversion.
    """
    my_str = json.loads(my_str)
    print(my_str)
