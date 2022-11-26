"""module storage.py pour définir la classe Storage
version 1.0
date 05/11/2022
auteur : Chloé Contant
"""
from abc import ABC, abstractmethod

class Storage(ABC):
    '''Classe qui permet de gérer le stockage des fichiers,
        elle supprime les fichiers s'ils sont trop nombreux dans un dossier.
        Attributes
        ----------'''

    @abstractmethod
    def count():
        '''Méthode qui compte le nombre de fichiers qu'il y a dans le dossier'''
        pass

    @abstractmethod
    def delete_older_file():
        '''Méthode qui supprime le fichier le plus ancien d'un dossier pour libérer de la place.'''
        pass