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

    def nom_communes(self, id_com: str): # OK
        """Retourne le nom de la commune correspondant à l'identifiant"""
        request = "SELECT nom_com FROM Commune WHERE id_com = %(id_com)s"
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request,
                    {"id_com": id_com}
                )
                res = cursor.fetchone() 
        return res

    def recherche(self, id_com:str): # OK
        """Recherche une commune par son identifiant"""
        request = "SELECT * FROM Commune WHERE id_com = %(id_com)s"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request,
                    {"id_com": id_com}
                )
                res = cursor.fetchall()
        if res ==[] :
            print("la commune n'est pas dans la base de données")
        else : 
            return res
        
    
    def ajout_commune(self, id_com: str, nom_com: str):
        """Ajouter commune à la table Commune dans la table si elle n'existe pas déjà"""

        if self.recherche(id_com) == [] or self.recherche(id_com) == None : # la commune n'est pas présente dans la table
            id_dep = id_com[0:1]
            if id_dep=="97": # Dom Tom : ont un num de département à 3 chiffres
                id_dep = id_com[0:2]
            request = "INSERT INTO Commune (id_com, nom_commune, id_dep)"\
            "VALUES (%(id_com)s, %(nom_com)s, %(id_dep)s)"\
            #"WHERE NOT EXISTS (SELECT id_com FROM Commune WHERE id_com = %(id_com)s)" #  test de pré-existance

            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        request,
                        {"id_com": id_com, "nom_com": nom_com, "id_dep": id_dep}
                    )
        else : # la commune est déjà dans la table
            pass # on ne fait rien
        
    def suppression_commune(self, id_com: str): # OK
        """Supprime la ligne d'une commune dans la table Commune de la BdD """
        request = "DELETE FROM Commune WHERE id_com =%(id_com)s"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request,
                    {"id_com": id_com}
                )
    


################################################## TESTS ##################################################

#c = CommuneDAO()

#### test ajout_commune
#c.ajout_commune('02012', 'AMBRIEF')

#### test nom_commune : OK
#print(c.nom_communes('35170'))
#print(c.nom_communes('35000'))

#### test recherche : OK
#print(c.recherche('35170'))
#print(c.recherche('35000'))

#### test suppression commune : OK
#c.suppression_commune('35000')