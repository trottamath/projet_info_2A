from dao.commune_commune_dao import CommuneCommuneDAO
from dao.parcelle_dao import ParcelleDAO

from client.lien_service import LienService
from objets.zone.zonage import Zonage
from departements import Departement
from instanciation import Instanciation


class Requete ():
    """Classe qui lie le Service à la DAO : envoie de la requête
    à la DAO, et récupération du résultat"""

    def __init__(self, dico_requete:dict) :
        """
        Parametres:
        -----------
            dico_requete: dict
                les clées de ce dictionnaire sont
                num : str
                    numero de la requete (1 ou 2 dans le cas de l'appel à la DAO)
                    "1" pour les communes contigües à la commune donnée
                    "2" pour les parcelles en limite de la commune donnée
                id : str
                    identifiant de la commune donnée
                date : str
                    date du fichier cadatral de référence
                """
        self.dico_requete = dico_requete
            

    def Get_DAO(self):
        """pour demander le resultat à la DAO qui va interroger la base de données"""
        #res= None
        if self.dico_requete["num"] == "1" : # voisines communes à une voisine donnée
            com = CommuneCommuneDAO()
            res = com.recherche_com(self.dico_requete["id"], self.dico_requete["date"])
        
        elif self.dico_requete["num"] == "2" : # parcelles en bordure d'une commune donnée
            com = ParcelleDAO()
            res = com.research_all_lim(self.dico_requete["id"])

        return res
    
    def Get_Client(self):
        """pour déterminer le résultat de requête en interaction avec le Client 
        et les méthodes de la couche Objets"""
        if self.dico_requete["num"] == "1" :
            #recuperer le numéro de dep de la com
            #recuperer la liste des dep limitrophes
            #instancier toutes les communes du dep et des limitrophe
            #

            



