"""module session.py pour définir la classe Session
version 1.0
date 25/10/2022
auteurs : Fiona Fonkou et Jean-Philippe Trotta
"""
from utils.singleton import Singleton

class Session(metaclass = Singleton):
    '''classe Session définie comme Singleton pour l'unicité de connexion à la bdd'''
    def __init__(self):
        """
        Définition des variables que l'on stocke en session
        La syntaxe => ref:type = valeur nous permet de donner le type des variables.
        """
        self.date : str = "latest" #date du fichier
        self.num : str = None #numero de la requete
        self.id : str = None #identifiant de la commune ou parcelle
        self.list_res : list = None #liste des identifiants récupéré par la couche service
        self.user_name : str = "utilisateur" #au cas où cela soit utile dans une version 
