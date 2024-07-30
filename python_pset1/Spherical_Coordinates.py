# https://www.nhc.noaa.gov/gccalc.shtml
# Location 1 UNC: 35.9049° N, 79.0469° W
# Location 2 Home: (Sylvania, OH) 41.7189° N, 83.7130° W
# Distance: 470 miles / 762 km

import math

def sphericalcoordinates(lat1, long1, lat2, long2):
    print("Location1 = " , lat1, long1)
    print("Location2 =", lat2, long2)
    
    A = long2 - long1
    b = 90 - lat1
    c = 90 - lat2

    A_rad = A * (math.pi / 180)
    b_rad = b * (math.pi / 180)
    c_rad = c * (math.pi / 180)

    a = math.acos((math.cos(b_rad) * math.cos(c_rad)) + (math.sin(b_rad) * math.sin(c_rad) * math.cos(A_rad)))

    Distance_calculated = a * 3958.8

    Applet_distance = 470
    print("Distance from Applet =", Applet_distance)

    return Distance_calculated

print(sphericalcoordinates(41.7189, 83.7130, 35.9049, 79.0469))
