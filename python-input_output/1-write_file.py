#!/usr/bin/python3
"""
Module permettant d'écrire du texte dans un fichier.
"""


def write_file(filename="", text=""):
    """
    Écrit du texte dans un fichier en UTF-8
    et retourne le nombre de caractères écrits.

    Args:
        filename (str): Le nom du fichier.
        text (str): Le texte à écrire.

    Returns:
        int: Le nombre de caractères écrits.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
