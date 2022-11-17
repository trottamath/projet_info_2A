from objets.geometrie.point import Point

import unittest

class PointTest(unittest.TestCase):
    
    def test_test_egal(self):
        
        pt1 = Point([0,0])
        pt2 = Point([4,10])
        
        test1 = pt1.test_egal (autre_point = pt2)
        test2 = pt2.test_egal(autre_point = pt2)
        test = test2 and not test1 
        self.assertEqual(test, True)

if __name__ == '__main__':
    unittest.main()
