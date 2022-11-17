from objets.geometrie.point import Point
from objets.geometrie.segment import Segment

import unittest

class SegmentTest(unittest.TestCase):
    
    def test_test_egal(self):
        
        pt1 = Point([0,0])
        pt2 = Point([4,10])
        pt3 = Point([2.5,-1])

        sgm1 = Segment(point1= pt1, point2= pt2)
        sgm2 = Segment(point1= pt2, point2= pt3)
        sgm3 = Segment(point1= pt2, point2= pt1)

        test1 = sgm1.test_egal (autre_segment = sgm2) #False
        test2 = sgm1.test_egal (autre_segment = sgm3) #True

        test = test2 and not test1 
        self.assertEqual(test, True)

if __name__ == '__main__':
    unittest.main()
