""" module departement_test
test unitaire de la classe Departement
auteur: Jean-Philippe Trotta
date : 10/10/2022
"""

from objets.zone.departement import Departement
import unittest

class DepartementTest(unittest.TestCase):
    def test_dep_contig(self):

        list_dep13 = Departement(id_dep= "13").dep_contig()
        liste = ['30', '84', '04', '83']
        

        self.assertEqual(liste, list_dep13)

if __name__ == '__main__':
    unittest.main()
