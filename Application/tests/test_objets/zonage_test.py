""" module zonage_test
test unitaire de la classe Zonage
auteur: Jean-Philippe Trotta
date : 10/10/2022
"""

from objets.zone.zonage import Zonage
from objets.zone.parcelle import Parcelle
from objets.zone.commune import Commune
from objets.geometrie.polygone import Polygone
from objets.geometrie.multi_polygone import MultiPolygone

import unittest

class ZonageTest(unittest.TestCase):
    def test_test_zone_proche(self):

        poly1 = Polygone([[[1,3],[2,1],[3,3]]])
        parc1 = Parcelle(id= "01001001", geom_coord = poly1)
        poly2 = Polygone([[[2,0],[5,0],[3,2]]])
        parc2 = Parcelle(id= "01001002", geom_coord = poly2)
        poly3 = Polygone([[[4,2],[9,2],[5,5]],[[5,3],[6,3],[6,4],[5,4]]])
        parc3 = Parcelle(id= "01001003", geom_coord = poly3)


        test1 = parc1.test_zone_proche ( autre_zone = parc2 ) #True
        test2 = parc1.test_zone_proche (autre_zone = parc3 ) #False

        m1 = MultiPolygone([[[[4,2],[9,2],[5,5]],[[5,3],[6,3],[6,4],[5,4]]]])
        com1 = Commune(id= "01002", geom_coord=m1, nom="fake1")
        m2 = MultiPolygone([[[[1,3],[2,1],[3,3]]],[[[2,0],[5,0],[3,2]]]])
        com2 = Commune(id= "01003", geom_coord=m2, nom="fake2")

        test3 = com2.test_zone_proche(autre_zone = com1) #True
        test4 = com2.test_zone_proche(autre_zone = parc3) #True
        test5 = parc1.test_zone_proche(autre_zone = com1) #False

        test = test1 and not test2 and test3 and test4 and not test5

        self.assertEqual(test, True)

    def test_test_zone_contigu(self):
        poly1 = Polygone([[[5,1],[4,4],[4,5],[6,6],[6,1]]])
        parc1 = Parcelle(id= "01001001", geom_coord= poly1)
        poly2 = Polygone([[[4,4],[4,5],[6,7]]])
        parc2 = Parcelle(id= "01001002", geom_coord= poly2)

        test1 = parc1.test_zone_contigu( macro_zone= parc2) #True

        poly3 = Polygone([[[4,4],[4,5],[6,7]],[[4.01,4.2],[4.02,4.8],[4.015,4.5]]])
        parc3 = Parcelle(id= "01001003", geom_coord= poly3)
        m1 = MultiPolygone([[[[1,5545.3254],[654436.65,25545.444],[5425,11]],[[12,322],[4,10],[35,44]]],[[[2,25545],[654436.65,25545.444],[5425,5545.3254],[654436.65,25545.444],[5425,22]]]])
        com1= Commune(id="01002", geom_coord= m1, nom="fake")

        test2 = parc3.test_zone_contigu(macro_zone = com1) #False
        test3 = com1.test_zone_contigu(macro_zone = com1) #True

        test = test1 and not test2 and test3

        self.assertEqual(test, True)

    def test_ss_list_contig(self):
        poly1 = Polygone([[[5,1],[4,4],[4,5],[6,6],[6,1]]])
        parc1 = Parcelle(id= "01001001", geom_coord= poly1)
        poly2 = Polygone([[[4,4],[4,5],[6,7],[5425,22],[2,25545]]])
        parc2 = Parcelle(id= "01001002", geom_coord= poly2)
        poly3 = Polygone([[[4,4],[4,5],[6,7],[1,5545.3254],[654436.65,25545.444]],[[4.01,4.2],[4.02,4.8],[4.015,4.5]]])
        parc3 = Parcelle(id= "01001003", geom_coord= poly3)
        
        m1 = MultiPolygone([[[[1,5545.3254],[654436.65,25545.444],[5425,11]],[[12,322],[4,10],[35,44]]],[[[2,25545],[654436.65,25545.444],[5425,5545.3254],[654436.65,25545.444],[5425,22]]]])
        com1 = Commune(id="01002", geom_coord= m1, nom="fake")

        liste = com1.ss_list_contig(list_zones=[parc1,parc2,parc3])
        for i in range(len(liste)):
            liste[i]= liste[i].id
        
        self.assertEqual(liste,['01001002', '01001003'])

if __name__ == '__main__':
    unittest.main()
