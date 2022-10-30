import os
from datetime import datetime

class Suppression():
    '''Classe qui permet de gérer le stockage des fichiers, elle supprime les fichiers s'ils sont trop nombreux'''
    
    def __init__():
        pass


    def delete_file(filename):
        '''Méthode qui supprime un fichier en particulier
        Parameters:
        -----------
        
        Return:
        -----------
        '''
        if os.path.exists(filename):
            os.remove(filename)
        else:
            print("The file does not exist")
        
        #os.rmdir("myfolder") #supprime un dossier

    def create_place():
        '''Méthode qui supprime le fichier le plus ancien d'un dossier pour libérer de la place'''
        pass
    #fixer un quota par dossier 
    #récuperer les dates de téléchargement pour supprimer le plus ancien