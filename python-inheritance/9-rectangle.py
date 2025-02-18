#!/usr/bin/python3
"""
Module contenant la classe Rectangle, dérivée de BaseGeometry.

Ce module définit la classe Rectangle, qui hérite de la classe BaseGeometry
et implémente des validations pour les attributs de dimensions .
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Représente un rectangle.

    Rectangle hérite de la classe BaseGeometry et valide que la largeur
    et la hauteur sont des entiers positifs.
    Elle utilise la méthode integer_validator
    de la classe parente pour s'assurer que les dimensions sont correctes.
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec des dimensions valides.

        Args:
        width (int): La largeur du rectangle.
        height (int): La hauteur du rectangle.

        La méthode vérifie que la largeur et
        touch 9-main.py la hauteur sont des entiers positifs.
        Lève des exceptions si les dimensions ne sont pas valides.
        """
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
    Calcule l'aire du rectangle.

    Retourne :
        int : L'aire du rectangle (largeur * hauteur).
    """
        return self.__width * self.__height

    def __str__(self):
        """
    Retourne une représentation sous forme de chaîne de caractères du rectangle

    Retourne :
        str : La chaîne de caractères représentant le rectangle sous la forme
              "[Rectangle] largeur/hauteur".
    """
        return f"[Rectangle] {self.__width}/{self.__height}"
