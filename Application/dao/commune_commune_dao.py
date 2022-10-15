from utils.singleton import Singleton
from dao.db_connection import DBConnection

connexion = DBConnection().connection
cursor = connexion.cursor()

class CommuneCommuneDAO():
    '''classe de communication avec la table commune_commune de la bdd'''
    
    def create(self, id_com1 : str, id_com2 : str, date):
        '''ajoute une nouvelle paire de communes limitrophes pour la date donnée'''
        # à faire

    def recherche_com(self,id_com: str,date):
        '''recherche les communes limitrophes à une commune donnée'''
        cursor.execute(
            "SELECT id_com1, id_com2"\
                "\n\t FROM commune_commune"\
                    "\n\t WHERE (id_com1=%(id_com)s OR id_com2=%(id_com)s) AND date=%(date)s ",
            {"id_com": id_com}
        )  # à revoir : il faut récupérer la liste des id_com1 et id_com2 différent de id_com
        res = cursor.fetchall()
        return res

    