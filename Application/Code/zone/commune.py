"""module commune.py pour définir la classe Commune
version 1.1
date 18/09/2022
auteur : Jean-Philippe Trotta
"""

import gzip
import json
#import requests #(TODO problème avec pip install à résoudre)
import urllib
from urllib import request

from zonage import Zonage

from Application.Code.geometrie.polygone import Polygone
from Application.Code.geometrie.multi_polygone import MultiPolygone

class Commune(Zonage):
    """
    Attributs:
    ----------
        id : str
            identifiant de la commune
        geom_coord : MultiPolygone
    """


m1=MultiPolygone([[[2,1],[3,5],[2,7]],[[0,0]]],[[[1,1],[3,5],[0,0]]])

com1= Commune(id="13400", geom_coord=m1)
print(com1)
