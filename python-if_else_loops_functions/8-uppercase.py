#!/usr/bin/python3
def uppercase(str):
    # Parcours chaque caractère de la chaîne
    # Si le caractère est une lettre minuscule, convertir en majuscule
    result = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            # Convertir la minuscule en majuscule avec - 32 à son code ASCII
            result += chr(ord(c) - 32)
        else:
            # Si déjà une majuscule ou un autre caractère afficher tel quel
            result += c
    print(result)
