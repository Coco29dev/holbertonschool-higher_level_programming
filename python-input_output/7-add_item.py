#!/usr/bin/python3
"""
Module permettant d'ajouter tous les arguments de la ligne de commande
à une liste Python et de les sauvegarder dans un fichier JSON.

- Utilise `save_to_json_file` pour enregistrer la liste dans un fichier.
- Utilise `load_from_json_file` pour charger la liste depuis un fichier.
- Le fichier utilisé est `add_item.json`.
- Si le fichier n'existe pas, une nouvelle liste est créée.

"""


import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    ma_list = load_from_json_file(filename)
except FileNotFoundError:
    ma_list = []

ma_list.extend(sys.argv[1:])
save_to_json_file(ma_list, filename)
