#!/usr/bin/python3
"""
Ce module contient une fonction qui divise chaque élément d'une matrice
par un diviseur donné.

La fonction `matrix_divided(matrix, div)` prend une matrice (liste de
listes d'entiers ou de flottants) et un diviseur, puis divise chaque
élément de la matrice par ce diviseur. Tous les résultats sont arrondis
à deux décimales.

Fonction(s) dans ce module :
    - matrix_divided(matrix, div) : Divise tous les éléments d'une matrice
      par un nombre et retourne une nouvelle matrice avec les résultats
      arrondis à deux décimales.

Exemples d'utilisation :
    >>> from 2-matrix_divided import matrix_divided
    >>> matrix = [
    >>>     [1, 2, 3],
    >>>     [4, 5, 6]
    >>> ]
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> matrix
    [[1, 2, 3], [4, 5, 6]]
"""


def matrix_divided(matrix, div):
    """
    Divise chaque élément d'une matrice par un diviseur et retourne une
    nouvelle matrice.

    Cette fonction prend une matrice (une liste de listes) et divise
    chaque élément par le diviseur `div`. Elle vérifie que la matrice est
    valide (une liste de listes d'entiers ou de flottants) et que chaque
    ligne de la matrice a la même taille. Le résultat de chaque division
    est arrondi à deux décimales. Si l'un des arguments est invalide, une
    exception appropriée est levée.

    Paramètres :
        matrix (list of list of int/float) : La matrice à diviser. Chaque
            élément doit être un entier ou un flottant.
        div (int/float) : Le diviseur. Ce doit être un nombre (entier ou
            flottant) et ne peut pas être égal à zéro.

    Retourne :
        list of list of float : Une nouvelle matrice où chaque élément
        est le résultat de la division du correspondant dans la matrice
        d'origine, arrondi à deux décimales.

    Lève :
        TypeError : Si `matrix` n'est pas une matrice valide (une liste de
            listes d'entiers ou de flottants), si `div` n'est pas un nombre,
            ou si les lignes de la matrice n'ont pas la même taille.
        ZeroDivisionError : Si `div` est égal à zéro.

    Exemple :
        >>> matrix = [
        >>>     [1, 2, 3],
        >>>     [4, 5, 6]
        >>> ]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
        >>> matrix
        [[1, 2, 3], [4, 5, 6]]
    """
    # Vérification que la matrice est une liste de listes d'entiers ou de flottants
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                                for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                         "of integers/floats")
    
    # Vérification que chaque ligne de la matrice a la même taille
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Vérification que chaque élément de la matrice est un entier ou un flottant
    for row in matrix:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) "
                             "of integers/floats")
    
    # Vérification que le diviseur est un nombre (int ou float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Vérification que le diviseur n'est pas égal à zéro
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Diviser chaque élément de la matrice et arrondir à 2 décimales
    return [[round(elem / div, 2) for elem in row] for row in matrix]