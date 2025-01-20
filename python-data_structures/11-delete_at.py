#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Vérifie si l'index est invalide
    if idx < 0 or idx >= len(my_list):
        return my_list  # Retourne la liste inchangée si l'index est invalide
    # Utilisation du slicing pour supprimer l'élément à l'index 'idx'
    del my_list[idx]  # Supprime l'élément directement dans my_list
    return my_list  # Retourne la liste modifiée
