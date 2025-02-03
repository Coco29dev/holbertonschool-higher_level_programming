#!/usr/bin/python3
"""
Module contenant la fonction `inherits_from`.

La fonction `inherits_from` vérifie si un objet est une instance d'une
classe qui hérite directement ou indirectement de la classe spécifiée.

Exemple d'utilisation:
    >>> inherits_from(42, int)
    False
    >>> inherits_from(42, object)
    True
    >>> inherits_from("Hello", str)
    False
"""


def inherits_from(obj, a_class):
    """
    Vérifie si un objet est une instance d'une classe qui hérite
    de la classe spécifiée.

    Cette fonction retourne True si l'objet est une instance
    d'une classe qui hérite de `a_class`,
    mais elle retourne False si l'objet est une instance exacte de `a_class`.

    Args:
        obj (any): L'objet à tester.
        a_class (type): La classe à vérifier.

    Returns:
        bool: Retourne True si l'objet est une instance d'une classe
        qui hérite de `a_class`, sinon retourne False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
