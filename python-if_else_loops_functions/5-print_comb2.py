#!/usr/bin/python3
# Boucle itération de 0 à 99
for i in range(0, 100):
    # Vérifie si ce n'est pas le dernier nombre
    if i != 99:
        # Le format {:02d} affiche les deux chiffres
        print("{:02d}".format(i), end=", ")
    else:
        # Imprime 99 sans virgule et espace
        print("{:02d}".format(i))
