"""module multi_polygone.py pour définir la classe MultiPolygone
version 1.0
date 10/09/2022
auteur : Jean-Philippe Trotta
"""
from polygone import Polygone

class MultiPolygone():
    """Classe MultiPolygone
    Attributs :
    -----------
        liste_polyg : list [Polygone]
    
    """
    

    def __init__(self, liste_brute : list[list[list[float]]]):
        """constructeur de la classe MultiPolygone
        Paramètres
        ----------
            liste_brute : list [ list [ list[float] ] ]
        """
        liste_polyg = []
        for i in range(len(liste_brute)):
            liste_polyg.append(Polygone(liste_brute[i]))
        self.liste_polyg = liste_polyg


    
    def __str__(self) -> str:
        """affichage"""
        print("multi-polygone:")
        return "\n".join("{}#".format(str(self.liste_polyg[i])) for i in range(len(self.liste_polyg)))

