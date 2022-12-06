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

    def __init__(self, liste_coordo: list[float]):
        """constructeur de la classe Point
        Paramètres
        ----------
            liste_coordo : list [float]
        """
        self.latitude = liste_coordo[0]
        self.longitude = liste_coordo[1]

    def distance(self, autre_point) -> float:
        '''calcule la distance entre 2 points, valable pour des petites
        distances (approximation euclidienne)
        Paramètre:
        ----------
            autre_point : Point'''
        return sqrt((self.latitude - autre_point.latitude)**2 +
                    (self.longitude - autre_point.longitude)**2)

    def test_proxim(self, autre_point, erreur: float) -> bool:
        '''teste si deux points sont à un plus petite distance 
        que l'erreur autorisée
        Paramètres:
        -----------
            autre_point : Point
            erreur : float'''
        return self.distance(autre_point=autre_point) < erreur

    def test_egal(self, autre_point) -> bool:
        """teste d'égalité avec un 2ème point
        Parametre:
        ----------
            autre_point : Point
        """
        # print("test d'égalité de points") # TODO à supprimer à la fin
        return (autre_point.latitude == self.latitude) and (autre_point.longitude == self.longitude)
        # à tester avec une erreur raisonnable ?
        #return self.test_proxim(autre_point=autre_point, erreur=0.0002)

    def __str__(self) -> str:
        """affichage"""
        # print("point:")
        return "( {} ; {} )".format(self.latitude, self.longitude)
