"""module zonage.py pour définir la classe Zonage
version 1.0
date 18/09/2022
auteur : Jean-Philippe Trotta
"""


from objets.geometrie.polygone import Polygone
from objets.geometrie.multi_polygone import MultiPolygone
from objets.geometrie.abstract_polygone import AbstractPolygone




class Zonage():
    """classe zonage (classe mère commune à Commune et Parcelle)
    Attributs:
    ----------
        id : str
            identifiant de la zone
        geom_coord : AbstractPolygone
    """
    def __init__(self, id : str, geom_coord : AbstractPolygone ):
        """constructeur de la classe Zonage

        """
        self.id = id
        self.geom_coord = geom_coord

    def test_egal_id(self,autre_zone): #à voir si utile
        """teste si deux zonages ont le même identifiant
        Paramètre:
        ----------
            autre_zone : Zonage"""
        return self.id == autre_zone.id


    def ident_departement(self):
        id_dep = self.id[0] + self.id[1]
        if id_dep == "97":
            id_dep = id_dep + self.id[2]
        return id_dep


    def test_zone_proche(self, autre_zone) -> bool:
        """teste si l' autre_zone donnée est proche de cette zone
        Paramètres:
        -----------
            autre_zone : Zonage
        """
        return autre_zone.geom_coord.test_polyg_proche(self.geom_coord)

    def test_zone_contigu(self, macro_zone) -> bool:
        """teste si la macro_zone donnée est contigüe à cette zone
        Paramètres:
        -----------
            macro_zone : Zonage
        """
        return macro_zone.geom_coord.test_polyg_contigu(self.geom_coord)

    def ss_list_contig(self,list_zones) -> list :
        """ extrait une sous-liste de zones contigües
        Parametre:
            list_zones : list [ Zonage ]
            à priori, si c'est une liste de communes, self est aussi une commune
        Return :
            list [ Zonage ]
            """
        ss_list= []
        for zone in list_zones:
            if zone.test_zone_contigu(macro_zone= self) and self.id!=zone.id:
                ss_list.append(zone)
        return ss_list

    
    def __str__(self):
        return self.id

#print(Zonage(id="20", geom_coord=[]))
