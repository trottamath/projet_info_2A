from utils.singleton import Singleton
from dao.db_connection import DBConnection


class CommuneDAO(metaclass=Singleton):
    "Table Commune dans la base de données"

    def nom_communes(self, id_com):
        """Retourne le nom de la commune correspondant à l'identifiant"""
        request = "SELECT nom_commune FROM Commune"\
            "WHERE id_com = %(id_com)s"
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request,
                    {"id_com": id_com}
                )
                res = cursor.fetchall()
        return res

    
    def ajout_commune(self, id_com, nom_com):
        """Ajouter commune à la table Commune dans BdD"""
        request = "INSERT INTO Commune (id_com, nom_commune)"\
        "VALUES (%(id_com)s, %(nom_com)s)"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request,
                    {"id_com": id_com, "nom_com":nom_com}
                )
        

    def suppression_commune(self, id_com):
        """Supprime la ligne d'une commune dans la table Commune de la BdD """
        request = "DELETE FROM Commune"\
            "WHERE id_com =%(id_com)s"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request,
                    {"id_com": id_com}
                )
        
        