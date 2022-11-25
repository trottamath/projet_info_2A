""" module abstract_polygone_test
test unitaire de la classe AbstractPolygone
auteur: Jean-Philippe Trotta
date : 10/10/2022
"""
from objets.geometrie.multi_polygone import MultiPolygone
from objets.geometrie.polygone import Polygone
from objets.geometrie.abstract_polygone import AbstractPolygone
from objets.geometrie.rectangle import Rectangle

import unittest

class MultiPolygoneTest(unittest.TestCase):
    
    def test_test_intersect_rect (self):

        poly8 = Polygone([[[5,1],[4,4],[4,5],[6,6],[6,1]]])
        poly9 = Polygone([[[4,4],[4,5],[2.5,6]],[[3.6,5],[3.8,5],[3.8,4.6],[3.6,4.6]]])
        rect1 = Rectangle(lat_min= 3, lat_max= 7, long_min= 2, long_max= 3.5) 

        test1 = poly8.test_intersect_rect (rectangle = rect1) #true
        test2 = poly9.test_intersect_rect (rectangle = rect1) #false

        m1 = MultiPolygone([[[[1,5545.3254],[654436.65,25545.444],[5425,11]],[[8000,4000],[10000,4000],[8000,2000]]],[[[5,1],[4,4],[4,5],[6,6],[6,1]]]])
        rect2 = Rectangle(lat_min= 2000, lat_max= 4000, long_min= 2000, long_max= 4000)
        rect3 = Rectangle(lat_min= -10, lat_max= -5, long_min= -10, long_max= -5)

        test3 = m1.test_intersect_rect (rectangle = rect1) #True
        test4 = m1.test_intersect_rect (rectangle = rect2) #True
        test5 = m1.test_intersect_rect (rectangle = rect3) #False

        test = test1 and not test2 and test3 and test4 and not test5

        self.assertEqual(test, True)

    def test_test_polyg_proche (self):
        poly1 = Polygone([[[1,3],[2,1],[3,3]]])
        poly2 = Polygone([[[2,0],[5,0],[3,2]]])
        poly3 = Polygone([[[4,2],[9,2],[5,5]],[[5,3],[6,3],[6,4],[5,4]]])


        test1 = poly1.test_polyg_proche (autre_polyg = poly2 ) #True
        test2 = poly1.test_polyg_proche (autre_polyg = poly3 ) #False

        m1 = MultiPolygone([[[[4,2],[9,2],[5,5]],[[5,3],[6,3],[6,4],[5,4]]]])
        m2 = MultiPolygone([[[[1,3],[2,1],[3,3]]],[[[2,0],[5,0],[3,2]]]])

        test3 = m2.test_polyg_proche(autre_polyg = m1) #True
        test4 = m2.test_polyg_proche(autre_polyg = poly3) #True
        test5 = m1.test_polyg_proche(autre_polyg = poly1) #False

        test = test1 and not test2 and test3 and test4 and not test5

        self.assertEqual(test, True)


if __name__ == '__main__':
    unittest.main()
