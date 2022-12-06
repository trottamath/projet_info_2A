'''module initialisation_bdd de la classe InitialisationBdD'''
from service.instanciation import Instanciation
from service.requete import Requete

from dao.commune_dao import CommuneDAO
from dao.commune_commune_dao import CommuneCommuneDAO
from dao.parcelle_dao import ParcelleDAO

class InitialisationBdD():
    '''classe qui charge la base de données pour un département
     à une date donnée'''

    def __init__(self, id_dep: str, date: str = "latest"):
        '''constructeur'''
        self.id_dep = id_dep
        self.date = date

    def chargement_bdd(self):
        '''méthode qui charge la base de données'''
        list_com = Instanciation(
            zonage1="departements",
            id1=self.id_dep,
            zonage2="communes",
            date=self.date).instancier_zonage()

        taille = len(list_com)

        #passage provisoire pour reprendre après un élément de la liste
        while list_com[0].id != "35142":
            list_com.pop(0)
        print("il reste {} communes".format(len(list_com)))

    
        nb = 0
        for commune in list_com:
            nb = nb + 1
            Requete(
                dico_requete={
                    "num": "1",
                    "id": commune.id,
                    "date": self.date}).Get_Client()
            Requete(
                dico_requete={
                    "num": "2",
                    "id": commune.id,
                    "date": self.date}).Get_Client()
            print("{} pourcent de chargement de la base de données".format(round(nb/taille*100,2)))

    def supprime_dep(self):
        CommuneDAO().supprime_all_dep(id_dep=self.id_dep)
        CommuneCommuneDAO().supprime_all_dep(id_dep=self.id_dep)
        ParcelleDAO().supprime_all_dep(id_dep=self.id_dep)

        #partie provisoire pour vérifier pour l'oral
        listcom13007=["13007","13016","13086","13042","13110","83120","83093"]
        CommuneDAO().supprime_listcom(list_id_com=listcom13007)
        CommuneCommuneDAO().supprime_listcom(list_id_com=listcom13007)
        ParcelleDAO().suppression_parcelle(id_parc="13007000KV0045")
        ParcelleDAO().supprime_listcom(list_id_com=listcom13007)


    


#suppression de la Bdd pour le dep 13
InitialisationBdD(id_dep="13").supprime_dep()

# Initialisation de la bdd pour le dep 35
#InitialisationBdD(id_dep="35").chargement_bdd()
