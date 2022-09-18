"""module multi_polygone.py pour définir la classe MultiPolygone
version 1.1
date 18/09/2022
auteur : Jean-Philippe Trotta
"""

from rectangle import Rectangle
from abstract_polygone import AbstractPolygone
from polygone import Polygone

class MultiPolygone(AbstractPolygone):
    """Classe MultiPolygone
    Attributs :
    -----------
        liste_polyg : list [Polygone]
    
    """

    def __init__(self, liste_brute :  list[ list [ list[ list[ float ] ] ] ]):
        """constructeur de la classe MultiPolygone
        Paramètres
        ----------
            liste_brute :  list[ list [ list[ list[ float ] ] ] ]
        """
        liste_polyg = []
        for i in range(len(liste_brute)):
            liste_polyg.append(Polygone(liste_brute[i]))
        self.liste_polyg = liste_polyg

    def rectangle_circonscrit(self) -> Rectangle:
        """retourne le plus petit rectangle qui inclus tous les polygones du multipolygone
        """
        poly_ext = self.liste_polyg[0]
        rectangle = poly_ext.rectangle_circonscrit()
        for i in range(1,len(self.liste_polyg)):
            poly_ext = self.liste_polyg[i]
            rectangle = rectangle.union_rectangle(autre_rect= poly_ext.rectangle_circonscrit())
        return rectangle

    def test_polyg_contigu (self, autre_polyg : AbstractPolygone ) -> bool: #j'ai remplacé Polygone par AbstractPolygone (récursivité possible si autre_polyg est un multipolygone)
        """teste si un AbstractPolygone donné est contigu à ce MultiPolygone
        """
        if self.test_polyg_proche(autre_polyg):
            for polyg in self.liste_polyg:
                if autre_polyg.test_polyg_contigu(polyg):
                    return True
        return False
    
    #supprimmer la méthode suivante si le paramètre autre_polyg de la précédante peut être de type AbstractPolygone
    def test_multipolyg_contigu (self, autre_multipolyg ) -> bool:
        """teste si un autre multipolygone est contigu à celui-ci
        Paramètre :
        -----------
            autre_multipolyg : MultiPolygone
        """
        for polyg in self.liste_polyg:
            if autre_multipolyg.test_polyg_contigu(autre_polyg= polyg):
                return True
        return False
    
    def __str__(self) -> str:
        """affichage"""
        print("multi-polygone:")
        return "\n".join("{}#".format(str(self.liste_polyg[i])) for i in range(len(self.liste_polyg)))

#test polygones contigus
poly8 = Polygone([[[5,1],[4,4],[4,5],[6,6],[6,1]]])
poly9 = Polygone([[[4,4],[4,5],[6,7]]])
print(poly8.test_polyg_contigu(poly9)) #true


#test multipoly
m1 = MultiPolygone([[[[1,5545.3254],[654436.65,25545.444],[5425,11]],[[12,322],[4,10],[35,44]]],[[[2,25545],[654436.65,25545.444],[5425,5545.3254],[654436.65,25545.444],[5425,22]]]])

print(m1)

print(m1.test_polyg_contigu(poly9))