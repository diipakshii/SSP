from cmath import sqrt
import math
import numpy

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

# Angular Momentum (OD1)

# x = open("Pal_input.txt")
# components = x.readlines()

# x = float(components[0])
# y = float(components[1])
# z = float(components[2])
# vx = float(components[3])
# vy = float(components[4])
# vz = float(components[5])
 
# x_AU = x / (1.495978707 * 10**8) # converting from km to AU
# y_AU = y / (1.495978707 * 10**8)
# z_AU = z / (1.495978707 * 10**8)

# vx_gd = (vx * 3600 * 24) / (1.495978707 * 10**8 * 0.01720209895) # converting from km/s to AU/Gaussian day
# vy_gd = (vy * 3600 * 24) / (1.495978707 * 10**8 * 0.01720209895)
# vz_gd = (vz * 3600 * 24) / (1.495978707 * 10**8 * 0.01720209895)

# pos_vec = numpy.array([x_AU, y_AU,z_AU]) # creating matrices for cross product
# vel_vec = numpy.array([vx_gd, vy_gd, vz_gd])

def ang_momentum(pos_vec, vel_vec):
   angularmomentum = numpy.cross(pos_vec, vel_vec) # angular momentum = pos_vec x vel_vec
   return angularmomentum

# h = numpy.cross(pos_vec, vel_vec)
# h_scalar = math.sqrt(h[0]**2 + h[1]**2 + h[2]**2)

# Orbital elements (OD2)

# x = open("Pal_input.txt")
# components = x.readlines()
# act_e = float(components[6])
# act_i = float(components[7])
# act_O = float(components[8])
# act_w = float(components[9])
# act_M = float(components[10])
# act_TA = float(components[11])
# act_a = float(components[12])
# act_T = float(components[13])

k = 0.01720209894

def axis(pos_vec, vel_vec): # semi-major axis - a
    vsquared = numpy.dot(vel_vec, vel_vec)
    r = math.sqrt(pos_vec[0]**2 + pos_vec[1]**2 + pos_vec[2]**2)
    a = 1 / ((2 / r) - vsquared)
    return a 

def eccen(pos_vec, vel_vec, h_scalar):  # eccentricity - e
    frac_e = (h_scalar)**2 / axis(pos_vec, vel_vec)
    e = math.sqrt(1 - frac_e)
    return e

def inclin(h): # inclination - i
    numeratori = math.sqrt((h[0]**2) + (h[1]**2))
    denominatori = h[2] 
    i_rad = math.atan(numeratori / denominatori)
    i = math.degrees(i_rad)
    return i

def long_a(h, h_scalar): # longitude of ascending node - O
    cos_numerator = -1 * h[1]
    cos_denominator = h_scalar * math.sin(math.radians(inclin(h)))
    cosO = cos_numerator / cos_denominator

    sin_numerator = h[0]
    sin_denominator = h_scalar * math.sin(math.radians(inclin(h)))
    sinO = sin_numerator / sin_denominator

    O = trig_function(cosO, sinO)
    return O

def arg_per(pos_vec, vel_vec, h, h_scalar): # argument of perihelion - w
    o_rad = math.radians(long_a(h, h_scalar))
    cosU_numerator = (pos_vec[0] * math.cos(o_rad)) + (pos_vec[1] * math.sin(o_rad))
    r = math.sqrt(pos_vec[0]**2 + pos_vec[1]**2 + pos_vec[2]**2)
    cosU_denominator = r
    cosU = cosU_numerator / cosU_denominator

    sinU_numerator = pos_vec[2]
    sinU_denominator = r * math.sin(math.radians(inclin(h)))
    sinU = sinU_numerator / sinU_denominator

    U = trig_function(cosU, sinU)

    sinv = (axis(pos_vec, vel_vec) * (1 - eccen(pos_vec, vel_vec, h_scalar)**2)) / (eccen(pos_vec, vel_vec, h_scalar) * h_scalar) * (numpy.dot(pos_vec, vel_vec) / r)
    cosv = (1 / eccen(pos_vec, vel_vec, h_scalar)) * ( ( (axis(pos_vec, vel_vec) * (1 - eccen(pos_vec, vel_vec, h_scalar)**2)) / r ) - 1) 

    v = trig_function(cosv, sinv)
    w = math.radians(U) - math.radians(v)

    if w < 0:
        w_real = math.degrees((w + 2*math.pi))
    if w > 2*math.pi:
        w_real = math.degrees(w % 2*math.pi)
    return w_real

