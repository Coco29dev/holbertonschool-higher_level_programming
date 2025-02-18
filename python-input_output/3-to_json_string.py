#!/usr/bin/python3
"""
Module permettant de convertir un objet en une chaîne JSON.
"""


import json


def to_json_string(my_obj):
    """
    Convertit un objet Python en une chaîne de caractères au format JSON.

    Args:
        my_obj (any): L'objet à convertir.

    Returns:
        str: La représentation JSON de l'objet.
    """
    json_string = json.dumps(my_obj)
    return json_string
