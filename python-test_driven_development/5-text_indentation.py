#!/usr/bin/python3
"""
Ce module contient une fonction qui affiche un texte avec deux nouvelles lignes
après chaque caractère suivant : '.', '?', et ':'.

La fonction `text_indentation(text)` prend en entrée une chaîne de caractère et
affiche cette chaîne avec deux nouvelles lignes après chaque occurrence de ces
caractères. Les espace en début et en fin de chaque ligne imprimé sont supprimé

Fonction(s) dans ce module :
    - text_indentation(text) : Imprime le texte en ajoutant deux nouvelle ligne
      après chaque caractère '.', '?', ou ':'.

Exemples d'utilisation :
    >>> text_indentation("Hello. How are you? Fine: yes.")
    Hello.

    How are you?

    Fine:

    yes.
"""


def text_indentation(text):
    """
    Affiche un texte avec deux nouvelles lignes
    après chaque caractère '.', '?' ou ':'.

    Cette fonction prend en entrée une chaîne de caractères et imprime chaque
    partie du texte après avoir supprimé les espaces au début et à la fin de
    chaque ligne. Après chaque occurrence de '.', '?', ou ':', la fonction
    ajoute deux nouvelles lignes.

    Paramètre :
        text (str) : Le texte à imprimer. Il doit être une chaîne de caractères

    Lève :
        TypeError : Si le paramètre `text` n'est pas une chaîne de caractères.

    Exemple :
        >>> text_indentation("Hello. How are you?")
        Hello.

        How are you?
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in '.?:':
            print(text[i], end="\n\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            print(text[i], end="")
            i += 1
