""" module instanciation_test
test unitaire de la classe Instanciation
auteur: Jean-Philippe Trotta
date : 18/11/2022
"""

from service.instanciation import Instanciation
import unittest

class InstanciationTest(unittest.TestCase):
    def test_(self):

        test = True
        

        self.assertEqual(test, True)

if __name__ == '__main__':
    unittest.main()

#test
insta = Instanciation(zonage1="departements", id1="13", zonage2="communes", date="latest")

print(insta.dico)
print(insta.dico["zonage1"])

liste = insta.instancier_zonage()
print(liste[0].id)
