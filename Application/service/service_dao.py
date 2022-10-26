from Application.dao.commune_commune_dao import CommuneCommuneDAO
from Application.dao.parcelle_dao import ParcelleDAO

class Voisines ():
    """Classe qui lie le Service à la DAO : envoie de la requête
    à la DAO, et récupération du résultat"""

    def requete(self, id:str, date:str):
        if requete == 1 : # voisines communes à une voisine donnée
            com = CommuneCommuneDAO()
            res = com.recherche_com(id_com, date)
        
        elif requete == 2 : # parcelles en bordure d'une commune donnée
            com = ParcelleDAO()
            res = com.research_all_lim(id)

        #else : # requete == 3 : parcelles voisines d'une parcelle donnée
            #parc = ParcelleDAO()
            #res = parc.
