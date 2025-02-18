#!/usr/bin/python3
"""
Module qui fournit une fonction pour convertir un objet en dictionnaire JSON.
"""


def class_to_json(obj):
    """
    Retourne le dictionnaire des attributs d'une instance de classe,
    utilisable pour la sérialisation en JSON.

    La fonction utilise `vars()`, qui retourne le dictionnaire __dict__
    d'un objet, contenant tous ses attributs sous forme de paires clé-valeur.

    Args:
        obj (any): L'objet à convertir.

    Returns:
        dict: Le dictionnaire des attributs de l'objet.
    """
    return vars(obj)
