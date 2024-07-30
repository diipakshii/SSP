from odlib_TestCode2 import * 
from math import *
import numpy as np

def odcode():
    # constants 
    k = 0.01720209895 # Gaussian gravitational constant
    mu = 1.0
    cAU = 173.144643267 # speed of light in AU/(mean solar)day

    # time observations in Julian dates
    x = open("MoGtestinput_TestCode2.txt")
    components = x.readlines()
    time1 = float(components[1])
    time2 = float(components[9])
    time3 = float(components[17])

    # time intervals
    tau0 = k * (time3 - time1)
    tau1 = k * (time1 - time2)
    tau3 = k * (time3 - time2)

    # rough estimates for c1 and c3
    c1 = tau3/tau0
    c2 = -1
    c3 = -1 * tau1/tau0

    # Earth-Sun vectors in equatorial coordinates (x,y,z)
    ES_x1 = float(components[4])
    ES_y1 = float(components[5])
    ES_z1 = float(components[6])

    ES_x2 = float(components[12])
    ES_y2 = float(components[13])
    ES_z2 = float(components[14])

    ES_x3 = float(components[20])
    ES_y3 = float(components[21])
    ES_z3 = float(components[22])

    R1 = np.array([ES_x1, ES_y1, ES_z1])
    R2 = np.array([ES_x2, ES_y2, ES_z2])
    R3 = np.array([ES_x3, ES_y3, ES_z3])

    # RA and Dec from Observations
    RA1_deg = float(components[2])
    Dec1_deg = float(components[3])
    RA1_rad = radians(RA1_deg)
    Dec1_rad = radians(Dec1_deg)

    RA2_deg = float(components[10])
    Dec2_deg = float(components[11])
    RA2_rad = radians(RA2_deg)
    Dec2_rad = radians(Dec2_deg)

    RA3_deg = float(components[18])
    Dec3_deg = float(components[19])
    RA3_rad = radians(RA3_deg)
    Dec3_rad = radians(Dec3_deg)

    # calculating components of rho hat (phat) in cartesian plane
    phat_x1 = cos(RA1_rad) * cos(Dec1_rad)
    phat_y1 = sin(RA1_rad) * cos(Dec1_rad)
    phat_z1 = sin(Dec1_rad)

    phat_x2 = cos(RA2_rad) * cos(Dec2_rad)
    phat_y2 = sin(RA2_rad) * cos(Dec2_rad)
    phat_z2 = sin(Dec2_rad)

    phat_x3 = cos(RA3_rad) * cos(Dec3_rad)
    phat_y3 = sin(RA3_rad) * cos(Dec3_rad)
    phat_z3 = sin(Dec3_rad)

    # calculating rho hat (phat) in cartesian plane
    phat1 = np.array([phat_x1, phat_y1, phat_z1])
    phat2 = np.array([phat_x2, phat_y2, phat_z2])
    phat3 = np.array([phat_x3, phat_y3, phat_z3])

    # print(phat1)
    # print(phat2)
    # print(phat3)

    # calculating D for p1, p2, p3

    D0 = np.dot(phat1, np.cross(phat2, phat3))
    D11 = np.dot(np.cross(R1, phat2), phat3)
    D12 = np.dot(np.cross(R2, phat2), phat3)
    D13 = np.dot(np.cross(R3, phat2), phat3)

    D21 = np.dot(np.cross(phat1, R1), phat3)
    D22 = np.dot(np.cross(phat1, R2), phat3)
    D23 = np.dot(np.cross(phat1, R3), phat3)

    D31 = np.dot(phat1, np.cross(phat2, R1))
    D32 = np.dot(phat1, np.cross(phat2, R2))
    D33 = np.dot(phat1, np.cross(phat2, R3))

    # calculating p1, p2, p3
    p1num = c1*D11 + c2*D12 + c3*D13
    p1den = c1*D0

    p2num = c1*D21 + c2*D22 + c3*D23
    p2den = c2*D0

    p3num = c1*D31 + c2*D32 + c3*D33
    p3den = c3*D0

    p1 = p1num/p1den
    p2 = p2num/p2den
    p3 = p3num/p3den

    # print(c1, c2, c3)

    # print(D0)
    # print(D11, D12, D13)
    # print(D21, D22, D23)
    # print(D31, D32, D33)

    # print(p1, p2, p3)

    # calculating r1, r2, r3
    r1 = p1*phat1 - R1
    r2 = p2*phat2 - R2 
    r3 = p3*phat3 - R3

    # print(r1)
    # print(r2)
    # print(r3)

    # calculating initial r2dot
    r2dot = (r3 - r1) / tau0

    # print(r2dot)

    # light travel time correction
    t1_corrected = time1 - p1/cAU
    t2_corrected = time2 - p2/cAU
    t3_corrected = time3 - p3/cAU

    tau0 = k * (t3_corrected - t1_corrected)
    tau1 = k * (t1_corrected - t2_corrected)
    tau3 = k * (t3_corrected - t2_corrected)

    # print(tau0, tau1, tau3)

    # f and g series 

    f1g1 = fg(tau1, r2, r2dot, 4)
    f3g3 = fg(tau3, r2, r2dot, 4)

    f1 = f1g1[0]
    g1 = f1g1[1]
    f3 = f3g3[0]
    g3 = f3g3[1]

    # print(f1, f3, g1, g3)

    # calculating new c1, c3, d1, d3

    c1_num = g3
    c1_den = f1*g3 - g1*f3

    c1 = c1_num / c1_den

    c3_num = -1 * g1
    c3_den = f1*g3 - g1* f3

    c3 = c3_num / c3_den 

    d1_num = -1 * f3
    d1_den = f1*g3 - f3*g1

    d1 = d1_num / d1_den

    d3_num = f1
    d3_den = f1*g3 - f3*g1

    d3 = d3_num / d3_den 

    # print(c1, c3, d1, d3)

    # calculating rho (p)
    p1num = c1*D11 + c2*D12 + c3*D13
    p1den = c1*D0

    p2num = c1*D21 + c2*D22 + c3*D23
    p2den = c2*D0

    p3num = c1*D31 + c2*D32 + c3*D33
    p3den = c3*D0

    p1 = p1num/p1den
    p2 = p2num/p2den
    p3 = p3num/p3den

    # print(p1, p2, p3)

    # calculating r1, r2, r3
    r2_old = r2

    r1_temp = p1*phat1 - R1
    r3_temp = p3*phat3 - R3

    r2_new = c1*r1_temp + c3*r3_temp
    r2dot_new = d1*r1_temp + d3*r3_temp

    r1 = f1*r2 + g1*r2dot 
    r3_new = f3*r2 + g3*r2dot 

    # print(r1, r2, r3) 

    # # iteration
    while abs(r2_old[0] - r2_new[0]) > .000001 or abs(r2_old[1] - r2_new[1]) > .000001 or abs(r2_old[2] - r2_new[2]) > .000001:
        # iteration for f and g 
        f1g1 = fg(tau1, r2_new, r2dot_new, 4)
        f3g3 = fg(tau3, r2_new, r2dot_new, 4)

        # print(f1g1)
        # print(f3g3)

        f1 = f1g1[0]
        g1 = f1g1[1]
        f3 = f3g3[0]
        g3 = f3g3[1]

        # iteraation for calculating new c1, c3, d1, d3
        c1_num = g3
        c1_den = f1*g3 - g1*f3

        c1 = c1_num / c1_den

        c3_num = -1 * g1
        c3_den = f1*g3 - g1* f3

        c3 = c3_num / c3_den 

        d1_num = -1 * f3
        d1_den = f1*g3 - f3*g1

        d1 = d1_num / d1_den

        d3_num = f1
        d3_den = f1*g3 - f3*g1

        d3 = d3_num / d3_den 

        # iteration for calculating rho (p)
        p1num = c1*D11 + c2*D12 + c3*D13
        p1den = c1*D0

        p2num = c1*D21 + c2*D22 + c3*D23
        p2den = c2*D0

        p3num = c1*D31 + c2*D32 + c3*D33
        p3den = c3*D0

        p1 = p1num/p1den
        p2 = p2num/p2den
        p3 = p3num/p3den

        # iteration for calculating r1, r2, r3
        r2_old = r2_new

        r1_temp = p1*phat1 - R1
        r3_temp = p3*phat3 - R3

        r2_new = c1*r1_temp + c3*r3_temp
        r2dot_new = d1*r1_temp + d3*r3_temp

        r1 = f1*r2 + g1*r2dot 
        r3_new = f3*r2 + g3*r2dot   

        # print(r2_old, r2_new)

    p1 = p1 * phat1
    p2 = p2 * phat2
    p3 = p3 * phat3

    r2 = r2_new
    r2dot = r2dot_new

    # print(c1, c3, d1, d3)
    # print (r1, r2, r3) # r1 and r3 are off oops
    # print(p1, p2, p3) 
    # print(r2dot)

    r2exp = numpy.array([0.662642, 0.0561962, 0.262021])

    r2error_x = (abs(r2[0] - r2exp[0]) / r2exp[0]) * 100
    r2error_y = (abs(r2[0] - r2exp[0]) / r2exp[0]) * 100
    r2error_z = (abs(r2[0] - r2exp[0]) / r2exp[0]) * 100
    r2error = numpy.array([r2error_x, r2error_y, r2error_z])

    # print(r2error)

    # rotating r2 to ecliptic coordinates 
    Ec_deg = 23.43535
    Ec = radians(Ec_deg)

    r2_x = r2[0]
    r2_y = r2[1]
    r2_z = r2[2]

    r2matrix1 = numpy.array([[1,0,0], [0, cos(Ec), sin(Ec)], [0, -1 * sin(Ec), cos(Ec)]])
    r2matrix2 = numpy.array([r2_x, r2_y, r2_z])

    r2xyz_ec = r2matrix1 @ r2matrix2 

    # print(r2xyz_ec)

    # rotating r2dot to ecliptic coordinates
    Ec_deg = 23.43535
    Ec = radians(Ec_deg)

    r2dot_x = r2dot[0]
    r2dot_y = r2dot[1]
    r2dot_z = r2dot[2]

    r2dotmatrix1 = numpy.array([[1,0,0], [0, cos(Ec), sin(Ec)], [0, -1 * sin(Ec), cos(Ec)]])
    r2dotmatrix2 = numpy.array([r2dot_x, r2dot_y, r2dot_z])

    r2dotxyz_ec = r2dotmatrix1 @ r2dotmatrix2

    # print(r2dotxyz_ec)

    # computation of orbital elements using OD2 and OD3
    return((main(r2xyz_ec, r2dotxyz_ec)))

odcode()