#!/usr/bin/python3
"""
Ce module contient une fonction qui additionne deux nombres.

La fonction `add_integer(a, b=98)` permet d'additionner deux nombres, en
convertissant les flottants en entiers avant l'addition. Si l'un des arguments
n'est pas un entier ni un flottant, une exception `TypeError` est levée.

Fonction(s) dans ce module :
    - add_integer(a, b=98) : Additionne deux nombres après avoir vérifié leur
      type et effectué une conversion si nécessaire.

Exemples d'utilisation :
    >>> from 0-add_integer import add_integer
    >>> add_integer(1, 2)
    3
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    TypeError: b must be an integer

"""


def add_integer(a, b=98):
    """
    Additionne deux nombres après les avoir convertis en entiers.

    Cette fonction additionne les paramètres `a` et `b`, après avoir vérifié
    que ces derniers sont des entiers ou des flottants. Les flottants sont
    convertis en entiers avant l'addition. Si l'un des paramètres n'est pas un
    entier ou un flottant, une exception `TypeError` est levée.

    Paramètres :
        a (int ou float) : Le premier nombre à additionner.
        b (int ou float, optionnel) : Le deuxième nombre à additionner, avec
            une valeur par défaut de 98.

    Retourne :
        int : La somme de `a` et `b`, après avoir effectué la conversion des
            flottants en entiers.

    Lève :
        TypeError : Si `a` ou `b` ne sont pas des entiers ou des flottants.

    Exemple :
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98
        >>> add_integer(4, "School")
        TypeError: b must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
