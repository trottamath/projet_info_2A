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
