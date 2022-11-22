"""module departementcommunes.py pour définir la classe DepartementCommunes
version 1.0
date 29/10/2022
auteur : Chloé Contant
"""
import os
import time
from datetime import datetime
from abc import ABC, abstractmethod
from storage import Storage

class DepartementsCommunes(Storage):
    '''Classe qui gère le stockage du fichier communes dans départements.
    Attributes :
    -----------
        path : str = 'Application/client/data/departements/communes'
        quota : int = 99
            nombre maximum de fichiers dans le dossier 
    '''

    def __init__(self,path : str = 'Application/client/data/departements/communes', quota : int = 99):
        self.path = path
        self.quota = quota
    #mettre quota dans les attributs de la classe ? 
    #chemin également ? 

    def count(self) : 
        '''Méthode qui compte le nombre de fichiers qu'il y a dans le dossier'''
        count = 0
        for filename in os.listdir(self.path):
            count = count + 1
        return(count)

    def select_files(self):
        
        path = 'Application/client/data/departements/communes'

        quota = 99

        C = self.count()

        time = []
        for filename in os.listdir(self.path) :
            time.append(os.path.getctime(os.path.join(self.path,filename)))
        print(time)

        dictionary = dict(zip(os.listdir(self.path),time)) 

        L = time[0]
        file_remove = []

        while C > self.quota :
            #os.path.getctime(os.path.join(path,os.listdir(path)[0]))
            for filename in os.listdir(self.path) :
                if dictionary[filename] < L :
                    #os.path.getctime(os.path.join(path,filename))
                    #L = os.path.getctime(os.path.join(path,filename))
                    L = dictionary[filename]
                else : 
                    pass
            print(L)
            file_remove.append([key for (key, val) in dictionary.items() if val == L])
            #file_remove = [key for (key, val) in dictionary.items() if val == L]
            #print(file_remove)
        

            #del file_remove[file_remove.index(filename)]

    def delete_files(self):
        '''Méthode qui supprime à partir d'un certain quota les fichiers les plus anciens dans le dossier
        communes étant dans le dossier départements'''
        for filename in file_remove :
            os.remove(os.path.join(self.path,filename))


############################################################### TEST ############################################################################
    
#test pour fonction libère de la place dans le sous-dossier commune du dossier département

D = DepartementsCommunes()
D.count()
D.select_files()
#D.delete_files()

