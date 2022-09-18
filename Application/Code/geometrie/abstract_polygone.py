"""module abstract_polygone.py pour définir la classe AbstractPolygone
version 1
date 18/09/2022
auteur : Jean-Philippe Trotta
"""

from rectangle import Rectangle
from abc import ABC, abstractmethod

class AbstractPolygone():
    """classe abstraite pour définir les méthodes communes aux objets de type Polygone et Multipolygone
    """
    def __init__(self):
        pass

    @abstractmethod
    def rectangle_circonscrit(self):
        pass

    def test_intersect_rect (self, rectangle : Rectangle ) -> bool:
        """teste si l' AbstractPolygone (Polygone ou MultiPoligone) est proche d'un rectangle donné
            c'est-à-dire si le rectangle circonscrit à l' AbstractPolygone intersecte le rectangle donnée
        """
        print("test de proximité avec un rectangle") # TODO à supprimer à la fin
        return rectangle.test_intersect_rect(autre_rect= self.rectangle_circonscrit())

    def test_polyg_proche (self, autre_polyg ) -> bool:
        """teste si un autre AbstractPolygone donné est proche de l' AbstractPolygone initial 
                c'est-à-dire si leur rectangle circonscrit respectif s'intersectent
        Paramètre:
        ----------
            autre_polyg : AbstractPolygone
        """
        print("test polygones proches") # TODO à supprimer à la fin
        return autre_polyg.test_intersect_rect(self.rectangle_circonscrit())
