import pytest
from meteo import Meteo
from stockage import Stockage
from geocodage import Geocodage


class TestMeteo:
    """Tests pour la classe Meteo."""
    def test_creation_objet_meteo(self):
        """Vérifie qu'on peut créer un objet Meteo."""
        meteo = Meteo("Cotonou",6.3676, 2.4252)
        assert meteo.get_latitude() == 6.3676
        assert meteo.get_longitude() == 2.4252

    def test_get_latitude(self):
        """Vérifie que get_longitude retourne la onne valeur."""
        meteo = Meteo("Parakou", 9.3370, 2.6280)
        assert meteo.get_latitude() == 9.3370

    def test_get_longitude(self):
        """Vérifie que get longitude retourne la bonne valeur."""
        meteo = Meteo("Parakou", 9.3370, 2.6280)


class TestStockage:
    """Test pour la classe Stockage."""

    def test_sauvegerde_et_charger(self):
        """Vérifie qu'on peut sauvegarder et charger des données."""
        stockage = Stockage("test_donnees.json")
        donnees_test = {"daily":{"température_2m_max":[30.0], "température_2m_min":[20.0] }}
        stockage.sauvegarder("TestVille", donnees_test)
        donnees_chargees = stockage.charger_ville("TestVille")
        assert donnees_chargees == donnees_test

    def test_ville_existe(self):
        """Vérifie que ville_existe fonctionne correctement."""
        stockage = Stockage("test_donnees.json")
        assert stockage.ville_existe("TestVille") == True


    def test_ville_inexistante(self):
        """Vérifie que ville inexistante retourne False."""
        stockage = Stockage("test_donnees.json")
        assert stockage.ville_existe("VilleInexistante") == False



class TestGeocodage:
    """Tests pour la classe Geocodage"""
    def test_creation_objet_geocodage(self):
        """Verifie qu'on peut créer un objet Geocodage."""
        geo = Geocodage("Cotonou")
        assert geo is not None





