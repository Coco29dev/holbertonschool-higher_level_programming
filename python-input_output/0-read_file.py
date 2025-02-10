#!/usr/bin/python3
"""
Module fournissant une fonction pour
lire et afficher le contenu d'un fichier texte.
"""


def read_file(filename=""):
    """
    Lit un fichier texte encodé en UTF-8 et
    affiche son contenu sur la sortie standard.

    Args:
        filename (str): Le nom du fichier à lire. Par défaut, une chaîne vide.

    Utilisation :
        - Utilise l'instruction 'with' pour gérer les opérations sur le fichier
        - Supposé que le fichier existe et est lisible.
    """
    with open(filename, "r") as f:
        contenu = f.read()
        print(contenu)
