import requests
import gzip
import os
import json


downloadUrl = r'https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04004/cadastre-04004-communes.json.gz'

req = requests.get(downloadUrl)

print(req.headers)

filename = req.url[downloadUrl.rfind('/')+1:]
path = 'client/data/communes' #coder le chemin en fonction du zonage_1 (commune ou département (cf. nom du fichier))

print(filename)

print(os.path.join(path,filename))


# #téléchargement du json.gz dans le fichier "data"

# with req as rq:
#     with open("test.json.gz", 'wb') as file: #possibilité de changer le nom du fichier, ex : 'data.json.gz' au lieu de filename
#         file.write(rq.content)
with req as rq:
    with open(os.path.join(path,filename), 'wb') as file: #possibilité de changer le nom du fichier, ex : 'data.json.gz' au lieu de filename
        file.write(rq.content)

#lecture du json.gz sous forme de dictionnaire depuis un fichier donné

# data_folder = os.listdir('Application/Client/data/communes')
# data_files_names = data_files_names =[data_folder]
# data_folder[0]

with gzip.open(os.path.join(path,filename),'rb') as file:
    data = json.load(file) #, parse_float=float, parse_int=float
    print(data)
    print(data.get("type"))



