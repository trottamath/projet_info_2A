'''module de test de la classe LienService'''
from client.lien_service import LienService


D = {'zonage1': 'communes',
     'id1': '13207',
     'zonage2': 'parcelles',
     'date': 'latest'}
test = LienService(D)
print(test.dico)
dico = test.genere_dico()
# print(dico)


D = {'zonage1': 'departements',
     'id1': '2A',
     'zonage2': 'communes',
     'date': 'latest'}
test = LienService(D)
print(test.dico)

# bug pour une parcelle en zonage2, mais ok pour commune
list_dico = test.genere_dico()


D = {'zonage1': 'departements',
     'id1': '51',
     'zonage2': 'communes',
     'date': 'latest'
     }
test = LienService(D)
print(test.dico)


# pb résolu, à supprimer
# list_dico = test.genere_dico()  #bug pour une parcelle en zonage2, mais ok pour commune
# multi=list_dico[136]["geometry"]["coordinates"]
# print(list_dico[136]["geometry"]["type"])
# poly=multi[0]
# mpoly=poly[0]
# print(mpoly[0])
