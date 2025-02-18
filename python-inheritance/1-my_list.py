#!/usr/bin/python3

"""
Module: MyList

Ce module contient la définition de la classe `MyList`, qui hérite de la classe
native `list` de Python. La classe `MyList` ajoute une méthode personnalisée
`print_sorted` pour afficher la liste triée.

"""


class MyList(list):
    """
    Classe : MyList

    La classe `MyList` est une sous-classe de la classe `list` de Python. Elle
    étend le comportement standard des listes
    en ajoutant une méthode `print_sorted`
    qui affiche la liste triée sans modifier l'ordre original de la liste.

    Hérite de :
        list : La classe native de Python représentant une liste.

    Méthodes :
        print_sorted() : Affiche une version triée de la liste.
    """

    def print_sorted(self):
        """
        Fonction : print_sorted

        Cette méthode trie la liste de manière
        ascendante et affiche le résultat.
        Elle ne modifie pas la liste originale.

        Exemple d'utilisation :
            >>> ma_liste = MyList([3, 1, 2])
            >>> ma_liste.print_sorted()
            [1, 2, 3]

        """
        print(sorted(self))
