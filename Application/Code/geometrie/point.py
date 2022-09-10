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
    def __init__(self,liste_coordo : list[float]):
        """constructeur de la classe Point
        Paramètres
        ----------
            liste_coordo : list [float]
        """
        self.latitude = liste_coordo[0]
        self.longitude = liste_coordo[1]


