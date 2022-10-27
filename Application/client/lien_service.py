'''module lien_service.py'''

class LienService():
    '''classe qui créer les dictionnaires utiles pour la couche Service à partir des fichiers .json.gz stockés en local'''
    
    def __init__(self,dict_initial):
        '''Constructeur
        Paramètres:
        -----------
        dict_initial : dict
            Clés du dictionnaire :
            ---------------------
            zonage1: échelon principal (département ou commune)
            id: identifiant de l'échelon principal
            zonage2: échelon secondaire (découpage de l'échelon principal)  commune ou parcelle
            date: date du fichier'''
        self.dict = dict_initial 

    def genere_dict(self)->list[dict]: #la couche client ne renvoie pas un dictionnaire de dictionnaire comme prévu ? 
        '''retourne une liste d'au moins un dictionnaire
                Exemple: zonage1="departement", id="35", zonage2="commune", date="latest"
                La méthode retourne une liste de dictionnaires avec les communes du département 35
                chaque dictionnaire a en plus une clée "coordinates" 
                voire une clée "nom" pour le nom de commune

        
        
        Returns
        ------
        list_dict : list[dict]'''
        list_dict=[]
        

        #à coder, utiliser le Json local

        return list_dict
