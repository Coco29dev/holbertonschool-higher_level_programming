#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Utilise la fonction reversed() pour parcourir la liste à l'envers.
    # Pour chaque nombre dans la liste inversée
    # affiche-le sous forme d'entier formaté.
    # "{:d}".format(num) est utilisé pour
    # afficher l'élément sous forme d'entier.
    for num in reversed(my_list):
        print("{:d}".format(num))
