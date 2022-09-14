"""module parcelle.py pour définir la classe Parcelle
version 1.0
date 10/09/2022
auteur : Jean-Philippe Trotta
"""
#from geometrie.polygone import Polygone #TODO 
import gzip
import json
#import requests #(TODO problème avec pip install à résoudre)
import urllib
from urllib import request

class Parcelle():
    """
    Attributs:
    ----------
        id_parc : str
            identifiant de la parcelle
        geom_type : str = "polygone"
            ou "multipolygone" ?
        geom_coord : Polygone
            ou Multipoligone ??
    """
    def __init__(self, id_parc : str, geom_type : str = "polygone", geom_coord = [[]] ): #, geom_coord : Polygone
        """constructeur de la classe Parcelle

        """
        self.id_parc = id_parc
        self.geom_type = geom_type
        self.geom_coord = geom_coord

    def ident_commune(self):
        id=""
        for i in range(5):
            id = id + self.id_parc[i]
        return id

    def ident_departement(self):
        return self.id_parc[0]+self.id_parc[1]




# à modifier cf tp2

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
        #méthode statique car commune à la classe Parcelle et Commune (voir si nécessaire du créer une classe mère commune)
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

  


    url=url_json(id_dep="13")
    print(url)
    with gzip.open(url, "rb") as file:
        data = json.loads(file.read(), encoding="utf-8")

    #autre essai
    #fich = urllib.urlopen(url)
    #print(json.loads(fich.read()))

    #data= requests.get(url).json()
