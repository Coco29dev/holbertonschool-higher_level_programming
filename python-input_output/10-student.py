#!/usr/bin/python3
"""
Module définissant la classe Student.
"""


class Student:
    """
    Représente un étudiant avec un prénom, un nom et un âge.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialise un étudiant avec ses informations personnelles.

        Args:
            first_name (str): Prénom de l'étudiant.
            last_name (str): Nom de l'étudiant.
            age (int): Âge de l'étudiant.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
    Retourne une représentation du dictionnaire de l'instance Student.

    Args:
        attrs (list, optionnel): Liste de chaînes contenant les noms des
        attributs à récupérer. Si None ou invalide, tous les attributs sont
        retournés dans un ordre spécifique.

    Returns:
        dict: Dictionnaire contenant les attributs demandés dans l'ordre
        ['age', 'last_name', 'first_name']. Si attrs est invalide, tous les
        attributs sont retournés dans cet ordre.
    """
        if (not isinstance(attrs, list) or
                not all(isinstance(attr, str) for attr in attrs)):
            return {"age": self.age, "last_name": self.last_name,
                    "first_name": self.first_name}
        en_ordre = {}
        for key in ["age", "last_name", "first_name"]:
            if key in attrs and key in self.__dict__:
                en_ordre[key] = self.__dict__[key]

        return en_ordre
