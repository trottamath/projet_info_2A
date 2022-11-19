"""module departementcommunes.py pour définir la classe DepartementCommunes
version 1.0
date 05/11/2022
auteur : Chloé Contant
"""
import os
import time
from datetime import datetime
#from abc import ABC, abstractmethod
#from storage import Storage
# from telechargement import Telechargement

class DepartementCommunes():
    '''Classe qui gère le stockage du fichier communes dans départements

    '''

    def create_place(self):
        path = 'Application/client/data/departements/communes'
        count = 0
        now_time = time.ctime()
        now = time.time()
        print(len(os.listdir(path)))

        for filename in os.listdir(path):
            count = count + 1
        
        print(count)

        if count > 10:
            for filename in os.listdir(path):
                if time.ctime(os.path.getctime(os.path.join(path,filename))) < (time.time()- (7*86000)): #les 2 membres sont biens des nombres ? TODO vérifier
                    os.remove(filename)
                else : 
                    print('False')


############################################################### TEST ############################################################################
    
#test pour fonction libère de la place dans le sous-dossier commune du dossier département

D = DepartementCommunes()
D.create_place()
# TypeError: '<' not supported between instances of 'str' and 'float'

