"""module polygone.py pour définir la classe Polygone
version 1.1
date 18/09/2022
auteur : Jean-Philippe Trotta
"""
from objets.geometrie.point import Point
from objets.geometrie.segment import Segment
from objets.geometrie.rectangle import Rectangle
from objets.geometrie.abstract_polygone import AbstractPolygone
import doctest

class Polygone(AbstractPolygone):
    """Classe Polygone
    Attributs :
    -----------
        liste_poly_geom : list [ list[Segment] ]
            liste de polygones au sens géométrique
    
    """
    def __init__(self, liste_brute : list [ list [ list[ float ] ] ] ):
        """constructeur de la classe Polygone (au sens du cadastre)
        Paramètres
        ----------
            liste_brute : list [ list [ list[ float ] ] ] 
                la list [float] la plus à l'intérieur correspond à des coordonnées de points (latitude et longitude)
                la list [ list[ float ] ]  est une liste de coordonnées de points (les sommets d'un polygone au sens géométrique ) 
                enfin list [ list [ list[ float ] ] ]  est un polygone au sens du cadastre i.e une liste de polygones dont 
                    le 1er est la bordure extérieure et les éventuels suivants sont des trous (pour une parcelle)
        """
        liste_poly_geom = []
        #1ère boucle sur la liste de polygones au sens géométrique
        for i in range(len(liste_brute)):
            # initialisation : création du segment passant par le 1er et dernier point de la liste des sommets
            liste_segments = [Segment(point1 = Point(liste_brute[i][-1]), point2 = Point(liste_brute[i][0]))]

            #boucle sur la liste des points d'un polygone au sens géométrique
            for j in range(len(liste_brute[i])-1):
                liste_segments.append(Segment(point1 = Point(liste_brute[i][j]), point2 = Point(liste_brute[i][j+1])))
            
            liste_poly_geom.append(liste_segments)
        
        self.liste_poly_geom = liste_poly_geom

    def test_segment(self, autre_segment : Segment) -> bool:
        """teste si un segment appartient au 1er polygone géométrique
        """
        print("test d'appartenance d'un segment au polygone principal (bordure)") # à supprimer à la fin TODO
        for sgm in self.liste_poly_geom[0]:
            if autre_segment.test_egal(sgm):
                return True
        return False

    def rectangle_circonscrit (self) -> Rectangle:
        """retourne le plus petit rectangle qui inclus le polygone géométrique extérieur (selon ces latitudes et longitudes extrèmes)
        """
        print("recherche du rectangle circonscrit") # TODO à supprimer à la fin

        #initialisation sur les coordonnées du 1er point du 1er segment du polygone géométrique extérieur
        sgm = self.liste_poly_geom[0][0]
        lat_min = sgm.point1.latitude
        lat_max = sgm.point1.latitude
        long_min = sgm.point1.longitude
        long_max = sgm.point1.longitude
        # boucle de recherche des extrema
        for sgm in self.liste_poly_geom[0]:
            if sgm.point1.latitude > lat_max:
                lat_max = sgm.point1.latitude
            if sgm.point1.latitude < lat_min:
                lat_min = sgm.point1.latitude
            if sgm.point1.longitude > long_max:
                long_max = sgm.point1.longitude
            if sgm.point1.longitude < long_min:
                long_min = sgm.point1.longitude
        return Rectangle(lat_min = lat_min, lat_max = lat_max, long_min = long_min, long_max = long_max)

    def test_polyg_contigu (self, autre_polyg ) -> bool: #TODO à tester (car modifié)
        """ teste si deux polygones ont au moins un segment commun
                le test s'effectue sur les polygones géométriques extérieurs
        Paramètre:
        ----------
            autre_polyg : Polygone
        """
        print("test polygones contigus") # TODO à supprimer à la fin
        if self.test_polyg_proche(autre_polyg= autre_polyg):  
            for sgm1 in self.liste_poly_geom[0]:
                if autre_polyg.test_segment(autre_segment=sgm1):
                    return True
        return False

    def __str__(self) -> str:
        """affichage
        """
        print("sommets du polygone extérieur:")
        return "".join("{}/".format(str(self.liste_poly_geom[0][i].point1)) for i in range(len(self.liste_poly_geom[0])))
