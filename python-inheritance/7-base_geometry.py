#!/usr/bin/python3
"""
Module contenant la classe de base pour les opérations géométriques.
"""


class BaseGeometry:
    """
    Classe de base pour les objets géométriques.
    """

    def area(self):
        """
       Méthode non implémentée pour calculer l'aire.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
    Valide que la valeur est un entier positif.

    Args:
        name (str): Le nom de l'attribut à valider.
        value (int): La valeur à valider.

    Lève :
        TypeError : Si la valeur n'est pas un entier.
        ValueError : Si la valeur est inférieure ou égale à 0.
       """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
