#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    total = 0
    valeur_precedente = 0

    for char in roman_string:
        if char == 'I':
            valeur = 1
        elif char == 'V':
            valeur = 5
        elif char == 'X':
            valeur = 10
        elif char == 'L':
            valeur = 50
        elif char == 'C':
            valeur = 100
        elif char == 'D':
            valeur = 500
        elif char == 'M':
        	valeur = 1000
        else:
            return 0

        if valeur > valeur_precedente:
            total += valeur - 2 * valeur_precedente
        else:
            total += valeur

        valeur_precedente = valeur

    return total
