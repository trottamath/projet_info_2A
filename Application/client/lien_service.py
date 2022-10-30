'''module lien_service.py'''

from client.importation import Importation


class LienService():
    '''Classe qui créer les dictionnaires utiles pour la couche Service à partir des fichiers .json.gz stockés en local
    Attributes
    ----------

    Example
    -------
    
    '''
    
    def __init__(self,dict_initial):
        '''Constructeur
        Parameters:
        -----------
        dict_initial : dict
            Clés du dictionnaire :
            ---------------------
            zonage1: échelon principal (département ou commune)
            id1: identifiant de l'échelon principal
            zonage2: échelon secondaire (découpage de l'échelon principal)  commune ou parcelle
            date: date du fichier
        '''
        self.dict = dict_initial 

    def genere_dict(self)->list[dict]: 
        '''retourne une liste de dictionnaires
                Exemple: zonage1="departement", id="35", zonage2="commune", date="latest"
                La méthode retourne une liste de dictionnaires avec les communes du département 35
                chaque dictionnaire a entre autres une clée "coordinates" , un clé "id"
                voire une clée "nom" pour le nom de commune
        Parameters:
        -----------
        
        
        Returns
        ------
        list_dict : list[dict]
        
        Example
        -------
        '''
        zonage1 = self.zonage1
        id1= self.id1
        zonage2 = self.zonage2
        date = self.date

        dico_extract_json #à stocker ici

        list_dict = dico_extract_json["features"]
        

        return list_dict
