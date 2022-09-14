"""module rectangle.py pour définir la classe Rectangle
version 1.0
date 10/09/2022
auteur : Jean-Philippe Trotta
"""
from point import Point


class Rectangle():
    """Classe Rectangle
    Attributs :
    -----------
        lat_min : float
        lat_max : float
        long_min : float
        long_max : float
    
    """
    def __init__(self, lat_min : float, lat_max : float, long_min : float, long_max : float):
        """constructeur de la classe Rectangle
        Paramètres
        ----------
            lat_min : float
            lat_max : float
            long_min : float
            long_max : float
        """
        self.lat_min = lat_min
        self.lat_max = lat_max
        self.long_min = long_min
        self.long_max = long_max
    
    def test_point_inclus ( self, autre_point : Point ) -> bool:
        """teste si un point est inclus dans un rectangle
        """
        print("test inclusion dans rectangle") # TODO à supprimer à la fin
        return (autre_point.latitude <= self.lat_max) and (autre_point.latitude >= self.lat_min) and (autre_point.longitude <= self.long_max) and (autre_point.longitude >= self.long_min)

    def __str__(self) -> str:
        """affichage"""
        print("rectangle:")
        return "Latitude min : {}; latitude max: {}; longitude min: {}; longitude max: {})".format(self.lat_min, self.lat_max, self.long_min, self.long_max)

