"""module commune_dao.py pour définir la classe CommuneDAO
version 1.0
date 25/10/2022
auteurs : Jean-Philippe Trotta et Chloé Contant
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
            zonage1: échelon principal (département ou commune)
            id1: identifiant de l'échelon principal
            zonage2: échelon secondaire (découpage de l'échelon principal)  commune ou parcelle
            date: date du fichier
        '''
        self.dico = dict_initial 

    def genere_dico(self) -> list[dict]: 
        '''Méthode qui retourne une liste de dictionnaire 
                Exemple: zonage1="departement", id="35", zonage2="commune", date="latest"
                La méthode retourne une liste de dictionnaires avec les communes du département 35
                chaque dictionnaire a entre autres une clée "coordinates" , un clé "id"
                voire une clée "nom" pour le nom de commune.
        Parameters:
        -----------
        
        Returns
        ------
        list_dict : list[dict]
        
        '''

        zonage1 = self.dico['zonage1']
        id_dep= self.dico['id1']
        zonage2 = self.dico['zonage2']
        date = self.dico['date']
        print(zonage1,id_dep,zonage2,date)
        link = Telechargement().generator_link(id_dep = id_dep, date=date, zonage1=zonage1, id_zone = None, zonage2=zonage2)
        print(link)
        path = Telechargement().generator_path(link)
        print(path)
        dico_extract_json = Telechargement().read_json(link,path) #dictionnaire

        list_dict = dico_extract_json['features'] #extraction de la liste de dictionnaire
        
        return (list_dict)

############################################################### TEST ############################################################################

#test pour fonction qui genère dictionnaire

D = {'zonage1' : 'departements',
    'id1' : '01',
    'zonage2' : 'communes',
    'date' : 'latest'}
test = LienService(D)
dico = test.genere_dico()
print(dico)
