from utils.singleton import Singleton
from dao.db_connection import DBConnection

from objets.zone.zonage import Zonage


class CommuneDAO(metaclass=Singleton):
    "Table Commune dans la base de données"

    def nom_communes(self, id_com: str):
        """Retourne le nom de la commune correspondant à l'identifiant"""
        request = "SELECT nom_commune FROM Commune"\
            "WHERE id_com = %(id_com)s"
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request,
                    {"id_com": id_com}
                )
                res = cursor.fetchone() 
        return res

    def recherche(self, id_com:str):
        """Recherche une commune par son identifiant"""
        request = "SELECT * FROM Commune WHERE id_com = %(id_com)s"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request,
                    {"id_com": id_com}
                )
            res = cursor.fetchall()
        return res

    
    def ajout_commune(self, id_com: str, nom_com: str):
        """Ajouter commune à la table Commune dans la table si elle n'existe pas déjà"""

        if recherche(id_com) == None : # la commune n'est pas présente dans la table
            id_dep = ss_str(chaine= id_com, nbr_caract= 2)
            if id_dep=="97": # Dom Tom : ont un num de département à 3 chiffres
                id_dep = ss_str(chaine= id_com, nbr_caract= 3)
            request = "INSERT INTO Commune (id_com, nom_commune, id_dep)"\
            "VALUES (%(id_com)s, %(nom_com)s, %(id_dep)s)"\
            "WHERE NOT EXISTS (SELECT id_com FROM Commune WHERE id_com = %(id_com)s)" #  test de pré-existance

            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        request,
                        {"id_com": id_com, "nom_com": nom_com, "id_dep": id_dep}
                    )
        else : # la commune est déjà dans la table
            pass # on ne fait rien
        
    def suppression_commune(self, id_com: str):
        """Supprime la ligne d'une commune dans la table Commune de la BdD """
        request = "DELETE FROM Commune WHERE id_com =%(id_com)s"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request,
                    {"id_com": id_com}
                )
    


        
        