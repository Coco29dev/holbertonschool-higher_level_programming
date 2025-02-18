#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Crée une nouvelle liste vide pour stocker les résultats
    new_list = []
    # Parcourt chaque élément de la liste my_list
    for num in my_list:
        # Vérifie si l'élément est divisible par 2
        if num % 2 == 0:
            new_list.append(True)  # Si divisible par 2, ajoute True
        else:
            new_list.append(False)  # Sinon, ajoute False
    # Retourne la nouvelle liste contenant les résultats
    return new_list
