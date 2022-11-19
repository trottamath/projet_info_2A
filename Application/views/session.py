"""module session.py pour définir la classe Session
version 1.0
date 25/10/2022
auteurs : Fiona Fonkou et Jean-Philippe Trotta
"""
from utils.singleton import Singleton
# utiliser Requete(dico_requete= ???? ).Get_or_create()
# voir les clés de dico_requete (à récuperer par Insomnia ?)
            #dico_requete: dict
               # les clées de ce dictionnaire sont
                #num : str
                 #   numero de la requete (1 ou 2 dans le cas de l'appel à la DAO)
                  #  "1" pour les communes contigües à la commune donnée
                   # "2" pour les parcelles en limite de la commune donnée
                    #"3" pour les parcelles contigües à la parcelle donnée
               # id : str
                #    identifiant du zonage donnée
                #date : str
                 #   date du fichier cadatral de référence

class Session(metaclass=Singleton):
    def __init__(self):
        """
        Définition des variables que l'on stocke en session
        La syntaxe => ref:type = valeur nous permet de donner le type des variables.
        """
        self.date: str = "latest" #date du fichier
        self.num: str = None #numero de la requete
        self.id : str = None #identifiant de la commune ou parcelle
        self.list_res: list = None #liste des identifiants récupéré par la couche service
        self.user_name: str = "user" #à voir si c'est utile ?
        

