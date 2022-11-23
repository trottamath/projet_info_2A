from client.lien_service import LienService
 

D = {'zonage1' : 'communes',
    'id1' : '13400',
    'zonage2' : 'parcelles',
    'date' : 'latest'}
test = LienService(D)
print(test.dico) #{'zonage1': 'departements', 'id1': '01', 'zonage2': 'communes', 'date': 'latest'}

dico = test.genere_dico()  #bug pour une parcelle en zonage2, mais ok pour commune
print(dico)
