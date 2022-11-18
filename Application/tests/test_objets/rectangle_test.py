from objets.geometrie.rectangle import Rectangle

import unittest

class RectangleTest(unittest.TestCase):
    
    def test_test_intersect_rect (self):
        
        rect1 = Rectangle(lat_min=-1, lat_max=5, long_min=-2, long_max=7)
        rect2 = Rectangle(lat_min=-3, lat_max=2, long_min=-1, long_max=8)
        rect3 = Rectangle(lat_min=-10, lat_max=-5, long_min=-7, long_max=-3)
        
        test1 = rect1.test_intersect_rect (autre_rect = rect3) #False
        test2 = rect1.test_intersect_rect (autre_rect = rect2) #True

        test = test2 and not test1 
        self.assertEqual(test, True)
    
    def test_union_rectangle(self):

if __name__ == '__main__':
    unittest.main()