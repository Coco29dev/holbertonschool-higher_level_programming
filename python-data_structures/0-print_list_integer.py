#!/usr/bin/python3
def print_list_integer(my_list=[]):
    # Parcourt chaque élément de la liste my_list et l'affiche.
    # "{:d}".format(num) est utilisé pour formater l'élément comme un entier
    for num in my_list:
        print("{:d}".format(num))
