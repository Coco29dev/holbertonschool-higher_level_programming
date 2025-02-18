#!/usr/bin/python3
def element_at(my_list, idx):
    # Si l'index est négatif, retourne None car un index négatif est invalide.
    if idx < 0:
        return None
    # Si l'index est supérieur ou égal à la longueur de la liste, retourne None
    elif idx >= len(my_list):
        return None
    # Si l'index est valide, retourne l'élément à cet index dans la liste.
    else:
        return my_list[idx]
