"""module telechargement.py pour définir la classe Telechargement
version 1.1
date 20/10/2022
auteurs : Chloé Contant, Jean-Philippe Trotta et Puchalski Eva
"""

import requests
import json    
import os
import gzip

class Telechargement():

    def __init():
        '''Classe qui permet de télécharger des fichiers json.gz depuis un site web'''
        pass
    
    def generator_link(self, id_dep : str, date = "latest", zonage1 = "departements", id_zone = None, zonage2 = "communes"):
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
            url : str
        '''
            
        url = "https://cadastre.data.gouv.fr/data/etalab-cadastre/"

        if zonage1 == "departements":
            id_zone = id_dep
            url_zone1 = id_dep
        elif zonage1 == "communes":
            url_zone1="{}/{}".format(id_dep,id_zone)
        else :
            print("Départements ou communes")

        fichier ="cadastre-{}-{}.json.gz".format(id_zone,zonage2)

        if zonage1 == "france" and zonage2== "communes":
            url = "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/france/cadastre-france-communes.json.gz"
        else:
            url = "{}{}/geojson/{}/{}/{}".format(url,date,zonage1,url_zone1,fichier)
        return url
    
    
    def generator_path(self, url : str):
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
        path = r'/data'  #essaie avec modification provisoire de 'Application/client/data' 
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

    
    def download(self, url : str , path : str):
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
       #path = "Application/client"+path #ajout provisoire à tester
       #path= generator_path(url=url) #pourquoi path est un paramètre au lieu d'utiliser la fonction generator_path ? TODO
       req = requests.get(url)
       filename = req.url[url.rfind('/')+1:]
       print(filename)
       print(os.path.join(path,filename))
       chemin1 = os.path.join(path,filename) #version d'origine mais avec bug (non effacée pour conserver la version qui fonctionne sur le pc de Chloé mais pas sur la VM)
       print(chemin1)
       
       chemin2 = os.path.dirname(os.path.abspath(__file__))+path+"/"+filename
       print(chemin2) #version2 à tester
       
       with req as rq:
            with open(chemin2, 'wb') as file: #possibilité de changer le nom du fichier, ex : 'data.json.gz' au lieu de filename
                file.write(rq.content)
    
    def read_json(self, url : str, path : str): #bug TODO méthode à tester !
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
       #path= generator_path(url=url) #pourquoi path est un paramètre au lieu d'utiliser la fonction generator_path ? TODO
        req = requests.get(url)
        
        filename = req.url[url.rfind('/')+1:]

        print(filename)
        chemin1 = os.path.join(path,filename) #version d'origine mais avec bug
        print(chemin1)

        chemin2 = os.path.dirname(os.path.abspath(__file__))+path+"/"+filename
        print(chemin2) #version2 à tester

        with gzip.open(chemin2,'rb') as file:
           data = json.load(file) #, parse_float=float, parse_int=float
        return(data)


############################################################### TEST ############################################################################
    
#test pour fonction qui recup url
# t = Telechargement()
# lien_1 = t.generator_link(id_dep="08",date="latest",zonage1="departements", id_zone = None)
# print(lien_1)
# lien_2 = t.generator_link("08","latest","communes", id_zone = "08124")
# print(lien_2)
# lien_3 = t.generator_link(id_dep="08",date="latest",zonage1="france",id_zone=None,zonage2="communes")
# print(lien_3)

#test pour le générateur de chemin : 

#print(generator_path('https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04004/cadastre-04004-communes.json.gz'))

#test fonction telechargement
#download('https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04004/cadastre-04004-communes.json.gz','Application/client/data/communes/communes')
#download('https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04005/cadastre-04005-communes.json.gz','Application/client/data/communes/communes')

#Telechargement().download('https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04006/cadastre-04006-communes.json.gz','/data/communes/communes') #ça fonctionne TODO

#path1=Telechargement().generator_path(url='https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04006/cadastre-04006-communes.json.gz')
#print(path1)
#lecture du json.gz

#dico = Telechargement().read_json('https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04004/cadastre-04004-communes.json.gz','/data/communes/communes')
#print(dico) #ça fonctionne sur la vm TODO à tester ailleur
