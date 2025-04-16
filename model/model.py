import json
from datetime import datetime

class model():
    def sauvegarde_json(mesure):
            fichier = "donneesCaptees.json"
            try:
                with open(fichier, "r") as file:
                    data = json.load(file)
            # gestion d'erreur       
            except (FileNotFoundError, json.JSONDecodeError):
                data = []

# A VERIFIER
            data.append(mesure.retourner())
            with open(fichier, "w") as file:
                json.dump(data, file, indent = 4)