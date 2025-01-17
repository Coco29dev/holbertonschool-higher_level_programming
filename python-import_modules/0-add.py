#!/usr/bin/python3
from add_0 import add
# Ici, on importe la fonction 'add' depuis le fichier 'add_0.py'.
if __name__ == "__main__":
	# Cette condition vérifie si ce script est exécuté directement, et non importé comme module.
    a = 1
    b = 2
    resultat = add(a, b)
    # On appelle la fonction 'add' en passant 'a' et 'b' en arguments 
    # et on stocke le résultat dans 'resultat'.
    print("{} + {} = {}".format(a, b, resultat))
    # On affiche le résultat de l'addition dans le format "1 + 2 = 3".
