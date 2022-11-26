'''module de test de la classe LienService
test unitaire de la classe Telechargement
auteurs: Jean-Philippe Trotta et Chloé Contant
date : 21/11/2022'''
from client.lien_service import LienService
import unittest


class LienServiceTest(unittest.TestCase):

     def test_genere_dico(self):
          '''Test de la méthode qui retourne la liste de dictionnaires à la couche service'''
          D1 = {'zonage1': 'communes',
               'id1': '13207',
               'zonage2': 'parcelles',
               'date': 'latest'}
          t1 = LienService(D1)
          test1 = t1.genere_dico() is None
     
          D2 = {'zonage1': 'departements',
               'id1': '51',
          'zonage2': 'communes',
          'date': 'latest'}
          t2 = LienService(D2)
          test2 = t2.genere_dico() is None

if __name__ == '__main__':
    unittest.main()