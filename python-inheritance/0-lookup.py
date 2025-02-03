#!/usr/bin/python3

""" Module pour fonction qui retourne une liste
d'attributs et méthodes d'une classe
"""


def lookup(obj):
    """
     Retourne une liste des attributs et méthodes d'un objet.

     Args:
         obj (object): L'objet dont on souhaite obtenir
         la liste des attributs et méthodes.

     Returns:
         list: Une liste contenant les noms
         des attributs et méthodes de l'objet.
    """
    return (dir(obj))
