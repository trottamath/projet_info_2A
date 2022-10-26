from client.lien_service import LienService

class Instanciation():
    def __init__(self,zonage1:str, id1:str, zonage2:str,date:str )->dict:
        '''constructeur
        Paramètres:
        -----------
        zonage1: échelon principal (departement ou commune)
        id1: identifiant de l'échelon principal
        zonage2: échelon secondaire (découpage de l'échelon principal)  commune ou parcelle
        date: date du fichier'''
        self.dico = {"zonage1": zonage1, "id1": id1, "zonage2": zonage2, "date": date}
    

test= Instanciation("dep","13","com","latest").dico
print(test)