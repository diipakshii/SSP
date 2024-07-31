import math
import numpy
import matplotlib.pyplot as plt

def montecarlo():
    interval = 10000
    circledarts = 0 
    squaredarts = 0

    pi = numpy.zeros(1000)
    
    for j in range(1000):
        for i in range(interval):
            x = numpy.random.random()
            y = numpy.random.random()
            if x**2 + y**2 <= 1:
                circledarts = circledarts + 1
            squaredarts = squaredarts + 1
        pi[j] = 4 * (circledarts / squaredarts)

    mean = numpy.mean(pi)
    SD = numpy.std(pi)
    SDOM = SD / math.sqrt(1000)
    error = (abs(mean - math.pi) / math.pi) * 100

    return mean, SD, SDOM, error

print(montecarlo())