#!/usr/bin/python3
def no_c(my_string):
    # Utilise la méthode translate() pour supprimer 'c' et 'C' de la chaîne
    # ord('c') et ord('C') renvoient les codes ASCII des caractères à supprimer
    # On remplace ces caractères par None, ce qui les supprime de la chaîne
    return my_string.translate({ord('c'): None, ord('C'): None})
