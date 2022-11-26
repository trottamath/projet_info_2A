'''module initialisation_bdd de la classe InitialisationBdD'''
from service.instanciation import Instanciation
from service.requete import Requete


class InitialisationBdD():
    '''classe qui charge la base de données pour un département à une date donnée'''

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
        for commune in list_com:
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


InitialisationBdD(id_dep="13").chargement_bdd()
