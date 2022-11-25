from service.instanciation import Instanciation
from service.requete import Requete


class InitialisationBdD():
    def __init__(self,id_dep,date="latest"):
        self.id_dep = id_dep
        self.date = date
    
    def chargement_bdd(self):
        list_com = Instanciation(zonage1="departements", id1=self.id_dep, zonage2="communes", date=self.date).instancier_zonage()
        for commune in list_com:
            Requete(dico_requete={"num":"1","id":self.id_dep,"date":self.date}).Get_client()
            Requete(dico_requete={"num":"2","id":commune.id,"date":self.date}).Get_client()
