#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Créer une nouvelle matrice vide
    new_matrix = []
    # Itérer sur chaque ligne de la matrice
    for row in matrix:
        # Pour chaque ligne créer une nouvelle
        # ligne avec les carrés des éléments
        new_row = [element ** 2 for element in row]
        new_matrix.append(new_row)
    return new_matrix
