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
        for dico in list_dico:
            if dico["zonage2"]=="commune":
                list_zonage.append(Commune(id=dico["id"], geom_coord=dico["coordinates"], nom=dico["nom"]))
            elif dico["zonage2"]=="parcelle":
                list_zonage.append(Parcelle(id=dico["id"], geom_coord=dico["coordinates"]))
        return list_zonage


    




    

test= Instanciation("dep","13","com","latest").dico
print(test["zonage1"])
