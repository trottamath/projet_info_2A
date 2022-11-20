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
    '''Classe qui permet de télécharger des fichiers json.gz depuis un site web
    Attributs :
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
                '''

    def __init__(self, id_dep : str, date = "latest", zonage1 = "departements", id_zone = None, zonage2 = "communes"):
        '''constructeur de la classe Telechargement
        
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
        '''

        self.id_dep = id_dep
        self.date = date
        self.zonage1 = zonage1
        self.id_zone = id_zone
        self.zonage2 = zonage2
    
    def generator_link(self) -> str :
        '''Genère un lien url selon certains critères 

        Returns 
        -------
            url : str
        '''
            
        url = "https://cadastre.data.gouv.fr/data/etalab-cadastre/"

        if self.zonage1 == "departements":
            self.id_zone = self.id_dep
            url_zone1 = self.id_dep
        elif self.zonage1 == "communes":
            url_zone1="{}/{}".format(self.id_dep,self.id_zone)
        else :
            print("Départements ou communes")

        fichier ="cadastre-{}-{}.json.gz".format(self.id_zone,self.zonage2)

        if self.zonage1 == "france" and self.zonage2== "communes":
            url = "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/france/cadastre-france-communes.json.gz"
        else:
            url = "{}{}/geojson/{}/{}/{}".format(url,self.date,self.zonage1,url_zone1,fichier)
        return url
    
    
    def generator_path(self) -> str:
        '''Méthode qui dirige le fichier json.gz dans un dossier en fonction du zonage_1
        
        Return
        ------
            path : str
                Chemin du fichier

        '''
        url = self.generator_link()
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

    
    def download(self):
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
       url = self.generator_link()
       #path = "Application/client"+self.generator_path(url) #ajout provisoire à tester
       path= self.generator_path() 
       req = requests.get(url)
       filename = req.url[url.rfind('/')+1:]
       print(filename)
       print(os.path.join(path,filename))
       chemin1 = os.path.join(path,filename) #version d'origine mais avec bug (non effacée pour conserver la version qui fonctionne sur le pc de Chloé mais pas sur la VM)
       print(chemin1)
       
       chemin2 = os.path.dirname(os.path.abspath(__file__))+path+"/"+filename
       print(chemin2) #version2 à tester, OK sur VM
       
       with req as rq:
            with open(chemin2, 'wb') as file: #possibilité de changer le nom du fichier, ex : 'data.json.gz' au lieu de filename
                file.write(rq.content)
    
    def read_json(self) -> dict : #bug TODO méthode à tester !
        '''Lis le fichier json comme un dictionnaire
        Parameters
        ----------
        path : str 
        Chemin dans lequel le fichier json.gz est stocké

        Return
        ------
        data 
        Fichier json sous la forme d'un dictionnaire python

       
       '''
        url = self.generator_link()
        path = self.generator_path() 
        req = requests.get(url)
        
        filename = req.url[url.rfind('/')+1:]

        print(filename)
        chemin1 = os.path.join(path,filename) #version d'origine mais avec bug (à supprimer ?)
        print(chemin1)

        chemin2 = os.path.dirname(os.path.abspath(__file__))+path+"/"+filename
        print(chemin2) #version2 à tester, ok sur VM

        with gzip.open(chemin2,'rb') as file:
           data = json.load(file) #, parse_float=float, parse_int=float
        return(data)


############################################################### TEST ############################################################################
    
#test pour fonction qui recup url

# t1 = Telechargement(id_dep="08",date="latest",zonage1="departements", id_zone = None)
# lien_1 = t1.generator_link()
# print(lien_1)

#t2 = Telechargement(id_dep="08",date="latest",zonage1="communes", id_zone = "08124")
# lien_2 = t2.generator_link()
# print(lien_2)

#t3= Telechargement(id_dep="08",date="latest",zonage1="france",id_zone=None,zonage2="communes")
# lien_3 = t3.generator_link()
# print(lien_3)

#test pour le générateur de chemin : 
#t4 = Telechargement(id_dep="04",id_zone="04004",zonage1="communes")
#print(t4.generator_path())

#test fonction telechargement
#t4 = Telechargement(id_dep="06",id_zone="06005",zonage1="communes")
#t4.download()

#lecture de json vers dictionnaire
#dico = t4.read_json()
#print(dico) #ça fonctionne sur la vm TODO à tester ailleur
