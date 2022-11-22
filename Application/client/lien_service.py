"""module commune_dao.py pour définir la classe CommuneDAO
version 1.0
date 25/10/2022
auteurs : Chloé Contant et Jean-Philippe Trotta
"""
from client.telechargement import Telechargement

class LienService():
    '''Classe qui créer les dictionnaires utiles pour la couche Service à partir des fichiers .json.gz stockés en local
    
    Attributes
    ----------
    dict_initial : dict

    '''
    
    def __init__(self,dict_initial):
        '''Constructeur
        Parameters:
        -----------
        dict_initial : dict
            Description des clés du dictionnaire :
            --------------------------------------
            zonage1: échelon principal (départements ou communes)
            id1: identifiant de l'échelon principal
            zonage2: échelon secondaire (découpage de l'échelon principal)  communes ou parcelles
            date: date du fichier
        '''
        self.dico = dict_initial 

    def genere_dico(self) -> list[dict]: 
        '''Méthode qui retourne une liste de dictionnaire 
                Exemple: zonage1="departements", id="35", zonage2="communes", date="latest"
                La méthode retourne une liste de dictionnaires avec les communes du département 35
                chaque dictionnaire a entre autres une clée "coordinates" , un clé "id"
                voire une clée "nom" pour le nom de commune.

        
        Returns
        ------
            list_dict : list[dict]
        
        '''
        tel = Telechargement(id_zone1=self.dico['id1'],zonage1 = self.dico['zonage1'],date = self.dico['date'], zonage2 = self.dico['zonage2'] )
        
        dico_extract_json = tel.read_json() #dictionnaire TODO le bug est ici pour les parcelles uniquement!!!!
        
        list_dict = dico_extract_json['features'] #extraction de la liste de dictionnaire
        
        return (list_dict)

############################################################### TEST ############################################################################

#test pour fonction qui genère dictionnaire (déplacé dans un fichier test TODO à supprimer ici)

#D = {'zonage1' : 'departements',
 #   'id1' : '01',
  #  'zonage2' : 'communes',
   # 'date' : 'latest'}
#test = LienService(D)
#dico = test.genere_dico()
#print(dico)
