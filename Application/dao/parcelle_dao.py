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

connexion = DBConnection().connection
cursor = connexion.cursor()

class ParcelleDAO(metaclass=Singleton):
    """classe ParcelleDAO """


    def create(self, parcel : Parcelle ): # à supprimer ?
        '''pour ajouter une nouvelle parcelle dans la table parcelle de la base de données'''
     #   with DBConnection().connection as connection:
      #      with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO parcelle (id_parc, id_com_limit)"
            " VALUES (%(id_parc)s, %(id_com_limit)s) RETURNING parcelle_id", # RETURNING parcelle_id;"  ???
            {"id_parc": parcel.id, "id_com_limit": parcel.ident_commune()} )
        res = cursor.fetchone() #facultatif ? 
        return res  #['parcelle_id']  #??
    
    def research(self, id_parcel : str): #est-ce qu'il vaut mieux commencer par cette méthode, pour tester l'existance avant de créer ?
        '''pour chercher une parcelle dans la base de données à partir de son identifiant (code)'''
        cursor.execute(
            "SELECT id_parc, id_com_limit"
            "\n\t FROM parcelle"
            "\n\t WHERE id_parc=%(id_parcel)s",
            {"id_parc": id_parc} )  # ou id_parcel ???
        res = cursor.fetchone()
        return res

    def create_id(self, id_parcel : str):
        #ajouter un test de pré-exitance ? TODO
        #if self.research(id_parcel= id_parcel)!=None : pass
        '''pour ajouter une nouvelle parcelle dans la table parcelle de la base de données,
        directement à partir de son identifiant'''
        id_com = id_parcel[0:4]
        cursor.execute(
            "INSERT INTO parcelle (id_parc, id_com_limit)"
            "VALUES (%(id_parc)s, %(id_com_limit)s) RETURNING parcelle_id",
            {"id_parc": id_parcel, "id_com_limit": id_com} )
        res = cursor.fetchone()
        return res



    def create_list(self, list_id_parc : list[str]):
        '''pour ajouter toute une liste de parcelles'''
        for id_parcel in list_id_parc:
            if self.research(id_parcel= id_parcel) == None:
                self.create_id(id_parcel= id_parcel)

    def research_all_lim(self, id_com_lim: str):
        '''pour chercher toutes les parcelles de la bdd qui sont en limite de la commune dont l'identifiant est donné'''
        cursor.execute(
            "SELECT id_parc"
            "\n\t FROM parcelle"
            "\n\t WHERE id_com_limit=%(id_com_lim)s",
            {"id_com_limit": id_com_lim} )  # à vérifier
        res = cursor.fetchall()
        return res

#update inutile dans ce cas ?

    def drop(self, id_parcel : str):
        '''pour supprimer une parcelle de la base de données'''
        cursor.execute(
            "DELETE FROM parcelle"\
            "WHERE id_par =%(id_parcel)s",
            {"id_parc": id_parc} ) 
        res = cursor.fetchone()
        return res
