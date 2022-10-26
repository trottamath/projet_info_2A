from Application.dao.commune_commune_dao import CommuneCommuneDAO
from Application.dao.parcelle_dao import ParcelleDAO

class Requete ():
    """Classe qui lie le Service à la DAO : envoie de la requête
    à la DAO, et récupération du résultat"""

    def __init__(self, num:str) :
        """num : int, numero de la requete (1 ou 2 dans le cas de l'appel à la DAO"""
        self.requete = num
            

    def requeter(self, id:str, date:str):
        """id : str, identifiant de la commune ou de la parcelle à traiter"""
        if self.requete == 1 : # voisines communes à une voisine donnée
            com = CommuneCommuneDAO()
            res = com.recherche_com(id_com, date)
        
        elif self.requete == 2 : # parcelles en bordure d'une commune donnée
            com = ParcelleDAO()
            res = com.research_all_lim(id)

        return res


