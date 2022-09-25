"""module parcelle.py pour définir la classe Parcelle
version 1.1
date 18/09/2022
auteur : Jean-Philippe Trotta
"""

import gzip
import json
#import requests #(TODO problème avec pip install à résoudre)

from urllib import request
from zonage import Zonage

from Application.Code.geometrie.polygone import Polygone

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




# à modifier cf tp2 et à déplacer dans la classe mère (ou dans une classe import ?)

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
