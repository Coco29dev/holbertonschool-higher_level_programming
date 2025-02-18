#!/usr/bin/python3
"""
Module: Square
Ce module définit une classe `Square` qui représente un carré géométrique.
Elle permet de manipuler des objets de type carré avec une taille spécifiée.
Elle offre une propriété pour accéder et modifier
la taille, avec des vérifications
de validité. Elle fournit également des
méthodes pour calculer l'aire du carré et
afficher un carré constitué de `#`.

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
        __init__(size): Initialise un carré avec la taille donnée.

        size: Propriété pour accéder et modifier la taille du carré.
        Si la taille
        n'est pas un entier ou est
        négative, une exception est levée.

        area(): Calcule et retourne l'aire du carré.

        my_print(): Affiche un carré constitué de `#` de la taille spécifiée.
    """
    def __init__(self, size=0):
        """
        Constructeur pour initialiser un carré.

        Arguments:
            size (int, optionnel): La taille du côté du carré. Par défaut, elle
            est égale à 0. La taille doit être un entier positif ou égal à zéro
        """
        self.__size = size

    @property
    def size(self):
        """
        Propriété pour accéder à la taille du carré.

        Retourne:
            int: La taille du côté du carré.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Propriété pour modifier la taille du carré.

        Arguments:
            value (int): La nouvelle taille du carré. Doit être un entier
            positif ou égal à zéro.

        Exceptions:
            TypeError: Si `value` n'est pas un entier.
            ValueError: Si `value` est un entier négatif.

        Modifie l'attribut `__size` avec la nouvelle valeur,
        après avoir effectué les vérifications nécessaires.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calcule l'aire du carré.

        Retourne:
            int: L'aire du carré (côté * côté).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Affiche un carré constitué de `#` de la taille spécifiée.

        Si la taille du carré est 0, rien n'est affiché. Sinon, le carré est
        affiché ligne par ligne, chaque ligne étant composée de `#` répétés
        selon la taille du carré.

        Exemple:
            Pour un carré de taille 3 :
            ###
            ###
            ###
        """
        if self.__size == 0:
            print()
        else:
            print('\n'.join([''.join('#' * self.__size)] * self.__size))
