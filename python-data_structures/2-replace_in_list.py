#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # Si l'index est négatif, retourne la liste inchangée.
    if idx < 0:
        return my_list
    # Si l'index est supérieur ou égal à la longueur
    # de la liste, retourne la liste inchangée.
    elif idx >= len(my_list):
        return my_list
    # Si l'index est valide, remplace l'élément
    # à cet index par le nouvel élément.
    else:
        my_list[idx] = element
        return my_list
