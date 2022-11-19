"""module commune.py pour définir la classe Commune
version 1.1
date 18/09/2022
auteur : Jean-Philippe Trotta
"""


from objets.zone.zonage import Zonage
from objets.zone.parcelle import Parcelle

from objets.geometrie.polygone import Polygone
from objets.geometrie.multi_polygone import MultiPolygone

class Commune(Zonage):
    """
    Attributs:
    ----------
        id : str
            identifiant de la commune
        geom_coord : MultiPolygone
        nom : str
            nom de la commune
    """
    def __init__(self, id : str, geom_coord : MultiPolygone, nom : str):
        '''constructeur de la classe Commune'''
        #super().__init__(self, id= id, geom_coord= geom_coord) TODO bug à corriger
        self.id = id
        self.geom_coord = geom_coord
        
        
        self.nom = nom
    

    def lien_zone(self, autre_zone : Zonage) -> str: #pas forcément utilisé
        """si autre_zone est une commune contigue, retourne "contigues"
            si autre_zone est une commune non-contigue, retourne "non-contigues"
            si autre_zone est une parcelle contigue, retourne "contigue"
            si autre_zone est une parcelle à la limite, retourne "limite"
            si autre_zone est une parcelle strictement à l'intérieur de la commune, retourne "interieure"
            si autre_zone est une parcelle à l'extérieur et non-contigues, retourne "disjointe"
        """
        # on teste si autre_zone est une parcelle (identifiant à plus de 5 caractères)
        if len(autre_zone.id)>5:
            # ensuite on teste si les polygones (de la parcelle et de la commune) sont contigues (un segment commun)
            if self.geom_coord.test_polyg_contigu(autre_zone.geom_coord):
                # enfin on teste si la parcelle est dans la commune (à l'aide de l'identifiant)
                if self.id == autre_zone.ident_commune():
                    return "limite"
                else:
                    return "contigue"
            else:
                if self.id == autre_zone.ident_commune():
                    return "interieure"
                else:
                    return "disjointe"
        else:
            if self.geom_coord.test_polyg_contigu(autre_zone.geom_coord):
                return "contigues"
            else:
                return "non-contigues"

    def __str__(self):
        return "{}_{}".format(self.id,self.nom)


#m1=MultiPolygone([[[[2,1],[3,5],[2,7]],[[0,0],[3,5],[2,7]]],[[[1,1],[3,5],[0,0]]]])  #bug TODO

#com1= Commune(id="13400", geom_coord=m1,nom="coucou")
#print(com1)
