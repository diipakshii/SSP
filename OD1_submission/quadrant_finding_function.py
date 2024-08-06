import math

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


print(trig_function(1.5, -0.5))
print(trig_function(0.4,0.8))
print(trig_function(0.4,0.916515139))
print(trig_function(0.4, -0.916515139))
print(trig_function(-0.4, 0.916515139))
print(trig_function(-0.4, -0.916515139))