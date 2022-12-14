"""module telechargement.py pour définir la classe Telechargement
version 1.1
date 20/10/2022
auteurs : Chloé Contant, Jean-Philippe Trotta et Eva Puchalski
"""

import json
import os
import gzip
import requests
import urllib.request
from client.departementscommunes import DepartementsCommunes
from client.departementsparcelles import DepartementsParcelles
from client.communescommunes import CommunesCommunes
from client.communesparcelles import CommunesParcelles

class Telechargement():
    '''Classe qui permet de télécharger des fichiers json.gz depuis un site web
    Attributes :
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

    def __init__(
            self,
            id_zone1=None,
            zonage1="departements",
            zonage2="communes",
            date="latest"):
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

        if self.date == "latest": #webscapping de la vraie date
            url = "https://cadastre.data.gouv.fr/data/etalab-cadastre/"
            opener = urllib.request.FancyURLopener({})
            date = ''
            with opener.open(url) as file:
                content = file.readlines()
                previous_line = ''
                for line in content:
                    line = str(line)
                    if 'latest' in line:
                        previous_line = previous_line[previous_line.index('''/">''')+3:previous_line.index("/</a>")]
                        date = previous_line.strip(' ')
                    else :
                        previous_line = line
            self.date = date


    def generator_link(self) -> str:
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
            url_zone1 = "{}/{}".format(self.id_dep, self.id_zone)

        fichier = "cadastre-{}-{}.json.gz".format(self.id_zone, self.zonage2)

        if self.zonage1 == "france" and self.zonage2 == "communes":
            url = "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/france/cadastre-france-communes.json.gz"
        else:
            url = "{}{}/geojson/{}/{}/{}".format(
                url, self.date, self.zonage1, url_zone1, fichier)
        return url

    def generator_path(self) -> str:
        '''Méthode qui dirige le fichier json.gz dans un dossier en fonction du zonage_1

        Return
        ------
            path : str
                Chemin du fichier

        '''
        url = self.generator_link()
        path = r'Application/client/data'
        req = requests.get(url)
        filename = req.url[url.rfind('/') + 1:]
        if 'departements' in url:
            path = os.path.join(path, 'departements').replace("\\", "/")
            if 'communes' in filename:
                path = os.path.join(path, 'communes').replace("\\", "/")
            else:
                path = os.path.join(path, 'parcelles').replace("\\", "/")
        elif 'france' in url:
            path = os.path.join(path, 'france').replace("\\", "/")
        else:
            path = os.path.join(path, 'communes').replace("\\", "/")
            if 'communes' in filename:
                path = os.path.join(path, 'communes').replace("\\", "/")
            else:
                path = os.path.join(path, 'parcelles').replace("\\", "/")
        return(path)

    def download(self):
        '''Télécharge un fichier depuis une url donnée et
        l'enregistre dans un dossier donné

        ''' 
        url = self.generator_link()
        path = self.generator_path()

        if 'departements' in path : 
            if 'communes' in path :
                DepartementsCommunes().delete_older_file()
            else :
                DepartementsParcelles().delete_older_file()
        else : 
            if 'parcelles' in path : 
                CommunesParcelles().delete_older_file()
            else : 
                CommunesCommunes().delete_older_file()

        req = requests.get(url)
        filename = req.url[url.rfind('/') + 1:]
        chemin = os.path.join(path, ('cadastre-{}-{}-{}.json.gz').format(
            self.id_zone, self.zonage2, self.date).replace("\\", "/"))
        #print(chemin)
        with req as request:
            with open(chemin, 'wb') as file:
                file.write(request.content)
                #print(("Le fichier {} a bien été téléchargé.").format(filename))
        print("{} est téléchargé".format(chemin))

    def recherche_fichier(self) -> bool:
        '''Méthode qui regarde si le fichier existe en local

        Returns
        -------
            bool
        '''
        url = self.generator_link()
        path = self.generator_path()
        req = requests.get(url)
        filename = req.url[url.rfind('/') + 1:]

        #chemin = os.path.join(path,filename).replace("\\","/")
        chemin = os.path.join(path, ('cadastre-{}-{}-{}.json.gz').format(
            self.id_zone, self.zonage2, self.date).replace("\\", "/"))

        isfile = os.path.isfile(chemin)

        return isfile

    def read_json(self) -> dict:
        '''Lis le fichier json comme un dictionnaire

        Return
        ------
            dict
        '''
        if self.recherche_fichier() == False:
            self.download()

        url = self.generator_link()
        path = self.generator_path()
        req = requests.get(url)

        filename = req.url[url.rfind('/') + 1:]
        chemin = os.path.join(path, ('cadastre-{}-{}-{}.json.gz').format(
            self.id_zone, self.zonage2, self.date).replace("\\", "/"))
        print("{} est lu".format(chemin))

        with gzip.open(chemin, 'rb') as file:
            # , parse_float=float, parse_int=float
            # TODO il y a pb ici lorsque le code du zonage1 est faux.
            data = json.load(file)
        return data


