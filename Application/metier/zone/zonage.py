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

from metier.geometrie.polygone import Polygone
from metier.geometrie.multi_polygone import MultiPolygone
from metier.geometrie.abstract_polygone import AbstractPolygone

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


    @staticmethod
    def url_json(id_dep : str, date = "latest", zonage1 = "departements", id_zone = None, zonage2 = "communes" ):
        """import d'un fichier json à partir du web
        Parametres:
        -----------
            date : str = "latest" 
                sinon saisir au format "AAAA-MM-JJ"
            zonage1 : str = "departements"
                zonage au choix parmi "departements" ou "france" ou "communes"
            id_dep : str
                code de département
            id_zone : str = None
                saisir le code communes si zone1="communes"
            zonage2 : str = "communes"
                zonage au choix parmi "parcelles" ou "communes"
                sauf si zonage1="france" alors laisser par défaut zonage2="communes"
        
        """
        
        url = "https://cadastre.data.gouv.fr/data/etalab-cadastre/"

        if zonage1 == "departements":
            id_zone = id_dep
            url_zone1 = id_dep
        elif zonage1 == "communes":
            url_zone1="{}/{}".format(id_dep,id_zone)

        fichier ="cadastre-{}-{}.json.gz".format(id_zone,zonage2)

        if zonage1 == "france" and zonage2== "communes":
            url = "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/france/cadastre-france-communes.json.gz"
        else:
            url = "{}{}/geojson/{}/{}/{}".format(url,date,zonage1,url_zone1,fichier)
        return url
    
    def __str__(self) -> str:
        return "identifiant : {} \n coordonnées : \n {}".format(self.id, self.geom_coord)
    


