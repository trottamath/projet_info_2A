import requests
#import gzip

downloadUrl ='https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04004/cadastre-04004-communes.json.gz'

req = requests.get(downloadUrl)

print(req.headers)

filename = req.url[downloadUrl.rfind('/')+1:]

print(filename)


#téléchargement du json.gz

with open(filename, 'wb') as f:
    for data in req.iter_content():
            f.write(data)

#téléchargement du json et transfère dans le fichier data(inputs)



#lecture du json.gz
with gzip.GzipFile(filename, 'rb') as f:
    data = f.read()
print(data)