""" module instanciation_test
test unitaire de la classe Instanciation
auteur: Jean-Philippe Trotta
date : 18/11/2022
"""

from service.instanciation import Instanciation


#test ok
insta = Instanciation(zonage1="departements", id1="13", zonage2="communes", date="latest")

#print(insta.dico) #{'zonage1': 'departements', 'id1': '13', 'zonage2': 'communes', 'date': 'latest'}
#print(insta.dico["zonage1"]) # "departement"

liste = insta.instancier_zonage()  
print(liste[1].id)

#test ok avec un bon numéro de commune
insta = Instanciation(zonage1="communes", id1="13207", zonage2="parcelles", date="latest")
print(insta.dico) #{'zonage1': 'departements', 'id1': '13', 'zonage2': 'communes', 'date': 'latest'}
print(insta.dico["zonage1"]) # "departement"

liste = insta.instancier_zonage()   #fonctionne avec un code commune qui existe, attention à ce qui se passe qd il n'esiste pas
print(liste[1].id)

