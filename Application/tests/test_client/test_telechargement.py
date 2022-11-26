""" module test_telechargement
test unitaire de la classe Telechargement
auteurs: Jean-Philippe Trotta et Chloé Contant
date : 20/11/2022
"""
from client.telechargement import Telechargement
import unittest

class TelechargementTest(unittest.TestCase):
    '''classe de tests unitaires de la classe Telechargement'''

    def test_generator_link(self):
        '''Test de la méthode qui recupère url'''

        t1 = Telechargement(
            id_zone1="08",
            date="latest",
            zonage1="departements")
        lien_1 = t1.generator_link()
        test1 = lien_1 == "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/departements/08/cadastre-08-communes.json.gz"

        t2 = Telechargement(
            id_zone1="08124",
            date="latest",
            zonage1="communes")
        lien_2 = t2.generator_link()
        test2 = lien_2 == "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/08/08124/cadastre-08124-communes.json.gz"

        t3 = Telechargement(
            id_zone1="08",
            date="latest",
            zonage1="france",
            zonage2="communes")
        lien_3 = t3.generator_link()
        test3 = lien_3 == "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/france/cadastre-france-communes.json.gz"

        test = test1 and test2 and test3
        self.assertEqual(test, True)

    def test_generator_path(self):
        '''test pour le générateur de chemin'''
        t4 = Telechargement(id_zone1="04004", zonage1="communes")
        test4 = t4.generator_path() == "Application/client/data/communes/communes"
        self.assertEqual(test4, True)

    def test_download(self):
        '''test pour le téléchargement du fichier json.gz'''
        t5 = Telechargement(
            id_zone1="07003",
            zonage1="communes",
            zonage2="parcelles")
        test5 = t5.download() is None
        self.assertEqual(test5, True)

    def recherche_fichier(self):
        '''test pour la recherche d'un fichier json.gz'''
        t6 = Telechargement(
            id_zone1="07003",
            zonage1="communes",
            zonage2="parcelles")
        test6 = t6.recherche_fichier() is None
        self.assertEqual(test6, True)

    def test_read_json(self):
        '''test pour la lecture du fichier json.gz'''
        t7 = Telechargement(
            id_zone1="07003",
            zonage1="communes",
            zonage2="parcelles")
        t7.download()
        dico = t7.read_json()
        id = dico["features"][0]["id"]
        test7 = id == "07003000AB0001"
        self.assertEqual(test7, True)  

if __name__ == '__main__':
    unittest.main()
