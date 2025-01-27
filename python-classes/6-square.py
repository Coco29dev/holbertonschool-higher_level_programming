#!/usr/bin/python3
"""
Module Square

Ce module contient la classe `Square`, qui permet de manipuler un carré
avec une taille et une position données. Il permet de calculer l'aire du
carré et d'afficher le carré avec un décalage en fonction de la position.

La classe `Square` a les fonctionnalités suivantes :
- Calcul de l'aire du carré.
- Affichage du carré avec des "#" à la taille et la position spécifiées.
- Vérification des types et des contraintes pour la taille et la position.

Exemple d'utilisation :
    carré = Square(3, (1, 2))
    carré.my_print()
    print(carré.area())
"""


class Square:
    """
    Représente un carré avec une taille et une position données.

    Attributes:
        size (int): La taille du côté du carré.
        position (tuple): La position du carré dans le format (x, y).

    Methods:
        area(): Calcule l'aire du carré.
        my_print(): Affiche le carré avec la taille et la position données.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise un carré avec une taille et une position.

        Args:
            size (int): La taille du carré (doit être un entier >= 0).
            position (tuple): La position du carré sous forme de tuple (x, y).
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Retourne la taille actuelle du carré.

        Returns:
            int: La taille du côté du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Définit la taille du carré.

        Args:
            value (int): La taille du côté du carré (doit être un entier >= 0).

        Raises:
            TypeError: Si la valeur n'est pas un entier.
            ValueError: Si la valeur est inférieure à 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retourne la position actuelle du carré.

        Returns:
            tuple: La position du carré sous forme de tuple (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Définit la position du carré.

        Args:
            value (tuple): La position sous forme de tuple (x, y).

        Raises:
            TypeError: Si la position ne contient pas 2 entiers positifs.
        """
        if value < 0:
            raise TypeError("Position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calcule l'aire du carré.

        Returns:
            int: L'aire du carré (taille^2).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Affiche le carré avec des '#' selon la taille et la position.

        Si la taille du carré est 0, rien n'est affiché.
        """
        for _ in range(self.__position[1]):
            print()
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
