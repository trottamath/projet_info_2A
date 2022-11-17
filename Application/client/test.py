import requests
import gzip
import os
import json
import time
import datetime


<<<<<<< HEAD
downloadUrl =r'https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04004/cadastre-04004-communes.json.gz'
=======
# downloadUrl = r'https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/04/04004/cadastre-04004-communes.json.gz'
>>>>>>> a73275470c37513a7bcec274d2fd5c2b03e78972

# req = requests.get(downloadUrl)

# print(req.headers)

# filename = req.url[downloadUrl.rfind('/')+1:]
# path = 'Application/client/data/commune/commune' #coder le chemin en fonction du zonage_1 (commune ou département (cf. nom du fichier))

# print(filename)

# print(os.path.join(path,filename))


<<<<<<< HEAD
#téléchargement du json.gz dans le fichier "data"
f = open(r'c:\toto.txt',"w")
f.close()
with req as rq:
    with open('test.json.gz', 'wb') as file: #possibilité de changer le nom du fichier, ex : 'data.json.gz' au lieu de filename
        file.write(rq.content)
=======
# #téléchargement du json.gz dans le fichier "data"

# with req as rq:
#     with open("test.json.gz", 'wb') as file: #possibilité de changer le nom du fichier, ex : 'data.json.gz' au lieu de filename
#         file.write(rq.content)
# with req as rq:
#     with open(os.path.join(path,filename), 'wb') as file: #possibilité de changer le nom du fichier, ex : 'data.json.gz' au lieu de filename
#         file.write(rq.content)
>>>>>>> a73275470c37513a7bcec274d2fd5c2b03e78972

#lecture du json.gz sous forme de dictionnaire depuis un fichier donné

# data_folder = os.listdir('Application/Client/data/communes')
# data_files_names = data_files_names =[data_folder]
# data_folder[0]

<<<<<<< HEAD
with gzip.open('test.json.gz','rb') as f_in :
    with open('json_decomp.json','wb') as f_out:
        shutil.copyfileobj(f_in,f_out)

#with gzip.open(filename,'rb') as file:
    #raw_json = file.read()
    #data = json.load(file) #, parse_float=float, parse_int=float
    #print(data)
    #print(data.get("type"))

#os.path.join(path,filename)

=======
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
>>>>>>> a73275470c37513a7bcec274d2fd5c2b03e78972
