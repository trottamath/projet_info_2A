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
    '''Classe qui gère le stockage du fichier communes dans départements

    '''

    def __init__(self):
        pass
    #mettre quota dans les attributs de la classe ? 

    def create_place(self):
        '''Méthode qui supprime à partir d'un certain quota les fichiers les plus anciens dans le dossier
        communes étant dans le dossier départements'''
        
        path = 'Application/client/data/departements/communes'
        count = 0
        quota = 90

        for filename in os.listdir(path):
            count = count + 1
        print(count)

        time = []
        for filename in os.listdir(path) :
            time.append(os.path.getctime(os.path.join(path,filename)))

        dictionary = dict(zip(os.listdir(path),time)) 

        while count > quota :
            L = os.path.getctime(os.path.join(path,os.listdir(path)[0]))
            for filename in os.listdir(path) :
                if os.path.getctime(os.path.join(path,filename)) < L :
                    L = os.path.getctime(os.path.join(path,filename))
                else : 
                    pass
                print(L)

                file_remove = [key for (key, val) in dictionary.items() if val == L]
                print(file_remove)
        
                for filename in file_remove :
                    os.remove(os.path.join(path,filename))
                    del file_remove[file_remove.index(filename)]

############################################################### TEST ############################################################################
    
#test pour fonction libère de la place dans le sous-dossier commune du dossier département

D = DepartementsCommunes()
D.create_place()

