import requests
import gzip
import os
import tarfile

downloadUrl ='https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04004/cadastre-04004-communes.json.gz'

req = requests.get(downloadUrl)

print(req.headers)

filename = req.url[downloadUrl.rfind('/')+1:]
path = 'Application/Client/data/communes' #coder le chemin en fonction du zonage_1 (commune ou département (cf. nom du fichier))

print(filename)

#téléchargement du json.gz dans le fichier "data"

with req as rq:
    with gzip.open(os.path.join(path,filename), 'wb') as file: #possibilité de changer le nom du fichier, ex : 'data.json.gz' au lieu de filename
        file.write(rq.content)
        
#lecture du json.gz
with gzip.GzipFile(filename,'rb') as f:
    donnees = f.read()
print(donnees)