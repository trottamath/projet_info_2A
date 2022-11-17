import requests
import gzip
import os
import json
import time
import datetime


# downloadUrl = r'https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04004/cadastre-04004-communes.json.gz'

# req = requests.get(downloadUrl)

# print(req.headers)

# filename = req.url[downloadUrl.rfind('/')+1:]
# path = 'Application/client/data/commune/commune' #coder le chemin en fonction du zonage_1 (commune ou département (cf. nom du fichier))

# print(filename)

# print(os.path.join(path,filename))


# #téléchargement du json.gz dans le fichier "data"

# with req as rq:
#     with open("test.json.gz", 'wb') as file: #possibilité de changer le nom du fichier, ex : 'data.json.gz' au lieu de filename
#         file.write(rq.content)
# with req as rq:
#     with open(os.path.join(path,filename), 'wb') as file: #possibilité de changer le nom du fichier, ex : 'data.json.gz' au lieu de filename
#         file.write(rq.content)

#lecture du json.gz sous forme de dictionnaire depuis un fichier donné

# data_folder = os.listdir('Application/Client/data/communes')
# data_files_names = data_files_names =[data_folder]
# data_folder[0]

# with gzip.open(os.path.join(path,filename),'rb') as file:
#     data = json.load(file) #, parse_float=float, parse_int=float
#     #print(data)
#     print(data.get("type"))


ctime = time.ctime(os.path.getctime("Application/client/data/commune/commune/cadastre-04004-communes.json.gz"))
print(ctime)
#print(time.time()-ctime)
# if ctime < time.time()- (3600):
#     print('True')
# else : 
#     print('False')

def create_place():
    path = 'Application/client/data/commune/commune'
    count = 0
    #now_time = time.ctime()
    #now = time.time()
    for filename in os.listdir(path):
        count = count + 1
    
    print(count)
    
    if count > 2:
        for filename in os.listdir(path):
            if os.path.getctime(os.path.join(path,filename)) < (time.time()- 360):
                os.remove(os.path.join(path,filename))
                print('True')
            else : 
                print('False')


create_place()
