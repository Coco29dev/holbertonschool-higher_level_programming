#!/usr/bin/python3

def generate_invitations(template, attendees):
    """
    Génère des fichiers d'invitation personnalisés à partir d'un modèle avec des espaces réservés
    et une liste d'objets. Chaque fichier de sortie est nommé séquentiellement, en commençant par 1.

    Args:
        template (str): Le modèle avec des espaces réservés au format {placeholder}.
        attendees (list): Une liste de dictionnaires contenant les données pour chaque invité.

    Returns:
        None
    """
    # Vérification que template est une chaîne de caractères
    if not isinstance(template, str):
        print(
            f"Error: Template must be a string, but got {type(template).__name__}")
        return

    # Vérification que attendees est une liste
    if not isinstance(attendees, list):
        print(
            f"Error: Attendees must be a list, but got {type(attendees).__name__}")
        return

    # Vérification que tous les éléments de attendees sont des dictionnaires
    if attendees and not all(isinstance(item, dict) for item in attendees):
        print("Error: All items in attendees must be dictionaries")
        return

    # Vérification que template n'est pas vide
    if not template:
        print("Template is empty, no output files generated.")
        return

    # Vérification que attendees n'est pas vide
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Traitement de chaque invité
    for i, attendee in enumerate(attendees, 1):
        # Création d'une copie du modèle à modifier
        personalized_invitation = template

        # Remplacement des espaces réservés par les valeurs du dictionnaire de l'invité
        for key in ["name", "event_title", "event_date", "event_location"]:
            # Si la clé est manquante ou la valeur est None, utiliser "N/A"
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"

            # Remplacement de l'espace réservé par la valeur
            personalized_invitation = personalized_invitation.replace(
                f"{{{key}}}", str(value))

        # Écriture dans le fichier de sortie
        with open(f"output_{i}.txt", "w") as file:
            file.write(personalized_invitation)
