"""module commune_commune_dao.py pour définir la classe CommuneCommuneDAO
version 1.0
date 15/10/2022
auteurs : Jean-Philippe Trotta et Eva Puchalski
"""

from utils.singleton import Singleton
from dao.db_connection import DBConnection
from dao.commune_dao import CommuneDAO


class CommuneCommuneDAO():
    '''classe de communication avec la table commune_commune de la bdd'''

    def recherche(self, id_com1: str, id_com2: str, date: str):
        """Recherche un couple de commune pour une date donnée
        Parameters
        ------
        id_com1 : str
            code postal de la première commune
        id_com2 : str
            code postal de la deuxième commune
        date : str
            date de l'information
        """
        request = "SELECT * FROM commune_commune WHERE id_com1 = %(id_com1)s AND id_com2 = %(id_com2)s AND date = %(date)s"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request,
                    {"id_com1": id_com1, "id_com2": id_com2, "date": date}
                )
                res = cursor.fetchall()
        return res


    def create(self, id_com1: str, id_com2: str, date):
        """ajoute une nouvelle paire de communes limitrophes pour la date donnée
        Parameters
        ------
        id_com1 : str
            code postal de la première commune
        id_com2 : str
            code postal de la deuxième commune
        date : str
            date de l'information
        """
        # si le couple existe déjà pour la date donnée, on ne l'ajoute pas à la base de données
        if self.recherche(id_com1,id_com2,date) == None or self.recherche(id_com1,id_com2,date) == []: # le couple n'existe pas déjà
            request = "INSERT INTO commune_commune (id_com1, id_com2, date) VALUES (%(id_com1)s, %(id_com2)s, %(date)s)"
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        request,
                        {"id_com1": id_com1, "id_com2": id_com2, "date": date}
                    )
        else :
            pass
    

    def recherche_com(self, id_com: str, date: str):
        """recherche les communes limitrophes à une commune donnée
        Parameters
        ------
        id_com : str
            code postal de la commune
        date : str
            date de l'information
        """
        request = "SELECT id_com2 FROM commune_commune WHERE id_com1=%(id_com)s AND date=%(date)s"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request,
                    {"id_com": id_com, "date": date}
                )
                res = cursor.fetchall()
        voisines = []
        for i in range(len(res)):
            voisines.append(res[i]['id_com2'])
        return voisines



    def create_all(self, id_com1: str, list_id_com2: list[str], date: str):
        """Ajoute un ensemble de communes voisines à une commune donnée
        Parameters
        ------
        id_com1 : str
            code postal de la première commune
        list_id_com2 : list[str]
            liste des codes postaux des communes à ajouter
        date : str
            date de l'information
        """
        for id_com2 in list_id_com2:
            self.create(id_com1= id_com1, id_com2= id_com2, date= date)
