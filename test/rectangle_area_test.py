import unittest

from app import geometry

class TestGetAreaRectangle(unittest.TestCase):
        
    def test_nominal(self):
        result = geometry.calculate_area_rectangle(1,2)
        self.assertEqual(result, 3, "nominal inputs")
        
        
    def test_negative_width(self):
        result = geometry.calculate_area_rectangle(-1,2)
        self.assertEqual(result, None, "negative value for width")
        
        
if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
    
    
    