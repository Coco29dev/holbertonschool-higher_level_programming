#!/usr/bin/python3
# Boucle pour le premier chiffre
for i in range(0, 9):
    # Boucle pour le deuxième chiffre qui sera tjr plus > que i
    for j in range(i + 1, 10):
        # Si c'est pas la dernière combinaison, ajouter ", "
        if i == 8 and j == 9:
            # dernière combinaison
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
