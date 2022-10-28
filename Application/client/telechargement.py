import requests
import json    
import os

class Telechargement():
    
    #@staticmethod
    def generator_link(id_dep : str, date = "latest", zonage1 = "departements", id_zone = None, zonage2 = "communes" ):
        '''import d'un fichier json à partir du web
        Parametres:
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
    
    def download(url : str , path : str):
       '''telecharge un fichier depuis une url donnée et l'enregistre dans un dossier donné
       
        Attributes
        ----------
        url : str 
        Lien de téléchargement du fichier json.gz

        path : str 
        Chemin vers lequel le fichier json.gz sera stocké
       
       '''
       req = requests.get(url)
       filename = req.url[url.rfind('/')+1:]
       
       with req as rq:
            with open(os.path.join(path,filename), 'wb') as file: #possibilité de changer le nom du fichier, ex : 'data.json.gz' au lieu de filename
                file.write(rq.content)
        

    ############################################################### TEST ############################################################################
    
    #test pour fonction qui recup url
    lien_1 = generator_link("08","latest","departements", id_zone = None)
    print(lien_1)
    lien_2 = generator_link("08","latest","communes", id_zone = "08124")
    print(lien_2)

    #test fonction telechargement
    download('https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04004/cadastre-04004-communes.json.gz','Application/client/data/communes')

    #lecture du json.gz
