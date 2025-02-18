#!/usr/bin/python3
"""
Module permettant d'ajouter du texte à la fin d'un fichier.
"""


def append_write(filename="", text=""):
    """
    Ajoute du texte à la fin d'un fichier en
    UTF-8 et retourne le nombre de caractères ajoutés.

    Args:
        filename (str): Le nom du fichier.
        text (str): Le texte à ajouter.

    Returns:
        int: Le nombre de caractères ajoutés.
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
