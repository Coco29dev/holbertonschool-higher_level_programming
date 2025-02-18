#!/usr/bin/python3
"""
Module: Square
Ce module définit une classe `Square` qui représente un carré géométrique.
Il permet de manipuler des objets de type carré en définissant
un attribut pour la taille et en fournissant
des méthodes pour interagir avec cet objet.

Classe:
    Square: Représente un carré avec une taille spécifique.

"""


class Square:
    """
    Classe représentant un carré.

    Attributs:
        __size (int): La taille du côté du carré, un nombre entier positif.

    Méthodes:
        __init__(size): Initialise un carré avec la taille donnée.
    """
    def __init__(self, size):
        """
        Constructeur pour initialiser un carré.

        Arguments:
            size (int): La taille du côté du carré
            Doit être un entier positif.

        L'attribut `__size` est défini comme privé
        et stocke la taille du carré.
        """
        self.__size = size
