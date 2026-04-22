# Explorateur de Donnée Météo

## Description
Application Python qui récupère des données météorolgiques réelles via l'API Open-Meteo, les stocke en JSON et affiche des statistiques comparatives.

## Auteur
- ADAGBE Chrismelle Mauricette M. 
- TOSSOUVI Stephen Richard
- Niveau : L2
- Projet N°3

## Fonctionnalités 
* Recherche météo par ville
* Recherche automatique des coordonnées GPS
* Saisie manuelle de la latitude et longitude
* Affichage des températures max, min et moyenne
* Sauvegarde des données en JSON

## Structure de projet
- api_base.py : Classe mère (POO)
- meteo.py : Récupération des données météo
- geocodage.py : Recherche automatique des coordonnées
- stockage.py : Sauvegarde des données en JSON
- main.py : Programme principal

## Installation
1- Cloner le dépôt
2- Créer l'environnement virtuel : python -m venv venv
3- Activer le venv : .\venv\Scripts\activate
4- Installer les dépendances : pip install -r requirements.txt

## Lancement 
python main.py

## API utilisée
Open-Meteo (gratuite, sans clé API)
https://open-meteo.com