#!/usr/bin/python3
"""
Module task_01_pickle

Ce module contient la classe CustomObject qui permet
de sérialiser et désérialiser des objets personnalisés
en utilisant le module pickle.
"""

import pickle


class CustomObject:
    """Classe représentant un objet personnalisé
    avec des attributs de nom, âge et statut d'étudiant.
    """

    def __init__(self, name, age, is_student):
        """Initialise une nouvelle instance de CustomObject.

        Args:
            name (str): Le nom de la personne.
            age (int): L'âge de la personne.
            is_student (bool): Indique si la personne est étudiante.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    @property
    def name(self):
        """Retourne le nom de la personne."""
        return self._name

    @name.setter
    def name(self, name):
        """Définit le nom de la personne."""
        if not isinstance(name, str):
            raise TypeError("Name doit être un str")
        if name is None or name.strip() == "":
            raise ValueError("Name doit être plein ou None")
        self._name = name

    @property
    def age(self):
        """Retourne l'âge de la personne."""
        return self._age

    @age.setter
    def age(self, age):
        """Définit l'âge de la personne."""
        if not isinstance(age, int):
            raise TypeError("Age doit être un int")
        if age < 0:
            raise ValueError("Age doit être >= 0")
        self._age = age

    @property
    def is_student(self):
        """Retourne le statut d'étudiant de la personne."""
        return self._is_student

    @is_student.setter
    def is_student(self, is_student):
        """Définit le statut d'étudiant de la personne"""
        if not isinstance(is_student, bool):
            raise TypeError("is_student doit être un boolean")
        self._is_student = is_student

    def display(self):
        """Affiche les attributs de l'objet."""
        print(f'Name: {self.name}\n'
              f'Age: {self.age}\n'
              f'Is Student: {self.is_student}')

    def serialize(self, filename):
        """Sérialise l'objet actuel et l'enregistre dans un fichier.

        Args:
            filename (str): Le nom du fichier
            dans lequel l'objet sera sérialisé.

        Returns:
            None
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            print(f"Il y a une erreur lors de la sérialisation")
            return None

    @classmethod
    def deserialize(cls, filename):
        """Désérialise un objet à partir d'un fichier et le retourne.

        Args:
            filename (str): Le nom du fichier à partir
            duquel l'objet sera désérialisé.

        Returns:
            CustomObject: Une instance de CustomObject ou None en cas d'erreur.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.PickleError):
            print(f"Il y a une erreur lors de la désérialisation")
            return None
