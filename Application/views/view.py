class View(AbstractView):

    def choix_utilisateur(self, id_utilisateur):
        id_utilisateur = input("tapez votre identifiant : ")
        if not id_utilisateur:
            return None
        return id_utilisateur

    def choix_requete(self, id_requete):
        """Vérification de la requête demandée."""
        id_requete = input("tapez la requête voulue :")
        if not id_requete:
            return None
        return id_requete

    def nouvelle_requete(self):
        """Demande une nouvelle analyse ou non."""
        print("Souhaitez vous refaire une analyse ?")
        choice = input("Y/n: ")
        if choice == "n":
            return False
        return True
    