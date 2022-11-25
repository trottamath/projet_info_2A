'''module departement.py pour définir la classe Departement
on initialise ce module par l'import d'un fichier csv qui contient les couples de départements limitrophes

auteur: Jean-Philippe Trotta
date : 10/10/2022
'''

import csv
from pathlib import Path 
script_location=Path(__file__).absolute().parent
file_location = script_location / 'departements_contigus.csv'
file = file_location.open()
data = csv.reader(file,delimiter=';')

dep1=[]
dep2=[]
for col in data:
    dep1.append(col[0])
    dep2.append(col[1])


class Departement():
    '''classe Departement
    Attribut:
    ---------
        id_dep : str
            le code de département''' 
    
    def __init__(self,id_dep:str):
        '''constructeur'''
        self.id_dep=id_dep
    
    def dep_contig(self)->list[str]:
        '''retourne la liste des identifients de départements limitrophes à ce département'''
        liste_dep=[]
        for i in range(len(dep1)):
            if dep1[i]==self.id_dep:
                liste_dep.append(dep2[i])
            if dep2[i]==self.id_dep:
                liste_dep.append(dep1[i])
        return liste_dep


#départements à anomalies dans le json:
list_pb = ["06", "14", "15", "16", "21", "22", "24", "25", "27", "28", "29", "34", "40", "43", "50", "51", "54", "55", "59", "60", "65", "67", "69", "77", "79", "81", "87", "90", "96", "971", "975"]
#print(len(list_pb))
list_next=[]
for i in range(len(dep1)):
    if dep1[i] in list_pb and dep2[i] not in list_pb and dep2[i] not in list_next:
        list_next.append(dep2[i])
    if dep1[i] not in list_pb and dep2[i] in list_pb and dep1[i] not in list_next:
        list_next.append(dep1[i])
list_pb = list_pb + list_next
list_pb.sort()
#print(list_pb) # il reste 05, 09, 13, 2A, 2B, 26, 37, 44, 73, 74, 75, 84 qui fonctionnent sans anomalies dans les départements voisins

