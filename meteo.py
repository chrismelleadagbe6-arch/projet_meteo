import urllib.request
import json

class Meteo:
    """Classe pour récupérer les données météo via l'API Open-Météo."""

    def __init__(self, ville, latitude, longitude):
        self.ville = ville
        self.latitude = latitude
        self.longitude = longitude
        self.donnees = {}


    def recuperer_donnees(self):
        """Récupère les données météo de l'API Open-Météo."""
        url  = (
            f"https://api.open-meteo.com/v1/forecast?" 
            f"latitude={self.latitude}&longitude={self.longitude}"
            f"&daily=temperature_2m_max,temperature_2m_min"
            f"&timezone=auto"
        )

        with urllib.request.urlopen(url) as reponse:
            self.donnees = json.loads(reponse.read())
        return self.donnees
