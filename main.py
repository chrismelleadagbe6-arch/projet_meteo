from meteo import Meteo
from stockage import Stockage


def main():
    """Fonction principale du programme."""

    print("=== Explorateur de Données Météo ===")

    ville = input("Entrez le nom d'une ville: ")
    latitude = float(input("Entrez la latitude de la ville: "))
    longitude = float(input("Entrez la longitude de la ville: "))

    # Récupérer les données météo
    meteo = Meteo(ville, latitude, longitude)
    donnees = meteo.recuperer_donnees()

    #Sauvegarder les données
    stockage = Stockage()
    stockage.sauvegarder(ville, donnees)

    print(f"\nDonnées météo de {ville} sauvegardées avec succès!")

if __name__ == "__main__":
 main()


