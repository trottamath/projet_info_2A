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

    @staticmethod
    def ss_str(chaine: str, nbr_caract: int):
        '''pour une chaine de caractère donnée, et nbr_caract un nombre entier de caractères à conserver
        retourne les nbr_caract premiers caractères de la chaine'''
        firsts=""
        for i in range(nbr_caract):
            firsts = firsts + chaine[i]
        return firsts

    @staticmethod
    def ident_dep(id: str):
        id_dep= id[0] + id[1]
        if id_dep == "97":
            id_dep = id_dep + id[2]
        return id_dep

    

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
                ss_list.append(zone)  # ou avec zone.id
        return ss_list #selon les besoins, on aurait pu ne retourner que la liste des identifiants
    
    def __str__(self):
        return self.id

#print(Zonage(id="20", geom_coord=[]))
