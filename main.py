from meteo import Meteo
from stockage import Stockage
from geocodage import Geocodage


def afficher_statistique(ville, donnees):
   """Afficher les statistiques météo d'une ville"""
   try:
   
       temperatures_max = donnees["daily"]["temperature_2m_max"]
       temperatures_min = donnees["daily"]["temperature_2m_min"]


       temp_max = max(temperatures_max)
       temp_min = min(temperatures_min)
       temp_moyenne = sum(temperatures_max)/len(temperatures_max)

       print(f"\n===Statistiques météo de {ville} ===")
       print(f"Température maximale : {temp_max} °C")
       print(f"Température minimale : {temp_min} °C")
       print(f"Température moyenne : {temp_moyenne: .1f} °C")
   
   except KeyError:
      print("Erreur : Les données météo sont incomplètes !")
   except Exception as e:
      print(f"Erreur inattendue : {e}")

def saisir_coordonnees():
   """Demende à l'utilisateur d'entrée la latitude et longitude."""
   try:
      latitude = float(input("Entrez la latitude : "))
      longitude = float(input("Entrez la longitude : "))
      return latitude, longitude 
   except ValueError:
      print("Erreur : Priez d'entrer des chiffres valides !")
      return None, None     



def main():
    """Fonction principale du programme."""

    print("=== Explorateur de Données Météo ===")
    stockage = Stockage()
    continuer = True
    ville_consultees = []

    while continuer:
       stockage.afficher_historique()

       ville = input("\nEntrez le nom d'une ville : ").strip()
       if stockage.ville_existe(ville):
          print(f"\n {ville} est déjà sauvegardée !")
          reponse = input("Voulez-vous recharger depuis internet?")
          if reponse.lower() == "non":
             donnees = stockage.charger_ville(ville)
             afficher_statistique(ville, donnees)
             ville_consultees.append(ville)
             reponse = input("\nVoulez-vous consulter une autre ? (oui/non) : ")
             if reponse.lower() != "oui":
                continuer = False
                continue

       reponse = input("Connaissez-vous la latitude et la longitude de cette ville ? (oui/non) : ")

       if reponse.lower() == "oui" :
          latitude, longitude = saisir_coordonnees()
          if latitude is None:
             continue 

       else:
          print(f"Recherche automatique des coordonnées de {ville} ")
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

       if donnees is None:
          print("Impossible de récupérer les données météo.")
          continue

       #Sauvegarder les données
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


