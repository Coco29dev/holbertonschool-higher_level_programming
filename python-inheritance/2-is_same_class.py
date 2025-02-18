#!/usr/bin/python3
"""
Module qui contient la fonction `is_same_class`.

La fonction `is_same_class` permet de vérifier si un objet est
exactement une instance de la classe spécifiée.

Exemple d'utilisation:
    >>> is_same_class(42, int)
    True
    >>> is_same_class(42, str)
    False
"""


def is_same_class(obj, a_class):
    """
    Vérifie si un objet est exactement une instance de la classe spécifiée.

    Args:
        obj (any): L'objet à tester.
        a_class (type): La classe à comparer avec l'objet.

    Returns:
        bool: Retourne True si l'objet est une instance exacte
        de la classe a_class, sinon retourne False.
    """
    return type(obj) is a_class
