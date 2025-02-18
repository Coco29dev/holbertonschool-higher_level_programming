#!/usr/bin/python3
"""
Module: Square
Ce module définit une classe `Square` qui représente un carré géométrique.
La classe permet de manipuler des objets
de type carré avec une taille spécifiée.
Elle vérifie également que la taille est un entier positif ou égal à zéro.
Elle fournit également une méthode pour calculer l'aire du carré.

Classe:
    Square: Représente un carré avec une taille définie par un entier.

"""


class Square:
    """
    Classe représentant un carré.

    Attributs:
        __size (int): La taille du côté du carré, un entier positif ou égal
        à zéro.

    Méthodes:
        __init__(size): Initialise un carré avec la taille donnée. Si la taille
        n'est pas un entier ou est négative, une exception est levée.
        area(): Calcule et retourne l'aire du carré.
    """

    def __init__(self, size=0):
        """
        Constructeur pour initialiser un carré.

        Arguments:
            size (int, optionnel): La taille du côté du carré. Par défaut, elle
            est égale à 0. La taille doit être un entier positif ou égal à zéro

        Exceptions:
            TypeError: Si `size` n'est pas un entier.
            ValueError: Si `size` est un entier négatif.

        Initialise l'attribut `__size` en fonction
        de la taille donnée et effectue
        des validations sur celle-ci.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calcule l'aire du carré.

        Retourne:
            int: L'aire du carré (côté * côté).
        """
        return self.__size * self.__size
