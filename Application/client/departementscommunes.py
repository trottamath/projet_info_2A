"""module departementcommunes.py pour définir la classe DepartementCommunes
version 1.0
date 29/10/2022
auteur : Chloé Contant
"""
import os
import time
from client.storage import Storage

class DepartementsCommunes(Storage):
    '''Classe qui gère le stockage du fichier communes dans départements.
    Attributes :
    -----------
        path : str = 'Application/client/data/departements/communes'
        quota : int = 99
            nombre maximum de fichiers dans le dossier
    '''

    def __init__(
            self,
            path: str = 'Application/client/data/departements/communes',
            quota: int = 101):
        '''constructeur'''
        self.path = path
        self.quota = quota

    def count(self):
        '''Méthode qui compte le nombre de fichiers qu'il y a dans le dossier'''
        count = 0
        for filename in os.listdir(self.path):
            count = count + 1
        return count

    def delete_older_file(self):
        count = self.count()

        while self.quota - 1 < count:

            time = []
            for filename in os.listdir(self.path):
                time.append(os.path.getctime(
                    os.path.join(self.path, filename).replace("\\", "/")))
            min_time = min(time)

            dictionary = dict(zip(os.listdir(self.path), time))

            older_file = []
            older_file = [
                key for (key, val) in dictionary.items() if val == min_time]
            count = count - len(older_file)
            print(older_file)

            for filename in older_file:
                os.remove(os.path.join(self.path, filename).replace("\\", "/"))


######## TEST #####

# test pour fonction libère de la place dans le sous-dossier commune du
# dossier département

D = DepartementsCommunes()
print(D.count())
#D.delete_older_file()
