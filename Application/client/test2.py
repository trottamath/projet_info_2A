import requests
import gzip
import shutil
import os
import json


# downloadUrl = r'https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04004/cadastre-04004-communes.json.gz'

# req = requests.get(downloadUrl)

# print(req.headers)

# filename = req.url[downloadUrl.rfind('/')+1:]
# path = 'Application/Client/data/communes' #coder le chemin en fonction du zonage_1 (commune ou département (cf. nom du fichier))

# print(filename)

# print(os.path.join(path,filename))


# #téléchargement du json.gz dans le fichier "data"

# with req as rq:
#     with open("test.json.gz", 'wb') as file: #possibilité de changer le nom du fichier, ex : 'data.json.gz' au lieu de filename
#         file.write(rq.content)

#lecture du json.gz sous forme de dictionnaire depuis un fichier donné

# data_folder = os.listdir('Application/Client/data/communes')
# data_files_names = data_files_names =[data_folder]
# data_folder[0]

# with gzip.open("test.json.gz",'rb') as f_in :
#     with open('client\data\communes\json_decomp.json','wb') as f_out:
#         shutil.copyfileobj(f_in,f_out)

#with gzip.open(filename,'rb') as file:
    #raw_json = file.read()
    #data = json.load(file) #, parse_float=float, parse_int=float
    #print(data)
    #print(data.get("type"))

#os.path.join(path,filename)

os.remove('Application/client/data/communes/cadastre-04004-communes.json.gz')