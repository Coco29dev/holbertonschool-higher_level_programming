#!/usr/bin/python3
def uppercase(str):
    # Parcours chaque caractère de la chaîne
    # Si le caractère est une lettre minuscule, convertir en majuscule
    resultat = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            # Convertir la minuscule en majuscule avec - 32 à son code ASCII
            resultat += chr(ord(c) - 32)
        else:
            # Si déjà une majuscule ou un autre caractère afficher tel quel
            resultat += c
    print("{}".format(resultat))