def meana(pos_vec, vel_vec, h_scalar): # Mean Anomaly - M
    r = math.sqrt(pos_vec[0]**2 + pos_vec[1]**2 + pos_vec[2]**2)

    E = math.acos((1/eccen(pos_vec, vel_vec, h_scalar)) * (1 - r/axis(pos_vec, vel_vec)))

    sinv = (axis(pos_vec, vel_vec) * (1 - eccen(pos_vec, vel_vec, h_scalar)**2)) / (eccen(pos_vec, vel_vec, h_scalar) * h_scalar) * (numpy.dot(pos_vec, vel_vec) / r)
    cosv = (1 / eccen(pos_vec, vel_vec, h_scalar)) * ( ( (axis(pos_vec, vel_vec) * (1 - eccen(pos_vec, vel_vec, h_scalar)**2)) / r ) - 1) 

    v = math.radians(trig_function(cosv, sinv))

    if v > math.pi and E < math.pi:
        E_act = E + (1.5 * math.pi) 
    if v < math.pi and E > math.pi:
        # E_act = 2 * math.pi - E
        E_act = (1.5 * math.pi) - E

    M_rad = E_act - (eccen(pos_vec, vel_vec, h_scalar) * math.sin(E_act))
    M_deg = math.degrees(M_rad)
    return M_deg
    
def time_per(pos_vec, vel_vec, h_scalar): # Time of Last Perihelion passage
    n = math.sqrt(k**2 / axis(pos_vec, vel_vec)**3)
    time = 2458312.500000000

    T_per = time - (meana(pos_vec, vel_vec, h_scalar) / n) 
    return T_per

def main(r2xyz_ec, r2dotxyz_ec):

    x = r2xyz_ec[0]
    y = r2xyz_ec[1]
    z = r2xyz_ec[2]
    vx = r2dotxyz_ec[0]
    vy = r2dotxyz_ec[1]
    vz = r2dotxyz_ec[2]

    pos_vec = numpy.array([x, y, z]) # creating matrices for cross product
    vel_vec = numpy.array([vx, vy, vz])

    h = numpy.cross(pos_vec, vel_vec)
    h_scalar = math.sqrt(h[0]**2 + h[1]**2 + h[2]**2)

    a = axis(pos_vec, vel_vec)
    e = eccen(pos_vec, vel_vec, h_scalar)
    i = inclin(h)
    O = long_a(h, h_scalar)
    w_real = arg_per(pos_vec, vel_vec, h, h_scalar)
    M_deg = meana(pos_vec, vel_vec, h_scalar)
    T_per = time_per(pos_vec, vel_vec, h_scalar)

    act_e = 0.5317493696688808 
    act_i = 3.875284337689891 
    act_O = 238.8360495504369 
    act_w = 107.9214075204697
    act_M = 339.757416
    # act_TA = 
    act_a = 2.726573219901208 
    # act_T = 

    error_a = (abs(act_a - a) / act_a) * 100                      # 0.2% / 0.427%       little off
    error_e = (abs(act_e - e) / act_e) * 100                      # 0.9% / 1.257%       little off
    error_i = (abs(act_i - i) / act_i) * 100                      # 0.006% / 1.811%     VERY off 
    error_O = (abs(act_O - O) / act_O) * 100                      # 0.35% / 0.014%      very good
    error_w = (abs(act_w - w_real) / act_w) * 100                 # 0.08% / 0.024%      very good
    error_M = (abs(act_M - M_deg) / act_M) * 100                  # 0.7% / 1.810%       little off
    # error_T = (abs(act_T - T_per) / act_T) * 100

    print("Semi-major axis //", "Expected:", act_a, "/", "Actual:", a, "/", "Error:", error_a, "%")
    print("Eccentricity //", "Expected:", act_e, "/", "Actual:", e, "/", "Error:", error_e, "%")
    print("Inclination //", "Expected:", act_i, "/", "Actual:", i, "/", "Error:", error_i, "%") 
    print("Longitude of Ascending Node //", "Expected:", act_O, "/", "Actual:", O, "/", "Error:", error_O, "%")
    print("Argument of Perihelion //", "Expected:", act_w, "/", "Actual:", w_real, "/", "Error:", error_w, "%")
    print("Mean Anomaly //", "Expected:", act_M, "/", "Actual:", M_deg, "/", "Error:", error_M, "%")
    # print("Time of Last Perihelion Passage", act_T, T_per, error_T)

