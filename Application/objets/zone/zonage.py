"""module zonage.py pour définir la classe Zonage
version 1.0
date 18/09/2022
auteur : Jean-Philippe Trotta
"""

import gzip
import json
#import requests #(TODO problème avec pip install à résoudre)
import urllib
from urllib import request

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

    def ident_departement(self):
        return self.id[0] + self.id[1]


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

