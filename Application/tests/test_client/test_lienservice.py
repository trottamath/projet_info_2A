from client.lien_service import LienService
 

D = {'zonage1' : 'departements',
    'id1' : '01',
    'zonage2' : 'communes',
    'date' : 'latest'}
test = LienService(D)
dico = test.genere_dico()
print(dico)

