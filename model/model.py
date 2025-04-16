def sauvegarde_json(nom, lvl, score, sequences):
        resultat = {
            "Date": str(datetime.now()),
            "Nom" : nom,
            "Niveau" : lvl,
            "Score" : score,
             "Sequences" : sequences
        }

        fichier = "resultat.json"
        try:
            with open(fichier, "r") as file:
                data = json.load(file)
        # gestion d'erreur       
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(resultat)
        with open(fichier, "w") as file:
            json.dump(data, file, indent = 4)