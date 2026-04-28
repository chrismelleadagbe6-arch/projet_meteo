import json
import os


class Stockage:

    """Classe pour sauvegarder et lire les données météo en JSON."""

    def __init__(self, fichier="donnees_meteo.json"):
           self.__fichier = fichier

    def sauvegarder(self, ville, donnees):
        """Sauvegarde les données météo d'une ville dans le fichier JSON."""

        historique = self.charger_tout()
        historique[ville] = donnees
        with open(self.__fichier, "w") as f:
         json.dump(historique, f, indent=4)


    def charger_tout(self):
        """Charge tout les données sauvegardées."""

        if os.path.exists(self.__fichier):
           with open(self.__fichier, "r") as f:
               return json.load(f)
        return {}
                
    def charger_ville(self, ville):
        """Charge les données d'une ville spécifique."""
        historique = self.charger_tout()
        if ville in historique:
            return historique[ville]
        return None
    
    def afficher_historique(self):
        """Afficher la liste de toutes les villes sauvegardées."""
        historique = self.charger_tout()
        if len(historique) == 0:
            print("Aucune ville sauvegardée pour le moment.")
        
        else:
            print("\n=== La ville est déjà sauvegardée ===")
            for ville in historique:
                print(f" - {ville}")
    
    def ville_existe(self, ville):
        """Vérifie si une ville est déjà sauvegardée."""
        historique = self.charger_tout()
        return ville in historique



            

