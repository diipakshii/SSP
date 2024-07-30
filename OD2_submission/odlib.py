from cmath import sqrt
import math
import numpy

# Python Module example
def add(a, b):
   result = a + b
   return result

# Angle.py (Warmup #1) **

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

def ang_momentum():
   angularmomentum = numpy.cross(pos_vec, vel_vec) # angular momentum = pos_vec x vel_vec
   return angularmomentum

h = numpy.cross(pos_vec, vel_vec)
h_scalar = math.sqrt(h[0]**2 + h[1]**2 + h[2]**2)

# Orbital elements 

x = open("Pal_input.txt")
components = x.readlines()
act_e = float(components[6])
act_i = float(components[7])
act_O = float(components[8])
act_w = float(components[9])
act_M = float(components[10])
act_TA = float(components[11])
act_a = float(components[12])


def orbitalelements(): 
    # semimajor axis - a
    vsquared = numpy.dot(vel_vec, vel_vec)
    r = math.sqrt(pos_vec[0]**2 + pos_vec[1]**2 + pos_vec[2]**2)
    a = 1 / ((2 / r) - vsquared)
    error_a = (abs(act_a - a) / act_a) * 100

    # eccentricity - e
    frac_e = (h_scalar)**2 / a
    e = math.sqrt(1 - frac_e)
    error_e = (abs(act_e - e) / act_e) * 100

    # inclination - i
    numeratori = math.sqrt((h[0]**2) + (h[1]**2))
    denominatori = h[2] 
    i_rad = math.atan(numeratori / denominatori)
    i = math.degrees(i_rad)
    error_i = (abs(act_i - i) / act_i) * 100

    # longitude of ascending node - O
    cos_numerator = -1 * h[1]
    cos_denominator = h_scalar * math.sin(i_rad)
    cosO = cos_numerator / cos_denominator

    sin_numerator = h[0]
    sin_denominator = h_scalar * math.sin(i_rad)
    sinO = sin_numerator / sin_denominator

    O = trig_function(cosO, sinO)
    error_O = (abs(act_O - O) / act_O) * 100
  
    # argument of perihelion - w
    
    o_rad = math.radians(O)
    cosU_numerator = (pos_vec[0] * math.cos(o_rad)) + (pos_vec[1] * math.sin(o_rad))
    r = math.sqrt(pos_vec[0]**2 + pos_vec[1]**2 + pos_vec[2]**2)
    cosU_denominator = r
    cosU = cosU_numerator / cosU_denominator

    sinU_numerator = pos_vec[2]
    sinU_denominator = r * math.sin(i_rad)
    sinU = sinU_numerator / sinU_denominator

    U = trig_function(cosU, sinU)

    sinv = (a * (1 - e**2)) / (e * h_scalar) * (numpy.dot(pos_vec, vel_vec) / r)

    cosv = (1 / e) * ( ( (a * (1 - e**2)) / r ) - 1) 

    v = trig_function(cosv, sinv)

    w = math.radians(U) - math.radians(v)

    if w < 0:
        w_real = math.degrees((w + 2*math.pi))
    if w > 2*math.pi:
        w_real = math.degrees(w % 2*math.pi)

    error_w = (abs(act_w - w_real) / act_w) * 100

    print ("Semi-major axis", act_a, a, error_a)
    print ("Eccentricity", act_e, e, error_e)
    print ("Inclination", act_i, i, act_i, error_i)
    print ("Longitude of Ascending Node", act_O, O, error_O)
    print ("Argument of Perihelion", act_w, w_real, error_w)

orbitalelements()
