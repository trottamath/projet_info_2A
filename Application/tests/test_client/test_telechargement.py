""" module test_telechargement 
test unitaire de la classe Telechargement
auteurs: Jean-Philippe Trotta et Chloé Contant
date : 20/11/2022
"""
from client.telechargement import Telechargement

import unittest

class TelechargementTest(unittest.TestCase):
    
    def test_generator_link(self):
        '''test de la méthode qui recupère url'''
        
        t1 = Telechargement(id_zone1="08",date="latest",zonage1="departements")
        lien_1 = t1.generator_link()
        test1= lien_1 == "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/departements/08/cadastre-08-communes.json.gz"
        
        t2 = Telechargement(id_zone1="08124",date="latest",zonage1="communes")
        lien_2 = t2.generator_link()
        test2 = lien_2 == "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/08/08124/cadastre-08124-communes.json.gz"
        

        t3= Telechargement(id_zone1="08",date="latest",zonage1="france",zonage2="communes")
        lien_3 = t3.generator_link()
        test3 = lien_3 == "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/france/cadastre-france-communes.json.gz"
        
        test = test1 and test2 and test3 
        self.assertEqual(test, True)

    def test_generator_path(self):
        '''test pour le générateur de chemin'''
        t4 = Telechargement(id_zone1="04004",zonage1="communes")
        test4 = t4.generator_path() == "/data\communes\communes"
        self.assertEqual(test4, True)


if __name__ == '__main__':
    unittest.main()
    


#test fonction telechargement
t4 = Telechargement(id_zone1="07003",zonage1="departements",zonage2="communes")
t4.download()  #bug TODO

#lecture de json vers dictionnaire
#dico = t4.read_json()
#print(dico) #ça fonctionne sur la vm TODO à tester ailleur