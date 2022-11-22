"""module departementcommunes.py pour définir la classe DepartementCommunes
version 1.0
date 30/10/2022
auteur : Chloé Contant
"""
import os
import time
from datetime import datetime
from abc import ABC, abstractmethod
from storage import Storage

class DepartementsParcelles(Storage):
    '''Classe qui gère le stockage du fichier communes dans départements

    '''

    def __init__(self):
        pass

    def create_place(self):
        '''Méthode qui supprime à partir d'un certain quota les fichiers les plus anciens dans le dossier
        communes étant dans le dossier départements'''
        
        path = 'Application/client/data/departements/parcelles'
        count = 0

        for filename in os.listdir(path):
            count = count + 1

        time = []
        for filename in os.listdir(path) :
            time.append(os.path.getctime(os.path.join(path,filename)))

        dictionary = dict(zip(os.listdir(path),time)) 

        if count > 50 :
            L = os.path.getctime(os.path.join(path,os.listdir(path)[0]))
            for filename in os.listdir(path) :
                if L > os.path.getctime(os.path.join(path,filename)):
                    L = os.path.getctime(os.path.join(path,filename))
                else : 
                    pass
        
            file_remove = [key  for (key, val) in dictionary.items() if val == L]
        
            for filename in file_remove :
                os.remove(os.path.join(path,filename))

        else : 
            pass


############################################################### TEST ############################################################################
    
#test pour fonction libère de la place dans le sous-dossier commune du dossier département

D = DepartementsParcelles()
D.create_place()

