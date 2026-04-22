from meteo import Meteo
from stockage import Stockage
from geocodage import Geocodage


def afficher_statistique(ville, donnees):
   """Afficher les statistiques météo d'une ville"""
   temperatures_max = donnees["daily"]["temperature_2m_max"]
   temperatures_min = donnees["daily"]["temperature_2m_min"]


   temp_max = max(temperatures_max)
   temp_min = min(temperatures_min)
   temo_moyenne = sum(temperatures_max)/len(temperatures_max)

   print(f"\n===Statistiques météo de {ville} ===")
   print(f"Température maximale : {temp_max} °C")
   print(f"Température minimale : {temp_min} °C")
   print(f"Température moyenne : {temo_moyenne: .1f} °C")



def main():
    """Fonction principale du programme."""

    print("=== Explorateur de Données Météo ===")

    continuer = True
    ville_consultees = []

    while continuer:

       ville = input("\nEntrez le nom d'une ville: ")

       reponse = input("Connaissez-vous la latitude et la longitude de cette ville ? (oui/non) : ")

       if reponse.lower() == "oui" :
          latitude = float(input("Entrez la latitude : "))
          longitude = float(input("Entrez la longitude : "))

       else:
          print(f"Reherche automatique des coordonnées de {ville} ")
          geo = Geocodage(ville)
          latitude, longitude = geo.get_coordonnees()

          if latitude is None:
             print("La ville recherchée est introuvable, veuillez réessayer.")
             continue
          
          print(f"Latitude trouvée : {latitude}")
          print(f"Longitude trouvée : {longitude}")
       
       # Récupérer les données météo
       meteo = Meteo(ville, latitude, longitude)
       donnees = meteo.recuperer_donnees()

       #Sauvegarder les données
       stockage = Stockage()
       stockage.sauvegarder(ville, donnees)

       #Afficher les statistiques
       afficher_statistique(ville, donnees)

       #Ajouter la ville à la liste
       ville_consultees.append(ville)


       print(f"\nVilles consultées jusqu'ici : {ville_consultees}")

       reponse = input("\nVoulez-vous consulter une autre ville ? (oui/non) : ")
       if reponse.lower() != "oui":
         continuer = False

    print("\n Merci d'avoir utilisé l'Explorateur de Donnée Météo!" )

if __name__ == "__main__":
 main()


