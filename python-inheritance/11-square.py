#!/usr/bin/python3
"""
Module contenant la classe Square, dérivée de Rectangle.

Ce module définit la classe Square qui hérite de la classe Rectangle. La classe
Square est utilisée pour représenter un carré et valider que sa taille est un
entier positif.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Représente un carré, dérivé de la classe Rectangle.

    La classe Square hérite de Rectangle et valide que la taille est entier
    positif Elle utilise la méthode integer_validator de la classe parente pour
    garantir la validité de la taille.
    """

    def __init__(self, size):
        """
    Initialise un carré avec une taille valide.

    Args:
        size (int): La taille du carré.

    La méthode vérifie que la taille est un entier positif et appelle
    le constructeur de la classe parente (Rectangle) en passant la taille
    pour la largeur et la hauteur.
    """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calcule l'aire du carré.

        Retourne :
        int : L'aire du carré (taille * taille).
        """
        return self.__size * self.__size

    def __str__(self):
        """"
        Retourne une représentation sous forme de chaîne de caractères du carré

        Retourne :
        str : La chaîne de caractères représentant le carré sous la forme
              "[Carré] côtér/côté".
        """
        return f"[Square] {self.__size}/{self.__size}"
