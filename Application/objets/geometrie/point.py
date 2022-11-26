"""module point.py pour définir la classe Point
version 1.0
date 10/09/2022
auteur : Jean-Philippe Trotta
"""
from math import sqrt

class Point():
    """Classe Point
    Attributs :
    -----------
        latitude : float
        longitude : float
    
    """
    def __init__(self, liste_coordo : list[float]):
        """constructeur de la classe Point
        Paramètres
        ----------
            liste_coordo : list [float]
        """
        self.latitude = liste_coordo[0]
        self.longitude = liste_coordo[1]

    def distance(self, autre_point) -> float :
        return sqrt((self.latitude - autre_point.latitude)**2 + (self.longitude - autre_point.longitude)**2)

    def test_proxim(self, autre_point, erreur : float) -> bool:
        return self.distance(autre_point= autre_point) < erreur

    def test_egal (self, autre_point) -> bool:
        """teste d'égalité avec un 2ème point
        Parametre:
        ----------
            autre_point : Point
        """
        #print("test d'égalité de points") # TODO à supprimer à la fin
        #return (autre_point.latitude == self.latitude) and (autre_point.longitude == self.longitude)
        return self.test_proxim(autre_point= autre_point, erreur=0.0001) #à tester avec une erreur raisonnable ? 

    def __str__(self) -> str:
        """affichage"""
        #print("point:")
        return "( {} ; {} )".format(self.latitude, self.longitude)
