import math
import numpy

# Python Module example
def add(a, b):
   result = a + b
   return result

# Angle.py (Warmup #1)

# Quadrant Finding Function (Spherical Trig Q4)
def trig_function(cosine, sine):
    if abs((cosine**2 + sine**2)-1) < 0.000001:
        angle = math.acos(cosine)
        if sine < 0:
            angle = 2*(math.pi) - angle 
            return math.degrees(angle)
        if sine > 0:
            return math.degrees(angle)
    else:
        return "User error: invalid input"

# Angular Momentum
def ang_momentum():
   x = open("Pal_input.txt")
   components = x.readlines()
   x = float(components[0])
   y = float(components[1])
   z = float(components[2])
   vx = float(components[3])
   vy = float(components[4])
   vz = float(components[5])
   x_AU = x / (1.495978707 * 10**8) # converting from km to AU
   y_AU = y / (1.495978707 * 10**8)
   z_AU = z / (1.495978707 * 10**8)
   vx_gd = (vx * 3600 * 24) / (1.495978707 * 10**8 * 0.01720209895) # converting from km/s to AU/Gaussian day
   vy_gd = (vy * 3600 * 24) / (1.495978707 * 10**8 * 0.01720209895)
   vz_gd = (vz * 3600 * 24) / (1.495978707 * 10**8 * 0.01720209895)
   pos_vec = numpy.array([x_AU, y_AU,z_AU]) # creating matrices for cross product
   vel_vec = numpy.array([vx_gd, vy_gd, vz_gd])
   angularmomentum = numpy.cross(pos_vec, vel_vec) # angular momentum = pos_vec x vel_vec
   return angularmomentum