"""module instanciation.py pour définir la classe Instanciation
version 1.0
date 20/10/2022
auteur : Jean-Philippe Trotta
"""

from client.lien_service import LienService
from objets.zone.parcelle import Parcelle
from objets.zone.commune import Commune
from objets.zone.zonage import Zonage
from objets.geometrie.polygone import Polygone
from objets.geometrie.multi_polygone import MultiPolygone
#from objets.zone.departement import Departement

class Instanciation():
    def __init__(self, zonage1:str, id1:str, zonage2:str, date:str ) -> dict:
        '''constructeur
        Paramètres:
        -----------
        zonage1: échelon principal (departements ou communes)
        id1: identifiant de l'échelon principal
        zonage2: échelon secondaire (découpage de l'échelon principal)  communes ou parcelles
        date: date du fichier'''
        self.dico = {"zonage1": zonage1, "id1": id1, "zonage2": zonage2, "date": date}


    def instancier_zonage(self)->list[Zonage]:
        '''créer une liste d'instances de Commune ou Parcelle à partir d'une liste de dictionnaires demandée au client'''
        list_dico = LienService(self.dico).genere_dico() #bug ici pour parcelle
        #print(list_dico)
        list_zonage = []
        if self.dico["zonage2"] == "communes":
            for dico in list_dico:
                list_zonage.append(Commune(id=dico["id"], geom_coord= MultiPolygone(liste_brute= dico["geometry"]["coordinates"]), nom= dico["properties"]["nom"]))
        elif self.dico["zonage2"]=="parcelles":
            for dico in list_dico:
                list_zonage.append(Parcelle(id=dico["id"], geom_coord= Polygone(liste_brute= dico["geometry"]["coordinates"]))) #à vérifier

        return list_zonage

#test
#insta = Instanciation(zonage1="departements", id1="13", zonage2="communes", date="latest")

#print(insta.dico)
#print(insta.dico["zonage1"])

#liste = insta.instancier_zonage()
#print(liste[0].id)

