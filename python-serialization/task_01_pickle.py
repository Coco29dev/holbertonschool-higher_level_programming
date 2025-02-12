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

    def __init__(self, name: str, age: int, is_student: bool):
        """Initialise une nouvelle instance de CustomObject.

        Args:
            name (str): Le nom de la personne.
            age (int): L'âge de la personne.
            is_student (bool): Indique si la personne est étudiante.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Affiche les attributs de l'objet."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

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
        except Exception as e:
            print(f"Il y a une erreur lors de la sérialisation: {e}")
            return None

    @classmethod
    def deserialize(cls, filename: str):
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
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Il y a une erreur lors de la désérialisation: {e}")
            return None
