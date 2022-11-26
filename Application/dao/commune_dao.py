"""module commune_dao.py pour définir la classe CommuneDAO
version 1.0
date 15/10/2022
auteurs : Jean-Philippe Trotta et Eva Puchalski
"""
from utils.singleton import Singleton
from dao.db_connection import DBConnection

from objets.zone.zonage import Zonage


class CommuneDAO(metaclass=Singleton):
    "Table Commune dans la base de données"

    def nom_commune(self, id_com: str):
        """Retourne le nom de la commune correspondant à l'identifiant
        Parameters
        ------
        id_com : str
            code postal de la commune
        """

        request = "SELECT nom_commune FROM Commune WHERE id_com = %(id_com)s"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    request,
                    {"id_com": id_com}
                )
                res = cursor.fetchone()
        return res['nom_commune']

    def recherche_commune(self, id_com: str):
        """Recherche une commune par son identifiant
        Parameters
        ------
        id_com : str
            code postal de la commune
        """
        request = "SELECT * FROM Commune WHERE id_com = %(id_com)s"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    request,
                    {"id_com": id_com}
                )
                res = cursor.fetchall()
        return res

    def ajout_commune(self, id_com: str, nom_commune: str):
        """Ajouter commune à la table Commune dans la table si elle n'existe pas déjà
        Parameters
        ------
        id_com : str
            code postal de la commune
        nom_commune : str
            nom de la commune
        """
        print(self.recherche_commune(id_com))  # provisoire
        if self.recherche_commune(id_com) == [] or self.recherche_commune(
                id_com) is None:  # la commune n'est pas présente dans la table
            id_dep = id_com[0:2]
            if id_dep == "97":  # Dom Tom : ont un num de département à 3 chiffres
                id_dep = id_com[0:3]
            request = "INSERT INTO commune (id_com, nom_commune, id_dep)"\
                "VALUES (%(id_com)s, %(nom_commune)s, %(id_dep)s)"\

            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        request,
                        {"id_com": id_com, "nom_commune": nom_commune, "id_dep": id_dep})
        else:  # la commune est déjà dans la table
            print('la commune est déjà dans la base de données')

    def suppression_commune(self, id_com: str):
        """Supprime la ligne d'une commune dans la table Commune de la BdD
        Parameters
        ------
        id_com : str
            code postal de la commune
        """
        request = "DELETE FROM commune WHERE id_com = %(id_com)s"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    request,
                    {"id_com": id_com}


)################################################## TESTS : OK ############

c = CommuneDAO()
# print(c.recherche_commune(id_com="13207"))

# test ajout_commune : OK
c.ajout_commune('33000', 'BORDEAUX')
#c.ajout_commune('39000', 'LONS-LE-SAUNIER')
# print(c.recherche_commune(id_com="83000"))

# test nom_commune : OK
# print(c.nom_commune('35170'))
# print(c.nom_communes('35000'))

# test recherche_commune : OK
# print(c.recherche_commune('45678'))
# print(c.recherche_commune('84000'))

# test suppression commune : OK
# c.suppression_commune('83000')
#>>>>>>> 699776ce20f4fb8aa84912f69193d3b55a710382
