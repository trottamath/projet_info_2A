"""module polygone.py pour définir la classe Polygone
version 1.0
date 10/09/2022
auteur : Jean-Philippe Trotta
"""
from point import Point
from rectangle import Rectangle
import doctest

class Polygone():
    """Classe Polygone
    Attributs :
    -----------
        liste_points : list [Point]
    
    """
    def __init__(self, liste_brute : list[list[float]]):
        """constructeur de la classe Polygone
        Paramètres
        ----------
            liste_brute : list [ list[float] ]
        """
        liste_points = []
        for i in range(len(liste_brute)):
            liste_points.append(Point(liste_brute[i]))
        self.liste_points = liste_points
    
    def test_sommet(self, autre_point : Point) -> bool:
        """teste si un point est un sommet du polygone
        """
        print("teste de sommet") # à supprimer à la fin TODO
        for pt in self.liste_points:
            if autre_point.test_egal(pt):
                return True
        return False

    def rectangle_circonscrit (self) -> Rectangle:
        """retourne le plus petit rectangle qui inclus le polygone (selon ces latitudes et longitudes extrèmes)
        """
        print("recherche du rectangle circonscrit") # TODO à supprimer à la fin
        
        #initialisation sur les coordonnées du 1er point du polygone
        pt = self.liste_points[0]
        lat_min = pt.latitude
        lat_max = pt.latitude
        long_min = pt.longitude
        long_max = pt.longitude
        # boucle de recherche des extrema
        for pt in self.liste_points:
            if pt.latitude > lat_max:
                lat_max = pt.latitude
            if pt.latitude < lat_min:
                lat_min = pt.latitude
            if pt.longitude > long_max:
                long_max = pt.longitude
            if pt.longitude < long_min:
                long_min = pt.longitude
        return Rectangle(lat_min = lat_min, lat_max = lat_max, long_min = long_min, long_max = long_max)

    def test_intersect_rect (self, rectangle : Rectangle ) -> bool:
        """teste si le polygone a au moins un sommet à l'intérieur (ou en contact) d'un rectangle donné
        """
        print("test d'intersection avec un rectangle") # TODO à supprimer à la fin
        for pt in self.liste_points:
            if rectangle.test_point_inclus(pt):
                return True
        return False

    def test_point_proche (self, autre_point : Point ) -> bool:
        """teste si un point est dans le voisinage du polygone (c'est-à-dire inclus dans le rectangle circonscrit)
        """
        print("test point voisin") # TODO à supprimer à la fin
        return self.rectangle_circonscrit().test_point_inclus(autre_point)

    def test_polyg_proche (self, autre_polyg ) -> bool:
        """teste si un autre polygone donné rencontre le rectangle circonscrit au polygone initial 
        (voire teste si chaque polygone rencontre le rectangle circonscrit de l'autre)
        Paramètre:
        ----------
            autre_polyg : Polygone
        """
        print("test polygone proche") # TODO à supprimer à la fin
        return autre_polyg.test_intersect_rect(self.rectangle_circonscrit()) and self.test_intersect_rect(autre_polyg.rectangle_circonscrit()) # TODO tester sans le and si trop lent

    def test_polyg_contigu (self, autre_polyg ) -> bool:
        """ teste si deux polygones ont strictement plus d'un sommet commun
        Paramètre:
        ----------
            autre_polyg : Polygone
        """
        print("test polygones contigus") # TODO à supprimer à la fin
        nb = 0 
        for pt1 in self.liste_points:
            if autre_polyg.test_sommet(pt1):
                nb += 1
        return nb>1

    def __str__(self) -> str:
        """affichage
        """
        print("polygone:")
        return "/".join("{}/".format(str(self.liste_points[i])) for i in range(len(self.liste_points)))
