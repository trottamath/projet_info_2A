from utils.singleton import Singleton
from dao.db_connection import DBConnection

connexion = DBConnection().connection
cursor = connexion.cursor()

class CommuneCommuneDAO():
    '''classe de communication avec la table commune_commune de la bdd'''
    
    def create(self, id_com1 : str, id_com2 : str, date):
        '''ajoute une nouvelle paire de communes limitrophes pour la date donnée'''
        request = "INSERT INTO Commune (id_com1, id_com2, date)" \
                "VALUES (%(id_com1)s, %(id_com2)s, %(date)s)"\

        cursor.execute(
            request, {"id_com1" : id_com1, "id_com2":id_com2, "date":date}
        )
  

    def recherche_com(self,id_com: str,date):
        '''recherche les communes limitrophes à une commune donnée'''
        cursor.execute(
            "SELECT id_com1, id_com2"\
                "\n\t FROM commune_commune"\
                    "\n\t WHERE (id_com1=%(id_com)s OR id_com2=%(id_com)s) AND date=%(date)s ",
            {"id_com": id_com}
        )  

        res = cursor.fetchall() # liste de tuples (id_com1, id_com2) des lignes retournées
        voisins = []
        for i in range(len(res)) : 
            for j in range(len(res[i])): # res[i] de longueur 2 car (id_com1, id_com2)
                if res[i][j] != id_com : # voisin de la commune et non la commune elle-même
                    voisins.append(res[i][j])
        return voisins # liste des communes voisines


    