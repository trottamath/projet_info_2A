""" module multi_polygone_test
test unitaire de la classe MultiPolygone
auteur: Jean-Philippe Trotta
date : 10/10/2022
"""
from objets.geometrie.multi_polygone import MultiPolygone
from objets.geometrie.polygone import Polygone

import unittest

class MultiPolygoneTest(unittest.TestCase):
    '''test de la classe MultiPolygone'''

    def test_test_polyg_contigu (self):
        '''test de la méthode test_polyg_contigu'''

        poly7 = Polygone([[[4,4],[4,6],[6,6]]])
        poly8 = Polygone([[[5,1],[4,4],[4,5],[6,6],[6,1]]])
        poly9 = Polygone([[[4,4],[4,5],[6,7]],[[4.01,4.2],[4.02,4.8],[4.015,4.5]]])
        test1 = poly8.test_polyg_contigu(autre_polyg = poly9) #true
        test2 = poly8.test_polyg_contigu(autre_polyg = poly7) #false

        m1 = MultiPolygone([[[[1,5545.3254],[654436.65,25545.444],[5425,11]],[[12,322],[4,10],[35,44]]],[[[2,25545],[654436.65,25545.444],[5425,5545.3254],[654436.65,25545.444],[5425,22]]]])
        test3 = m1.test_polyg_contigu(autre_polyg = poly9) #False
        test4 = m1.test_polyg_contigu(autre_polyg = m1) #True
        test = test1 and not test2 and not test3 and test4
        self.assertEqual(test, True)
    


if __name__ == '__main__':
    unittest.main()
