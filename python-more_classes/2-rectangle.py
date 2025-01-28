#!/usr/bin/python3
"""
Ce module définit une classe Rectangle.

La classe Rectangle permet de créer des
objets représentant des rectangles,
avec des attributs pour la largeur et la hauteur.
Des méthodes peuvent être ajoutées
plus tard pour calculer des propriétés telles que la surface ou le périmètre.
"""


class Rectangle:
    """
    Représente un rectangle.

    Cette classe permet de définir un rectangle par sa largeur et sa hauteur.
    Elle permet de manipuler ces propriétés et peut être étendue pour ajouter
    d'autres fonctionnalités liées aux rectangles, telles que le calcul de la
    surface ou du périmètre.

    Attributs :
        largeur (int) : La largeur du rectangle.
        hauteur (int) : La hauteur du rectangle.

    Méthodes :
        __init__(self, width, height) : Initialise un rectangle avec la
        largeur et la hauteur spécifiées.
        width(self) : Retourne la largeur du rectangle.
        width(self, value) : Définit la largeur du rectangle avec une valeur
        spécifiée.
        height(self) : Retourne la hauteur du rectangle.
        height(self, value) : Définit la hauteur du rectangle avec une
        valeur spécifiée.
    """
    def __init__(self, width=0, height=0):
        """
        Initialise un nouveau rectangle.

        Cette méthode initialise un rectangle avec la largeur et la hauteur
        spécifiées. Par défaut, ces valeurs sont initialisées à 0.

        Arguments :
            width (int) : La largeur du rectangle. Doit être un entier
            positif ou égal à zéro.
            height (int) : La hauteur du rectangle. Doit être un entier
            positif ou égal à zéro.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Retourne la largeur du rectangle.

        Cette méthode est utilisée pour accéder à la largeur du rectangle.

        Retourne :
            int : La largeur du rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Définit la largeur du rectangle.

        Cette méthode est utilisée pour définir la largeur du rectangle. Si
        la valeur n'est pas un entier ou est inférieure à zéro, une exception
        sera levée.

        Arguments :
            value (int) : La nouvelle largeur du rectangle.

        Lève :
            TypeError : Si la valeur de la largeur n'est pas un entier.
            ValueError : Si la largeur est inférieure à zéro.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retourne la hauteur du rectangle.

        Cette méthode est utilisée pour accéder à la hauteur du rectangle.

        Retourne :
            int : La hauteur du rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Définit la hauteur du rectangle.

        Cette méthode est utilisée pour définir la hauteur du rectangle. Si
        la valeur n'est pas un entier ou est inférieure à zéro, une exception
        sera levée.

        Arguments :
            value (int) : La nouvelle hauteur du rectangle.

        Lève :
            TypeError : Si la valeur de la hauteur n'est pas un entier.
            ValueError : Si la hauteur est inférieure à zéro.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calcule la surface du rectangle.

        Cette méthode retourne la surface du rectangle en multipliant
        la largeur par la hauteur.

        Retourne :
            int : La surface du rectangle (en unités carrées).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Cette méthode retourne le périmètre du rectangle en ajoutant la largeur
        et la hauteur, puis en multipliant la somme par 2.

        Retourne :
            int : Le périmètre du rectangle (en unités linéaires).
        """
        return (self.__width + self.__height) * 2
