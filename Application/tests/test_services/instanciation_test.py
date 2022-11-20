""" module instanciation_test
test unitaire de la classe Instanciation
auteur: Jean-Philippe Trotta
date : 18/11/2022
"""

from service.instanciation import Instanciation


#test
insta = Instanciation(zonage1="departements", id1="13", zonage2="communes", date="latest")

print(insta.dico) #{'zonage1': 'departements', 'id1': '13', 'zonage2': 'communes', 'date': 'latest'}
print(insta.dico["zonage1"]) # "departement"

liste = insta.instancier_zonage()   #ne fonctionne pas probablement à cause de la couche client TODO Telechargement (résolu sur VM)
print(liste[0].id)

# No such file or directory: 'Application/client/data\\departements\\communes\\cadastre-13-communes.json.gz'
