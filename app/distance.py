

from math import sin, cos, sqrt, atan2, radians
    
def calculate_distance(lat1:float, lon1:float, lat2:float, lon2:float) -> float:
    """
    Calculates the distance between two geospatial
    points identified by their latitude and longitude.
    Returns the distance between these points in kilometers.
    """

    # Check validity of coordinates for point 1    
    if lat1 < -90 or lat1 > 90 or lon1 < -180 or lon1 > 180:
        return None
    
    # Check validity of coordinates for point 2    
    if lat2 < -90 or lat2 > 90 or lon2 < -180 or lon2 > 180:
        return None

    # Approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return round(distance)