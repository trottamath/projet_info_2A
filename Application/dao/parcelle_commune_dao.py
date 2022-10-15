from utils.singleton import Singleton
from dao.db_connection import DBConnection


connexion =  DBConnection().connection
cursor = connexion.cursor()

class ParcelleCommuneDAO():
    """classe ParcelleCommuneDAO pour communiquer avec la base de bonnées
    concernant les assiations (relation de contiguité) entre parcelles et communes"""

    def recherche_unit(self, id_parc: str, id_com: str, date):
        '''recherche d'un couple parcelle/commune contigües à une date donnée'''
        cursor.execute(
            "SELECT id_parc, id_com, date"\
            "\n\t FROM parcelle_commune"\
            "\n\t WHERE id_parc=%(id_parc)s AND id_com=%(id_com)s AND date=%(date)s",
            {"id_parc": id_parc, "id_com": id_com, "date":date}
        )
        res= cursor.fetchone()
        return res
    
    def create(self, id_parc: str, id_com: str, date):
        '''ajout d'un couple parcelle/commune contigues à une date donnée'''
        # if self.recherche_unit(id_parc,id_com,date) == None :
        cursor.execute(
            "INSERT INTO parcelle_commune (id_parc, id_com, date)"\
            "VALUES (%(id_parc)s, %(id_com)s, %(date)s) ",
            {"id_parc": id_parc, "id_com": id_com, "date": date}
        )
        res = cursor.fetchone()
        return res

    def recherche_coms(self, id_parc: str, date):
        '''recherche les communes limitrophes à une parcelle donnée pour une date donnée, dans bdd'''
        cursor.execute(
            "SELECT id_com"\
            "FROM parcelle_commune"\
            "\n\t WHERE id_parc=%(id_parc)s",
            {"id_parc": id_parc}
        )
        res = cursor.fetchall()
        return res 

    



