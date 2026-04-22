import json
import os


class Stockage:

    """Classe pour sauvegarder et lire les données météo en JSON."""

    def __init__(self, fichier="donnees_meteo.json"):
           self.fichier = fichier
    def sauvegarder(self, ville, donnees):
        """Sauvegarde les données météo d'une ville dans le fichier JSON."""

        historique = self.charger_tout()
        historique[ville] = donnees
        with open(self.fichier, "w") as f:
         json.dump(historique, f, indent=4)


    def charger_tout(self):
        """Charge tout les données sauvegardées."""

        if os.path.exists(self.fichier):
           with open(self.fichier, "r") as f:
               return json.load(f)
        return {}
                
        

