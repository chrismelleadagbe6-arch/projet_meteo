import tkinter as tk
from tkinter import messagebox
from meteo import Meteo
from stockage import Stockage
from geocodage import Geocodage



class Interface:
    """Interface graphique pour l'Explorateur de données Météo."""


    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Explorateur de Données Météo")
        self.fenetre.geometry("500x600")
        self.fenetre.configure(bg="#99C3FF")
        self.stockage = Stockage()
        self.creer_widgets()

    def creer_widgets(self):
        """Créer tous les éléments de l'interface."""


        #Titre
        titre = tk.Label(
            self.fenetre,
            text="Explorateur de Données Météo",
            font=("Arial", 16, "bold"),
            bg="#1A3557",
            fg="#FFFFFF"
        )
        titre.pack(pady=20)

        #  Champ ville
        tk.Label(
            self.fenetre, 
            text="Nom de la ville : ",
            font=("Arial", 11),
            bg="#1A3557",
            fg="white"
        ).pack()
        
        self.champ_ville = tk.Entry(self.fenetre, font=("Arial", 12), width=30)
        self.champ_ville.pack(pady=5)

        # Bouton recherche automatique
        btn_auto=tk.Button(
            self.fenetre,
            text="Recherche automatique",
            font=("Arial", 11),
            bg="#1A3557",
            fg="white",
            command=self.recherche_automatique
        )
        btn_auto.pack(pady=5)

        # Separateur
        tk.Label(
            self.fenetre,
            text="==== Entrer les coordonnées=== ",
            font=("Arial",10),
            bg="#1A3557",
            fg="#D6E4F0"
        ).pack(pady=10)

        #Champ latitude
        tk.Label(
            self.fenetre,
            text="Latitude",
            font=("Arial", 11),
            bg="#1A3557",
            fg="white"
        ).pack()

        self.champ_latitude = tk.Entry(self.fenetre,font=("Arial", 12), width=30)
        self.champ_latitude.pack(pady=5)


        #Champ longitude
        tk.Label(
            self.fenetre,
            text="Longitude",
            font=("Arial", 11),
            bg="#1A3557",
            fg="white"
        ).pack()
    
        self.champ_longitude = tk.Entry(self.fenetre,font=("Arial", 12), width=30)
        self.champ_longitude.pack(pady=5)

        #Bouton recherche manuelle
        btn_manuel=tk.Button(
            self.fenetre,
            text="Recherche manuelle",
            font=("Arial", 11),
            bg="#1A3557",
            fg="white",
            command= self.recherche_manuelle
        )
        btn_manuel.pack(pady=5)

        #Zone résultats
        self.zone_resultats=tk.Text(
            self.fenetre,
            font=("Arial", 11),
            width=45,
            height=10,
            bg="#D6E4F0",
            fg="#1A3557"
        )
        self.zone_resultats.pack(pady=5)


    def afficher_resultats(self,ville,donnees):
        """Affiche les statistiques dans la zone de résultats."""
        try:
            temperatures_max = donnees["daily"]["temperature_2m_max"]
            temperatures_min = donnees["daily"]["temperature_2m_min"]

            temp_max = max(temperatures_max)
            temp_min = min(temperatures_min)
            temp_moyenne = sum(temperatures_max)/len(temperatures_max)

            self.zone_resultats.insert(tk.END, f"\n=== Météo de {ville}===\n")
            self.zone_resultats.insert(tk.END, f"Température maximale: {temp_max}°C \n")
            self.zone_resultats.insert(tk.END, f"Température minimale : {temp_min}°C \n")
            self.zone_resultats.insert(tk.END, f"Température moyenne : {temp_moyenne:.1f}°C\n")
            self.zone_resultats.insert(tk.END, f"Données sauvegardées")

        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur : {e}")


    def recherche_automatique(self):
        """Recherche les coordonnées automatiquement"""
        ville= self.champ_ville.get().strip()
        if not ville:
            messagebox.showwarning("Attention", "Veuillez entrer le nom d'une ville")
            return
        
        try:
            geo=Geocodage(ville)
            latitude, longitude = geo.get_coordonnees()
            if latitude is None:
                messagebox.showerror("Erreur",f"La ville {ville}  est introuvable")
                return
            meteo = Meteo(ville, latitude, longitude)
            donnees = meteo.recuperer_donnees()
            if donnees is None:
                messagebox.showerror("Erreur", "Impssible de récupérer les donnes météo")
                return
            self.stockage.sauvegarder(ville, donnees)
            self.afficher_resultats(ville, donnees)
       
        except Exception as e:
            messagebox.showerror("Erreur",f"Erreur:{e}")

    def recherche_manuelle(self):
        """Recherche avec les coordonnées manuelles"""
        ville = self.champ_ville.get().strip()
        if not ville:
            messagebox.showwarning("Veuillez entrer le nom de la ville")
            return
        try:
            latitude = float(self.champ_latitude.get())
            longitude = float(self.champ_longitude.get())
            meteo = Meteo(ville, latitude, longitude)
            donnees = meteo.recuperer_donnees()
            if donnees is None:
                messagebox.showerror("Erreur", "Impossible de récupérer les données météo")
                return
            self.stockage.sauvegarder(ville, donnees)
            self.afficher_resultats(ville, donnees)
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur:{e}")    

if __name__=="__main__":
    fenetre = tk.Tk()
    app = Interface(fenetre)
    fenetre.mainloop()

