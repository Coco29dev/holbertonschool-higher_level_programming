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
    number_of_instances = 0
    print_symbol = "#"

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
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol

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
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Retourne une représentation visuelle du rectangle sous forme de chaîne.

        Cette méthode crée un rectangle en utilisant
        le caractère '#' pour représenter
        les lignes et les colonnes du rectangle.
        Si la largeur ou la hauteur est égale à zéro,
        une chaîne vide est retournée.

        Retourne :
        str : Une chaîne représentant le rectangle, ou une chaîne vide si l'une
        des dimensions est égale à zéro.
        """
        rectangle_str = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle_str
        for i in range(self.__height):
            rectangle_str += (str(self.print_symbol) * self.__width)
            if i is not self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        """
        Retourne une chaîne de caractères représentant l'objet Rectangle.

        La chaîne retournée est une représentation
        exécutable qui permet de recréer
        une nouvelle instance de la classe
        Rectangle en utilisant la fonction eval().

        Par exemple, pour un objet Rectangle
        avec une largeur de 2 et une hauteur
        de 4, la méthode __repr__ renverra la chaîne suivante :

        "Rectangle(2, 4)"

        Cette chaîne peut être utilisée avec eval() pour recréer un objet
        Rectangle identique à l'original.

        Returns:
        str: Représentation en chaîne de l'objet Rectangle sous la forme
            "Rectangle(width, height)".
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Destructeur de la classe Rectangle.
        Affiche un message lorsque l'objet est supprimé.
        La ligne 'del my_rectangle' supprime simplement la référence
        à la classe et non l'instance actuelle.
        Cette méthode est appelée automatiquement lors
        de la collecte de l'objet par le garbage collector.
        """
        Rectangle.number_of_instances -= 1
        print(f"Bye rectangle...")
        my_rectangle = Rectangle
        del my_rectangle

    def bigger_or_equal(rect_1, rect_2):
        """
        Compare les aires de deux rectangles et retourne celui avec l'aire
        la plus grande. Si les aires sont égales retourne le premier rectangle.

        Paramètres:
        rect_1 (Rectangle): Le premier rectangle à comparer.
        rect_2 (Rectangle): Le deuxième rectangle à comparer.

        Retourne:
        Rectangle: Le rectangle avec l'aire la plus grande, ou rect_1 si
                   les aires sont égales.

        Lève:
        TypeError: Si rect_1 ou rect_2 n'est pas une instance de Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2
