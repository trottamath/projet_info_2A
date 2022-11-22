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

    def count(self) :
        '''Méthode qui compte le nombre de fichiers qu'il y a dans le dossier'''
        count = 0
        for filename in os.listdir(self.path):
            count = count + 1
        return(count)

    def find_older_file(self):
        C = self.count()

        time = []
        for filename in os.listdir(self.path) :
            time.append(os.path.getctime(os.path.join(self.path,filename)))
        min_time = min(time)
        print(min_time)


        dictionary = dict(zip(os.listdir(self.path),time))

        older_file = []

        while self.quota < C :
            #L = time[0]
            # for filename in os.listdir(self.path) :
            #     if dictionary[filename] < L :
            #             #os.path.getctime(os.path.join(path,filename))
            #             #L = os.path.getctime(os.path.join(path,filename))
            #         L = dictionary[filename]
            #     else :
            #         pass
            #older_file.append([key for (key, val) in dictionary.items() if val == L])
            older_file = [key for (key, val) in dictionary.items() if val == min_time]
            print(older_file)
            C = C - len(older_file)
            # #del file_remove[file_remove.index(filename)]
            # #return(older_file)
            # for filename in older_file :
            #     os.remove(os.path.join(self.path,filename))


    def select_files(self) :
        '''Méthode qui sélectionne les fichiers du dossier à supprimer'''
        C = self.count()

        while self.quota < C :
            self.find_older_file()

        return(older_file)



    def delete_files(self) :
        '''Méthode qui supprime à partir d'un certain quota les fichiers les plus anciens dans le dossier
        communes étant dans le dossier départements'''



############################################################### TEST ############################################################################

#test pour fonction libère de la place dans le sous-dossier commune du dossier département

D = DepartementsCommunes()
print(D.count())
print(D.find_older_file())
#D.select_files()
#D.delete_files()

