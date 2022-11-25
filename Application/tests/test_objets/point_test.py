""" module point_test
test unitaire de la classe Point
auteur: Jean-Philippe Trotta
date : 10/10/2022
"""
from objets.geometrie.point import Point

import unittest

class PointTest(unittest.TestCase):
    '''test de la classe Point'''
    
    def test_test_egal(self):
        '''test de la méthode test_egal'''
        
        pt1 = Point([0,0])
        pt2 = Point([4,10])
        
        test1 = pt1.test_egal (autre_point = pt2)
        test2 = pt2.test_egal(autre_point = pt2)
        test = test2 and not test1 
        self.assertEqual(test, True)

if __name__ == '__main__':
    unittest.main()
