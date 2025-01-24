#!/usr/bin/python3
"""
Module pour afficher un carré avec le caractère '#'.

Ce module définit une fonction `print_square` qui prend un entier `size`
et affiche un carré de taille `size` avec le caractère `#`. Si la taille
n'est pas un entier ou est inférieure à zéro, des exceptions sont levées.
"""


def print_square(size):
    """
    Affiche un carré de taille `size` avec le caractère '#'.

    Arguments :
        size (int) : La taille du carré à afficher.

    Lève :
        TypeError : Si `size` n'est pas un entier.
        ValueError : Si `size` est un entier négatif.
        TypeError : Si `size` est un flottant négatif.

    Affiche :
        Un carré de caractères '#' avec une taille de `size` par `size`.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
