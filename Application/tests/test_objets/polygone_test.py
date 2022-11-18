""" module polygone_test
test unitaire de la classe Polygone
auteur: Jean-Philippe Trotta
date : 10/10/2022
"""
from objets.geometrie.point import Point
from objets.geometrie.segment import Segment
from objets.geometrie.polygone import Polygone

import unittest

class PolygoneTest(unittest.TestCase):
    
    def test_test_segment(self):
        
        pt1 = Point([654436,25545.444])
        pt2 = Point([4,10])
        pt3 = Point([5425,5545.3254])

        sgm1 = Segment(point1= pt1, point2= pt2)
        sgm2 = Segment(point1= pt3, point2= pt1)


        poly = Polygone([[[5425.25,5545],[654436,25545.444],[5425,5545.3254],[654436.65,25545]],[[12,322],[4,10],[35,44]]])

        test1 = poly.test_segment(autre_segment = sgm1) #False
        test2 = poly.test_segment(autre_segment = sgm2) #True

        test = test2 and not test1 
        self.assertEqual(test, True)

    def test_test_polyg_contigu (self):
        poly1 = Polygone([[[5,1],[4,4],[4,5],[6,6],[6,1]]])
        poly2 = Polygone([[[4,4],[4,5],[6,7]]])
        self.assertEqual(poly1.test_polyg_contigu(autre_polyg=poly2), True)

  


if __name__ == '__main__':
    unittest.main()
