import urllib.request
import urllib.parse
import json


class Geocodage:
    """Classe pour trouver automatiquement la latitude et la longitude d'une ville."""

    def __init__(self, ville):
        self.__ville = ville

    def get_coordonnees(self):
        """Retourne la latitude et la longitude d'une ville demandée."""

        url = (
            f"https://geocoding-api.open-meteo.com/v1/search?"
            f"name={urllib.parse.quote(self.__ville)}&count=1&language=fr&format=json"
        )
        with urllib.request.urlopen(url) as reponse:
            donnees = json.loads(reponse.read())

        if "results" in donnees and len(donnees["results"])>0:
            resultat = donnees["results"][0]
            latitude = resultat["latitude"]
            longitude = resultat["longitude"]
            return latitude, longitude
        else:
            print(f"La ville '{self.__ville}' est inretrouvable.")
            return None, None