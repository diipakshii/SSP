import math
import numpy

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

    if flag == function:

        return (f,g)

# test case 1
# F AND G FUNCTION

# test case 2 
tau1 = -0.32618617484601165
tau3 = 0.0508408854033231
r2 = [0.26799552002875776, -1.3726277901924608, -0.5026729612047128]
r2dot = [0.8456809141954584, -0.3838382184712308, 0.14215854191172816] 

print(fg(tau1, r2, r2dot, 3))
print(fg(tau3, r2, r2dot, 3))

# test case 3
tau1 = -0.3261857571141891
tau3 = 0.05084081855693949
r2 = [0.26662393644794813, -1.381475976476564, -0.5048589337503169]
r2dot = [0.8442117090940343, -0.39728396707075087, 0.14202728258915864] 

print(fg(tau1, r2, r2dot, 4))
print(fg(tau3, r2, r2dot, 4))
