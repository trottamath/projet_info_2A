"""module point.py pour définir la classe Point
version 1.0
date 10/09/2022
auteur : Jean-Philippe Trotta
"""

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

    def test_egal (self, autre_point) -> bool:
        """teste d'égalité avec un 2ème point
        Parametre:
        ----------
            autre_point : Point
        """
        #print("test d'égalité de points") # TODO à supprimer à la fin
        return (autre_point.latitude == self.latitude) and (autre_point.longitude == self.longitude)

    def __str__(self) -> str:
        """affichage"""
        print("point:")
        return "( {} ; {} )".format(self.latitude,self.longitude)


