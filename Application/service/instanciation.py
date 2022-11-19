"""module instanciation.py pour définir la classe Instanciation
version 1.0
date 20/10/2022
auteur : Jean-Philippe Trotta
"""

from client.lien_service import LienService
from objets.zone.parcelle import Parcelle
from objets.zone.commune import Commune
from objets.zone.zonage import Zonage
#from objets.zone.departement import Departement

class Instanciation():
    def __init__(self, zonage1:str, id1:str, zonage2:str, date:str ) -> dict:
        '''constructeur
        Paramètres:
        -----------
        zonage1: échelon principal (departement ou commune)
        id1: identifiant de l'échelon principal
        zonage2: échelon secondaire (découpage de l'échelon principal)  commune ou parcelle
        date: date du fichier'''
        self.dico = {"zonage1": zonage1, "id1": id1, "zonage2": zonage2, "date": date}

    def instancier_zonage(self)->list[Zonage]:
        '''créer une liste d'instances de Commune ou Parcelle à partir d'une liste de dictionnaires demandée au client'''
        list_dico=LienService(self.dico).genere_dico()
        list_zonage=[]
        if self.dico["zonage2"]=="commune":
            for dico in list_dico:
                list_zonage.append(Commune(id=dico["id"], geom_coord=dico["geometry"]["coordinates"], nom=dico["properties"]["nom"]))
        elif self.dico["zonage2"]=="parcelle":
            for dico in list_dico:
                list_zonage.append(Parcelle(id=dico["id"], geom_coord=dico["geometry"]["coordinates"]))

        return list_zonage


    




    

test= Instanciation("dep","13","com","latest").dico
print(test["zonage1"])
