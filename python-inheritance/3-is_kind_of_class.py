#!/usr/bin/python3
"""
Module contenant la fonction `is_kind_of_class`.

La fonction `is_kind_of_class` permet de vérifier si un objet est
une instance d'une classe ou d'une de ses sous-classes.

Exemple d'utilisation:
    >>> is_kind_of_class(42, int)
    True
    >>> is_kind_of_class(42, object)
    True
    >>> is_kind_of_class(42, str)
    False
"""


def is_kind_of_class(obj, a_class):
    """
    Vérifie si un objet est une instance de la
    classe spécifiée ou d'une de ses sous-classes.

    Args:
        obj (any): L'objet à tester.
        a_class (type): La classe à comparer avec l'objet.

    Returns:
        bool: Retourne True si l'objet est une instance de
        a_class ou de l'une de ses sous-classes,
              sinon retourne False.
    """
    return isinstance(obj, a_class)
