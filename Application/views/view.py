#régler la couche view avec le logiciel insomnia  
#

#class View(AbstractView):

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

#requete 1 : trouver la liste des communes limitrophes 
class view1:
    def __init__(self,):
        pass
    def input(self,):
        """ recuperer la requête à valider"""
        print "Recherche de la requête"
        print "Introduire une commune"
        nom_commune = raw_input()
        return nom_commune
    def output(self, personnes):
        """ afficher les informations d'une liste des
personnes """
        print "La liste des communes trouvées"
        print " %d communes trouvées"%len(communes)
        for id_commune in communes:
print id_commune['Identifiant de la commune trouvée']
