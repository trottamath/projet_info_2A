"""module parcelle_commune_dao.py pour définir la classe ParcelleCommuneDAO
version 1.0
date 15/10/2022
auteurs : Jean-Philippe Trotta et Eva Puchalski
"""

from utils.singleton import Singleton
from dao.db_connection import DBConnection
from dao.parcelle_dao import ParcelleDAO


class ParcelleCommuneDAO():
    """classe ParcelleCommuneDAO pour communiquer avec la base de bonnées
    concernant les assiations (relation de contiguité) entre parcelles et communes"""

    def recherche_unit(self, id_parc: str, id_com: str, date): # OK
        '''recherche d'un couple parcelle/commune contigües à une date donnée'''
        request = "SELECT * FROM parcelle_commune WHERE id_parc=%(id_parc)s AND id_com=%(id_com)s AND date=%(date)s"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request,
                    {"id_parc": id_parc, "id_com": id_com, "date":date}
                    )
                res = cursor.fetchall() #fetchone ?
        return res
    
    def create(self, id_parc: str, id_com: str, date):
        '''ajout d'un couple parcelle/commune contigues à une date donnée'''
        # if self.recherche_unit(id_parc,id_com,date) != None : pass
        request = "INSERT INTO parcelle_commune (id_parc, id_com, date) VALUES (%(id_parc)s, %(id_com)s, %(date)s)"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request,
                    {"id_parc": id_parc, "id_com": id_com, "date": date}
                    )
    

    def create_all(self, id_com: str, list_id_parc: list[str], date):
        '''ajout d'une liste de parcelles en limite d'une commune pour une date donnée'''
        for id_parc in list_id_parc:
            self.create(id_parc= id_parc, id_com= id_com, date= date)
        #ParcelleDAO().ajout_liste_parc(list_id_parc= list_id_parc) #à la place de crearte.list()

#################################### TESTS : ##########################################

pc = ParcelleCommuneDAO()

#### test recherche_unit : OK
#print(pc.recherche_unit('132078290I0071', '13207', 'latest'))

#### test create : OK
#pc.create('111111', '22222', 'latest')

#### test create_all :
pc.create_all('11111',['2222','33333','44444'], 'latest')



