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
        """recherche d'un couple parcelle/commune contigües à une date donnée
        Parameters
        ------
        id_parc : str
            identifiant de la parcelle
        id_com : str
            code postal de la commune
        date : str
            date de l'information
        """
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
        """ajout d'un couple parcelle/commune contigues à une date donnée
        Parameters
        ------
        id_parc : str
            identifiant de la parcelle
        id_com : str
            code postal de la commune
        date : str
            date de l'information
        """
        # if self.recherche_unit(id_parc,id_com,date) != None : pass
        request = "INSERT INTO parcelle_commune (id_parc, id_com, date) VALUES (%(id_parc)s, %(id_com)s, %(date)s)"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request,
                    {"id_parc": id_parc, "id_com": id_com, "date": date}
                    )
    

    def create_all(self, id_com: str, list_id_parc: list[str], date):
        """Ajout d'une liste de parcelles en limite d'une commune pour une date donnée
        Parameters
        ------
        id_com : str
            code postal de la commune
        list_id_parc : list[str]
            liste des identifiants des parcelles à ajouter
        date : str
            date de l'information
        """
        for id_parc in list_id_parc:
            self.create(id_parc= id_parc, id_com= id_com, date= date)


