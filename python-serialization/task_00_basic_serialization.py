#!/usr/bin/python3
"""
Module de sérialisation et désérialisation JSON.

Ce module permet de :
- Sauvegarder un dictionnaire Python dans un fichier JSON.
- Charger un dictionnaire Python depuis un fichier JSON.
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire et l'enregistre dans un fichier JSON.

    Paramètres :
    - data (dict) : Le dictionnaire à enregistrer.
    - filename (str) : Le nom du fichier JSON de sortie.

    Retourne :
    - None
    """
    with open(filename, "w") as f:
        json_string = json.dumps(data)
        f.write(json_string)


def load_and_deserialize(filename):
    """
    Charge et désérialise un fichier JSON en dictionnaire Python.

    Paramètres :
    - filename (str) : Le nom du fichier JSON à lire.

    Retourne :
    - dict : Le contenu du fichier JSON sous forme de dictionnaire.
    """
    with open(filename, "r") as f:
        return json.load(f)
