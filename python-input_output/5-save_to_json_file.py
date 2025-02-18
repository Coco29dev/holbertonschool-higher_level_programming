#!/usr/bin/python3
"""
Module permettant de sauvegarder un
objet Python au format JSON dans un fichier.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Sérialise un objet Python en JSON et l'écrit dans un fichier.

    Args:
        my_obj (any): L'objet à convertir en JSON.
        filename (str): Le nom du fichier où enregistrer l'objet.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
