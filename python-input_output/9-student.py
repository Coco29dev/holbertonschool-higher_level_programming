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

    def to_json(self):
        """
        Retourne une représentation en dictionnaire de l'étudiant.

        Returns:
            dict: Dictionnaire contenant les attributs de l'étudiant.
        """
        return self.__dict__
