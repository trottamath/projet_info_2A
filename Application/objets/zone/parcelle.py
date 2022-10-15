"""module parcelle.py pour définir la classe Parcelle
version 1.1
date 18/09/2022
auteur : Jean-Philippe Trotta
"""

from objets.zone.zonage import Zonage

from objets.geometrie.polygone import Polygone

class Parcelle(Zonage):
    """
    Attributs:
    ----------
        id_parc : str
            identifiant de la parcelle
        geom_coord : Polygone
    """

    def ident_commune(self): 
        """retourne l'identifiant de la commune dont la parcelle est issue
        """
        id=""
        for i in range(5):
            id = id + self.id_parc[i]
        return id # à vérifier pour les DOM, si les id communes ont aussi 5 caractères

    def lien_zone(self, autre_parcelle) -> str:
        """retourne "contigues" si les deux parcelles sont contigües
                sinon renourne "non-contigues"
        Parametres :
        ------------
            autre_parcelle : Parcelle
        """
        if self.geom_coord.test_polyg_contigu(autre_parcelle.geom_coord):
            return "contigues"
        return "non-contigues"
