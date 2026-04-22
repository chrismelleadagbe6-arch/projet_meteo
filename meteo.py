import urllib.request
import json
from api_base import APIBase

class Meteo(APIBase):
    """Classe fille qui hérite de APIBase pour récupérer les données météo."""

    def __init__(self, ville, latitude, longitude):
        super().__init__(ville)
        self.latitude = latitude
        self.longitude = longitude
        self.donnees = {}


    def get_latitude(self):
        """Retourne la latitude de la ville."""
        return self.__latitude
    
    def get_longitude(self):
        """Retourne la longitude de la ville."""
        return self.__longitude
    
    
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
