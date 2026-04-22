class APIBase:
    """Classe mère pour toutes les classes qui appellent une API."""

    def __init__(self, ville):
        self.ville = ville

    def get_ville(self):
        """Retourne le nom dela ville."""
        return self.__ville

    def set_ville(self, ville):
        """Modifie le nom de la ville."""
        self.__ville = ville


    def recuperer_donnees(self):
        """Méthode à redéfinir dans les classes filles."""
        raise NotImplementedError("Méthode qui doit être implémentée dans la classe fille.")    