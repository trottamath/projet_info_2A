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
                identifiant du zonage1
            zonage2 : str = "communes"
                zonage au choix parmi "parcelles" ou "communes"
                sauf si zonage1="france" alors laisser par défaut zonage2="communes"
                '''

    def __init__(self, id_zone1 = None , zonage1 = "departements",  zonage2 = "communes", date = "latest"):
        '''constructeur de la classe Telechargement
        
        Parameters:
        -----------
            date : str = "latest" 
                sinon saisir au format "AAAA-MM-JJ"
            zonage1 : str = "departements"
                zonage au choix parmi "departements" ou "france" ou "communes"
            id_zone1 : str
                identifiant du zonage1 (code)
            zonage2 : str = "communes"
                zonage au choix parmi "parcelles" ou "communes"
                sauf si zonage1="france" alors laisser par défaut zonage2="communes" et id_zone = None
        '''

        self.id_dep = id_zone1[0:2]
        if self.id_dep == "97":
            self.id_dep = id_zone1[0:3]
        self.date = date
        self.zonage1 = zonage1
        self.id_zone = id_zone1
        self.zonage2 = zonage2
    
    def generator_link(self) -> str :
        '''Genère un lien url selon certains critères 

        Returns 
        -------
            url : str
        '''
            
        url = "https://cadastre.data.gouv.fr/data/etalab-cadastre/"

        if self.zonage1 == "departements":
            #self.id_zone = self.id_dep
            url_zone1 = self.id_dep
        elif self.zonage1 == "communes":
            url_zone1="{}/{}".format(self.id_dep,self.id_zone)
        

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
        path = r'Application/client/data'  #essai avec modification provisoire de '/data/' 
        req = requests.get(url)
        filename = req.url[url.rfind('/')+1:]
        if 'departements' in url:
            path = os.path.join(path,'departements').replace("\\","/")
            if 'communes' in filename :
                path = os.path.join(path,'communes').replace("\\","/")
            else : 
                path = os.path.join(path,'parcelles').replace("\\","/")
        elif 'france' in url:
            path = os.path.join(path,'france').replace("\\","/")
        else : 
            path = os.path.join(path,'communes').replace("\\","/")
            if 'communes' in filename :
                path = os.path.join(path,'communes').replace("\\","/")
            else : 
                path = os.path.join(path,'parcelles').replace("\\","/")
        return(path)

    
    def download(self):
       '''Télécharge un fichier depuis une url donnée et l'enregistre dans un dossier donné
             
       '''
       url = self.generator_link()

       path= self.generator_path() 
       print(path)
       req = requests.get(url)
       filename = req.url[url.rfind('/')+1:]
       print(filename)
       chemin = os.path.join(path,filename).replace("\\","/") #version d'origine mais avec bug (non effacée pour conserver la version qui fonctionne sur le pc de Chloé mais pas sur la VM)
       print(chemin)
       
       #chemin2 = os.path.dirname(os.path.abspath(__file__))+path+"/"+filename
       #print(chemin2) #version2 ne fonctionne pas dès que le test n'est plus dans ce fichier
       
       with req as rq:
            with open(chemin, 'wb') as file: #possibilité de changer le nom du fichier, ex : 'data.json.gz' au lieu de filename
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
        chemin = os.path.join(path,filename).replace("\\","/") #version d'origine mais avec bug sur la VM
        print(chemin)

        #chemin2 = os.path.dirname(os.path.abspath(__file__))+path+"/"+filename
        #print(chemin2) #version2 qui ne fonctionne qu'en test dans le même fichier... WTF

        with gzip.open(chemin,'rb') as file:
           data = json.load(file) #, parse_float=float, parse_int=float
        return(data)


############################################################### TEST ############################################################################
    # à faire absolument dans un fichier test, sinon ça fait croire que c ok alors que non
#test pour fonction qui recup url

# t1 = Telechargement(id_zone1="08",date="latest",zonage1="departements")
# lien_1 = t1.generator_link()
# print(lien_1)

#t2 = Telechargement(date="latest",zonage1="communes", id_zone1 = "08124")
# lien_2 = t2.generator_link()
# print(lien_2)

#t3= Telechargement(id_zone1="08",date="latest",zonage1="france",zonage2="communes")
# lien_3 = t3.generator_link()
# print(lien_3)

#test pour le générateur de chemin : 
#t4 = Telechargement(id_zone1="13400",zonage1="communes",zonage2="parcelles")
#t4.generator_path()

#test fonction telechargement
t4 = Telechargement(id_zone1="08004",zonage1="communes")
#t4.download()

#t5 = Telechargement(id_zone1="08",date="latest",zonage1="departements")
#t5.download()


#lecture de json vers dictionnaire
dico = t4.read_json()
print(dico) #ça fonctionne sur la vm TODO à tester ailleur
