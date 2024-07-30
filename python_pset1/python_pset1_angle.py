# PART1
import math

from numpy import true_divide

def convertAngle(degrees, minutes, seconds):
    # handle a negative angle
    degrees_new = 0
    if degrees < 0:
        degrees_new = math.copysign(degrees, 1)
    elif degrees > 0:
        degrees_new = degrees 
    else:
        degrees_new = 0

    # perform angle conversion
    
    deg_minutes = minutes / 60
    # since there are 60 arc minutes in one degree, one arc minute is equal to 1/60 degrees
    deg_seconds = seconds / 3600
    # similar conversion as deg_minutes
    total_deg = degrees_new + deg_minutes + deg_seconds

    if degrees <= 0:
        total_deg = 0 - total_deg

    # return result
    return total_deg

# test cases for part a
print(convertAngle(90, 6, 36)) # should print 90.11
print(convertAngle(-90, 6, 36)) # should print -90.11
print(convertAngle(-0.0, 30, 45)) # should print -0.5125

# PART2
def convertAngle(degrees, minutes, seconds, radian):
    # handle a negative angle
    degrees_new = 0
    if degrees < 0:
        degrees_new = math.copysign(degrees, 1)
    elif degrees > 0:
        degrees_new = degrees 
    else:
        degrees_new = 0

    # perform angle conversion
    
    deg_minutes = minutes / 60
    # since there are 60 arc minutes in one degree, one arc minute is equal to 1/60 degrees
    deg_seconds = seconds / 3600
    # similar conversion as deg_minutes
    total_deg = degrees_new + deg_minutes + deg_seconds

    if degrees <= 0:
        total_deg = 0 - total_deg

    if radian == True:
        total_deg = ((2 * math.pi) / 360) * total_deg

    # return result
    return total_deg

# test cases for part b (uncomment these, comment out previous tests)
print(convertAngle(90, 6, 36, True)) # should print 1.57271618897
print(convertAngle(-90, 6, 36, True)) # should print -1.57271618897
print(convertAngle(90, 6, 36, False)) # should print 90.11
print(convertAngle(-90, 6, 36, False)) # should print -90.11

# PART3
def convertAngle(degrees, minutes, seconds, radian, normalize):
    # handle a negative angle
    degrees_new = 0
    if degrees < 0:
        degrees_new = math.copysign(degrees, 1)
    elif degrees > 0:
        degrees_new = degrees 
    else:
        degrees_new = 0

    # perform angle conversion
    
    deg_minutes = minutes / 60
    # since there are 60 arc minutes in one degree, one arc minute is equal to 1/60 degrees
    deg_seconds = seconds / 3600
    # similar conversion as deg_minutes
    total_deg = degrees_new + deg_minutes + deg_seconds

    if degrees <= 0:
        total_deg = 0 - total_deg

    if radian == True:
        total_deg = ((2 * math.pi) / 360) * total_deg

    if normalize == True:
        if radian == True:
            total_deg = total_deg % (2 * math.pi)
        elif radian != True:
            total_deg = total_deg % 360

    # return result
    return total_deg


# these are the test cases you will demonstrate when getting this homework checked off
# test cases for part c (uncomment these, comment out previous tests)
print(convertAngle(90, 6, 36, False, False)) # should print 90.11
print(convertAngle(90, 6, 36, True, False)) # should print 1.57271618897
print(convertAngle(90, 6, 36, False, True)) # should print 90.11
print(convertAngle(90, 6, 36, True, True)) # should print 1.57271618897
print(convertAngle(-90, 6, 36, False, False)) # should print -90.11
print(convertAngle(-90, 6, 36, True, False)) # should print -1.57271618897
print(convertAngle(-90, 6, 36, False, True)) # should print 269.89
print(convertAngle(-90, 6, 36, True, True)) # should print 4.71046911821
print(convertAngle(540, 0, 0, False, True)) # should print 180.0
print(convertAngle(-0.0, 30, 45, False, False)) # should print -0.5125
