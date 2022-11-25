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
    def __init__(self, id : str, geom_coord : Polygone ):
        """contructeur de la classe Parcelle"""
        #super().__init__(self, id= id, geom_coord= geom_coord) TODO bug
        self.id = id
        self.geom_coord = geom_coord

    def ident_commune(self): 
        """retourne l'identifiant de la commune dont la parcelle est issue
        """
        id = ""
        for i in range(5):
            id = id + self.id_parc[i]
        return id

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


#Test ok
#parc=Parcelle(id="20", geom_coord=Polygone([[[5425.25,5545],[654436,25545.444],[5425,5545.3254],[654436.65,25545]],[[12,322],[4,10],[35,44]]]))
#print(parc.geom_coord)
#print(parc)
#parc2=Parcelle(id="20", geom_coord=Polygone([[[5425,5544],[654436,25545.444],[5426,5546],[654437,25546]]]))
#print(parc.lien_zone(autre_parcelle = parc2))
#print(parc.lien_zone(autre_parcelle = parc))
