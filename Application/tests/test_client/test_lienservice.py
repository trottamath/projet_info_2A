from client.lien_service import LienService
 

D = {'zonage1' : 'departements',
    'id1' : '01',
    'zonage2' : 'communes',
    'date' : 'latest'}
test = LienService(D)
print(test.dico) #{'zonage1': 'departements', 'id1': '01', 'zonage2': 'communes', 'date': 'latest'}

dico = test.genere_dico()  #bug TODO
print(dico)

#No such file or directory: 'Application/client/data/communes/communes\\cadastre-04004-communes.json.gz' TODO bug