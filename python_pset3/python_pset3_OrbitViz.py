import txaio
txaio.use_asyncio()
from vpython import *
import math
import numpy 

x = open("elements.txt")
file_read = x.readlines()

# a represents length of semi-major axis 
a = float(file_read[0])

# e represents the eccentricity of the orbit
e = float(file_read[1])

# M represents the mean anomaly 
M = float(file_read[2])

# O represents the longitude of the ascending node
Oprime = radians(float(file_read[3]))

# i represents inclination
iprime = radians(float(file_read[4]))

# w represents argument of perihelion
wprime = radians(float(file_read[5]))

k = 0.01720209894 # added according to guidelines in the step by step guide

sqrtmu = 0.01720209895
mu = 1.000000 # changed according to guidelines in the step by step guide

n = k * sqrt( mu / a**3) # added to redefine M in the function

time = 0
dt = .05 #deltaT

period = sqrt(4*pi**2*a**3/mu)

def solvekep(M):
    M = n * (time - period) # added equation needed to define M = n(t-T)
    Eguess = M
    Mguess = Eguess - e*sin(Eguess)
    Mtrue = M
    while abs(Mguess - Mtrue) > .00001: # changed from less than to greater than to allow for the while loop to repeat when true 
        Mguess = Eguess - e*sin(Eguess)
        Eguess = Eguess - (M - Mguess) / (e*cos(Eguess) - 1) # changed to follow the formula 
    return Eguess

r1ecliptic = vector(0, 0, 0)

Mtrue = 2*pi / period*(time) + M
Etrue = solvekep(Mtrue)

# r1ecliptic.x = (cos(wprime)*cos(Oprime) - sin(wprime)*cos(iprime)*sin(Oprime))*(a*cos(Etrue)-a*e) - (cos(wprime)*cos(iprime)*sin(Oprime) + sin(wprime)*cos(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
# r1ecliptic.y = (cos(wprime)*sin(Oprime) + sin(wprime)*cos(iprime)*cos(Oprime))*(a*cos(Etrue)-a*e) + (cos(wprime)*cos(iprime)*cos(Oprime) - sin(wprime)*sin(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
# r1ecliptic.z = sin(wprime)*sin(iprime)*(a*cos(Etrue)-a*e) + cos(wprime)*sin(iprime)*(a*sqrt(1-e**2)*sin(Etrue))

xyz = numpy.array([[a*cos(Etrue) - a*e],[a * sqrt(1 - e**2) * sin(Etrue)], [0]])

matrix1 = numpy.array([[cos(Oprime), -sin(Oprime), 0], [sin(Oprime), cos(Oprime), 0], [0,0,1]])

matrix2 = numpy.array([[1,0,0], [0, cos(iprime), -sin(iprime)], [0, sin(iprime), cos(iprime)]])

matrix3 = numpy.array([[cos(wprime), -sin(wprime), 0], [sin(wprime), cos(wprime), 0], [0,0,1]])

x1y1z1 = matrix1 @ matrix2 @ matrix3 @ xyz # added matrices and used matrix multiplication to avoid undefined mathematical functions

r1ecliptic = vector (x1y1z1[0], x1y1z1[1], x1y1z1 [2])

asteroid = sphere(pos=r1ecliptic*150, radius=(15), color=color.white)
asteroid.trail = curve(color=color.white)
sun = sphere(pos=vector(0,0,0), radius=(50), color=color.yellow)

while (1==1):
    rate(200)
    time = time + 1
    Mtrue = 2*pi/period*(time) + M
    Etrue = solvekep(Mtrue)
    r1ecliptic.x = (cos(wprime)*cos(Oprime) - sin(wprime)*cos(iprime)*sin(Oprime))*(a*cos(Etrue)-a*e) - (cos(wprime)*cos(iprime)*sin(Oprime) + sin(wprime)*cos(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
    r1ecliptic.y = ((cos(wprime)*sin(Oprime) + sin(wprime)*cos(iprime)*cos(Oprime))*(a*cos(Etrue)-a*e)) + (cos(wprime)*cos(iprime)*cos(Oprime) - sin(wprime)*sin(Oprime))*(a*sqrt(1-e**2)*sin(Etrue))
    r1ecliptic.z = sin(wprime)*sin(iprime)*(a*cos(Etrue)-a*e) + cos(wprime)*sin(iprime)*(a*sqrt(1-e**2)*sin(Etrue))
    asteroid.pos = r1ecliptic*150 # indented to add into while loop
    asteroid.trail.append(pos=asteroid.pos)  # indented to add into while loop