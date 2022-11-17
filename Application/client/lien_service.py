from client.telechargement import Telechargement

class LienService():
    '''Classe qui créer les dictionnaires utiles pour la couche Service à partir des fichiers .json.gz stockés en local
    
    Attributes
    ----------
    dico : dict

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
        keys = list(self.dico.keys())
        zonage1 = keys[0]
        id1= keys[1]
        zonage2 = keys[2]
        date = keys[3]
        link = telechargement.generator_link(id1, date, zonage1, id_zone, zonage2)
        print(link)
        path = telechargement.generator_paht(link)
        print(path)
        dico_extract_json = read_json(url,path) #dictionnaire

        list_dict = dico_extract_json["features"]
        
        return (list_dict)

############################################################### TEST ############################################################################

#test pour fonction qui genère dictionnaire

D = {'zonage1' : 'departement',
    'id1' : '01',
    'zonage2' : 'commune',
    'date' : 'latest'}
dico = LienService(D).genere_dico()
print(dico)
