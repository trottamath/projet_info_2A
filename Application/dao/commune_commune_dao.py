from utils.singleton import Singleton
from dao.db_connection import DBConnection
from dao.commune_dao import CommuneDAO

connexion = DBConnection().connection
cursor = connexion.cursor()

class CommuneCommuneDAO():
    '''classe de communication avec la table commune_commune de la bdd'''

    def recherche(self, id_com1: str, id_com2: str, date):
        cursor.execute(
            "SELECT id_com1, id_com2"\
                "\n\t FROM commune_commune"\
                    "\n\t WHERE (id_com1=%(id_com1)s AND id_com2=%(id_com2)s) AND date=%(date)s ",
            {"id_com1": id_com1, "id_com2": id_com2, "date": date}
        )  

        res = cursor.fetchall()
        return res


    def create(self, id_com1: str, id_com2: str, date):
        '''ajoute une nouvelle paire de communes limitrophes pour la date donnée'''
        # si le couple existe déjà, on ne l'ajoute pas à la base de données
        if self.recherche(id_com1,id_com2,date) == None : # le couple n'existe pas déjà
            request = "INSERT INTO Commune (id_com1, id_com2, date)" \
                    "VALUES (%(id_com1)s, %(id_com2)s, %(date)s)"
            cursor.execute(
                request, {"id_com1" : id_com1, "id_com2": id_com2, "date": date}
            )
        else :
            pass
    

    def recherche_com(self, id_com: str, date):
        '''recherche les communes limitrophes à une commune donnée'''
        # request = "SELECT id_com1, id_com2"\
        #         "\n\t FROM commune_commune"\
        #         "\n\t WHERE (id_com1=%(id_com)s OR id_com2=%(id_com)s) AND date=%(date)s "
        request = "SELECT id_com2"\
            "\n\t FROM commune_commune"\
            "\n\t WHERE (id_com1=%(id_com)s AND date=%(date)s "
        cursor.execute(
            {"id_com": id_com, "date":date}
        )  
        # res = cursor.fetchall() # liste de tuples (id_com1, id_com2) des lignes retournées
        # voisins = []
        # for i in range(len(res)) : 
        #     for j in range(len(res[i])): # res[i] de longueur 2 car (id_com1, id_com2)
        #         if res[i][j] != id_com : # voisin de la commune et non la commune elle-même
        #             voisins.append(res[i][j])
        # return voisins # liste des communes voisines



    def create_all(self, id_com1: str, list_id_com2: list[str], date):
        for id_com2 in list_id_com2:
            self.create(id_com1= id_com1, id_com2= id_com2, date= date)
        
    
