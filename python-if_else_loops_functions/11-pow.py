#!/usr/bin/python3
def pow(a, b):
    # Cas où l'exposant est 0
    if b == 0:
        return 1

    resultat = 1
    # On initialise le résultat à 1
    # Si b est positif, on fait une boucle
    # pour multiplier a par lui-même b fois
    if b > 0:
        for _ in range(b):
            resultat *= a

    # Si b est négatif, on calcule a^(-b) puis on retourne l'inverse
    else:
        for _ in range(-b):
            resultat *= a
        resultat = 1 / resultat
        # Retourner l'inverse de a^(-b)
    return resultat