k = 0.01720209894
mu = 1.000000

# n = k * math.sqrt( mu / axis(pos_vec, vel_vec)**3)

# Newton - Raphson Method

def newton_rap():
    M = meana()
    e = eccen()

    Eguess = M
    count = 0
    oldguess = 0
    
    while abs(Eguess - oldguess) > .00001: 
        Mguess = Eguess - e * math.sin(Eguess)
        oldguess = Eguess
        Eguess = oldguess - (M - Mguess) / (e * math.cos(oldguess) - 1)
        count = count + 1
    return Eguess 

# Ephermeris (OD4)

x = open("Pal_input.txt")
components = x.readlines()
x_sun = float(components[14])
y_sun = float(components[15])
z_sun = float(components[16])

def ephermeris():
    E = newton_rap()

    xyz = numpy.array([[axis() * math.cos(E) - axis() * eccen()],[axis() * math.sqrt(1 - eccen()**2) * math.sin(E)], [0]])

    i = math.radians(inclin())
    omega = math.radians(long_a())
    w = math.radians(arg_per())

    matrix1 = numpy.array([[math.cos(long_a()), -1 * math.sin(long_a()), 0], [math.sin(long_a()), math.cos(long_a()), 0], [0,0,1]])
    matrix2 = numpy.array([[1,0,0], [0, math.cos(inclin()), -1 * math.sin(inclin())], [0, math.sin(inclin()), math.cos(inclin())]])
    matrix3 = numpy.array([[math.cos(arg_per()), -1 * math.sin(arg_per()), 0], [math.sin(arg_per()), math.cos(arg_per()), 0], [0,0,1]])

    x1y1z1 = matrix1 @ matrix2 @ matrix3 @ xyz

    ecliptic_degrees = 23.43535
    ecliptic = math.radians(ecliptic_degrees)

    matrix4 = numpy.array([[1,0,0], [0, math.cos(ecliptic), -1 * math.sin(ecliptic)], [0, math.sin(ecliptic), math.cos(ecliptic)]])

    x2y2z2 = matrix4 @ x1y1z1
    x2y2z2 = numpy.array([x2y2z2[0,0], x2y2z2[1,0], x2y2z2[2,0]])
    print (x2y2z2) # HELP THIS DOESNT MATCH UP W/ JPL

    earth_sun = numpy.array([x_sun, y_sun, z_sun])

    p = x2y2z2 + earth_sun

    p_mag = math.sqrt(x2y2z2[0]**2 + x2y2z2[1]**2 + x2y2z2[2]**2)

    p_hat = p / p_mag

    Dec = math.degrees(math.asin(p_hat[2]))
    RA = math.degrees(math.acos( p_hat[0] / math.cos(Dec)))

    return RA, Dec 

# f and g functions

mu = 1.0000

def fg(tau,r2,r2dot,flag):
    magr2 = math.sqrt(r2[0]**2 + r2[1]**2 + r2[2]**2)

    if flag == 3:
        u = mu / magr2**3
        z = numpy.dot(r2, r2dot) / magr2**2
        q = (numpy.dot(r2dot,r2dot) / magr2**2) - u

        f = 1 - ((1/2) * u * tau**2) + ((1/2) * u * z * tau**3) 
        g = tau - ((1/6) * u * tau**3)

        return (f,g)

    if flag == 4:
        u = mu / magr2**3
        z = numpy.dot(r2, r2dot) / magr2**2
        q = (numpy.dot(r2dot,r2dot) / magr2**2) - u

        f = 1 - ((1/2) * u * tau**2) + ((1/2) * u * z * tau**3) + ((1/24) * ((3 * u * q) - (15 * u * z**2) + (u**2)) * (tau**4))
        g = tau - ((1/6) * u * tau**3) + ((1/4) * u * z * tau**4)

        return (f,g)