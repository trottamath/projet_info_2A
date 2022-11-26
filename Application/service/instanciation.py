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


class Instanciation():
    '''classe qui instancie les objets Commune ou Pacelle
    à partir d'un dictionnaire extrait du geojson par la couche Client'''
    def __init__(
            self,
            zonage1: str,
            id1: str,
            zonage2: str,
            date: str) -> dict:
        '''constructeur
        Paramètres:
        -----------
        zonage1: échelon principal (departements ou communes)
        id1: identifiant de l'échelon principal
        zonage2: échelon secondaire (découpage de l'échelon 
            principal)  communes ou parcelles
        date: date du fichier'''
        self.dico = {
            "zonage1": zonage1,
            "id1": id1,
            "zonage2": zonage2,
            "date": date}

    def instancier_zonage(self) -> list[Zonage]:
        '''créer une liste d'instances de Commune ou Parcelle à partir 
        d'une liste de dictionnaires demandée au client'''
        list_dico = LienService(self.dico).genere_dico()
        
        list_zonage = []
        # if self.dico["zonage2"] == "communes":
        #    for dico in list_dico:
        #        list_zonage.append(Commune(id= dico["properties"]["id"], 
        #              geom_coord= MultiPolygone(liste_brute= dico["geometry"]["coordinates"]), 
        #              nom= dico["properties"]["nom"]))
        # elif self.dico["zonage2"] == "parcelles":
        #    for dico in list_dico:
        #        list_zonage.append(Parcelle(id= dico["properties"]["id"], geom_coord=
        #           Polygone(liste_brute= dico["geometry"]["coordinates"]))) #ancienne version
        for dico in list_dico:
            if dico["geometry"]["type"] == "Polygon":
                list_zonage.append(
                    Parcelle(
                        id=dico["properties"]["id"],
                        geom_coord=Polygone(
                            liste_brute=dico["geometry"]["coordinates"])))
            if dico["geometry"]["type"] == "MultiPolygon":
                list_zonage.append(
                    Commune(
                        id=dico["properties"]["id"],
                        geom_coord=MultiPolygone(
                            liste_brute=dico["geometry"]["coordinates"]),
                        nom=dico["properties"]["nom"]))

        return list_zonage



###TESTS###
# Le 1er code laissé en commentaire ne fonctionne pas pour certains départements 14, 15,
#  16, 21, 22, 24, 25, 27, 28, 29, 34, 40, 43, 50, 51, 54, 55, 59,
# 60, 65, 67, 69, 77, 79, 81, 87, 90, 96, 971, 975   (car des communes de ces départements 
# sont de type Polygone et lieu de multiplolygone de les json du cadastre)


#list_com1 = Instanciation(zonage1="departements", id1="2A", 
# zonage2="communes", date="latest").instancier_zonage()

#list_com2 = Instanciation(zonage1="departements", id1="06", 
# zonage2="communes", date="latest").instancier_zonage()

# for i in [ "2A", "06", "13","51", '55', '56', '57', '58', '59', 
# '60', '61', '62', '63', '64', '65', '67', '68', '69', '70', '71', 
# '72', '76', '77', '78', '79', '80', '81', '82', '83', '85', '86', 
# '87', '88', '89', '90', '91', '93', '94', '95', '96', '971', '975']:
#    Instanciation(id1=i,zonage1="departements",
#       zonage2="communes",date="latest").instancier_zonage()

# print(insta.dico)
# print(insta.dico["zonage1"])

#liste = insta.instancier_zonage()
# print(liste[0].id)


# 120com13110 = Instanciation(zonage1="communes", id1="13110", 
# zonage2="communes", date="latest").instancier_zonage() #liste d'une seule commune
#print (com13110[0].geom_coord)

#com83120 = Instanciation(zonage1="communes", id1="83120", 
# zonage2="communes", date="latest").instancier_zonage()
#print (com83120[0].geom_coord)

#from objets.zone.commune import Commune
# print(com13110[0].lien_zone(autre_zone = com83120[0])) # non-contigues
# (alors qu'elles devraient l'être) # pb réglé en modifiant la classe Point 
# pour autoriser une marge d'erreur pour le test d'égalité de points



#Test de parcelles approximativement contigues
#com13007 = Instanciation(zonage1="communes", id1="13007", zonage2="parcelles", date="latest").instancier_zonage()
#com83120 = Instanciation(zonage1="communes", id1="83120", zonage2="parcelles", date="latest").instancier_zonage()
#for parc in com13007:
#    if parc.id == "13007000KT0037":
#        parc13_037 = parc
#for parc in com83120:
#    if parc.id == "831200000A0314":
#        parc83_316 = parc
#from objets.zone.zonage import Zonage
#print(parc13_037.test_zone_contigu(macro_zone=parc83_316))