import requests
import json    
import os
import gzip

class Telechargement():

    def __init():
        '''Classe qui permet de télécharger des fichiers json.gz depuis un site web
        Attributes
        ----------
        
        url
        path

        Examples
        --------
        
        '''
        pass
    
    def generator_link(id_dep : str, date = "latest", zonage1 = "departements", id_zone = None, zonage2 = "communes"):
        '''Genère un lien url selon certains critères 

        Parameters:
        -----------
            date : str = "latest" 
                sinon saisir au format "AAAA-MM-JJ"
            zonage1 : str = "departements"
                zonage au choix parmi "departements" ou "france" ou "communes"
            id_dep : str
                code de département
            id_zone : str = None
                saisir le code communes si zone1="communes"
            zonage2 : str = "communes"
                zonage au choix parmi "parcelles" ou "communes"
                sauf si zonage1="france" alors laisser par défaut zonage2="communes"

        Returns 
        -------

        Example
        -------
        '''
            
        url = "https://cadastre.data.gouv.fr/data/etalab-cadastre/"

        if zonage1 == "departements":
            id_zone = id_dep
            url_zone1 = id_dep
        elif zonage1 == "communes":
            url_zone1="{}/{}".format(id_dep,id_zone)

        fichier ="cadastre-{}-{}.json.gz".format(id_zone,zonage2)

        if zonage1 == "france" and zonage2== "communes":
            url = "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/france/cadastre-france-communes.json.gz"
        else:
            url = "{}{}/geojson/{}/{}/{}".format(url,date,zonage1,url_zone1,fichier)
        return url
    
    
    def generator_path(url : str):
        '''Méthode qui dirige le fichier json.gz dans un dossier en fonction du zonage_1
        Parameters:
        -----------
        url : str
        Lien du fichier json.gz
        
        Return
        ------
        path
        Chemin du fichier

        Example
        -------
        '''
        path = r'Application/client/data'
        req = requests.get(url)
        filename = req.url[url.rfind('/')+1:]
        if 'departements' in url:
            path = os.path.join(path,'departements')
            if 'communes' in filename :
                path = os.path.join(path,'communes')
            else : 
                path = os.path.join(path,'parcelles')
        elif 'france' in url:
            path = os.path.join(path,'france')
        else : 
            path = os.path.join(path,'communes')
            if 'communes' in filename :
                path = os.path.join(path,'communes')
            else : 
                path = os.path.join(path,'parcelles')
        return(path)

    
    def download(url : str , path : str):
       '''Télécharge un fichier depuis une url donnée et l'enregistre dans un dossier donné
        Parameters
        ----------
        url : str 
        Lien de téléchargement du fichier json.gz

        path : str 
        Chemin vers lequel le fichier json.gz sera stocké

        Example
        -------
       
       '''
       req = requests.get(url)
       filename = req.url[url.rfind('/')+1:]
       
       with req as rq:
            with open(os.path.join(path,filename), 'wb') as file: #possibilité de changer le nom du fichier, ex : 'data.json.gz' au lieu de filename
                file.write(rq.content)
    
    def read_json(url : str, path : str):
        '''Lis le fichier json comme un dictionnaire
        Parameters
        ----------
        path : str 
        Chemin dans lequel le fichier json.gz est stocké

        Return
        ------
        data 
        Fichier json sous la forme d'un dictionnaire python

        Example
        -------
       
       '''
        req = requests.get(url)
        filename = req.url[url.rfind('/')+1:]

        with gzip.open(os.path.join(path,filename),'rb') as file:
            data = json.load(file) #, parse_float=float, parse_int=float
        return(print(data))


    ############################################################### TEST ############################################################################
    
    #test pour fonction qui recup url
    lien_1 = generator_link("08","latest","departements", id_zone = None)
    print(lien_1)
    lien_2 = generator_link("08","latest","communes", id_zone = "08124")
    print(lien_2)

    #test pour le générateur de chemin : 

    print(generator_path('https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04004/cadastre-04004-communes.json.gz'))

    #test fonction telechargement
    download('https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04004/cadastre-04004-communes.json.gz','Application/client/data/commune/commune')
    #download('https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04005/cadastre-04005-communes.json.gz','Application/client/data/commune/commune')
    #download('https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04006/cadastre-04006-communes.json.gz','Application/client/data/commune/commune')




    #lecture du json.gz
    read_json('https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04004/cadastre-04004-communes.json.gz','Application/client/data/commune/commune')
