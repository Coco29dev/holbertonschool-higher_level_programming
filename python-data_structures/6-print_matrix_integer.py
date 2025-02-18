#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Parcourt chaque ligne de la matrice (chaque "row" dans matrix)
    for row in matrix:
        # Convertit chaque élément de la ligne en chaîne formatée et
        # les joint avec un espace, puis les affiche.
        # "{:d}".format(element) formate l'élément comme un entier.
        # ' '.join() crée une chaîne avec les éléments séparés par un espace.
        print(' '.join("{:d}".format(element) for element in row))
