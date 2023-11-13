import unittest

from app import distance

class TestDistance(unittest.TestCase):
        
    def test_nominal(self):
        """
        Test the nominal case
        """
        # Point 1
        lat1 = 52.2296756
        lon1 = 21.0122287
        # Point 2
        lat2 = 52.406374
        lon2 = 16.9251681
        result = distance.calculate_distance(lat1, lon1, lat2, lon2)
        self.assertEqual(result, 279, "nominal case")
        
    def test_lat1_min_minus(self):
        """
        Test min- for lat1
        """
        # Point 1
        lat1 = -98.1
        lon1 = 21.0122287
        # Point 2
        lat2 = 52.406374
        lon2 = 16.9251681
        result = distance.calculate_distance(lat1, lon1, lat2, lon2)
        self.assertEqual(result, None, "lat1 min-")
        
if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
    
    
    