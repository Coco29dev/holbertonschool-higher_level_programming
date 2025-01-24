#!/usr/bin/python3
"""
Module pour afficher un message avec le prénom et le nom de famille.

Ce module définit une fonction `say_my_name` qui prend un prénom
et un nom de famille optionnel, et affiche un message sous la forme :
"Mon nom est <prénom> <nom de famille>".
Si l'entrée n'est pas une chaîne de caractères,
une exception TypeError est levée.
"""


def say_my_name(first_name, last_name=""):
    """
    Affiche un message avec le prénom et le nom de famille.
    Arguments :
        first_name (str) : Le prénom de la personne.
        last_name (str, optionnel) : Le nom de famille de la personne.
        Par défaut une chaîne vide.
    Lève :
        TypeError : Si `first_name` ou `last_name`
        n'est pas une chaîne de caractères.
    Affiche :
        "Mon nom est <first_name> <last_name>".
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))