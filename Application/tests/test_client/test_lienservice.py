from client.lien_service import LienService
from telechargement import Telechargement 

D = {'zonage1' : 'departement',
    'id1' : '01',
    'zonage2' : 'commune',
    'date' : 'latest'}
test = LienService(D)
dico = test.genere_dico()
print(dico)

