"""module polygone.py pour définir la classe Polygone
version 1.0
date 10/09/2022
auteur : Jean-Philippe Trotta
"""
from point import Point
from rectangle import Rectangle

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
            


    

    def __str__(self) -> str:
        """affichage
        """
        print("polygone:")
        return "/".join("{}/".format(str(self.liste_points[i])) for i in range(len(self.liste_points)))


p1 = Polygone([[5425.25,5545],[654436,25545.444],[5425,5545.3254],[654436.65,25545]])
print(p1.rectangle_circonscrit())