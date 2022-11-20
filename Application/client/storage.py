from abc import ABC, abstractmethod
"""module storage.py pour définir la classe Storage
version 1.0
date 05/11/2022
auteur : Chloé Contant
"""

class Storage(ABC):
    '''Classe qui permet de gérer le stockage des fichiers, elle supprime les fichiers s'ils sont trop nombreux dans un dossier
        Attributes
        ----------
        '''
    @abstractmethod
    def __init__():
        pass


    # def delete_file(path):
    #     '''Méthode qui supprime un fichier en particulier
    #     Parameters:
    #     -----------
    #     path 
    #     Chemin entier du fichier 
        
    #     Return:
    #     -----------
    #     '''
    #     if os.path.exists(filename):
    #         os.remove(filename)
    #         print("The file has been deleted")
    #     else:
    #         print("The file does not exist")
        
    #     #os.rmdir("myfolder") #supprime un dossier

    def create_place():
        '''Méthode qui supprime le fichier le plus ancien d'un dossier pour libérer de la place
        Parameters
        ----------

        Returns
        -------

        Example
        -------
        '''
        pass
    #fixer un quota par dossier 
    #récuperer les dates de téléchargement pour supprimer le plus ancien
    #héritage selon les dossiers communes départements... 