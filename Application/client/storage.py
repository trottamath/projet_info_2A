from abc import ABC, abstractmethod
"""module storage.py pour définir la classe Storage
version 1.0
date 05/11/2022
auteur : Chloé Contant
"""

class Storage(ABC):
    '''Classe qui permet de gérer le stockage des fichiers, 
        elle supprime les fichiers s'ils sont trop nombreux dans un dossier.
        Attributes
        ----------'''
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create_place(self):
        '''Méthode qui supprime le fichier le plus ancien d'un dossier pour libérer de la place.'''
        pass
