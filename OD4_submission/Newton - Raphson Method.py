# Method 1: Graphing
# y = .42 and y = x - 0.8sin(x) intersect at (1.1503, 0.42)

# Method 2: Homemade Implementation of the Newton-Raphson Method 

import math 

def newton_rap(x):
    M = 0.42
    e = 0.8

    Eguess = x
    Mguess = Eguess - e*math.sin(Eguess)
    Mtrue = M
    count = 0

    while abs(Mguess - Mtrue) > .00001: 
        Mguess = Eguess - e * math.sin(Eguess)
        Eguess = Eguess - (M - Mguess) / (e * math.cos(Eguess) - 1) 
        count = count + 1
    return Eguess, count 
    
print(newton_rap(.42))