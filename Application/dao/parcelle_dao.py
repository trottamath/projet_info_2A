"""module parcelle_dao.py pour définir la classe ParcelleDAO
version 1.0
date 15/10/2022
auteurs : Jean-Philippe Trotta et Eva Puchalski
"""

from typing import Optional
import hashlib

from utils.singleton import Singleton
from dao.db_connection import DBConnection
from objets.zone.parcelle import Parcelle
from objets.zone.zonage import Zonage   # pour importer la staticmethode pour les chaines de caractères tronquées

from dao.commune_dao import CommuneDAO

connexion = DBConnection().connection
cursor = connexion.cursor()

class ParcelleDAO(metaclass=Singleton):
    """classe ParcelleDAO """


    # def ajout_parcelle2(self, parcel : Parcelle ): # à supprimer ?
    #     '''pour ajouter une nouvelle parcelle dans la table parcelle de la base de données'''
    #  #   with DBConnection().connection as connection:
    #   #      with connection.cursor() as cursor:
    #     cursor.execute(
    #         "INSERT INTO parcelle (id_parc, id_com_limit)"
    #         " VALUES (%(id_parc)s, %(id_com_limit)s) RETURNING parcelle_id", # RETURNING parcelle_id;"  ???
    #         {"id_parc": parcel.id, "id_com_limit": parcel.ident_commune()} )
    #     res = cursor.fetchone() #facultatif ? 
    #     return res  #['parcelle_id']  #??
    
    def recherche_parcelle(self, id_parc:str): # OK
        '''pour chercher une parcelle dans la base de données à partir de son identifiant (code)'''
        request = "SELECT * FROM parcelle WHERE id_parc = %(id_parc)s"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request,
                    {"id_parc": id_parc}
                )
                res = cursor.fetchall()
        return res

    def ajout_parcelle(self, id_parc:str): # OK
        '''pour ajouter une nouvelle parcelle dans la table parcelle de la base de données,
        directement à partir de son identifiant
        On ajoute une parcelle dans la base de données seulement si elle est en limite de sa commune'''

        if self.recherche_parcelle(id_parc) == [] or self.recherche_parcelle(id_parc) == None : # la parcelle n'est pas présente dans la table
            id_com_limit = id_parc[0:5]
            request = "INSERT INTO parcelle (id_parc, id_com_limit) VALUES (%(id_parc)s, %(id_com_limit)s)"
        
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        request,
                        {"id_parc": id_parc, "id_com_limit" : id_com_limit}
                )
                    #res = cursor.fetchall()
            #return res


        #cursor.execute(
            #"INSERT INTO parcelle (id_parc, id_com_limit)"
            #"VALUES (%(id_parc)s, %(id_com_limit)s) RETURNING parcelle_id",
            #{"id_parc": id_parc, "id_com_limit": id_com} )
        #res = cursor.fetchall()
        #return res


    def ajout_liste_parc(self, list_id_parc : list[str]):
        '''pour ajouter toute une liste de parcelles à la base de données'''
        for id_parc in list_id_parc:
            if self.recherche_parcelle(id_parc) == None or self.recherche_parcelle(id_parc) == [] :
                self.ajout_parcelle(id_parc= id_parc)


    def research_all_lim(self, id_com_limit: str):
        '''pour chercher toutes les parcelles de la bdd qui sont en limite de la commune dont l'identifiant est donné'''
        request = "SELECT id_parc FROM parcelle WHERE id_com_limit = %(id_com_limit)s "
        with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        request,
                        {"id_com_limit": id_com_limit}
                )
                res = cursor.fetchall()      #méthode à vérifier (pose pb pour la requete 2)
        return res


#update inutile dans ce cas ?

    def suppression_parcelle(self, id_parc : str): # OK
        '''pour supprimer une parcelle de la base de données'''
        request = "DELETE FROM parcelle WHERE id_parc =%(id_parc)s"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request,
                    {"id_parc": id_parc})



############################################ TESTS ############################################

#p = ParcelleDAO()
#print(p.recherche_parcelle(id_parc="132078290I0071"))
#print(p.research_all_lim(id_com_limit="13207")) #ne fonctionne pas ?
# test recherche_parcelle : OK
#print(p.recherche_parcelle('50250AZ4'))

#### test suppression_parcelle : OK
#p.drop('50250AZ4')

#### test ajout_parcelle : OK
#p.ajout_parcelle('14302B6')

#### test research_all_lim
#p.research_all_lim('50250')