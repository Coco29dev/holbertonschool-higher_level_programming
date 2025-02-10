#!/usr/bin/python3
"""
Module permettant de créer un objet Python à partir d'un fichier JSON.
"""


import json


def load_from_json_file(filename):
    """
    Lit un fichier JSON et renvoie l'objet Python correspondant.

    Args:
        filename (str): Nom du fichier JSON à lire.

    Returns:
        any: Objet Python converti depuis le JSON.
    """
    with open(filename, "r") as f:
        return json.load(f)
