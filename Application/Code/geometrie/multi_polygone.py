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
        rectangle= slef[0].rectangle_circonscrit()
        for i in range(1,len(self)):
            rectangle= rectangle.union_rectangle(autre_rect= self[i].rectangle_circonscrit())
        return rectangle

    def test_polyg_contigu (self, autre_polyg : AbstractPolygone ) -> bool: #j'ai remplacé Polygone par AbstractPolygone (récursivité possible)
        for polyg in self:
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
        for polyg in self:
            if autre_multipolyg.test_poly_contigu(autre_polyg= polyg):
                return True
        return False


    



    
    def __str__(self) -> str:
        """affichage"""
        print("multi-polygone:")
        return "\n".join("{}#".format(str(self.liste_polyg[i])) for i in range(len(self.liste_polyg)))

