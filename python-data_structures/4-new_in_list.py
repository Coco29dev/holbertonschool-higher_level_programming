#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Si l'index est négatif, retourne une copie de la liste sans modification
    if idx < 0:
        return my_list.copy()
    # Si l'index est supérieur ou égal à la longueur de la liste
    # retourne une copie
    elif idx >= len(my_list):
        return my_list.copy()
    # Si l'index est valide, crée une copie
    # de la liste et modifie l'élément à l'index donné.
    else:
        new_list = my_list.copy()
        new_list[idx] = element  # Remplace l'élément à l'index spécifié
        return new_list
