#!/usr/bin/python3
def max_integer(my_list=[]):
    # Si la liste est vide, retourne None.
    if not my_list:
        return None
    # Initialiser la variable 'largest' avec le premier élément de la liste
    largest = my_list[0]
    # Parcourt chaque élément de la liste pour trouver le plus grand
    for valeur in my_list:
        # Si un élément est plus grand que 'largest', on le met à jour
        if valeur > largest:
            largest = valeur
    # Retourne le plus grand élément trouvé.
    return largest
