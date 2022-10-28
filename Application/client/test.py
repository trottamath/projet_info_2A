import requests
import gzip
import os
import json
import pandas



downloadUrl ='https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04004/cadastre-04004-communes.json.gz'

req = requests.get(downloadUrl)

print(req.headers)

filename = req.url[downloadUrl.rfind('/')+1:]
path = 'Application/Client/data/communes' #coder le chemin en fonction du zonage_1 (commune ou département (cf. nom du fichier))

print(filename)

print(os.path.join(path,filename))

#téléchargement du json.gz dans le fichier "data"

with req as rq:
    with gzip.open(os.path.join(path,filename), 'wb') as file: #possibilité de changer le nom du fichier, ex : 'data.json.gz' au lieu de filename
        file.write(rq.content)

#lecture du json.gz

with gzip.open(filename,mode="rt", encoding='utf-8') as gzfile:
    data = json.load(gzfile) #, parse_float=float, parse_int=float
    print(data) 

# def lecture_dictionnaire(path,name_file):

#     with gzip.open(name_file,mode="rt", encoding='utf-8') as gzfile:
#         data = json.load(gzfile) #, parse_float=float, parse_int=float
#         print(data) 
        # print(data.get("type"))

#lecture_dictionnaire(path,name_file)

#os.path.join(path,filename)

# body = []

# with gzip.open('cadastre-04004-communes.json.gz', mode="rt", encoding='utf-8') as gzfile:
#     body.extend(
#         json.load(gzfile, parse_float=float, parse_int=float))

# print(body)