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
