#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, "r") as csv_f:
            csv.reader = csv.DictReader(csv_f)
            data = list(csv.reader)
        with open("data.json", "w") as json_f:
            json.dump(data, json_f)
        return True
    except FileNotFoundError:
        print(f"Fichier {csv_filename} non trouvé")
        return False
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return False
