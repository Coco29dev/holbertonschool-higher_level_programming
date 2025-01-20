#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return None  # Si la chaîne est vide, retourne None
    else:
        return (len(sentence), sentence[0])
        # Retourne la longueur et le premier caractère
