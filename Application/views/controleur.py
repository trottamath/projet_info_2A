#à supprimer 

from service.requete import Requete

# utiliser Requete(dico_requete= ???? ).Get_or_create()
# voir les clés de dico_requete (à récuperer par Insomnia ?)
            #dico_requete: dict
               # les clées de ce dictionnaire sont
                #num : str
                 #   numero de la requete (1 ou 2 dans le cas de l'appel à la DAO)
                  #  "1" pour les communes contigües à la commune donnée
                   # "2" pour les parcelles en limite de la commune donnée
                    #"3" pour les parcelles contigües à la parcelle donnée
               # id : str
                #    identifiant du zonage donnée
                #date : str
                 #   date du fichier cadatral de référence

class Controler:
    """."""

    def __init__(self, id_utilisateur,id_requete, view):
        """Has a deck, a list of players and a view."""
        # models
        self.id_utilisateur = id_utilisateur
        self.id_requete = id_requete

        # views
        self.view = view


#Le rôle des contrôleurs est de récupérer les données utilisateurs, 
#de les filtrer et de les contrôler, de déclencher le traitement approprié (via le modèle), 
#et finalement de déléguer la production du document de sortie à la vue. 
