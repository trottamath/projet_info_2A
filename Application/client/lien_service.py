'''module lien_service.py'''

class LienService():
    '''classe qui créer les dictionnaires utiles pour la couche Service à partir des fichier Json locaux'''
    def __init__(self,dico_initial):
        '''constructeur
        Paramètres:
        -----------
        dico_initial : dict
            clés du dictionnaire
            ---------------------
            zonage1: échelon principal (departement ou commune)
            id1: identifiant de l'échelon principal
            zonage2: échelon secondaire (découpage de l'échelon principal)  commune ou parcelle
            date: date du fichier'''
        self.dico = dico_initial 

    def genere_dico(self)->list[dict]:
        '''retourne une liste d'au moins un dictionnaire
                par exemple: lorsque zonage1="departement", id1="35", zonage2="commune", date="latest"
                la méthode retourne un liste avec un dictionnaire pour chaque commune du département 35
                chaque dictionnaire a en plus une clée "coordinates" 
                voire une clée "nom" pour le nom de commune

        
        
        Retuns
        ------
        list_dico : list[dict]'''
        list_dico=[]
        

        #à coder, utiliser le Json local

        return list_dico
